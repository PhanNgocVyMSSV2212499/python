import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Đăng ký học phần")
root.geometry("400x400")
root.configure(bg="lightgreen")


label_title = tk.Label(root, text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", font=("Arial", 12, "bold"), bg="lightgreen", fg="darkgreen")
label_title.pack(pady=5)


fields = ["Mã số sinh viên", "Họ và tên", "Ngày sinh", "Email", "Số điện thoại", "Học kỳ"]
entries = {}

for field in fields:
    frame = tk.Frame(root, bg="lightgreen")
    frame.pack(pady=2, fill="x", padx=20)
    
    label = tk.Label(frame, text=field, width=15, anchor="w", bg="lightgreen")
    label.pack(side="left")
    
    entry = tk.Entry(frame, width=25)
    entry.pack(side="right", padx=5)
    entries[field] = entry

frame_namhoc = tk.Frame(root, bg="lightgreen")
frame_namhoc.pack(pady=2, fill="x", padx=20)

tk.Label(frame_namhoc, text="Năm học", width=15, anchor="w", bg="lightgreen").pack(side="left")
namhoc_values = ["2022-2023", "2023-2024", "2024-2025"]
namhoc_combobox = ttk.Combobox(frame_namhoc, values=namhoc_values, width=22, state="readonly")
namhoc_combobox.pack(side="right", padx=5)
namhoc_combobox.set(namhoc_values[0])


frame_monhoc = tk.Frame(root, bg="lightgreen")
frame_monhoc.pack(pady=5, padx=20, fill="x")

tk.Label(frame_monhoc, text="Môn học:", bg="lightgreen").pack(anchor="w")
monhoc_vars = {}
monhoc_list = ["Lập trình Python", "Lập trình Java", "Công nghệ phần mềm", "Phát triển ứng dụng web"]
for mon in monhoc_list:
    var = tk.IntVar()
    chk = tk.Checkbutton(frame_monhoc, text=mon, variable=var, bg="lightgreen")
    chk.pack(anchor="w")
    monhoc_vars[mon] = var


frame_buttons = tk.Frame(root, bg="lightgreen")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Đăng ký", width=10, bg="green", fg="white").pack(side="left", padx=10)
tk.Button(frame_buttons, text="Thoát", width=10, bg="red", fg="white", command=root.quit).pack(side="right", padx=10)
root.mainloop()
