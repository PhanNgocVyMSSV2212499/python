import tkinter as tk
from tkinter import messagebox

def btn_click(item):
    entry_text.set(entry_text.get() + str(item))

def btn_clear():
    entry_text.set("")

def btn_back():
    entry_text.set(entry_text.get()[:-1])

def btn_equal():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ")

def btn_close():
    root.destroy()

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="#A5D6A7")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 16), justify='right', bd=5, relief=tk.RIDGE)
entry.pack(fill="both", ipadx=8, pady=5, padx=5)

buttons = [
    ('Cls', btn_clear), ('Back', btn_back), ('Close', btn_close), ('/', lambda: btn_click('/')),
    ('7', lambda: btn_click('7')), ('8', lambda: btn_click('8')), ('9', lambda: btn_click('9')), ('*', lambda: btn_click('*')),
    ('4', lambda: btn_click('4')), ('5', lambda: btn_click('5')), ('6', lambda: btn_click('6')), ('-', lambda: btn_click('-')),
    ('1', lambda: btn_click('1')), ('2', lambda: btn_click('2')), ('3', lambda: btn_click('3')), ('+', lambda: btn_click('+')),
    ('0', lambda: btn_click('0')), ('.', lambda: btn_click('.')), ('=', btn_equal)
]

frame = tk.Frame(root)
frame.pack()

row_val = 0
col_val = 0
for text, cmd in buttons:
    tk.Button(frame, text=text, width=7, height=2, command=cmd, font=("Arial", 14)).grid(row=row_val, column=col_val, padx=3, pady=3)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
