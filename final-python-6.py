#!/usr/bin/env python
# coding: utf-8

# In[22]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import requests
from bs4 import BeautifulSoup
import sqlite3

def create_database():
    conn = sqlite3.connect("citations.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS citations (
        id INTEGER PRIMARY KEY,
        select_type TEXT,
        citation_type TEXT,
        authors TEXT,
        title TEXT,
        publication_year INTEGER,
        publisher TEXT,
        doi TEXT,
        url TEXT
    )
    """)

    conn.commit()
    conn.close()

create_database()

class MyHTMLParser:
    def __init__(self):
        self.authors = []
        self.publication_date = None    
        self.doi = None
        self.publisher = None
        self.title = None 

    def get_author_and_publication_year(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            author_tags = soup.find_all('a', {'data-test': 'author-name'})
            for tag in author_tags:
                author = tag.text.strip()
                self.authors.append(author)

            publication_date = soup.find('a', {'data-track-action': 'publication date'})
            doi = soup.find('meta', {'name': 'prism.doi'})
            publisher = soup.find('meta', {'name': 'dc.publisher'})
            title = soup.find('title')
            
            if publication_date and publication_date.text:
                self.publication_date = publication_date.text.strip()
            if doi and doi.text:
                self.doi = doi.text.strip()
            if publisher and publisher.text:
                self.publisher = publisher.text.strip()
            if title and title.text:
                self.title = title.text.strip()

            return self.authors, self.publication_date,self.doi,self.publisher, self.title
        
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None, None, None, None, None

# https://link.springer.com/article/10.1007/s13762-022-03948-9

class Citation:
    def __init__(self, select_type, citation_type, authors, title, publication_year, publisher=None, doi=None,url=None):
        self.select_type = select_type
        self.citation_type = citation_type if citation_type in ["journal", "book"] else None
        self.authors = authors
        self.title = title
        self.publication_year = publication_year
        self.publisher = publisher 
        self.doi = doi
        self.url= url


class CitationManager:
    def __init__(self):
        conn = sqlite3.connect("citations.db")
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS citations (
            id INTEGER PRIMARY KEY,
            authors TEXT,
            title TEXT,
            publication_year INTEGER,
            publisher TEXT,
            doi TEXT,
            url TEXT
        )
        """)

        conn.commit()
        conn.close()

    def add_citation(self, citation):
        conn = sqlite3.connect("citations.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO citations (authors, title, publication_year, publisher, doi, url) VALUES (?, ?, ?, ?, ?, ?)
        """, (", ".join(citation.authors), citation.title, citation.publication_year, citation.publisher, citation.doi, citation.url))


        conn.commit()
        conn.close()

    def remove_citation(self, citation):
        conn = sqlite3.connect("citations.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM citations WHERE id=?", (citation.id,))

        conn.commit()
        conn.close()

    def search_citations(self, query):
        conn = sqlite3.connect("citations.db")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT * FROM citations WHERE title LIKE ? OR authors LIKE ?
        """, ('%' + query.lower() + '%', '%' + query.lower() + '%'))

        results = cursor.fetchall()
        conn.close()

        return results
    def generate_bibliography(self, style):
        conn = sqlite3.connect("citations.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM citations")
        citations = cursor.fetchall()

        bibliography = []
        for citation in citations:
            bibliography.append(format_citation(citation, style))

        conn.close()

        return bibliography

def format_authors(authors):
    if len(authors) > 1:
        return ', '.join(authors[:-1]) + ', & ' + authors[-1]
    else:
        return authors[0]

def format_citation(citation, style):
    format_functions = {
        'APA': format_apa,
        'MLA': format_mla,
        'Chicago': format_chicago
    }
    if style not in format_functions:
        raise ValueError(f"Unknown citation style: {style}")

    return format_functions[style](citation)

def format_mla(citation):
    authors = format_authors(citation.authors)
    return f"{authors} ({citation.publication_year}). {citation.title}. {citation.publisher}. {citation.url}."

def format_apa(citation):
    authors = format_authors(citation.authors)
    return f"{authors} ({citation.publication_year}). {citation.title}. {citation.publisher}. {citation.url}."

def format_chicago(citation):
    authors = format_authors(citation.authors)
    return f"{authors} ({citation.publication_year}). {citation.title}."


class CitationManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Citation Manager")
        self.geometry("1000x800")

        self.manager = CitationManager()

        self.create_widgets()
        self.url_entry = None
        self.bibliography_style_var = tk.StringVar()
        self.bibliography_style_var.set("APA")
    def create_widgets(self):
            self.main_frame = ttk.Frame(self)
            self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

            self.title_label = ttk.Label(self.main_frame, text="Citation Manager", font=("Arial", 16, "bold"))
            self.title_label.pack(pady=20)

            self.add_citation_button = ttk.Button(self.main_frame, text="Add Citation", command=self.add_citation_window)
            self.add_citation_button.pack()
            
            self.remove_citation_button = ttk.Button(self.main_frame, text="Remove Citation", command=self.remove_citation)
            self.remove_citation_button.pack(pady=10)

            self.search_label = ttk.Label(self.main_frame, text="Search")
            self.search_label.pack(pady=10)

            self.search_entry = ttk.Entry(self.main_frame)
            self.search_entry.pack()

            self.search_button = ttk.Button(self.main_frame, text="Search", command=self.search_citations)
            self.search_button.pack(pady=10)

            self.citation_listbox = tk.Listbox(self.main_frame)
            self.citation_listbox.pack(fill=tk.BOTH, expand=True)

            self.generate_bibliography_button = ttk.Button(self.main_frame, text="Generate Bibliography", command=self.generate_bibliography_window)
            self.generate_bibliography_button.pack(pady=20)

    def add_citation_window(self):
        add_citation_win = tk.Toplevel(self)
        def submit():
            select_type = select_type_var.get()
            if select_type == "Manual":
                citation_type = "book"  # or "journal", depending on the type of the citation
                authors = author_entry.get().split(', ')
                title = title_entry.get()
                if not title:
                    title = ""
                publication_year = int(year_entry.get())
                url = url_entry.get()
                citation = Citation(select_type, citation_type, authors, title, publication_year, url=url, doi=doi_entry.get(), publisher=publisher_entry.get())
            elif select_type == "Auto":
                citation_type = "book"  # or "journal", depending on the type of the citation
                url = url_entry.get()
                parser = MyHTMLParser()
                author_name, publication_year_from_url,doi, publisher, title = parser.get_author_and_publication_year(url)
                if author_name:
                    authors = [author_name]
                else:
                    authors = []
                if publication_year_from_url:
                    publication_year = publication_year_from_url
                else:
                    publication_year = 0
                citation = Citation(select_type, citation_type, authors, title, publication_year, url=url, doi=doi_entry.get(), publisher=publisher_entry.get())




            self.manager.add_citation(citation)
            self.citation_listbox.insert(tk.END, f"{citation.title} | {', '.join(str(a) for a in citation.authors)}, {citation.publication_year}")


            add_citation_win.destroy()

            if url_entry.winfo_exists():
                url_entry.delete(0, tk.END)
            if author_entry.winfo_exists():
                author_entry.delete(0, tk.END)
                author_entry.insert(0, author_name)
            if year_entry.winfo_exists():
                year_entry.delete(0, tk.END)
                year_entry.insert(0, publication_year_from_url)


        def show_manual_fields():
            author_label.grid()
            author_entry.grid()
            title_label.grid()
            title_entry.grid()
            year_label.grid()
            year_entry.grid()
            url_label.grid
            url_entry.grid

        def show_auto_fields():
            author_label.grid_remove()
            author_entry.grid_remove()
            title_label.grid_remove()
            title_entry.grid_remove()
            year_label.grid_remove()
            year_entry.grid_remove()
            doi_label.grid_remove()
            doi_entry.grid_remove()
            publisher_label.grid_remove()
            publisher_entry.grid_remove()
            url_label.grid()
            url_entry.grid()
            add_citation_win = tk.Toplevel(self)
            add_citation_win.title("Add Citation")

        select_type_label = ttk.Label(add_citation_win, text="select_type")
        select_type_label.grid(row=0, column=0)
        select_type_var = tk.StringVar(value="Manual")
        select_type_radio_manual = ttk.Radiobutton(add_citation_win, text="Manual", variable=select_type_var, value="Manual", command=show_manual_fields)
        select_type_radio_manual.grid(row=0, column=1)
        select_type_radio_auto = ttk.Radiobutton(add_citation_win, text="Auto", variable=select_type_var, value="Auto", command=show_auto_fields)
        select_type_radio_auto.grid(row=0, column=2)

        fields_frame = ttk.Frame(add_citation_win)
        fields_frame.grid(row=1, column=0, columnspan=3)
        
        author_label = ttk.Label(add_citation_win, text="Authors (separated by ', ')")
        author_label.grid(row=1, column=0)
        author_entry = ttk.Entry(add_citation_win)
        author_entry.grid(row=1, column=1)

        title_label = ttk.Label(add_citation_win, text="Title")
        title_label.grid(row=2, column=0)
        title_entry = ttk.Entry(add_citation_win)
        title_entry.grid(row=2, column=1)

        year_label = ttk.Label(add_citation_win, text="Publication Year")
        year_label.grid(row=3, column=0)
        year_entry = ttk.Entry(add_citation_win)
        year_entry.grid(row=3, column=1)
        
        doi_label = ttk.Label(add_citation_win, text="DOI:")
        doi_label.grid(row=4, column=0)
        doi_entry = ttk.Entry(add_citation_win)
        doi_entry.grid(row=4, column=1)

        publisher_label = ttk.Label(add_citation_win, text="Publisher:")
        publisher_label.grid(row=5, column=0)
        publisher_entry = ttk.Entry(add_citation_win)
        publisher_entry.grid(row=5, column=1)

        url_label = ttk.Label(add_citation_win, text="URL")
        url_label.grid(row=6, column=0)
        url_entry = ttk.Entry(add_citation_win)
        url_entry.grid(row=6, column=1)
        self.url_entry = url_entry
        
        submit_button = ttk.Button(add_citation_win, text="Submit", command=submit)
        submit_button.grid(row=7, column=1, sticky="E")
       
        
    def remove_citation(self):
        selected_index = self.citation_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No citation selected.")
            return

        selected_citation = self.manager.citations[selected_index[0]]
        self.manager.remove_citation(selected_citation)
        self.citation_listbox.delete(selected_index)

    def search_citations(self):
        query = self.search_entry.get()
        results = self.manager.search_citations(query)

        self.citation_listbox.delete(0, tk.END)
        for result in results:
            self.citation_listbox.insert(tk.END, result.title)
        
    def generate_bibliography(self):
        style = self.bibliography_style_var.get()
        bibliography = self.manager.generate_bibliography(style)

        # Tạo cửa sổ mới để hiển thị danh mục tài liệu tham khảo
        bibliography_win = tk.Toplevel(self)
        bibliography_win.title("Bibliography")

        bibliography_text = tk.Text(bibliography_win, wrap=tk.WORD)
        bibliography_text.pack(padx=10, pady=10)

        for entry in bibliography:
            bibliography_text.insert(tk.END, entry + "\n\n")

        close_button = ttk.Button(bibliography_win, text="Close", command=bibliography_win.destroy)
        close_button.pack(pady=10)
    def generate_bibliography_window(self):
        generate_bibliography_win = tk.Toplevel(self)
        generate_bibliography_win.title("Generate Bibliography")

        style_label = ttk.Label(generate_bibliography_win, text="Style:")
        style_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        style_combobox = ttk.Combobox(generate_bibliography_win, textvariable=self.bibliography_style_var, values=["APA", "MLA", "Chicago"])
        style_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        generate_button = ttk.Button(generate_bibliography_win, text="Generate", command=self.generate_bibliography)
        generate_button.grid(row=1, column=1, padx=5, pady=5, sticky="e")

        style_var = tk.StringVar(generate_bibliography_win)
        style_var.set("APA")
        


if __name__ == "__main__":
    app = CitationManagerApp() 
    app.mainloop()
# https://link.springer.com/article/10.1007/s13762-022-03948-9


# In[ ]:





# In[ ]:




