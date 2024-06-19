import tkinter as tk
def take_input():
    input_text = inputtxt.get("1.0", "end-1c")
    print(input_text)

def button_action(number):
    print(f"Button {number} clicked")

prozor = tk.Tk()
prozor.geometry('700x700')

prozor.grid_rowconfigure(1, weight=1)
prozor.grid_columnconfigure(0, weight=1)

broj_klikova1 = 0
broj_klikova2 = 0
broj_klikova3 = 0
broj_klikova4 = 0

dugme1 = tk.Button(prozor, text="Save", command=lambda: button_action(1))
dugme2 = tk.Button(prozor, text="Edit", command=lambda: button_action(2))
dugme3 = tk.Button(prozor, text="Insert", command=lambda: button_action(3))
dugme4 = tk.Button(prozor, text="Font", command=lambda: button_action(4))

dugme1.grid(row=0, column=0, sticky="nw", padx=5, pady=5)
dugme2.grid(row=0, column=1, sticky="nw", padx=5, pady=5)
dugme3.grid(row=0, column=2, sticky="nw", padx=5, pady=5)
dugme4.grid(row=0, column=3, sticky="nw", padx=5, pady=5)

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
        dugme7 = tk.Button(prozor, text="Redo", command=lambda: button_action(7))
        dugme7.grid(row=0, column=5, sticky="nw", padx=5, pady=5)
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
        dugme4.configure(text="Italic")
        dugme5 = tk.Button(prozor, text="Bold", command=lambda: button_action(5))
        
        dugme5.grid(row=0, column=4, sticky="nw", padx=5, pady=5)
        
    elif broj_klikova4 == 2:
        pass
dugme4.bind("<ButtonRelease-1>", klik4)

inputtxt = tk.Text(prozor, height=20, width=50, bg="white")
inputtxt.grid(row=1, column=0, columnspan=6, sticky="nsew")  

prozor.mainloop()
print ("Dugme1 - file/save")
print ("Dugme2 - edit/undo")
print ("Dugme3 -insert/text ")
print ("Dugme4 - Font/Bold")
print ("Dugme5 - Italic")
print ("Dugme7 - Redo")