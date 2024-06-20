import tkinter as tk
from tkinter import font, filedialog
from PIL import Image, ImageTk
import re

# Initialize the main window
prozor = tk.Tk()
inputtxt = tk.Text(prozor, height=20, width=50, bg="white", undo=True)

# Initialize undo and redo stacks
undo_stack = []
redo_stack = []

# Dictionary to hold images
image_dict = {}

# Function to take input from the text widget
def take_input():
    input_text = inputtxt.get("1.0", "end-1c")
    print(input_text)

# Function to handle button actions
def button_action(number):
    print(f"Button {number} clicked")
    if number == 5:
        toggle_bold()
    elif number == 7:
        toggle_italic()
    elif number == 6:
        undo_action()
    elif number == 9:
        redo_action()
    elif number == 3:
        insert_picture()

# Functions to toggle bold and italic modes
def toggle_bold():
    global bold_mode
    bold_mode = not bold_mode

def toggle_italic():
    global italic_mode
    italic_mode = not italic_mode

# Function to handle key press events
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

# Function to save the current state of the text
def save_state():
    current_text = inputtxt.get("1.0", "end-1c")
    if not undo_stack or undo_stack[-1] != current_text:
        undo_stack.append(current_text)
    redo_stack.clear()

# Function to handle undo actions
def undo_action():
    if len(undo_stack) > 1:
        current_text = undo_stack.pop()
        redo_stack.append(current_text)
        previous_text = undo_stack[-1]
        inputtxt.delete("1.0", "end")
        inputtxt.insert("1.0", previous_text)

# Function to handle redo actions
def redo_action():
    if redo_stack:
        next_text = redo_stack.pop()
        undo_stack.append(next_text)
        inputtxt.delete("1.0", "end")
        inputtxt.insert("1.0", next_text)

# Function to insert a picture
def insert_picture():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((200, 200))
        photo = ImageTk.PhotoImage(img)
        image_id = len(image_dict)
        image_dict[image_id] = photo
        inputtxt.image_create(tk.END, image=photo)
        inputtxt.insert(tk.END, f" (Image {image_id}) ")

# Set up the main window layout and buttons
prozor.geometry('700x700')
prozor.grid_rowconfigure(1, weight=1)
prozor.grid_columnconfigure(0, weight=1)

bold_mode = False
italic_mode = False

dugme1 = tk.Button(prozor, text="Save", command=lambda: button_action(1))
dugme2 = tk.Button(prozor, text="Undo", command=lambda: button_action(6))
dugme3 = tk.Button(prozor, text="Insert", command=lambda: button_action(3))
dugme4 = tk.Button(prozor, text="Font", command=lambda: button_action(4))
dugme_save = tk.Button(prozor, text="Save while working", command=lambda: button_action(8))
redo_dugme = tk.Button(prozor, text="Redo", command=lambda: button_action(9))

dugme1.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
dugme_save.grid(row=0, column=1, sticky="nw", padx=5, pady=5)
dugme2.grid(row=0, column=3, sticky="nw", padx=5, pady=5)
dugme3.grid(row=0, column=4, sticky="nw", padx=5, pady=5)
dugme4.grid(row=0, column=5, sticky="nw", padx=5, pady=5)
redo_dugme.grid(row=0, column=2, sticky="nw", padx=5, pady=5)

def klik1(dogadjaj):
    from savingafile import save_on_click
    save_on_click(inputtxt)
dugme1.bind("<ButtonRelease-1>", klik1)

def klik2(dogadjaj):
    dugme2.configure(text="Undo")
dugme2.bind("<ButtonRelease-1>", klik2)

def klik3(dogadjaj):
    dugme3.configure(text="Picture")
dugme3.bind("<ButtonRelease-1>", klik3)

def klik4(dogadjaj):
    dugme4.destroy()
    bold_dugme = tk.Button(prozor, text="Bold", command=lambda: button_action(5))
    bold_dugme.grid(row=0, column=6, sticky="nw", padx=5, pady=5)
    italic_dugme = tk.Button(prozor, text="Italic", command=lambda: button_action(7))
    italic_dugme.grid(row=0, column=7, sticky="nw", padx=5, pady=5)
dugme4.bind("<ButtonRelease-1>", klik4)

inputtxt.grid(row=1, column=0, columnspan=8, sticky="nsew")

inputtxt.tag_configure("bold", font=font.Font(weight="bold"))
inputtxt.tag_configure("italic", font=font.Font(slant="italic"))
inputtxt.tag_configure("bold_italic", font=font.Font(weight="bold", slant="italic"))

inputtxt.bind("<KeyPress>", on_key_press)

# Initialize the undo stack with the initial content of the text box
save_state()

prozor.mainloop()
