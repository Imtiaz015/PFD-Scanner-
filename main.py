import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog, Text, Scrollbar, VERTICAL, RIGHT, Y, END
from tkinter import font
def info():
    root = tk.Tk()
    root.minsize(300, 300)
    root.title("Developer Information")
    root.configure(bg="black")

    label1 = tk.Label(root, text="Developer Information",bg='black', fg='white',font=('Helvetica',15))
    label1.pack(pady=(200,0))

    label2 = tk.Label(root, text="Developer Name: Imtiaz Ali Maitlo ...!!",bg='black',fg='white',font=('Helvetica',15))
    label2.pack(pady=(10,0))

    label3 = tk.Label(root, text="Contact: maitloimtiazali36@gmail.com",bg='black',fg='white',font=('Helvetica',15))
    label3.pack(pady=(10,0))

    label4 = tk.Label(root, text="GOOD LUCK",bg='black',fg='white',font=('Helvetica',15))
    label4.pack(pady=(10,0))
    

    # Run the main event loop
    root.mainloop()


def save():
    # Get the file path to save
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", 
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")])
    if file_path:
        with fitz.open(file_path) as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            text_box.delete(1.0, END)
            text_box.insert(END, text)

app = tk.Tk()
app.title("PDF Data Extractor")
app.configure(bg='black')
app.geometry("800x600")

frame = tk.Frame(app, bg='black')
frame.pack(pady=20)

open_button = tk.Button(frame, text="Open PDF", background='black', fg='white', font=('times new roman', 15), command=open_file)
open_button.grid(row=0, column=0, padx=20, pady=10)

info_button=tk.Button(frame,text="Developer Information", background='black', fg='white', font=('times new roman', 15),command=info)
info_button.grid(row=0, column=1, padx=20, pady=10)

save_button=tk.Button(frame,text="Save File", background='black', fg='white', font=('times new roman', 15),command=save)
save_button.grid(row=0, column=2, padx=20, pady=10)

scrollbar = Scrollbar(app, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

# Set larger font size for the text box
text_font = font.Font(family="Helvetica", size=12)

text_box = Text(app, wrap='word', yscrollcommand=scrollbar.set, font=text_font)
text_box.pack(expand=True, fill='both')

scrollbar.config(command=text_box.yview)
# app.attributes('-alpha', 0.9)
app.mainloop()
