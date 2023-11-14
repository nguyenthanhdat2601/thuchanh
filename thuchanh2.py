import math
from tkinter import *
from tkinter.ttk import Combobox

class HinhHoc:
    def __init__(self, master):
        self.master = master
        master.title("Tính Diện Tích và Chu Vi Hình Học")

        # Tạo các biến lưu giá trị nhập từ người dùng
        self.loai_hinh_var = StringVar()
        self.loai_hinh_var.set("ChuNhat")  # Giá trị mặc định

        self.chieudai_var = DoubleVar()
        self.chieurong_var = DoubleVar()
        self.canha_var = DoubleVar()
        self.canhb_var = DoubleVar()
        self.canhc_var = DoubleVar()
        self.bankinh_var = DoubleVar()
        self.canhvuong_var = DoubleVar()
        self.cao_var = DoubleVar()

        # Tạo các widget và button
        self.label_loai_hinh = Label(master, text="Chọn Loại Hình:")
        self.combobox_loai_hinh = Combobox(master, textvariable=self.loai_hinh_var,
                                           values=["ChuNhat", "TamGiac", "Tron", "Vuong", "HinhTamGiac"])
        self.combobox_loai_hinh.bind("<<ComboboxSelected>>", self.cap_nhat_giao_dien)

        self.label_chieudai = Label(master, text="Chiều Dài:")
        self.entry_chieudai = Entry(master, textvariable=self.chieudai_var)

        self.label_chieurong = Label(master, text="Chiều Rộng:")
        self.entry_chieurong = Entry(master, textvariable=self.chieurong_var)

        self.label_canha = Label(master, text="Cạnh a:")
        self.entry_canha = Entry(master, textvariable=self.canha_var)

        self.label_canhb = Label(master, text="Cạnh b:")
        self.entry_canhb = Entry(master, textvariable=self.canhb_var)

        self.label_canhc = Label(master, text="Cạnh c:")
        self.entry_canhc = Entry(master, textvariable=self.canhc_var)

        self.label_bankinh = Label(master, text="Bán Kính:")
        self.entry_bankinh = Entry(master, textvariable=self.bankinh_var)

        self.label_canhvuong = Label(master, text="Cạnh Hình Vuông:")
        self.entry_canhvuong = Entry(master, textvariable=self.canhvuong_var)

        self.label_cao = Label(master, text="Chiều Cao Hình Tam Giác:")
        self.entry_cao = Entry(master, textvariable=self.cao_var)

        self.button_tinh = Button(master, text="Tính", command=self.tinh_toan)
        self.button_reset = Button(master, text="Reset", command=self.reset_gia_tri)

        self.result_label = Label(master, text="Kết Quả: ")

        # Đặt vị trí các widget trên grid
        self.label_loai_hinh.grid(row=0, column=0)
        self.combobox_loai_hinh.grid(row=0, column=1, columnspan=2)

        self.label_chieudai.grid(row=1, column=0)
        self.entry_chieudai.grid(row=1, column=1)

        self.label_chieurong.grid(row=2, column=0)
        self.entry_chieurong.grid(row=2, column=1)

        self.label_canha.grid(row=3, column=0)
        self.entry_canha.grid(row=3, column=1)

        self.label_canhb.grid(row=4, column=0)
        self.entry_canhb.grid(row=4, column=1)

        self.label_canhc.grid(row=5, column=0)
        self.entry_canhc.grid(row=5, column=1)

        self.label_bankinh.grid(row=6, column=0)
        self.entry_bankinh.grid(row=6, column=1)

        self.label_canhvuong.grid(row=7, column=0)
        self.entry_canhvuong.grid(row=7, column=1)

        self.label_cao.grid(row=8, column=0)
        self.entry_cao.grid(row=8, column=1)

        self.button_tinh.grid(row=9, column=0)
        self.button_reset.grid(row=9, column=1)

        self.result_label.grid(row=10, columnspan=3)

        # Lưu trữ giá trị mặc định để có thể đặt lại sau này
        self.gia_tri_mac_dinh = {
            "chieudai": self.chieudai_var.get(),
            "chieurong": self.chieurong_var.get(),
            "canha": self.canha_var.get(),
            "canhb": self.canhb_var.get(),
            "canhc": self.canhc_var.get(),
            "bankinh": self.bankinh_var.get(),
            "canhvuong": self.canhvuong_var.get(),
            "cao": self.cao_var.get()
        }

    def cap_nhat_giao_dien(self, event):
        # Cập nhật giao diện dựa trên loại hình được chọn
        loai_hinh = self.loai_hinh_var.get()
        self.entry_chieudai.config(state=NORMAL if loai_hinh in ["ChuNhat", "Vuong"] else DISABLED)
        self.entry_chieurong.config(state=NORMAL if loai_hinh == "ChuNhat" else DISABLED)
        self.entry_canha.config(state=NORMAL if loai_hinh in ["TamGiac", "HinhTamGiac"] else DISABLED)
        self.entry_canhb.config(state=NORMAL if loai_hinh in ["TamGiac", "HinhTamGiac"] else DISABLED)
        self.entry_canhc.config(state=NORMAL if loai_hinh in ["TamGiac", "HinhTamGiac"] else DISABLED)
        self.entry_bankinh.config(state=NORMAL if loai_hinh == "Tron" else DISABLED)
        self.entry_canhvuong.config(state=NORMAL if loai_hinh == "Vuong" else DISABLED)
        self.entry_cao.config(state=NORMAL if loai_hinh == "HinhTamGiac" else DISABLED)

    def tinh_toan(self):
        loai_hinh = self.loai_hinh_var.get()

        chieudai = self.chieudai_var.get()
        chieurong = self.chieurong_var.get()
        canha = self.canha_var.get()
        canhb = self.canhb_var.get()
        canhc = self.canhc_var.get()
        bankinh = self.bankinh_var.get()
        canhvuong = self.canhvuong_var.get()
        cao = self.cao_var.get()

        chuvi = 0
        dientich = 0

        if loai_hinh == "ChuNhat":
            chuvi = 2 * (chieudai + chieurong)
            dientich = chieudai * chieurong
        elif loai_hinh == "TamGiac":
            chuvi = canha + canhb + canhc
            p = chuvi / 2
            dientich = math.sqrt(p * (p - canha) * (p - canhb) * (p - canhc))
        elif loai_hinh == "Tron":
            chuvi = 2 * math.pi * bankinh
            dientich = math.pi * bankinh ** 2
        elif loai_hinh == "Vuong":
            chuvi = 4 * canhvuong
            dientich = canhvuong ** 2
        elif loai_hinh == "HinhTamGiac":
            chuvi = 3 * canha
            dientich = (canha * cao) / 2

        result_text = f"Chu Vi: {chuvi:.2f}, Diện Tích: {dientich:.2f}"
        self.result_label.config(text=result_text)

    def reset_gia_tri(self):
        # Đặt lại giá trị các ô nhập liệu về giá trị mặc định
        for key, value in self.gia_tri_mac_dinh.items():
            getattr(self, key + "_var").set(value)

        # Xóa kết quả trên nhãn
        self.result_label.config(text="Kết Quả: ")

        # Đặt lại giá trị loại hình về giá trị mặc định
        self.loai_hinh_var.set("ChuNhat")

        # Cập nhật giao diện dựa trên loại hình mặc định
        self.cap_nhat_giao_dien(None)

if __name__ == "__main__":
    root = Tk()
    app = HinhHoc(root)
    root.mainloop()
