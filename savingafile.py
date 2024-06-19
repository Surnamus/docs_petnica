import tkinter as tk
from tkinter import filedialog
def savefile(doc):
    from toolbar_2 import inputtxt
    open(doc, 'w').write(inputtxt)
    doc.close()
def save_on_click(self):
        filetext = self.get("1.0", "end-1c")
        save_text = filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if save_text:
            with open(save_text, "w") as f:
                f.write(filetext)
        