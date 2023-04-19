#!/usr/bin/env python
# coding: utf-8

# In[55]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import datetime

class MyHTMLParser:
    def __init__(self):
        self.author_name = None
        self.publication_date = None

    def get_author_and_publication_year(self, url):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            
            author = soup.find(class_="author-name")
            publication_date = soup.find(class_="author-time")

            if author and author.text:
                self.author_name = author.text.strip()
            if publication_date and publication_date.text:
                self.publication_date = publication_date.text.strip()

            return self.author_name, self.publication_date
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None, None


citations = []
url = "https://dantri.com.vn/tam-long-nhan-ai/rot-nuoc-mat-canh-2-con-tho-cham-cha-u-nao-trong-can-nha-15m2-20230325152725236.htm"
parser = MyHTMLParser()
author_name, publication_date = parser.get_author_and_publication_year(url)
print(f"Author: {author_name}")
print(f"Publication Date: {publication_date}")


class Citation:
    def __init__(self, citation_type, authors, title, publication_year, publisher=None, journal_title=None, volume=None, issue=None, pages=None, doi=None, edition=None, city=None,url=None):
        self.citation_type = citation_type
        self.authors = authors
        self.title = title
        self.publication_year = publication_year
        self.publisher = publisher
        self.journal_title = journal_title
        self.volume = volume
        self.issue = issue
        self.pages = pages
        self.doi = doi
        self.edition = edition
        self.city = city
        self.url= url


class CitationManager:
    def __init__(self):
        self.citations = []

    def add_citation(self, citation):
        self.citations.append(citation)

    def remove_citation(self, citation):
        self.citations.remove(citation)

    def search_citations(self, query):
        results = []
        for citation in self.citations:
            if query.lower() in citation.title.lower() or any(query.lower() in author.lower() for author in citation.authors):
                results.append(citation)
        return results

    def sort_citations(self, key):
        return sorted(self.citations, key=lambda x: getattr(x, key))

    def generate_bibliography(self, style):
        bibliography = []
        for citation in self.citations:
            bibliography.append(format_citation(citation, style))
        return bibliography


def format_citation(citation, style):
    if style == 'APA':
        return format_apa(citation)
    elif style == 'MLA':
        return format_mla(citation)
    elif style == 'Chicago':
        return format_chicago(citation)
    else:
        raise ValueError(f"Unknown citation style: {style}")


def format_mla(citation):
    authors = ', '.join(citation.authors[:-1]) + ', and ' + citation.authors[-1]

    if citation.citation_type == 'journal':
        result = f"{authors}. \"{citation.title}.\" {citation.journal_title}, vol. {citation.volume}, no. {citation.issue}, {citation.publication_year}, pp. {citation.pages}."
        if citation.doi:
            result += f" doi:{citation.doi}"
    elif citation.citation_type == 'book':
        result = f"{authors}. {citation.title}. {citation.edition} ed., {citation.publisher}, {citation.publication_year}."
    else:
        raise ValueError(f"Unsupported citation type: {citation.citation_type}")

    if citation.url:
        result += f" Accessed {citation.url}"

    return result



def format_apa(citation):
    authors = ', '.join(citation.authors[:-1]) + ', & ' + citation.authors[-1]

    if citation.citation_type == 'journal':
        result = f"{authors} ({citation.publication_year}). {citation.title}. {citation.journal_title}, {citation.volume}({citation.issue}), {citation.pages}."
        if citation.url:
            result += f" Retrieved from {citation.url}"
    elif citation.citation_type == 'book':
        result = f"{authors} ({citation.publication_year}). {citation.title} ({citation.edition} ed.). {citation.publisher}."
        if citation.url:
            result += f" Retrieved from {citation.url}"
    else:
        raise ValueError(f"Unsupported citation type: {citation.citation_type}")

    return result
def format_chicago(citation):
    authors = ', '.join(citation.authors[:-1]) + ', and ' + citation.authors[-1]

    if citation.citation_type == 'journal':
        result = f"{authors}. \"{citation.title}.\" {citation.journal_title} {citation.volume}, no. {citation.issue} ({citation.publication_year}): {citation.pages}."
    elif citation.citation_type == 'book':
        result = f"{authors}. {citation.title}. {citation.edition} ed. {citation.city}: {citation.publisher}, {citation.publication_year}."
    else:
        raise ValueError(f"Unsupported citation type: {citation.citation_type}")

    # Thêm URL vào cuối trích dẫn (nếu có)
    if citation.url:
        result += f" Accessed {citation.url}"

    return result


class CitationManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Citation Manager")
        self.geometry("1000x800")

        self.manager = CitationManager()

        self.create_widgets()
        self.url_entry = None
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

            # Tạo khung chứa các tùy chọn tìm kiếm nâng cao
            self.advanced_search_frame = ttk.LabelFrame(self.main_frame, text="Advanced Search")
            self.advanced_search_frame.pack(pady=10)

            # Tùy chọn tìm kiếm theo tác giả
            self.author_search_var = tk.StringVar()
            self.author_search_checkbutton = ttk.Checkbutton(self.advanced_search_frame, text="Author", variable=self.author_search_var)
            self.author_search_checkbutton.pack(side=tk.LEFT, padx=10)

            self.author_search_entry = ttk.Entry(self.advanced_search_frame, state=tk.DISABLED)
            self.author_search_entry.pack(side=tk.LEFT)

            # Tùy chọn tìm kiếm theo năm xuất bản
            self.year_search_var = tk.StringVar()
            self.year_search_checkbutton = ttk.Checkbutton(self.advanced_search_frame, text="Publication Year", variable=self.year_search_var)
            self.year_search_checkbutton.pack(side=tk.LEFT, padx=10)

            self.year_search_entry = ttk.Entry(self.advanced_search_frame, state=tk.DISABLED)
            self.year_search_entry.pack(side=tk.LEFT)

            # Tùy chọn tìm kiếm theo tựa đề
            self.title_search_var = tk.StringVar()
            self.title_search_checkbutton = ttk.Checkbutton(self.advanced_search_frame, text="Title", variable=self.title_search_var)
            self.title_search_checkbutton.pack(side=tk.LEFT, padx=10)

            self.title_search_entry = ttk.Entry(self.advanced_search_frame, state=tk.DISABLED)
            self.title_search_entry.pack(side=tk.LEFT)

            self.citation_listbox = tk.Listbox(self.main_frame)
            self.citation_listbox.pack(fill=tk.BOTH, expand=True)

            self.generate_bibliography_button = ttk.Button(self.main_frame, text="Generate Bibliography", command=self.generate_bibliography)
            self.generate_bibliography_button.pack(pady=20)

    def add_citation_window(self):
        add_citation_win = tk.Toplevel(self)
        def submit():
            citation_type = citation_type_var.get()
            if citation_type == "Manual":
                authors = author_entry.get().split(', ')
                title = title_entry.get()
                publication_year = int(year_entry.get())
                url = url_entry.get()
                citation = Citation(citation_type, authors, title, publication_year, url=url)
            elif citation_type == "Auto":
                url = url_entry.get()
                parser = MyHTMLParser()
                author_name, publication_year_from_url = parser.get_author_and_publication_year(url)
                if author_name:
                    authors = [author_name]
                else:
                    authors = []
                if publication_year_from_url:
                    publication_year = publication_year_from_url
                else:
                    publication_year = 0
                citation = Citation(citation_type, authors, '', publication_year, url=url)
            
            self.manager.add_citation(citation)
            self.citation_listbox.insert(tk.END, citation.title)

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
            url_label.grid_remove()
            url_entry.grid_remove()

        def show_auto_fields():
            author_label.grid_remove()
            author_entry.grid_remove()
            title_label.grid_remove()
            title_entry.grid_remove()
            year_label.grid_remove()
            year_entry.grid_remove()
            url_label.grid()
            url_entry.grid()
            add_citation_win = tk.Toplevel(self)
            add_citation_win.title("Add Citation")

        citation_type_label = ttk.Label(add_citation_win, text="Citation Type")
        citation_type_label.grid(row=0, column=0)
        citation_type_var = tk.StringVar(value="Manual")
        citation_type_radio_manual = ttk.Radiobutton(add_citation_win, text="Manual", variable=citation_type_var, value="Manual", command=show_manual_fields)
        citation_type_radio_manual.grid(row=0, column=1)
        citation_type_radio_auto = ttk.Radiobutton(add_citation_win, text="Auto", variable=citation_type_var, value="Auto", command=show_auto_fields)
        citation_type_radio_auto.grid(row=0, column=2)

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

        url_label = ttk.Label(add_citation_win, text="URL")
        url_label.grid(row=4, column=0)
        url_entry = ttk.Entry(add_citation_win)
        url_entry.grid(row=4, column=1)
        self.url_entry = url_entry
        


        submit_button = ttk.Button(add_citation_win, text="Submit", command=submit)
        submit_button.grid(row=6, column=1, sticky="E")
       
        
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
                style = "APA"  # Sử dụng định dạng APA làm ví dụ
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

if __name__ == "__main__":
    app = CitationManagerApp()
    app.mainloop()



# In[ ]:





# In[ ]:




