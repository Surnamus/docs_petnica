import tkinter as tk
from tkinter import font
import re

def take_input():
    input_text = inputtxt.get("1.0", "end-1c")
    print(input_text)

def button_action(number):
    print(f"Button {number} clicked")
    if number == 5:
        toggle_bold()
    elif number == 7:
        toggle_italic()
    elif number == 6:
        undo_action()

def toggle_bold():
    global bold_mode
    bold_mode = not bold_mode

def toggle_italic():
    global italic_mode
    italic_mode = not italic_mode

def on_key_press(event):
    if bold_mode and italic_mode:
        inputtxt.tag_add("bold_italic", "insert-1c", "insert")
    elif bold_mode:
        inputtxt.tag_add("bold", "insert-1c", "insert")
        inputtxt.tag_remove("italic", "insert-1c", "insert")
    elif italic_mode:
        inputtxt.tag_add("italic", "insert-1c", "insert")
        inputtxt.tag_remove("bold", "insert-1c", "insert")
    else:
        inputtxt.tag_remove("bold", "insert-1c", "insert")
        inputtxt.tag_remove("italic", "insert-1c", "insert")
    save_state()

def save_state():
    current_text = inputtxt.get("1.0", "end-1c")
    if not undo_stack or undo_stack[-1] != current_text:
        undo_stack.append(current_text)

def undo_action():
    if len(undo_stack) > 1:
        current_text = undo_stack.pop()
        words = re.findall(r'\S+|\s', current_text)  
        if words:
            last_word = words[-1]
            if len(last_word.strip()) >= 15:
                words.pop()  # Remove the last word
            else:
                words[-1] = last_word[:-1]  
            previous_text = ''.join(words)
            inputtxt.delete("1.0", "end")
            inputtxt.insert("1.0", previous_text)
            save_state()  
    elif undo_stack:
        undo_stack.pop()
        inputtxt.delete("1.0", "end")

prozor = tk.Tk()
prozor.geometry('700x700')

prozor.grid_rowconfigure(1, weight=1)
prozor.grid_columnconfigure(0, weight=1)

undo_stack = []

broj_klikova1 = 0
broj_klikova2 = 0
broj_klikova3 = 0
broj_klikova4 = 0

dugme1 = tk.Button(prozor, text="Save", command=lambda: button_action(1))
dugme2 = tk.Button(prozor, text="Undo", command=lambda: button_action(6))
dugme3 = tk.Button(prozor, text="Insert", command=lambda: button_action(3))
dugme4 = tk.Button(prozor, text="Font", command=lambda: button_action(4))
dugme_save = tk.Button(prozor, text="Save while working", command=lambda: button_action(8))

dugme1.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
dugme_save.grid(row=0, column=1, sticky="nw", padx=5, pady=5)
dugme2.grid(row=0, column=3, sticky="nw", padx=5, pady=5)
dugme3.grid(row=0, column=4, sticky="nw", padx=5, pady=5)
dugme4.grid(row=0, column=5, sticky="nw", padx=5, pady=5)

bold_mode = False
italic_mode = False

def klik1(dogadjaj):
    global broj_klikova1
    broj_klikova1 += 1
    if broj_klikova1 >= 1:
        from savingafile import save_on_click
        save_on_click(inputtxt)
dugme1.bind("<ButtonRelease-1>", klik1)

def klik2(dogadjaj):
    global broj_klikova2
    broj_klikova2 += 1
    if broj_klikova2 == 1:
        dugme2.configure(text="Undo")
        redo_dugme = tk.Button(prozor, text="Redo", command=lambda: button_action(9))
        redo_dugme.grid(row=0, column=2, sticky="nw", padx=5, pady=5)
    elif broj_klikova2 == 2:
        pass
dugme2.bind("<ButtonRelease-1>", klik2)

def klik3(dogadjaj):
    global broj_klikova3
    broj_klikova3 += 1
    if broj_klikova3 == 1:
        dugme3.configure(text="Text")
    elif broj_klikova3 == 2:
        pass
dugme3.bind("<ButtonRelease-1>", klik3)

def klik4(dogadjaj):
    global broj_klikova4
    broj_klikova4 += 1
    if broj_klikova4 == 1:
        dugme4.destroy()
        global bold_dugme
        bold_dugme = tk.Button(prozor, text="Bold", command=lambda: button_action(5))
        bold_dugme.grid(row=0, column=6, sticky="nw", padx=5, pady=5)
        global italic_dugme
        italic_dugme = tk.Button(prozor, text="Italic", command=lambda: button_action(7))
        italic_dugme.grid(row=0, column=7, sticky="nw", padx=5, pady=5)
    elif broj_klikova4 == 2:
        pass
dugme4.bind("<ButtonRelease-1>", klik4)

inputtxt = tk.Text(prozor, height=20, width=50, bg="white", undo=True)  
inputtxt.grid(row=1, column=0, columnspan=8, sticky="nsew")

inputtxt.tag_configure("bold", font=font.Font(weight="bold"))
inputtxt.tag_configure("italic", font=font.Font(slant="italic"))
inputtxt.tag_configure("bold_italic", font=font.Font(weight="bold", slant="italic"))

inputtxt.bind("<KeyPress>", on_key_press)


save_state()

prozor.mainloop()