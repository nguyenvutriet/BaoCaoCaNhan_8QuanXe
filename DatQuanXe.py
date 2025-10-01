from tkinter import *
import numpy as np
from collections import deque
import copy
from queue import PriorityQueue
from tkinter import ttk
import math
import random
import time 

root = Tk()
root.title("Đặt 8 quân xe")
root.geometry("1400x695")

btns = [[None for _ in range(8)] for _ in range(8)]




# 1. NHỮNG HÀM PHỤ
def taoBanCo():
    for i in range(8):
        frm_VienTrong.rowconfigure(i, weight=1, uniform="rowv")
        frm_VienTrong.columnconfigure(i, weight=1, uniform="colv")
        for j in range(8):
            if (i+j) % 2 == 0:
                bg = "#F7C899"
            else:
                bg = "#CA8745"

            btns[i][j] = Button(
                frm_VienTrong, width=3, text="", background=bg,
                relief="flat", state="disabled", font=("Segoe UI Symbol", 16, "bold")
            )
            btns[i][j].grid(row=i, column=j, sticky="nsew")

def inBanCoNguoiChoi(arr, c=None):
    for i in range(8):
        for j in range(8):
            if arr[i][j] == 1:
                
                if c != None:
                    text_Area.insert(END, f"Quân xe thứ: {i+1} - Chi Phí: {c[j][0]}/ vị trí: ({i},{j})\n")
                else:
                    text_Area.insert(END, f"Quân xe thứ: {i+1}/ vị trí: ({i},{j})\n")
                
                btns[i][j].config(text="♖")
                root.after(70)
                root.update_idletasks()
            else:
                btns[i][j].config(text="")
                root.after(70)
                root.update_idletasks()

def trangThaiAnToan(arr_):
    for i in range(8):
        for j in range(8):
            if arr_[i][j] == 1:
                anNgang = np.sum(arr_[i, :] == 1)
                anDoc = np.sum(arr_[:, j] == 1)
                if anNgang > 1 or anDoc > 1:
                    return False
        
    return True

def kiemTraTrangThaiDich(arr_):
    soLuong = np.sum(arr_ == 1)
    if soLuong == 8:
        #inBanCoNguoiChoi(arr_)
        # tìm kiếm đến mục tiêu cuối cùng
        if np.array_equal(arr_, arr_MucTieu):
            return True
        # chỉ tìm kiếm đến khi nào đạt được trạng thái ai toàn
        #return trangThaiAnToan(arr_)
        else:
            #inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
            return False
    else: 
        return False
    
def kiemTraTrangThaiDich_Ver2(arr_):
    soLuong = np.sum(arr_ == 1)
    if soLuong == 8:
        #inBanCoNguoiChoi(arr_)
        # chỉ tìm kiếm đến khi nào đạt được trạng thái ai toàn
        return trangThaiAnToan(arr_)
    return False

def ResultAndOrTree(state, action):
    states = deque()
    for row in range(8):
        stateCopy = copy.deepcopy(state)
        stateCopy[row][action] = 1
        if trangThaiAnToan(stateCopy) == False:
            stateCopy[row][action] = 0
        else:
            states.append(stateCopy)

    return states

# Hàm tính nhiệu độ T 
def schedule(t):
    return ((0.8)**t)*50
    
# khoảng cách từ vị trí hiện tại đến vị trí (8,8)
def chiPhiHeruristics(row, j):
    return round(math.sqrt((row-8)**2+(j-8)**2), 0)

# khoảng cách từ vị trí (0,0) đến vị trí hiện tại
def chiPhi_PathCost(row, col, x_old, y_old):
    return round(math.sqrt((row-x_old)**2+(col-y_old)**2), 0)

def khoiTaoQuanThe():
    N = 6
    queue = []
    while N > 0:
        arrCaThe1D = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7) ,random.randint(0, 7), random.randint(0, 7),random.randint(0, 7)]
        arrCaThe2D = np.zeros((8,8), dtype=int)
        for i in range(8):
            arrCaThe2D[arrCaThe1D[i]][i] = 1
        soCapKhongAnNhau = doFitness(arrCaThe1D)
        queue.append([arrCaThe2D, arrCaThe1D, soCapKhongAnNhau])
        N -= 1

    return queue

def chonLocCacCaThe(quanThe):
    quanThe = list(quanThe)
    quanThe.sort(key=lambda x: x[2])
    chonLoc = [quanThe[5], quanThe[4]]
    indexRamdon = random.randint(0, 3)
    chonLoc.append(quanThe[indexRamdon])
    return chonLoc

def doFitness(arr1D):
    fitness = 0
    for i in range(8):
        for j in range(i+1, 8):
            if ((arr1D[i] - arr1D[j]) != 0):
                fitness += 1
    return fitness

def Dat(niemTin: deque, notFix=None):
    A = deque()

    for i in niemTin:
        for col in range(8):
            if notFix != None and col == notFix:
                continue
            Stop = False
            if 1 not in np.array(i)[:, col]:
                for row in range(8):
                    if notFix != None and row == notFix: 
                        continue
                    state = copy.deepcopy(i)
                    state[row][col] = 1
                    if trangThaiAnToan(np.array(state)) == False:
                        state[row][col] = 0
                    else:
                        A.append(state)
                        Stop = True
                        break
                    
            if Stop:
                break
    
    return A                     

# chỉ di chuyển những bàn cờ còn thiếu quân xe và các bước di chuyển phải hợp lệ
def diChuyen(niemTin: deque, notFix=None):
    B = deque()
    for i in niemTin:
        if np.sum(i == 1) == 8:
            continue

        Stop = False
        for row in range(8):
            if notFix != None and row == notFix:
                continue
            for col in range(8):
                if notFix != None and col == notFix:
                    continue
                if i[row][col] == 1:
                    # di chyển san phải
                    if (col + 1) < 8 and i[row][col+1] == 0:
                        stateCopy = copy.deepcopy(i)
                        stateCopy[row][col] = 0
                        stateCopy[row][col+1] = 1
                        if trangThaiAnToan(np.array(stateCopy)):
                            B.append(stateCopy)
                            Stop = True
                            break
                    # di chuyển sang trái
                    if (col - 1) >= 0 and i[row][col-1] == 0:
                        stateCopy = copy.deepcopy(i)
                        stateCopy[row][col] = 0
                        stateCopy[row][col-1] = 1
                        if trangThaiAnToan(np.array(stateCopy)):
                            B.append(stateCopy)
                            Stop = True
                            break
                    # di chuyển lên xuống
                    if (row + 1) < 8 and i[row+1][col] == 0:
                        stateCopy = copy.deepcopy(i)
                        stateCopy[row][col] = 0
                        stateCopy[row+1][col] = 1
                        if trangThaiAnToan(np.array(stateCopy)):
                            B.append(stateCopy)
                            Stop = True
                            break
                    # di chuyển lên 
                    if (row - 1) >= 0 and i[row-1][col] == 0:
                        stateCopy = copy.deepcopy(i)
                        stateCopy[row][col] = 0
                        stateCopy[row-1][col] = 1
                        if trangThaiAnToan(np.array(stateCopy)):
                            B.append(stateCopy)
                            Stop = True
                            break
            
            if Stop:
                break

    return B

def Herurictics_PartiallyObservable(niemTin: deque):
    Cost = 0
    for item in niemTin:
        soQuanDaDat = np.sum(item == 1)
        soQuanChuaDat = 8 - soQuanDaDat
        Cost += round(math.sqrt((8-soQuanChuaDat)**2 + (8-soQuanDaDat)**2), 2)

    return Cost 

def F(tapGiaTri, row, col):
    tapGTNew = []
    for i in tapGiaTri:
        if i[0] != row and i[1] != col:
            tapGTNew.append(i)
    return tapGTNew        



    


def suKienNhanNut():
    thuatToan = cbb_ThuatToan.get()
    text_Area.config(state="normal")
    for i in range(8):
        for j in range(8):
            btns[i][j].config(text="")
    if thuatToan == "Greedy Search":
        text_Area.insert(END, "Thuật toán: Greedy Search\nĐang chạy\n")
        start = time.time()
        GreedySearch()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Breadth First Search":
        text_Area.insert(END, "Thuật toán: Breadth First Search\nĐang chạy\n")
        start = time.time()
        BreadthFirstSearch()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Depth First Search":
        text_Area.insert(END, "Thuật toán: Depth First Search\nĐang chạy\n")
        start = time.time()
        DepFirstSearch()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Iterative Deepening Search With DLS":
        text_Area.insert(END, "Thuật toán: Iterative Deepening Search With DLS\nĐang chạy\n")
        start = time.time()
        IterativeDeepening_DLS()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Iterative Deepening Search With DFS":
        text_Area.insert(END, "Thuật toán: Iterative Deepening Search With DFS\nĐang chạy\n")
        start = time.time()
        IterativeDeepening_DFS()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Depth Limited Search":
        text_Area.insert(END, "Thuật toán: Depth Limited Search\nĐang chạy\n")
        start = time.time()
        DepthLimitedSearch(np.zeros((8,8), dtype=int), 0, 8)
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Uniform Cost Search":
        text_Area.insert(END, "Thuật toán: Uniform Cost Search\nĐang chạy\n")
        start = time.time()
        UniformCostSearch()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "A* Search":
        text_Area.insert(END, "Thuật toán: A* Search\nĐang chạy\n")
        start = time.time()
        AStarSearch()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Hill Climbing":
        text_Area.insert(END, "Thuật toán: Hill Climbing\nĐang chạy\n")
        start = time.time()
        if HillClimbing() == None:
            text_Area.insert(END, "Không thể sinh tiếp trạng thái!!\n")
        elif HillClimbing() == False:
            text_Area.insert(END, "Không có trạng thái nào tốt hơn trạng thái hiện tại!!\n")
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Simulated Annealing":
        text_Area.insert(END, "Thuật toán: Simulated Annealing\nĐang chạy\n")
        start = time.time()
        SimulatedAnnealing()
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Beam Search":
        text_Area.insert(END, "Thuật toán: Beam Search\nĐang chạy\n")
        start = time.time()
        if BeamSearch() != None:
            end = time.time()
            text_Area.insert(END, "Đã chạy xong!!\n")
            text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
            text_Area.update()
            text_Area.config(state="disabled")
        else:
            end = time.time()
            text_Area.insert(END, "Kết thúc!!\nKhông tìm thấy mục tiêu!\n")
            text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
            text_Area.update()
            text_Area.config(state="disabled")
    elif thuatToan == "Genetic Algorithms":
        text_Area.insert(END, "Thuật toán: Genetic Algorithms\nĐang chạy\nGiới hạn mã Gen = 1000\n")
        start = time.time()
        if GeneticAlgorithms() == None:
            text_Area.insert(END, "Chưa tìm thấy mục tiêu!\n")
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Recursive And Or Tree Search":
        text_Area.insert(END, "Thuật toán: Recursive And Or Tree Search\n(Lưu ý: Chỉ tìm thấy cách đặt nào hợp lý,\nkhông tìm ra một mục tiêu cụ thể)\nĐang chạy\n")
        start = time.time()
        if RecursiveAndOrTreeSearch_DFS() is False:
            text_Area.insert(END, "Không tìm thấy!!\n")
        else:
            text_Area.insert(END, "Đã tìm thấy một tập các trạng thái hợp lý\n")
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Search in an unobservable environment":
        text_Area.insert(END, "Thuật toán: Search in an unobservable environment\n(lưu ý: Chỉ tìm thấy tập các trạng thái hợp lệ\nkhông cần tìm theo bàn cờ mẫu)\nĐang chạy\n")
        start = time.time()
        if SearchUnobservable_DFS() is not None:
            text_Area.insert(END, "Đã tìm thấy một tập các trạng thái hợp lệ\n(chỉ in 1 trạng thái trong tập)\n")
        else:
            text_Area.insert(END, "Trạng thái niềm tin kết thúc chưa đa dạng\nnên không thể tìm thấy\n")
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "Search In Partially Observable Environment":
        text_Area.insert(END, "Thuật toán: Search In Partially Observable Environment WITH Greedy Search\n(Lưu ý: Chỉ tìm thấy tập nào giống tập mục tiêu và\nbàn cờ in bên trên chỉ là phần tử trong tập đó)\nĐang chạy\n")
        start = time.time()
        if PartiallyPbservable_GreedySearch() is not None:
            text_Area.insert(END, "Đã tìm thấy tập trạng thái hợp lệ\n")
        else:
            text_Area.insert(END, "Không tìm thấy trạng thái hợp lệ")
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "CSP BackTracking":
        text_Area.insert(END, "Thuật toán: CSP BackTracking\nĐang chạy\n")
        start = time.time()
        if CSP_Backtracking() is not None: 
            text_Area.insert(END, "Đã tìm thấy mục tiêu!!\n")
        else:
            text_Area.insert(END, "Không tìm thấy mục tiêu!!\n")
        start = time.time()
        text_Area.insert(END,"Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    elif thuatToan == "CSP Forward Checking":
        text_Area.insert(END, "Thuật toán: CSP Forward Checking\nĐang chạy\n")
        start = time.time()
        if CSP_FORWARDCHECKING() is not None:
            text_Area.insert(END, "Đã tìm thấy mục tiêu!!\n")
        else:
            text_Area.insert(END, "Không tìm thấy mục tiêu!!\n")
        end = time.time()
        text_Area.insert(END, "Đã chạy xong!!\n")
        text_Area.insert(END, f"Tổng thời gian chạy: {end-start:.2f}s\n")
        text_Area.update()
        text_Area.config(state="disabled")
    


# 2. THUẬT TOÁN TÌM KIẾM
# 2.1 LOCAL SEARCH
def HillClimbing():
    start = np.zeros((8,8), dtype=int)
    row = 0
    cPBanDau = 100
    thuTu = 0
    while True:
        queue = PriorityQueue()
        #queue.put((cPBanDau, row, start))

        # Sinh các trạng thái lân cận
        for col in range(8):
            state =  copy.deepcopy(start)
            state[row][col] = 1
            if(trangThaiAnToan(state) == False):
                state[row][col] = 0
            else:
                thuTu += 1
                if (row + 1) <= 8:
                    queue.put((chiPhiHeruristics(row, col), thuTu, row+1, state))

        if queue.empty():
            inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
            return None
        
        cP, tt, r, stateBest = queue.get()

        if (kiemTraTrangThaiDich(stateBest)):
            inBanCoNguoiChoi(stateBest)
            return True

        if cP >= cPBanDau:
            inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
            return False

        start = stateBest
        cPBanDau = cP
        row = r

def SimulatedAnnealing():
    start = np.zeros((8,8), dtype=int)
    row = 0
    chiPhi = 8*8
    thuTu = 0
    t = 1
    while True:
        if kiemTraTrangThaiDich(start):
            inBanCoNguoiChoi(start)
            return
        T = schedule(t)
        if T == 0:
            inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
            print("Không tìm thấy mục tiêu")
            return
        queue = PriorityQueue()
        l = []
        if row < 8:
            for col in range(8):
                state = copy.deepcopy(start)
                state[row][col] = 1
                if trangThaiAnToan(state) == False:
                    state[row][col] = 0
                else:
                    if (row + 1) <= 8:
                        thuTu += 1
                        chiPhiState = chiPhiHeruristics(row, col)
                        queue.put((chiPhiState, thuTu, row + 1, state))
                        l.append([chiPhiState,row + 1, state])
                    
        if queue.empty():
            inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
            print("Không thể sinh tiếp trạng thái lân cận")
            return
        
        cp, tt, r, stateBest = queue.get()
        
        if (cp - chiPhi) < 0:
            start = stateBest
            row = r
            chiPhi = cp
        else:
            index = random.uniform(0, len(l)-1)
            index = int(index)
            c = l[index][0]
            ro = l[index][1]
            stateBad = l[index][2]
            p = math.e**(-(c-chiPhi)/T)
            p_Random = random.uniform(0,1)
            if p > p_Random:
                start = stateBad
                row = ro
                chiPhi = c

        print(start , "  ", chiPhi, "  ", row)
        t = t + 1

def BeamSearch():
    arrBanDau = np.zeros((8,8), dtype=int)
    row = 0
    cp = 20
    queue = deque()
    k = 2
    queue.append((cp, row, arrBanDau))
    while len(queue) != 0:
        chP, r, state = queue.popleft()
        if kiemTraTrangThaiDich(state):
            inBanCoNguoiChoi(state)
            return
        
        if r == 8:
            continue

        sinhTT = PriorityQueue()
        thuTu = 0
        for col in range(8):
            stateNew = copy.deepcopy(state)
            stateNew[row][col] = 1
            if trangThaiAnToan(stateNew) == False:
                stateNew[row][col] = 0
            else:
                cP = chiPhiHeruristics(row, col)
                thuTu += 1
                if (row + 1) <= 8:
                    sinhTT.put((cP, thuTu,row + 1, stateNew))
        
        index = 0
        while index < k and not sinhTT.empty():
            c, t, r, stateBest = sinhTT.get()
            queue.append((c, r, stateBest))
            index += 1

    inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
    return None

def GeneticAlgorithms():
    # Khởi tạo ngẫu nhiên một quần thể có 6 cá thể và tính giá trị fitness cho từng cá thể 
    queueQuanThe = khoiTaoQuanThe()
    maxGen = 1000
    Gen = 0
    while Gen < maxGen:
        # Chọn lọc cả thể 
        quanTheChonLoc =  chonLocCacCaThe(queueQuanThe)

        # Đem cá thể chọn lọc đi lai
        quanTheMoi = []
        Flag = False
        for i in range(len(quanTheChonLoc)):
            for j in range(i+1, len(quanTheChonLoc)):
                # bắt đầu quá trình lai 
                rateLai = 0.65
                for k in range(8):
                    r = random.random()
                    if r < rateLai:
                        temp2D = quanTheChonLoc[i][0][:, k]
                        quanTheChonLoc[i][0][:, k] = quanTheChonLoc[j][0][:, k]
                        quanTheChonLoc[j][0][:, k] = temp2D

                        temp1D = quanTheChonLoc[i][1][k]
                        quanTheChonLoc[i][1][k] = quanTheChonLoc[j][1][k]
                        quanTheChonLoc[j][1][k] = temp1D

                        quanTheChonLoc[i][2] = doFitness(quanTheChonLoc[i][1])
                        quanTheChonLoc[j][2] = doFitness(quanTheChonLoc[j][1])


                # Bắt đầu đột biến gen
                rateDotBien = 0.05
                for m in range(8):
                    c1 = random.random()
                    c2 = random.random()
                    if c1 < rateDotBien:
                        index = random.randint(0, 7)
                        quanTheChonLoc[i][0][:, m] = 0
                        quanTheChonLoc[i][0][index][m] = 1
                        
                        quanTheChonLoc[i][1][m] = index

                        quanTheChonLoc[i][2] = doFitness(quanTheChonLoc[i][1])

                    if c2 < rateDotBien:
                        index = random.randint(0, 7)
                        quanTheChonLoc[j][0][:, m] = 0
                        quanTheChonLoc[j][0][index][m] = 1

                        quanTheChonLoc[j][1][m] = index

                        quanTheChonLoc[j][2] = doFitness(quanTheChonLoc[j][1])
                
                
                quanTheMoi.append(quanTheChonLoc[i])
                quanTheMoi.append(quanTheChonLoc[j])
                if len(quanTheMoi) == 6:
                    Flag = True
                    break
            if Flag:
                break
        
        # kiểm tra trong quần thể mới có cá thể mục tiêu không 
        for i in quanTheMoi:
            if kiemTraTrangThaiDich(i[0]):
                inBanCoNguoiChoi(i[0])
                return
        queueQuanThe = quanTheMoi
        Gen += 1
    return None

# 2.2. UNINFORMED SEARCH ALGORITHMS
# Cách 1: Iterative Deepening Search với Depth Limited Search
def IterativeDeepening_DLS():
    for depth in range(10):
        result = DepthLimitedSearch(np.zeros((8,8), dtype=int), 0, depth)
        if result is None:
            inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
        elif np.array_equal(result, np.zeros((8,8), dtype=int)):
            inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
        else: 
            inBanCoNguoiChoi(result)

# Cách 2: Iterative Deepening Search với Depth First Search 
def IterativeDeepening_DFS():
    for depth in range(10):
        stack = deque()
        arrBanDau = np.zeros((8,8), dtype=int)
        stack.append((arrBanDau, 0))
        while len(stack) != 0:
            state, row = stack.pop()
            
            if kiemTraTrangThaiDich(state):
                inBanCoNguoiChoi(state)
                #return state
                return
            
            if row == 8:
                continue

            if row < depth:
                if 1 not in state[row, :]:
                    for j in range(8):
                        stateNew = copy.deepcopy(state)
                        stateNew[row][j] = 1
                        if trangThaiAnToan(stateNew) == False:
                            stateNew[row][j] = 0
                        else:
                            if(row + 1) <= 8:
                                stack.append((stateNew, row + 1))           
                else:
                    if(row + 1) <= 8:
                        stack.append((state, row + 1))
                #root.after(50)
            #root.update_idletasks()
        #return None

def DepthLimitedSearch(arr, row, limit):
    result = RecusiveDLS(arr, row, limit)
    '''
    if result is None:
        inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
    elif np.array_equal(result, np.zeros((8,8), dtype=int)):
        inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
    else: 
        inBanCoNguoiChoi(result)
        tinhChiPhi(result)
    '''
    return result

def RecusiveDLS(arr, row, limit):
    if kiemTraTrangThaiDich(arr):
        return arr
    elif limit == 0: 
        return np.zeros((8,8), dtype=int)
    else:
        cutof_occurred = False
        for i in range(8):
            stateNew = copy.deepcopy(arr)
            stateNew[row][i] = 1
            if trangThaiAnToan(stateNew) == False:
                stateNew[row][i] = 0
            else:
                if (row + 1) <= 8:
                    result = RecusiveDLS(stateNew, row + 1, limit - 1)
                    if np.array_equal(result, np.zeros((8,8), dtype=int)):
                        cutof_occurred = True
                    elif result is not None: 
                        return result
                
        if cutof_occurred:
            return np.zeros((8,8), dtype=int)
        else:
            return None

def BreadthFirstSearch():
    queue = deque()
    arrBanDau = np.zeros((8,8), dtype=int)
    queue.append((arrBanDau, 0))
    print(len(queue))
    print("Mảng ban đầu: ", arrBanDau)
    while len(queue) != 0:
        state, row = queue.popleft()
        
        if kiemTraTrangThaiDich(state):
            inBanCoNguoiChoi(state)
            return state
        
        if row == 8:
            continue
        
        if 1 not in state[row, :]:
            for j in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][j] = 1
                if trangThaiAnToan(stateNew) == False:
                    stateNew[row][j] = 0
                else:
                    if(row + 1) <= 8:
                        queue.append((stateNew, row + 1))
        else:
            if(row + 1) <= 8:
                queue.append((state, row + 1))

        #root.after(50)
        root.update_idletasks()
    return None

def UniformCostSearch():
    queue =  PriorityQueue()
    arrBanDau = np.zeros((8,8), dtype=int)
    thoiGian = 0
    queue.put((0, thoiGian, arrBanDau, 0))
    while queue.qsize() != 0:
        chiPhi,tG, state, row = queue.get()

        if kiemTraTrangThaiDich(state):
            inBanCoNguoiChoi(state)
            
            #tinhChiPhi(state)
            return state
        
        if row == 8:
            continue
        
        if 1 not in state[row, :]:
            for j in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][j] = 1
                if trangThaiAnToan(stateNew) == False:
                    stateNew[row][j] = 0
                else:
                    if(row + 1) <= 8:
                        thoiGian += 1
                        chiPhiMoi = chiPhi + chiPhi_PathCost(row, j)
                        queue.put((chiPhiMoi, thoiGian, stateNew, row + 1))
        else:
            if(row + 1) <= 8:
                thoiGian = thoiGian + 1
                chiPhiMoi = chiPhi + chiPhi_PathCost(row, j)
                queue.put((chiPhiMoi, thoiGian, stateNew, row + 1))

        #root.after(50)
        root.update_idletasks()
    return None

def DepFirstSearch():
    stack = deque()
    arrBanDau = np.zeros((8,8), dtype=int)
    stack.append((arrBanDau, 0))
    print(len(stack))
    print("Mảng ban đầu: ", arrBanDau)
    while len(stack) != 0:
        state, row = stack.pop()
        
        if kiemTraTrangThaiDich(state):
            inBanCoNguoiChoi(state)
            return state
        
        if row == 8:
            continue
        
        if 1 not in state[row, :]:
            for j in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][j] = 1
                if trangThaiAnToan(stateNew) == False:
                    stateNew[row][j] = 0
                else:
                    if(row + 1) <= 8:
                        stack.append((stateNew, row + 1))           
        else:
            if(row + 1) < 8:
                stack.append((state, row + 1))
        root.update_idletasks()
    return None


# 2.3. INFORMED SEARCH ALGORITHMS
# 2.3.1. A * SEARCH
def AStarSearch():
    queue = PriorityQueue()
    arrBanDau = np.zeros((8,8), dtype=int)
    thuTu = 0
    queue.put((20, thuTu, arrBanDau, 0, 0, 0))
    while queue.qsize() != 0:
        chiPhi, tt, state, row,x, y = queue.get()
        if kiemTraTrangThaiDich(state):
            inBanCoNguoiChoi(state)
            #lbl_ChiPhi.config(text="Chi Phí: " + str(chiPhi))
            return state 
        
        if row == 8:
            continue

        if 1 not in state[row, :]:
            for col in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][col] = 1
                if trangThaiAnToan(stateNew) == False:
                    stateNew[row][col] = 0
                else:
                    if (row + 1) <= 8:
                        thuTu += 1
                        chiPhiMoi = chiPhi + chiPhi_PathCost(row, col, x, y) + chiPhiHeruristics(row, col)
                        queue.put((chiPhiMoi, thuTu, stateNew, row + 1, row, col))
        else:
            if (row + 1) <= 8:
                thuTu += 1
                queue.put((chiPhi, thuTu, state, row + 1))

# 2.3.2. GREEDY SEARCH
def GreedySearch():
    queue = PriorityQueue()
    arrBanDau = np.zeros((8,8), dtype=int)
    thuTu = 0
    queue.put((20, thuTu, arrBanDau, 0))
    arrFlagDemo = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    while queue.qsize() != 0:
        chiPhi, tt, state, row = queue.get()
        if kiemTraTrangThaiDich(state):
            print(arrFlagDemo)
            inBanCoNguoiChoi(state, arrFlagDemo)
            
            return state

        if row == 8:
            continue

        if 1 in state[row, :]:
            vT = -1
            for col in range(8):
                if state[row,:][col] == 1:
                    vT = col
                    break
            arrFlagDemo[vT] = [row, chiPhi]
            print(arrFlagDemo[col])

        if 1 not in state[row, :]:
            for col in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][col] = 1
                if trangThaiAnToan(stateNew) == False:
                    stateNew[row][col] = 0
                else:
                    if (row + 1) <= 8:
                        thuTu += 1
                        chiPhiMoi = chiPhiHeruristics(row, col)
                        queue.put((chiPhiMoi, thuTu, stateNew, row + 1))
        else:
            if (row + 1) <= 8:
                thuTu += 1
                queue.put((chiPhi, thuTu, state, row + 1))

# 2.4. TÌM KIẾM TRONG MÔI TRƯỜNG PHỨC TẠP
# 2.4.1. TÌM KIẾM CÓ HÀNH ĐỘNG KHÔNG XÁC ĐỊNH
def RecursiveAndOrTreeSearch_DFS():
    path = deque()
    result = OrSearch(np.zeros((8,8), dtype=int), path)
    if result is not False:
        inBanCoNguoiChoi(result)
        return True
    else:
        inBanCoNguoiChoi(np.zeros((8,8), dtype=int))
        return False
def OrSearch(state, path: deque):
    # HÀNH ĐỘNG ĐẶT THEO CỘT 
    # kiểm tra trạng thái đích 
    if kiemTraTrangThaiDich_Ver2(state):
        return state 
    
    # kiểm tra có chu trình hay không 
    stateTuple = tuple(map(tuple, state))
    if stateTuple in path:
        return False
    
    path.append(stateTuple)
    
    # Bắt đầu hành động đặt 
    if np.sum(state == 1) != 8:
        for action in range(np.sum(state == 1), 8):
            plan = AndSearch(ResultAndOrTree(state, action), path)
            if plan is not False:
                
                return plan
    return False   
def AndSearch(states, path):
    danhDau = None
    for s in states:
        planS = OrSearch(s, path)
        if planS is False: 
            return False
        danhDau = planS
    return danhDau

# 2.4.2. NHÓM TÌM KIẾM TRONG MÔI TRƯỜNG KHÔNG NHÌN THẤY 
# đối với thuật toán tìm kiếm trong môi trường không nhìn thấy ta có thể sử dụng chung với
# các thuật toán có thông tin và không có thông tin  
def SearchUnobservable_DFS():
    niemTinBanDau = deque()
    niemTinBanDau.append(
        [[0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]])
    niemTinBanDau.append(
         [[1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]])
    
    niemTinMucTieu = deque()
    niemTinMucTieu.append(
         [[1,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,1]])
    niemTinMucTieu.append(
        [[0,0,0,0,0,0,0,1],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,1,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0]])
    niemTinMucTieu.append(
         [[0,1,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0]])
    
    Action = ["Di chuyển", "Đặt"]
    queue = deque()
    queue.append(niemTinBanDau)
    while len(queue) != 0:
        A = queue.pop()

        Flag = True
        for i in A:
            if i not in niemTinMucTieu:
                Flag = False
                break
        if Flag:
            inBanCoNguoiChoi(A[0])
            return A[0]
        
        for action in Action:
            state = None
            if action == "Di chuyển":
                state = diChuyen(A)
            elif action == "Đặt":
                state = Dat(A)

            if len(state) > 0 and state != None:
                queue.append(state)
    
    return None

# 2.4.3. TÌM KIẾM TRONG MÔI TRƯỜNG NHÌN THẤY MỘT PHẦN
def PartiallyPbservable_GreedySearch():
    niemTinBanDau = deque()
    niemTinBanDau.append(
        [[1,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0]])
    niemTinBanDau.append(
         [[1,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,1]])
    
    niemTinMucTieu = deque()
    niemTinMucTieu.append(
         [[1,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,1]])
    niemTinMucTieu.append(
         [[1,0,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,1]])
    niemTinMucTieu.append(
         [[1,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,0,0,1],
          [0,0,1,0,0,0,0,0]])
    
    Action = ["Di chuyển", "Đặt"]
    queue = PriorityQueue()
    thuTu = 0
    queue.put((Herurictics_PartiallyObservable(niemTinBanDau), thuTu, niemTinBanDau))
    while queue.qsize() != 0:
        cp, tt, A = queue.get()

        Flag = True
        for i in A:
            if i not in niemTinMucTieu:
                Flag = False
                break
        if Flag:
            inBanCoNguoiChoi(A[0])
            return A[0]
        
        for action in Action:
            state = None
            if action == "Di chuyển":
                state = diChuyen(A, 0)
            elif action == "Đặt":
                state = Dat(A, 0)
            
            if state != None and len(state) > 0:
                cpH = Herurictics_PartiallyObservable(state)
                thuTu += 1
                queue.put((cpH, thuTu, state))

    return None


    

# 2.5. NHÓM TÌM KIẾM THÕA MÃN RÀNG BUỘC
# 2.5.1. CSP_BACKTRACKING
def CSP_Backtracking():
    # tập biến
    tapBien = [1,1,1,1,1,1,1,1]
    # tập giá trị
    tapGiaTri = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7],
                 [1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7],
                 [2,0], [2,1], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7],
                 [3,0], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7],
                 [4,0], [4,1], [4,2], [4,3], [4,4], [4,5], [4,6], [4,7],
                 [5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7],
                 [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7],
                 [7,0], [7,1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7]]
    # tập ràng buộc: không đặt cùng hàng và cùng cột, đạt trạng thái an toàn
    result = Backtracking(tapBien, tapGiaTri, np.zeros((8,8), dtype=int))

    if result is not None:
        inBanCoNguoiChoi(result)
        return True
    else:
        return None

def Backtracking(tapBien, tapGT, arr):

    if kiemTraTrangThaiDich_Ver2(arr):
        return arr
    else:
        if len(tapBien) == 0:
            return None
    
    bien = random.randint(0,len(tapBien)-1)

    arrCopy = copy.deepcopy(arr)
    for i in range(len(tapGT)):
        if arrCopy[tapGT[i][0]][tapGT[i][1]] == 0:
            arrCopy[tapGT[i][0]][tapGT[i][1]] = tapBien[bien]
            if trangThaiAnToan(arrCopy):
                tapBienNew = tapBien[:]
                tapGTNew = tapGT[:]
                del tapBienNew[bien]
                del tapGTNew[i]
                result = Backtracking(tapBienNew, tapGTNew,arrCopy)
                if result is not None:
                    return result

            arrCopy[tapGT[i][0]][tapGT[i][1]] = 0

    return None

# 2.5.2. CSP_FORWARDCHECKING
def CSP_FORWARDCHECKING():
    # tập biến
    tapBien = [1,1,1,1,1,1,1,1]
    # tập giá trị
    tapGiaTri = [[0,0], [0,1], [0,2], [0,3], [0,4], [0,5], [0,6], [0,7],
                 [1,0], [1,1], [1,2], [1,3], [1,4], [1,5], [1,6], [1,7],
                 [2,0], [2,1], [2,2], [2,3], [2,4], [2,5], [2,6], [2,7],
                 [3,0], [3,1], [3,2], [3,3], [3,4], [3,5], [3,6], [3,7],
                 [4,0], [4,1], [4,2], [4,3], [4,4], [4,5], [4,6], [4,7],
                 [5,0], [5,1], [5,2], [5,3], [5,4], [5,5], [5,6], [5,7],
                 [6,0], [6,1], [6,2], [6,3], [6,4], [6,5], [6,6], [6,7],
                 [7,0], [7,1], [7,2], [7,3], [7,4], [7,5], [7,6], [7,7]]
    # tập ràng buộc: không đặt cùng hàng và cùng cột, đạt trạng thái an toàn

    result = ForwardChecking(tapBien, tapGiaTri, np.zeros((8,8), dtype=int))

    if result is not None:
        inBanCoNguoiChoi(result)
        return True
    else:
        return None
    
def ForwardChecking(tapBien, tapGT, arr):
    if kiemTraTrangThaiDich_Ver2(arr):
        return arr
    else:
        if len(tapBien) == 0:
            return None
    
    bien = random.randint(0,len(tapBien)-1)

    arrCopy = copy.deepcopy(arr)
    for i in range(len(tapGT)):
        if arrCopy[tapGT[i][0]][tapGT[i][1]] == 0:
            arrCopy[tapGT[i][0]][tapGT[i][1]] = tapBien[bien]
            if trangThaiAnToan(arrCopy):
                tapBienNew = tapBien[:]
                tapGTNew = F(tapGT, tapGT[i][0], tapGT[i][1])
                del tapBienNew[bien]
                result = ForwardChecking(tapBienNew, tapGTNew,arrCopy)
                if result is not None:
                    return result

            arrCopy[tapGT[i][0]][tapGT[i][1]] = 0

    return None


# 2.5.3. CSP_AC3ARTCONCISTENCY


# 3. GIAO DIỆN

frm_Main = Frame(root, width=1400, height=695, bg="#EBD9D1")
frm_Main.grid(row=0, column=0)
frm_Main.grid_propagate(False)


lbl = Label(frm_Main, text="ĐẶT 8 QUÂN XE", font=("Times New Roman", 24, "bold"),
            fg="red", bg="#EBD9D1")
lbl.grid(row=0, column=0, columnspan=2, pady=10)

frm_TrangThai = Frame(frm_Main, bg="#EBD9D1")
frm_TrangThai.grid(row=1, column=0,pady=5, padx=10, sticky="ew")

frm_TrangThai.columnconfigure(0, weight=1)
frm_TrangThai.columnconfigure(1, weight=1)

btn_BatDau = Button(frm_TrangThai, text="Bắt Đầu", font=("Times New Roman", 20, "bold"),
                    fg="white", bg="#0593D0", width=10, command=suKienNhanNut)
btn_BatDau.grid(row=0, column=0, pady=5, padx=10, sticky="w")



lbl_ThoiGian = Label(frm_Main, text="Bàn Cờ Mẫu", font=("Times New Roman", 24, "bold"), fg="red", bg="#EBD9D1")
lbl_ThoiGian.grid(row=1, column=1, padx=10, sticky="n")

frm_BenTrai = Frame(frm_Main, width=500, height=450, bg="#8D320B")
frm_BenTrai.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
frm_BenTrai.grid_propagate(False)

# Cấu hình để các cột/hàng chia đều
for i in range(10):
    frm_BenTrai.columnconfigure(i, weight=1, uniform="col")
for i in range(10):
    frm_BenTrai.rowconfigure(i, weight=1, uniform="row")

arr_chu = np.array(['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ''])
for i in range(10):
    btn = Button(frm_BenTrai, text=str(arr_chu[i]), width=3, bg='white', relief="flat", state="disabled", font=("Times New Roman", 16, "bold"))
    btn.grid(row=0, column=i, sticky="nsew")

for i in range(8):
    btn = Button(frm_BenTrai, text=str(i+1), width=3, bg='white', relief="flat", state="disabled", font=("Times New Roman", 16, "bold"))
    btn.grid(row=(8-i), column=0, sticky="nsew")

for i in range(8):
    btn = Button(frm_BenTrai, text=str(i+1), width=3, bg='white', relief="flat", state="disabled", font=("Times New Roman", 16, "bold"))
    btn.grid(row=(8-i), column=9, sticky="nsew")

frm_VienTrong = Frame(frm_BenTrai)
frm_VienTrong.grid(row=1, column=1, columnspan=8, rowspan=8, sticky="nsew")
frm_VienTrong.grid_propagate(False)

arr_BanDau = np.zeros((8, 8), dtype=int)
# Gọi hàm tạo bàn cờ chính
taoBanCo()

for i in range(10):
    btn = Button(frm_BenTrai, text=str(arr_chu[i]), width=3, bg='white', relief="flat", state="disabled", font=("Times New Roman", 16, "bold"))
    btn.grid(row=9, column=i, sticky="nsew")

# Frame bàn cờ mẫu
frm_BenPhai = Frame(frm_Main, width=500, height=500, bg="#EBD9D1")
frm_BenPhai.grid(row=2, column=1, padx=10, pady=10)

frm_BanCo = Frame(frm_BenPhai, bg="white")
frm_BanCo.grid(row=0, column=0, pady=20, sticky="n")

# Mảng mẫu
arr_MucTieu = np.array([
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1]
])

# In bàn cờ mẫu 
for i in range(8):
        frm_BanCo.rowconfigure(i, weight=1, uniform="rowv")
        frm_BanCo.columnconfigure(i, weight=1, uniform="colv")
        for j in range(8):
            if arr_MucTieu[i][j] == 0:
                if (i+1)%2 != 0:
                    if (j+1)%2 !=0:
                        btn = Button(frm_BanCo, width=3,  text="", background="#F7C899", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
                    else:
                        btn = Button(frm_BanCo, width=3, text="", background="#CA8745", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
                else:
                    if (j+1)%2 !=0:
                        btn = Button(frm_BanCo, width=3, text="", background="#CA8745", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
                    else:
                        btn = Button(frm_BanCo, width=3, text="", background="#F7C899", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
            else:
                if (i+1)%2 != 0:
                    if (j+1)%2 !=0:
                        btn = Button(frm_BanCo,width=3,  text="♖", background="#F7C899", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
                    else:
                        btn = Button(frm_BanCo,width=3,  text="♖", background="#CA8745", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
                else:
                    if (j+1)%2 !=0:
                        btn = Button(frm_BanCo,width=3, text="♖", background="#CA8745", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")
                    else:
                        btn = Button(frm_BanCo,width=3, text="♖", background="#F7C899", relief="flat", state="disabled", font=("Segoe UI Symbol", 20, "bold"))
                        btn.grid(row=i, column=j, sticky="nsew")

# Bảng trạng thái thông tin

lbl_ThongTin = Label(frm_Main, text="Thông Tin", font=("Times New Roman", 24, "bold"), fg="red", bg="#EBD9D1")
lbl_ThongTin.grid(row=1, column=2, padx=5, pady=5, sticky="n")

frm_ThongTin = Frame(frm_Main, width=380, height=500, bg="#EBD9D1")
frm_ThongTin.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

lbl_ThuatToan = Label(frm_ThongTin, text="Chọn thuật toán: ", bg="#EBD9D1", fg="blue", font=("Times New Roman", 16, "bold"))
lbl_ThuatToan.grid(row=0, column=0, padx=5, pady=5, sticky="w")

cbb_ThuatToan = ttk.Combobox(frm_ThongTin, values=["","I. Uninformed Search Algorithms", 
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
                                                    "CSP Ac-3 Art Concistency"],font=("Times New Roman", 16, "bold"), width=16, state="readonly")
cbb_ThuatToan.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
cbb_ThuatToan.current(0)

lbl_TTBanDau = Label(frm_ThongTin, text="Trạng thái ban đầu: Ma Trận 0 8x8",  bg="#EBD9D1", fg="blue", font=("Times New Roman", 16, "bold"))
lbl_TTBanDau.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

lbl_DuongDi = Label(frm_ThongTin, text = "Đường đi", bg="#EBD9D1", fg="blue", font=("Times New Roman", 16, "bold"))
lbl_DuongDi.grid(row=2, column=0, padx=5, pady=5, sticky="w")

frame_text = Frame(frm_ThongTin)
frame_text.grid(row=3, column=0, columnspan=2, sticky="nesw")

text_Area = Text(frame_text, width=30, height=15, wrap="none", state="disabled")
text_Area.grid(row=0, column=0, sticky="nsew")

# Scrollbar dọc
scrollbar_y = Scrollbar(frame_text, orient="vertical", command=text_Area.yview)
scrollbar_y.grid(row=0, column=1, sticky="ns")

# Scrollbar ngang
scrollbar_x = Scrollbar(frame_text, orient="horizontal", command=text_Area.xview)
scrollbar_x.grid(row=1, column=0, sticky="ew")

text_Area.config(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

# Cho phép co giãn
frame_text.grid_rowconfigure(0, weight=1)
frame_text.grid_columnconfigure(0, weight=1)


root.mainloop()