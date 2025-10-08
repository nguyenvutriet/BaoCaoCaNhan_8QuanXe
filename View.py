# GUI 1
from tkinter import *
import numpy as np
import Controller
import tkinter as tk
from tkinter import ttk, messagebox
import time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Patch




class DatQuanXeView:
    def __init__(self):
        self.btns = [[None for _ in range(8)] for _ in range(8)]
        self.trangThaiMucTieu = [[None for _ in range(8)] for _ in range(8)]
        self.ThoiGianBatDau = None
        self.DangChayj = False
        self.job_timer = None
        self.luuLS = []
        self.Space = 0
        self.Timer = 0.0
        self.Algorithm = "Chưa chọn"
        self.index = 0
        self.FlagLoi = False
        self.FlagLuuY = False
        self.FlagColor = True
        self.controller = Controller.DatQuanXeController(self)


    def showView(self):
        self.root = Tk()
        self.root.title("Đặt 8 quân xe")
        self.root.geometry("1400x720")
        self.root.configure(bg="#F5F5F5")

        # ====== Frame chính ======
        frm_Main = Frame(self.root, width=1400, height=720, bg="#F5F5F5")
        frm_Main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # BẢNG ĐIỀU KHIỂN BÊN TRÁI 
        frm_BangTrai = Frame(frm_Main, bg="white")
        frm_BangTrai.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        # Tiêu đề
        lbl = Label(frm_BangTrai, text="♖ ĐẶT 8 QUÂN XE ♖", 
                    font=("Segoe UI", 28, "bold"),
                    fg="#2E86AB", bg="white")
        lbl.pack(pady=(0, 20))

        # Khung chứa các bàn cờ
        frm_KhungBanCo = Frame(frm_BangTrai, bg="white")
        frm_KhungBanCo.pack(fill=tk.BOTH, expand=True)

        frm_BanCoBanDau = Frame(frm_KhungBanCo, bg="#F5F5F5", relief=tk.RAISED, bd=2)
        frm_BanCoBanDau.pack(side=tk.LEFT, padx=10, pady=10)

        lbl_TTDB = Label(frm_BanCoBanDau, text="📍 TRẠNG THÁI BAN ĐẦU", 
                    font=("Segoe UI", 16, "bold"),
                    fg="#2E86AB", bg="#F5F5F5")
        lbl_TTDB.pack(pady=10)

        # ====== Bàn cờ ban đầu ======
        frm_BanCoChinh = Frame(frm_BanCoBanDau, width=500, height=500, bg="#CCCCCC", bd=3, relief="ridge")
        frm_BanCoChinh.pack(padx=15, pady=(0,15))

        arr_chu = np.array(['','A','B','C','D','E','F','G','H',''])
        for i in range(10):
            btn = Button(frm_BanCoChinh, text=str(arr_chu[i]), width=3,
                        bg='#F5F5F5', relief="flat", state="disabled",
                        font=("Segoe UI", 14, "bold"))
            btn.grid(row=0, column=i, sticky="nsew")

        for i in range(8):
            Button(frm_BanCoChinh, text=str(i+1), width=3, bg='#F5F5F5',
                relief="flat", state="disabled", font=("Segoe UI", 14, "bold")).grid(row=(8-i), column=0, sticky="nsew")
            Button(frm_BanCoChinh, text=str(i+1), width=3, bg='#F5F5F5',
                relief="flat", state="disabled", font=("Segoe UI", 14, "bold")).grid(row=(8-i), column=9, sticky="nsew")

        frm_VienTrong = Frame(frm_BanCoChinh)
        frm_VienTrong.grid(row=1, column=1, columnspan=8, rowspan=8, sticky="nsew")
        frm_VienTrong.grid_propagate(False)
        self.taoBanCo(frm_VienTrong)

        for i in range(10):
            Button(frm_BanCoChinh, text=str(arr_chu[i]), width=3,
                bg='#F5F5F5', relief="flat", state="disabled",
                font=("Segoe UI", 14, "bold")).grid(row=9, column=i, sticky="nsew")


        # Khung Bàn Cờ Mẫu
        frm_KhungMucTieu = Frame(frm_KhungBanCo, bg="#F5F5F5", relief=tk.RAISED, bd=2)
        frm_KhungMucTieu.pack(side=tk.LEFT, padx=10, pady=10)

        lbl_TTMT = Label(frm_KhungMucTieu, text="🎯 MỤC TIÊU", 
                    font=("Segoe UI", 16, "bold"),
                    fg="#2E86AB", bg="#F5F5F5")
        lbl_TTMT.pack(pady=10)

        # ====== Bàn cờ mục tiêu ======
        frm_BanCoMucTieu = Frame(frm_KhungMucTieu, width=500, height=500, bg="#CCCCCC", bd=3, relief="ridge")
        frm_BanCoMucTieu.pack(padx=15, pady=(0,15))

        arrchu = np.array(['','A','B','C','D','E','F','G','H',''])
        for i in range(10):
            btn = Button(frm_BanCoMucTieu, text=str(arrchu[i]), width=3,
                        bg='#F5F5F5', relief="flat", state="disabled",
                        font=("Segoe UI", 14, "bold"))
            btn.grid(row=0, column=i, sticky="nsew")

        for i in range(8):
            Button(frm_BanCoMucTieu, text=str(i+1), width=3, bg='#F5F5F5',
                relief="flat", state="disabled", font=("Segoe UI", 14, "bold")).grid(row=(8-i), column=0, sticky="nsew")
            Button(frm_BanCoMucTieu, text=str(i+1), width=3, bg='#F5F5F5',
                relief="flat", state="disabled", font=("Segoe UI", 14, "bold")).grid(row=(8-i), column=9, sticky="nsew")

        frm_Vien = Frame(frm_BanCoMucTieu)
        frm_Vien.grid(row=1, column=1, columnspan=8, rowspan=8, sticky="nsew")
        frm_Vien.grid_propagate(False)

        self.taoBanCoMucTieu(frm_Vien, self.controller.getMucTieu())

        for i in range(10):
            Button(frm_BanCoMucTieu, text=str(arr_chu[i]), width=3,
                bg='#F5F5F5', relief="flat", state="disabled",
                font=("Segoe UI", 14, "bold")).grid(row=9, column=i, sticky="nsew")
            

        # BẢNG ĐIỀU KHIỂN BÊN PHẢI 
        frm_BangPhai = Frame(frm_Main, bg="white", width=450)
        frm_BangPhai.pack(side=tk.RIGHT, fill=tk.BOTH)
        frm_BangPhai.pack_propagate(False)

        # Điều khiển thuật toán 
        frm_KhungDieuKhien = Frame(frm_BangPhai, bg="white", relief=tk.RAISED, bd=2)
        frm_KhungDieuKhien.pack(fill=tk.X, pady=(0,15))

        lbl_DKThuatToan = Label(frm_KhungDieuKhien, text="⚙️ ĐIỀU KHIỂN THUẬT TOÁN", 
                    font=("Segoe UI", 16, "bold"),
                    fg="#2E86AB", bg="white")
        lbl_DKThuatToan.pack(pady=10)

        #Khung lựa chọn thuật toán
        frm_ChonThuatToan = Frame(frm_KhungDieuKhien, bg="white")
        frm_ChonThuatToan.pack(fill=tk.X, padx=20, pady=10)

        lbl_ChonTT = Label(frm_ChonThuatToan, text="Chọn thuật toán:", 
                    font=("Segoe UI", 12, "bold"),
                    fg="#2E86AB", bg="white")
        lbl_ChonTT.pack(anchor=tk.W)

        self.cbb_ThuatToan = ttk.Combobox(frm_ChonThuatToan, values=["","I. Uninformed Search Algorithms", 
                                                   "Breadth First Search", "Depth First Search","Iterative Deepening Search With DLS", "Iterative Deepening Search With DFS", "Depth Limited Search", "Uniform Cost Search",
                                                   "II. Informed Search Algorithms", 
                                                   "Greedy Search","A* Search", 
                                                   "III. Local search",
                                                    "Hill Climbing", "Simulated Annealing", "Beam Search", "Genetic Algorithms",
                                                    "IV. Search In Complex Environment",
                                                    "Recursive And Or Tree Search", "Search in an unobservable environment", "Search In Partially Observable Environment",
                                                    "V. Constraint Satisfaction Search",
                                                    "CSP BackTracking",
                                                    "CSP Forward Checking",
                                                    "CSP Ac-3 Art Concistency",
                                                    "VI. Adversarial Search",
                                                    "MiniMax Algorithm",
                                                    "Alpha-Beta Pruning"], font=("Segoe UI", 12), width=20, state="readonly")
        self.cbb_ThuatToan.pack(fill=tk.X, pady=5)

        # Các nút điều khiển 
        frm_KhungNut = Frame(frm_KhungDieuKhien, bg="white")
        frm_KhungNut.pack(fill=tk.X, padx=20, pady=15)

        btn_Run = Button(frm_KhungNut, text="▶️ CHẠY", 
                         font=("Segoe UI", 8, "bold"), 
                         bg="#10b981", fg="white", 
                         activebackground="#059669", 
                         activeforeground="white", 
                         relief=tk.FLAT, cursor="hand2", command=lambda: self.controller.suKien(self.cbb_ThuatToan.get()))
        btn_Run.pack(side=tk.LEFT, padx=5, ipadx=15, ipady=8)

        btn_Reset = Button(frm_KhungNut, text="🔄 RESET",
            font=("Segoe UI", 8, "bold"),
            bg="#6366f1",
            fg="white",
            activebackground="#4f46e5",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2", command=self.btnReset)
        btn_Reset.pack(side=tk.LEFT, padx=5, ipadx=15, ipady=8)

        btn_ViewGraph =  Button(frm_KhungNut, text="📊 XEM ĐT",
            font=("Segoe UI", 8, "bold"),
            bg="#8b5cf6",
            fg="white",
            activebackground="#7c3aed",
            activeforeground="white",
            relief=tk.FLAT,
            cursor="hand2", command=self.doThiDanhGia)
        btn_ViewGraph.pack(side=tk.LEFT, padx=5, ipadx=15, ipady=8)

        # Thông Tin
        frm_KhungThongTin = Frame(frm_BangPhai, bg="white", relief=tk.RAISED, bd=2)
        frm_KhungThongTin.pack(fill=tk.X, pady=(0, 15))

        lbl_TrangThaiHT = Label(frm_KhungThongTin, text="📊 TRẠNG THÁI HIỆN TẠI", 
                    font=("Segoe UI", 16, "bold"),
                    fg="#2E86AB", bg="white")
        lbl_TrangThaiHT.pack(pady=10)

        self.frm_NoiDungTT = Frame(frm_KhungThongTin, bg="white")
        self.frm_NoiDungTT.pack(fill=tk.X, padx=20, pady=(0, 15))

        self.lbl_TT = Label(self.frm_NoiDungTT, text="Thuật toán: Chưa chạy",
        font=("Segoe UI", 12, "bold"),
        bg="white",
        fg="#94a3b8",
        anchor=tk.W)
        self.lbl_TT.pack(fill=tk.X, pady=3)

        self.lbl_ThoiGianChay = Label(self.frm_NoiDungTT, text="⏱️ Thời gian: 0.00s",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg="#60a5fa",
            anchor=tk.W)
        self.lbl_ThoiGianChay.pack(fill=tk.X, pady=3)

        self.lbl_SoTT = Label(self.frm_NoiDungTT, text="🔢 Trạng thái sinh ra: 0",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg="#fbbf24",
            anchor=tk.W)
        self.lbl_SoTT.pack(fill=tk.X, pady=3)

        nganCach = ttk.Separator(frm_KhungThongTin, orient="horizontal")
        nganCach.pack(fill=tk.X, padx=20, pady=(0, 15))

        lbl_LS = Label(frm_KhungThongTin,text="📜 LỊCH SỬ THỰC THI",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#f472b6" )
        lbl_LS.pack(fill=tk.X, padx=20, pady=(0, 15))

        frm_HopLS = Frame(frm_KhungThongTin, bg="white")
        frm_HopLS.pack(fill=tk.X, padx=20, pady=(0, 15))

        src_ThanhCuon = Scrollbar(frm_HopLS)
        src_ThanhCuon.pack(side=tk.RIGHT, fill=tk.Y)

        self.lbx_DSLS = Listbox(frm_HopLS, font=("Consolas", 9),
            bg="white",
            fg="#20252b",
            selectbackground="#6366f1",
            selectforeground="white",
            relief=tk.FLAT,
            yscrollcommand=src_ThanhCuon.set)
        self.lbx_DSLS.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        src_ThanhCuon.config(command=self.lbx_DSLS.yview)

        self.root.mainloop()

    def taoBanCo(self, frm):
        for i in range(8):
            frm.rowconfigure(i, weight=1)
            frm.columnconfigure(i, weight=1)
            for j in range(8):
                bg = "#F7DCB9" if (i+j) % 2 == 0 else "#A97155"
                self.btns[i][j] = Button(frm, width=4, text="", background=bg,
                                        relief="flat", state="disabled",
                                        font=("Segoe UI Symbol", 18, "bold"))
                self.btns[i][j].grid(row=i, column=j, sticky="nsew")

    def taoBanCoMucTieu(self, frm, arrMucTieu):
        for i in range(8):
            frm.rowconfigure(i, weight=1)
            frm.columnconfigure(i, weight=1)
            for j in range(8):
                bg = "#F7DCB9" if (i+j) % 2 == 0 else "#A97155"
                self.trangThaiMucTieu[i][j] = Button(frm, width=4, text="", background=bg,
                                        relief="flat", state="disabled",
                                        font=("Segoe UI Symbol", 18, "bold"))
                self.trangThaiMucTieu[i][j].grid(row=i, column=j, sticky="nsew")

                if arrMucTieu[i][j] == 1:
                    self.trangThaiMucTieu[i][j].config(text="♖")

    def inBanCoNguoiChoi(self, arr, c=None):
        for i in range(len(arr)):
            self.btns[arr[i][0]][arr[i][1]].config(text="♖")
            self.root.after(70)
            self.root.update_idletasks()

    def cauHinhThongTin(self, thuaToan):
        self.Algorithm = thuaToan
        self.lbl_TT.config(text= f"Thuật toán: {thuaToan}")
        self.root.update()

    def batDauDemGio(self):
        self.start_time = time.time()
        self.running = True
        self.capNhatThoiGian()

    def capNhatThoiGian(self):
        if self.running:
            elapsed = time.time() - self.start_time
            self.Timer = elapsed
            self.lbl_ThoiGianChay.config(text=f"⏱️ Thời gian: {elapsed:.2f}s")
            # gọi lại sau 100ms
            self.job_timer = self.root.after(100, self.capNhatThoiGian)

    def dungDemGio(self):
        self.running = False
        if self.running:
            self.root.after_cancel(self.job_timer)
            self.job_timer = None
            self.root.update()

        self.index += 1
        self.ghiLichSu()
        

    def reSetThongTin(self):
        self.lbl_ThoiGianChay.config(text=f"⏱️ Thời gian: 0.00s")
        self.lbl_TT.config(text="Thuật toán: Chưa chạy")
        self.lbl_SoTT.config(text="🔢 Trạng thái sinh ra: 0")

        if self.FlagLoi:
            self.lbl_Loi.destroy()
            del self.lbl_Loi
            self.FlagLoi = False

        if self.FlagLuuY:
            self.lbl_LuuY.destroy()
            del self.lbl_LuuY
            self.FlagLuuY = False
        
        for i in range(8):
            for j in range(8):
                self.btns[i][j].config(text="")

    def setSoTrangThai(self, soTT):
        self.Space = soTT
        self.lbl_SoTT.config(text=f"🔢 Trạng thái sinh ra: {soTT}")
        self.root.update()

    def loiOrLuuY(self, msg, str):

        if msg == "Lỗi":
            self.FlagLoi = True
            self.lbl_Loi = Label(self.frm_NoiDungTT,text=f"⚠️ Lỗi: {str}",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg="#ff2e51",
            anchor=tk.W)
            self.lbl_Loi.pack(fill=tk.X, pady=3)
        elif msg == "Lưu ý: ":
            self.FlagLuuY = True
            self.lbl_LuuY = Label(self.frm_NoiDungTT,text=f"📝 Lưu ý: {str}",
            font=("Segoe UI", 12, "bold"),
            bg="white",
            fg="#ff7a32",
            anchor=tk.W)
            self.lbl_LuuY.pack(fill=tk.X, pady=3)

    def ghiLichSu(self):
        self.lbx_DSLS.insert(END, f"#{self.index}: {self.Algorithm}\n")
        self.lbx_DSLS.insert(END, f"Time: {self.Timer:.2f} - Space: {self.Space}\n")

        self.luuLS.append([f"{self.Algorithm}", self.Timer, self.Space, self.FlagColor])

    def btnReset(self):
        self.reSetThongTin()
        self.dungDemGio()
        self.lbx_DSLS.delete(0, tk.END)
        self.cbb_ThuatToan.current(0)
        self.luuLS.clear()
        self.index = 0


    def doThiDanhGia(self):
        if len(self.luuLS) > 0:
            arrName = []
            arrX = []
            arrY = []
            arrColors = []
            for index, item in enumerate(self.luuLS):
                if item[0] in arrName:
                    for i in range(len(arrName)):
                        if arrName[i] == item[0] and arrX[i] > item[1]:
                            arrX[i] = item[1]
                            arrY[i] = item[2]
                            if item[3]:
                                arrColors[i] = "blue"
                            elif item[3] == False:
                                arrColors[i] = "red"
                            elif item[3] == None:
                                arrColors[i] = "orange"
                            break
                    continue
                arrName.append(item[0])   # tên thuật toán
                arrX.append(item[1])      # thời gian
                arrY.append(item[2])      # không gian
                if item[3]:
                    arrColors.append("blue")
                elif item[3] == False:
                    arrColors.append("red")
                elif item[3] == None:
                    arrColors.append("orange")
            windownNew = Tk()
            windownNew.title("Đánh giá thuật toán")

            fig, ax = plt.subplots(figsize=(10,7))

            # dùng index cho vị trí cột
            x_pos = range(len(arrName))  

            bars = ax.bar(x_pos, arrY, width=0.4, color=arrColors)
            ax.set_ylim(0, max(arrY) * 1.3)
            for bar, company in zip(bars, arrName):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2, height + 0.2,
                        company, ha='center', va='bottom', fontsize=9)

            ax.set_xlabel("Thuật toán (thời gian chạy)")
            ax.set_ylabel("Không gian")
            ax.set_title("Biểu đồ đánh giá thuật toán")

            # set nhãn trục X hiển thị thời gian
            ax.set_xticks(x_pos)
            ax.set_xticklabels([f"{d:.2f}" for d in arrX], rotation=45)

            # Chú thích
            legend_elements = [
                Patch(facecolor='blue', label='Tìm thấy mục tiêu'),
                Patch(facecolor='red', label='Không tìm thấy mục tiêu'),
                Patch(facecolor='orange', label='Tìm một tập hoặc một trạng thái hợp lệ.')
            ]
            ax.legend(handles=legend_elements, loc='best')

            canvas = FigureCanvasTkAgg(fig, master=windownNew)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

            windownNew.mainloop()
        else:
            messagebox.showinfo("THÔNG BÁO", "Không có dữ liệu để hiển thị đồ thị.")




                

            








        




    







