import tkinter as tk

def update_cursor_position(event=None):
    cursor_position = text_widget.index(tk.INSERT)
    line, column = cursor_position.split('.')
    cursor_position_label.config(text=f"Cursor Position: Line {line}, Column {column}")

def insert_text_at_cursor(event=None):
    original_text = text_widget.get("1.0", "end-1c")
    insert_text = insert_entry.get()
    cursor_position = text_widget.index(tk.INSERT) 
    line, column = cursor_position.split('.')
    line = int(line) - 1 
    column = int(column)

    cursor_index = text_widget.index(f"{line + 1}.{column}")

    text_widget.insert(cursor_index, insert_text)

    update_cursor_position()

root = tk.Tk()
root.title("Text Cursor Position Locator and Insertion")

text_widget = tk.Text(root, wrap='word', width=40, height=10)
text_widget.pack(padx=20, pady=20)
text_widget.bind('<KeyRelease>', update_cursor_position)
text_widget.bind('<ButtonRelease-1>', update_cursor_position)

cursor_position_label = tk.Label(root, text="Cursor Position: Line 1, Column 0", font=("Helvetica", 14))
cursor_position_label.pack(pady=10)

insert_entry = tk.Entry(root, font=("Helvetica", 14))
insert_entry.pack(pady=10)
insert_entry.bind('<Return>', insert_text_at_cursor)

update_cursor_position()

root.mainloop()
