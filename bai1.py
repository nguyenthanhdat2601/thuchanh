import numpy as np
from tkinter import *
from tkinter import messagebox


def Input1():
    sopt = IntVar()
    return sopt.get()


def Input2():
    soan = IntVar()
    return soan.get()


def test_input(sopt, soan):
    if sopt != soan or sopt < 0 or soan < 0:
        print("Error! Nhập lại!")
        sopt = Input1()
        soan = Input2()
        return test_input(sopt, soan)
    else:
        return sopt, soan


def Input3(sopt, soan):
    A = np.zeros((sopt, soan), dtype=float)
    B = np.zeros((sopt, 1), dtype=float)

    for pt in range(0, sopt):
        print(f"Nhập hệ số của phương trình thứ {pt + 1}: ")
        for an in range(0, sopt):
            A[pt, an] = float(input(f"----hệ số thứ {an + 1}: "))
        B[pt, 0] = float(input("----hệ số cuối: "))

    return A, B


def calculate(A, B):
    try:
        if np.linalg.det(A) != 0:
            X = np.dot(np.linalg.inv(A), B)
            return X
        else:
            messagebox.showerror("Lỗi", "Ma trận A không khả nghịch!")
            return None
    except Exception as e:
        print("Error:", e)
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")
        return None


def selection():
    opinion = input("Nhập vào lựa chọn: Continue hoặc Exit? ")
    if opinion == "Continue":
        sopt = Input1()
        soan = Input2()
        sopt, soan = test_input(sopt, soan)
        A, B = Input3(sopt, soan)
        X = calculate(A, B)
        if X is not None:
            print('Nghiệm của hệ:', X)
        print("=====================")
        selection()
    elif opinion == "Exit":
        print("Cảm ơn bạn đã sử dụng!")
        exit()
    else:
        print("Bạn đã nhập sai lựa chọn, vui lòng nhập lại!")
        selection()


def set_focus():
    entry.focus()


win = Tk()
win.title("Giải hệ có n phương trình và n ẩn")
win.geometry('900x700')
win.configure(bg='lightblue')
win.resizable(False, False)

Label(win, text='Giải hệ phương trình n ẩn', font=('Arial', 13), bg='yellow', fg='black', height=2, relief='solid',
      borderwidth=2, width=40).place(x=250, y=0)

sopt = IntVar()
Label(win, text='Nhập số phương trình', font=('Arial', 13), bg='yellow', fg='black', height=1, relief='solid',
      borderwidth=2, width=30).place(x=250, y=60)
entry = Entry(win, textvariable=sopt, font=('Arial', 13), bg='yellow', fg='black', relief='solid', borderwidth=2,
              width=5)
entry.place(x=565, y=60)
win.after(0, set_focus)


def create():
    A = []
    entries_A = []
    B = []
    entries_B = []
    soan = sopt.get()

    matrix_A = []
    matrix_B = []

    a = 'abcdefghijklmnopqrstuvwxyz'
    a1 = list(a)
    for i in range(sopt.get()):
        A.append([])
        entries_A.append([])
        B.append([])
        entries_B.append([])
        matrix_A.append([])
        matrix_B.append([])
        for j in range(soan):
            A[i].append(DoubleVar())
            Label(win, background='lightblue', text=a1[j] + f'{i}', width=4).place(x=250 + 80 * i, y=110 + 30 * j)
            entries_A[i].append(Entry(win, textvariable=A[i][j], width=4))
            entries_A[i][j].place(x=280 + 83 * j, y=110 + 30 * i)
            matrix_A[i].append(A[i][j].get())
        B[i].append(DoubleVar())
        Label(win, background='lightblue', text=f' = ', width=4).place(x=280 + 83 * soan, y=110 + 30 * i)
        entries_B[i].append(Entry(win, textvariable=B[i][0], width=4))
        entries_B[i][0].place(x=310 + 83 * soan, y=110 + 30 * i)
        matrix_B[i].append(B[i][0].get())

    # Đánh dấu A và B là biến toàn cục để có thể truy cập từ hàm calculate
    create.A = np.array(matrix_A)
    create.B = np.array(matrix_B)  # Cập nhật create.A và create.B


def clear():
    Label(win, background='lightblue', width=180 * sopt.get(), height=20).place(x=240, y=100)


def calculate():
    global create
    A = create.A
    B = create.B

    print("Ma trận A:")
    print(A)

    sopt = A.shape[0]  # Lấy số phương trình từ kích thước của ma trận A

    if sopt == 1:
        # Trong trường hợp có chỉ một phương trình, tính kết quả cho phương trình đó
        if A[0, 0] != 0:
            x = B[0, 0] / A[0, 0]
            result_label.config(text=f'x = {x}')  # Cập nhật nội dung của Label để hiển thị kết quả
        else:
            messagebox.showerror("Lỗi", "Phương trình không có nghiệm!")
    else:
        try:
            if (np.linalg.det(A) != 0):
                X = np.dot(np.linalg.inv(A), B)
                result_text = 'Nghiệm của hệ:\n'
                for i in range(sopt):
                    result_text += f'x{i} = {X[i][0]}\n'
                result_label.config(text=result_text)  # Cập nhật nội dung của Label để hiển thị kết quả
            else:
                messagebox.showerror("Lỗi", "Ma trận A không khả nghịch!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {e}")


# Thêm một Label để hiển thị kết quả
result_label = Label(win, background='lightblue', text='', width=15)
result_label.place(x=50, y=450)

Button(win, text='Create', command=create, font=('Times new roman', 15), fg='black', bg='brown', width=6, height=2,
       relief='solid', borderwidth=2).place(x=250, y=510)
Button(win, text='Exit', command=exit, font=('Times new roman', 15), fg='black', bg='brown', width=6, height=2,
       relief='solid', borderwidth=2).place(x=350, y=510)
Button(win, text='Clear', command=clear, font=('Times new roman', 15), fg='black', bg='brown', width=6, height=2,
       relief='solid', borderwidth=2).place(x=445, y=510)
Button(win, text='Calculate', command=calculate, font=('Times new roman', 15), fg='black', bg='brown', width=7,
       height=2, relief='solid', borderwidth=2).place(x=537, y=510)

win.mainloop()