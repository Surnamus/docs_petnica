import toolbar_2
import tkinter as tk
def savefile(doc):
    open(doc, 'w').write(toolbar_2.inputtxt)
    doc.close()
def save_on_click(self):
        filetext = self.basket_textbox.get("1.0", "end-1c")
        save_text = tk.filedialog.asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if save_text:
            with open(save_text, "w") as f:
                f.write(filetext)
        