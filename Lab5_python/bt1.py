import pyodbc
connectionString = '''DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-TCJV95V;
                      DATABASE=QLSinhVien;Trusted_Connection=yes;Encrypt=no'''

def get_connection():
    conn=pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection=get_connection()
        curso=connection.cursor()
        select_query='''SELECT * from Lop'''
        curso.execute(select_query)
        records=curso.fetchall()

        print(f"Danh sach cac lop la: ")
        for row in records:
            print("*"*50)
            print("Ma Lop ",row[0])
            print("Ten Lop",row[1])

        close_connection(connection)

    except(Exception,pyodbc.Error) as error:
        print("Xay ra loi thuc thi,thong tin loi: ",error)

def get_all_sv():
    try:
        connection=get_connection()
        curso=connection.cursor()
        select_query='''select sv.ID,sv.HoTen,l.ID,l.TenLop
                        from SinhVien sv,Lop l
                        Where MaLop=l.ID'''
        curso.execute(select_query)
        record=curso.fetchall()
        print("Danh sach tat ca sinh vien la: ")
        print ("Ma SV\t Ten Sinh Vien\t\t Ma Lop\t Ten Lop")
        for row in record:
             print(f"{row[0]}\t {row[1]:<20}\t {row[2]}\t {row[3]}")
        close_connection(connection)
    except(Exception,pyodbc.Error) as error:
        print("Xay ra loi thuc thi,thong tin loi: ",error)

def get_class_by_id(class_id):
    try:
        connection=get_connection()
        curso=connection.cursor()

        select_query="select * from Lop where id=?"

        params=(class_id,)
        curso.execute(select_query,params)
        record=curso.fetchone()

        print(f"Thong tin lop co id ={class_id}: ")
        print("Ma lop:",record[0])
        print("Ten Lop",record[1])
        close_connection(connection)
    except(Exception,pyodbc.Error) as error:
        print("Xay ra loi thuc thi,thong tin loi: ",error)

def hien_thi_sv_theo_masv(sv_id):
    try:
        connection = get_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        select_query = "SELECT * FROM SinhVien WHERE ID = ?"
        cursor.execute(select_query, (sv_id,))
        record = cursor.fetchone()

        if record:
            print(f"Thông tin sinh viên có ID = {sv_id}:")
            print(f"Mã SV: {record[0]}")
            print(f"Họ tên: {record[1]}")
            print(f"Mã lớp: {record[2]}")
        else:
            print(f" Không tìm thấy sinh viên có ID = {sv_id}")

        print("\n Danh sách sinh viên trong cùng lớp:")
        select_query = '''SELECT sv.ID, sv.HoTen, l.ID, l.TenLop
                          FROM SinhVien sv
                          JOIN Lop l ON sv.MaLop = l.ID
                          WHERE sv.MaLop = (SELECT MaLop FROM SinhVien WHERE ID = ?)'''
        cursor.execute(select_query, (sv_id,))
        records = cursor.fetchall()

        if records:
            print("Mã SV\tHọ tên\t\tMã lớp\tTên lớp")
            for row in records:
                print(f"{row[0]}\t {row[1]:<20}\t {row[2]}\t {row[3]}")
        else:
            print("Không có sinh viên nào trong lớp này.")

        close_connection(connection)

    except Exception as error:
        print("Xảy ra lỗi thực thi, thông tin lỗi:", error)

def insert_class(class_id, class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()


        select_query = "INSERT INTO Lop (ID, TenLop) VALUES (?, ?)"
        cursor.execute(select_query, (class_id, class_name))

        connection.commit()
        print("Đã thêm thành công")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

def update_class(class_id, new_class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "UPDATE Lop SET TenLop = ? WHERE ID = ?"
        cursor.execute(select_query, (new_class_name, class_id))

        connection.commit()
        print("Đã cập nhật thành công")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)


def delete_class(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "DELETE FROM Lop WHERE ID = ?"
        cursor.execute(select_query, (class_id,))

        connection.commit()
        print("Đã xoá thành công")

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)

insert_class(5, "CTK59A")
get_all_class()
hien_thi_sv_theo_masv(2)
delete_class(2)
update_class(2,"CTK46")