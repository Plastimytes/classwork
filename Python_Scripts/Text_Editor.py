import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self,root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack()

        self.menu_bar =tk.Menu(self.root)
        self.file_menu =tk.Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.file_menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu =tk.Menu(self.menu_bar,tearoff=0)
        self.file_menu.add_command(label="Cut", command=self.cut_text)
        self.file_menu.add_command(label="Copy", command=self.copy_text)
        self.file_menu.add_command(label="Paste", command=self.paste_text)
        self.file_menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.root.config(menu=self.menu_bar)

        def open_file(self):
            file_path =filedialog.askopenfilename(filetypes=["Text files",".txt"])
            if  file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.text_area.delete(1.0,tk.END)
                    self.text_area.insert(tk.END, content)

        def save_file(self):
            file_path = filedialog.asksaveasfilename(defaultextension="txt",filetypes=["Text files", ".txt"])
            if file_path:
                content = self.text_area.get("1.0", tk.END)
                with open(file_path, "w") as file:
                    file.write(content)

        def cut_text(self):
            self.text_area.event_generate ("<<Cut>>")          

        def copy_text(self):
            self.text_area.event_generate ("<<Copy>>")

        def paste_text(self):
            self.text_area.event_generate ("<<Paste>>")   

root = tk.Tk()
root.title("Text Editor")
app = TextEditor(root)
root.mainloop()                                                   

