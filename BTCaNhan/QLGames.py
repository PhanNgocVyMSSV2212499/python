import pyodbc
import tkinter as tk
from tkinter import ttk,messagebox
import matplotlib.pyplot as plt 

ConnetionString = '''DRIVER={ODBC Driver 17 for SQL Server};
                     SERVER=DESKTOP-TCJV95V;DATABASE=QLGame;Trusted_Connection=yes;Encrypt=no'''

def get_connection():
    return pyodbc.connect(ConnetionString)

def close_connection(conn):
    if conn:
        conn.close()


def get_all_the_loai():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT ID, TenTheLoai FROM TheLoai")
        records = cursor.fetchall()
        close_connection(connection)
        return {"Chọn thể loại": None} | {row[1]: row[0] for row in records} 
    except Exception as error:
        print("Lỗi:", error)
        return {"Chọn thể loại": None}

def get_filtered_games(the_loai, search_text):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """SELECT Games.MaGame, Games.TenGame, Games.GiaBan, TheLoai.TenTheLoai, Games.NhaSanXuat 
                   FROM Games JOIN TheLoai ON Games.TheLoai = TheLoai.ID"""

        conditions = []
        params = []

        if the_loai != "Chọn thể loại":
            conditions.append("TheLoai.TenTheLoai = ?")
            params.append(the_loai)

        if search_text:
            conditions.append("Games.TenGame LIKE ?")
            params.append(f"%{search_text}%")

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        cursor.execute(query, params)
        records = cursor.fetchall()
        close_connection(connection)
        return records
    except Exception as error:
        print("Lỗi:", error)
        return []

def update_listview(event=None):
    selected_the_loai = combobox.get()
    search_text = search_var.get().strip()
    games = get_filtered_games(selected_the_loai, search_text)

    tree.delete(*tree.get_children())

    for game in games:
        clean_data = [str(value) for value in game]  # Chuyển tất cả về string
        tree.insert("", "end", values=clean_data)


def show_price_chart():
    selected_the_loai = combobox.get()
    search_text = search_var.get().strip()
    games = get_filtered_games(selected_the_loai, search_text)

    if not games:
        messagebox.showwarning("Lỗi","Không có dữ liệu để hiển thị đồ thị!")
        return

    ten_games = [game[1] for game in games]  # Lấy tên game
    gia_ban = [game[2] for game in games]  # Lấy giá bán

    plt.figure(figsize=(10, 5))
    plt.barh(ten_games, gia_ban, color='skyblue')
    plt.xlabel("Giá Bán (VNĐ)")
    plt.ylabel("Tên Game")
    plt.title("Biểu Đồ Giá Bán Các Game")
    plt.gca().invert_yaxis()  # Đảo ngược trục Y để game giá cao xếp trên
    plt.show()

def xoa_game():
    selectItem=tree.selection()
    if not selectItem:
        messagebox.showwarning("Lỗi!","Vui lòng chọn 1 game để xóa!")
        return
    Game=tree.item(selectItem,"values")
    GameID=Game[0]
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE From Games where MaGame=?",GameID)
        connection.commit()
        tree.delete(selectItem)
        messagebox.showinfo("Thành công", "Game đã được xóa!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi xóa: {e}")


def ThemGame(ma_game, ten_game, gia_ban, the_loai, nhasx):
    if not(ma_game and ten_game and gia_ban and the_loai and nhasx):
        messagebox.showwarning("Lỗi!", "Nhập đầy đủ thông tin!")
        return
    the_loai_dict=get_all_the_loai()
    the_loai_id = the_loai_dict.get(the_loai) 

    if the_loai_id is None:
        messagebox.showwarning("Lỗi!", "Chọn thể loại hợp lệ!")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()
        query = "INSERT INTO Games(MaGame, TenGame, GiaBan, TheLoai, NhaSanXuat) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (ma_game, ten_game, gia_ban, the_loai_id, nhasx))  # Truyền ID thay vì tên
        connection.commit()
        close_connection(connection)
        messagebox.showinfo("Thành công", "Đã thêm game thành công!")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khi thêm game: {e}")


def update_game(game_id, ten_game, gia_ban, the_loai, nhasx, window):
    if not (ten_game and gia_ban and the_loai and nhasx):
        messagebox.showwarning("Lỗi!", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        connection = get_connection()
        cursor = connection.cursor()
        
       
        cursor.execute("SELECT ID FROM TheLoai WHERE TenTheLoai = ?", (the_loai,))
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Lỗi!", "Thể loại không hợp lệ!")
            return
        
        the_loai_id = result[0]

        query = """UPDATE Games 
                   SET TenGame=?, GiaBan=?, TheLoai=?, NhaSanXuat=? 
                   WHERE MaGame=?"""
        cursor.execute(query, (ten_game, gia_ban, the_loai_id, nhasx, game_id))
        connection.commit()
        close_connection(connection)

        messagebox.showinfo("Thành công!", "Game đã được cập nhật!")
        update_listview()  # Cập nhật danh sách game trên giao diện
        window.destroy()  # Đóng cửa sổ chỉnh sửa

    except Exception as e:
        messagebox.showerror("Lỗi!", f"Lỗi khi cập nhật game: {e}")


def open_edit_game_window():
    selectItem = tree.selection()
    if not selectItem:
        messagebox.showwarning("Lỗi!", "Vui lòng chọn một game để chỉnh sửa!")
        return

    selected_game = tree.item(selectItem, "values")
    game_id, ten_game, gia_ban, the_loai, nhasx = selected_game  # Lấy dữ liệu cũ

    edit_window = tk.Toplevel(root)
    edit_window.title("Chỉnh sửa Game")
    edit_window.geometry("300x250")

    tk.Label(edit_window, text="Mã Game:").grid(row=0, column=0)
    lbl_ma_game = tk.Label(edit_window, text=game_id)
    lbl_ma_game.grid(row=0, column=1)

    tk.Label(edit_window, text="Tên Game:").grid(row=1, column=0)
    entry_ten_game = tk.Entry(edit_window)
    entry_ten_game.grid(row=1, column=1)
    entry_ten_game.insert(0, ten_game)

    tk.Label(edit_window, text="Giá Bán:").grid(row=2, column=0)
    entry_gia_ban = tk.Entry(edit_window)
    entry_gia_ban.grid(row=2, column=1)
    entry_gia_ban.insert(0, gia_ban)


    tk.Label(edit_window, text="Thể Loại:").grid(row=3, column=0)
    the_loai_list = get_all_the_loai()
    combobox_the_loai = ttk.Combobox(edit_window, values=list(the_loai_list.keys()), state="readonly")
    combobox_the_loai.grid(row=3, column=1)
    combobox_the_loai.set(the_loai)  # Gán giá trị cũ vào combobox

    tk.Label(edit_window, text="Nhà Sản Xuất:").grid(row=4, column=0)
    entry_nhasx = tk.Entry(edit_window)
    entry_nhasx.grid(row=4, column=1)
    entry_nhasx.insert(0, nhasx)

    btn_update = tk.Button(edit_window, text="Cập Nhật", 
                           command=lambda: update_game(game_id, entry_ten_game.get(), 
                                                       entry_gia_ban.get(), combobox_the_loai.get(),
                                                       entry_nhasx.get(), edit_window))
    btn_update.grid(row=5, column=0, columnspan=2)


def open_add_Game_window():
    add_window = tk.Toplevel(root)
    add_window.title("Thêm Game")
    add_window.geometry("300x200")
    
    tk.Label(add_window, text="Mã Game:").grid(row=0, column=0)
    entry_ma_game = tk.Entry(add_window)
    entry_ma_game.grid(row=0, column=1)

    tk.Label(add_window, text="Tên Game:").grid(row=1, column=0)
    entry_ten_game = tk.Entry(add_window)
    entry_ten_game.grid(row=1, column=1)

    tk.Label(add_window, text="Giá bán:").grid(row=2, column=0)
    entry_gia_ban = tk.Entry(add_window)
    entry_gia_ban.grid(row=2, column=1)

    tk.Label(add_window, text="Thể Loại:").grid(row=3, column=0)
    the_loai_dict = get_all_the_loai()  # Lấy dictionary { "Action": 1, "RPG": 2 }
    combobox = ttk.Combobox(add_window, values=list(the_loai_dict.keys()), state="readonly")
    combobox.grid(row=3, column=1)
    combobox.current(0)

    tk.Label(add_window, text="Nhà sản xuất:").grid(row=4, column=0)
    entry_nhasx = tk.Entry(add_window)
    entry_nhasx.grid(row=4, column=1)

    # Nút để thêm nhân viên vào database
    btn_confirm = tk.Button(add_window, text="Xác nhận", 
                            command=lambda: ThemGame(entry_ma_game.get(), 
                                                         entry_ten_game.get(),
                                                         entry_gia_ban.get(),
                                                         combobox.get(),
                                                         entry_nhasx.get()))
    btn_confirm.grid(row=5, column=0, columnspan=2)
    

root = tk.Tk()
root.title("Quản Lý GAME")
root.geometry("1000x500")

label_title = tk.Label(root, text="Quản lý Game", bg="red", fg="white", font=("Times New Roman", 18))
label_title.pack(pady=10)

frame_top = tk.Frame(root)
frame_top.pack(pady=5, fill="x")

label_the_loai = tk.Label(frame_top, text="Thể loại:", font=("Times New Roman", 12))
label_the_loai.pack(side="left", padx=10)

the_loai_list = get_all_the_loai()
combobox = ttk.Combobox(frame_top, values=list(the_loai_list.keys()), state="readonly")
combobox.pack(side="left", padx=10)
combobox.current(0)  # Chọn "Tất cả" mặc định
combobox.bind("<<ComboboxSelected>>", update_listview)

label_search = tk.Label(frame_top, text="Tìm kiếm:", font=("Times New Roman", 12))
label_search.pack(side="left", padx=10)

search_var = tk.StringVar()
entry_search = tk.Entry(frame_top, textvariable=search_var, font=("Times New Roman", 12), width=20)
entry_search.pack(side="left", padx=5)
entry_search.bind("<KeyRelease>", update_listview)  # Sự kiện khi nhập dữ liệu

btn_chart = tk.Button(frame_top, text="Xem Đồ Thị", command=show_price_chart, font=("Times New Roman", 12))
btn_chart.pack(side="left", padx=10)


btn_them = tk.Button(frame_top, text="Thêm game", command=open_add_Game_window, font=("Times New Roman", 12))
btn_them.pack(side="left", padx=10)

btn_xoa = tk.Button(frame_top, text="Xóa game", command=xoa_game, font=("Times New Roman", 12))
btn_xoa.pack(side="left", padx=10)

btn_chinhsua = tk.Button(frame_top, text="Chỉnh sửa", command=open_edit_game_window, font=("Times New Roman", 12))
btn_chinhsua.pack(side="left", padx=10)

columns = ("Mã Game", "Tên Game", "Giá Bán", "Thể Loại", "Nhà Sản Xuất")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.pack(pady=10, fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

update_listview()
root.mainloop()