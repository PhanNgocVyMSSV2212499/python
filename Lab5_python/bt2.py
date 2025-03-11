import pyodbc
import tkinter as tk
from tkinter import ttk


def get_connection():
    connection_string = '''DRIVER={ODBC Driver 17 for SQL Server};
                           SERVER=DESKTOP-TCJV95V;DATABASE=QLMonAn;
                           Trusted_Connection=yes;Encrypt=no'''
    return pyodbc.connect(connection_string)

def fetch_nhom_mon_an():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TenNhom FROM NhomMonAn")
    nhom_list = [row[0] for row in cursor.fetchall()]
    conn.close()
    return nhom_list

def fetch_data(nhom_mon="Tất cả"):
    conn = get_connection()
    cursor = conn.cursor()
    
    if nhom_mon == "Tất cả":
        query = '''SELECT MonAn.MaMonAn, MonAn.TenMonAn, MonAn.DonViTinh, MonAn.DonGia, NhomMonAn.TenNhom
                   FROM MonAn JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom'''
        cursor.execute(query)
    else:
        query = '''SELECT MonAn.MaMonAn, MonAn.TenMonAn, MonAn.DonViTinh, MonAn.DonGia, NhomMonAn.TenNhom
                   FROM MonAn JOIN NhomMonAn ON MonAn.Nhom = NhomMonAn.MaNhom
                   WHERE NhomMonAn.TenNhom = ?'''
        cursor.execute(query, (nhom_mon,))
    
    data = cursor.fetchall()
    conn.close()
    return [[str(item).replace(",", "") for item in row] for row in data]

def update_table(event):
    selected_nhom = combo_nhom.get()
    tree.delete(*tree.get_children())  
    data = fetch_data(selected_nhom)  
    for row in data:
        tree.insert("", tk.END, values=row)


root = tk.Tk()
root.title("Quản Lý Món Ăn")
root.geometry("680x420")
root.configure(bg="#F8F9FA")


frame = tk.Frame(root, bg="white", padx=10, pady=10, relief=tk.RIDGE, borderwidth=3)
frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)


nhom_list = ["Tất cả"] + fetch_nhom_mon_an()
combo_nhom = ttk.Combobox(frame, values=nhom_list, state="readonly", font=("Arial", 12), width=20)
combo_nhom.current(0)
combo_nhom.grid(row=1, column=1, padx=10, pady=5, sticky="e") 
combo_nhom.bind("<<ComboboxSelected>>", update_table)

columns = ("Mã Món", "Tên Món", "Đơn Vị", "Đơn Giá", "Nhóm")
tree = ttk.Treeview(frame, columns=columns, show="headings", height=15)

for col in columns:
    tree.heading(col, text=col, anchor=tk.CENTER)
    tree.column(col, width=120, anchor=tk.CENTER)

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)

tree.grid(row=2, column=0, columnspan=2, sticky="nsew")
scrollbar.grid(row=2, column=2, sticky="ns")


data = fetch_data()
for row in data:
    tree.insert("", tk.END, values=row)

root.mainloop()