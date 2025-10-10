import numpy as np
from collections import deque
from queue import PriorityQueue
import copy
import math
import random
import time 


class DatQuanXeModel:
    def __init__(self, controller):
        self.arrMucTieu = np.array([
            [0,0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0,0],
            [0,0,0,0,1,0,0,0],
            [0,0,0,1,0,0,0,0],
            [0,0,1,0,0,0,0,0],
            [0,1,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1]
        ])

        self.controller = controller

    
    # NHỮNG HÀM PHỤ:
    def getMucTieu(self):
        return self.arrMucTieu
    
    def kiemTraTrangThaiDich(self, arr_):
        soLuong = np.sum(arr_ == 1)
        if soLuong == 8:
            if np.array_equal(arr_, self.arrMucTieu):
                return True
        return False
    
    def chiPhi_PathCost(self, row, col, x_old, y_old):
        return round(math.sqrt((row-x_old)**2+(col-y_old)**2), 0)

        
    def trangThaiAnToan(self, arr_):
        for i in range(8):
            for j in range(8):
                if arr_[i][j] == 1:
                    anNgang = np.sum(arr_[i, :] == 1)
                    anDoc = np.sum(arr_[:, j] == 1)
                    if anNgang > 1 or anDoc > 1:
                        return False
            
        return True
    
    def chiPhiHeruristics(self, row, j):
        return round(math.sqrt((row-8)**2+(j-8)**2), 2)
    
    def schedule(self,t):
        return ((0.8)**t)*50
    
    def khoiTaoQuanThe(self):
        N = 6
        queue = []
        vt = []
        while N > 0:
            arrCaThe1D = [random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7), random.randint(0, 7) ,random.randint(0, 7), random.randint(0, 7),random.randint(0, 7)]
            arrCaThe2D = np.zeros((8,8), dtype=int)
            for i in range(8):
                arrCaThe2D[arrCaThe1D[i]][i] = 1
                vt.append([arrCaThe1D[1], i])
            soCapKhongAnNhau = self.doFitness(arrCaThe1D)
            queue.append([arrCaThe2D, arrCaThe1D, soCapKhongAnNhau, vt])
            N -= 1

        return queue
    
    def chonLocCacCaThe(self, quanThe):
        quanThe = list(quanThe)
        quanThe.sort(key=lambda x: x[2])
        chonLoc = [quanThe[5], quanThe[4]]
        indexRamdon = random.randint(0, 3)
        chonLoc.append(quanThe[indexRamdon])
        return chonLoc

    def doFitness(self, arr1D):
        fitness = 0
        for i in range(8):
            for j in range(i+1, 8):
                if ((arr1D[i] - arr1D[j]) != 0):
                    fitness += 1
        return fitness
    
    def kiemTraTrangThaiDich_Ver2(self, arr_):
        soLuong = np.sum(arr_ == 1)
        if soLuong == 8:
            return self.trangThaiAnToan(arr_)
        return False
    
    def diChuyen(self, niemTin, notFix=None):
        B = []
        for i in niemTin:
            soQuanXe = 0
            for row in range(8):
                for col in range(8):
                    if i[0][row][col] == 1:
                        soQuanXe += 1
            if soQuanXe == 8:
                continue
            Stop = False
            for row in range(8):
                if notFix != None and row == notFix:
                    continue
                for col in range(8):
                    if notFix != None and col == notFix:
                        continue
                    if i[0][row][col] == 1:
                        # di chyển sang phải
                        if (col + 1) < 8 and i[0][row][col+1] == 0:
                            stateCopy = copy.deepcopy(i[0])
                            stateCopy[row][col] = 0
                            stateCopy[row][col+1] = 1
                            vtNew = copy.deepcopy(i[1])
                            if self.trangThaiAnToan(np.array(stateCopy)):
                                for k in vtNew:
                                    if k[0] == row  and k[1] == col:
                                        k[1] = col + 1
                                        break
                                
                                B.append((stateCopy, vtNew))
                                Stop = True
                                break
                        # di chuyển sang trái
                        if (col - 1) >= 0 and i[0][row][col-1] == 0:
                            stateCopy = copy.deepcopy(i[0])
                            stateCopy[row][col] = 0
                            stateCopy[row][col-1] = 1
                            vtNew = copy.deepcopy(i[1])
                            if self.trangThaiAnToan(np.array(stateCopy)):
                                for k in vtNew:
                                    if k[0] == row  and k[1] == col:
                                        k[1] = col - 1
                                        break
                                B.append((stateCopy, vtNew))
                                Stop = True
                                break
                        # di chuyển xuống
                        if (row + 1) < 8 and i[0][row+1][col] == 0:
                            stateCopy = copy.deepcopy(i[0])
                            stateCopy[row][col] = 0
                            stateCopy[row+1][col] = 1
                            vtNew = copy.deepcopy(i[1])
                            if self.trangThaiAnToan(np.array(stateCopy)):
                                for k in vtNew:
                                    if k[0] == row  and k[1] == col:
                                        k[0] = row + 1
                                        break
                                B.append((stateCopy, vtNew))
                                Stop = True
                                break
                        # di chuyển lên 
                        if (row - 1) >= 0 and i[0][row-1][col] == 0:
                            stateCopy = copy.deepcopy(i[0])
                            stateCopy[row][col] = 0
                            stateCopy[row-1][col] = 1
                            vtNew = copy.deepcopy(i[1])
                            if self.trangThaiAnToan(np.array(stateCopy)):
                                for k in vtNew:
                                    if k[0] == row  and k[1] == col:
                                        k[0] = row - 1 
                                        break
                                B.append((stateCopy, vtNew))
                                Stop = True
                                break
                
                if Stop:
                    break
            if Stop == False:
                B.append(i)
        return B
    
    def Dat(self, niemTin, notFix=None):
        A = []

        for i in niemTin:
            for col in range(8):
                if notFix != None and col == notFix:
                    continue
                Stop = False
                for row in range(8):
                    if notFix != None and row == notFix: 
                        continue
                    if i[0][row][col] == 0:
                        state = copy.deepcopy(i[0])
                        state[row][col] = 1
                        vtNew = copy.deepcopy(i[1])
                        if self.trangThaiAnToan(np.array(state)):
                            vtNew.append([row, col])
                            A.append((state, vtNew))
                            Stop = True
                            break
                                
                if Stop:
                    break
        
        return A 
    
    def Herurictics_PartiallyObservable(self, niemTin):
        Cost = 0
        for item in niemTin:
            soQuanDaDat = 0
            for i in range(8):
                for j in range(8):
                    if item[0][i][j] == 1:
                        soQuanDaDat += 1
            Cost += (8 - soQuanDaDat)
        return Cost 
    
    def F(self, tapGiaTri, row, col):
        tapGTNew = []
        for i in tapGiaTri:
            if i[0] != row and i[1] != col:
                tapGTNew.append(i)
        return tapGTNew        

    
    # NHÓM 1: THUẬT TOÁN TÌM KIẾM KHÔNG CÓ THÔNG TIN
    def BreadthFirstSearch(self):
        queue = deque()
        arrBanDau = np.zeros((8,8), dtype=int)
        queue.append((arrBanDau, 0, []))
        soTrangThai = 0
        
        while len(queue) != 0:
            state, row, vt = queue.popleft()
            
            if self.kiemTraTrangThaiDich(state):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTrangThai)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return
            
            if row == 8:
                continue
            
            for j in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][j] = 1
                vtNew = copy.deepcopy(vt)
                if self.trangThaiAnToan(stateNew):
                    if row <= 7:
                        soTrangThai += 1
                        vtNew.append([row, j])
                        queue.append((stateNew, row + 1, vtNew))

        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        self.controller.setSoTrangThai(soTrangThai)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        return None
    
    def DepFirstSearch(self):
        stack = deque()
        arrBanDau = np.zeros((8,8), dtype=int)
        stack.append((arrBanDau, 0, []))
        soTT = 0

        while len(stack) != 0:
            state, row, vt = stack.pop()
            
            if self.kiemTraTrangThaiDich(state):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return 
            
            if row == 8:
                continue
            
            for j in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][j] = 1
                vtNew = copy.deepcopy(vt)
                if self.trangThaiAnToan(stateNew):
                    if row <= 7:
                        soTT += 1
                        vtNew.append([row, j])
                        stack.append((stateNew, row + 1, vtNew))  

        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")                  
        return None
    
    def UniformCostSearch(self):
        queue =  PriorityQueue()
        arrBanDau = np.zeros((8,8), dtype=int)
        thoiGian = 0
        queue.put((0, thoiGian, arrBanDau, 0, [], 0, 0))
        soTT = 0
        while queue.qsize() != 0:
            chiPhi,tG, state, row, vt, x_Old, y_Old = queue.get()

            if self.kiemTraTrangThaiDich(state):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return 
            
            if row == 8:
                continue
        
            for j in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][j] = 1
                vtNew = copy.deepcopy(vt)
                if self.trangThaiAnToan(stateNew):
                    if row <= 7:
                        thoiGian += 1
                        soTT += 1
                        vtNew.append([row, j])
                        chiPhiMoi = chiPhi + self.chiPhi_PathCost(row, j, x_Old, y_Old)
                        queue.put((chiPhiMoi, thoiGian, stateNew, row + 1,vtNew, row, j))

        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")  
        self.controller.dungDemGio()
        return None
    
    def DepthLimitedSearch_Ver2(self):
        self.soTT = 0
        result, vt = self.RecusiveDLS(np.zeros((8,8), dtype=int), 0, 8, [])


        if result is not None and len(vt) == 8:
            self.controller.inBanCo(vt)
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(True)
            self.controller.dungDemGio()
            return True
        
        self.controller.setSoTrangThai(self.soTT)
        self.controller.setColor(False)
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        self.controller.dungDemGio()
        return False
    
    def RecusiveDLS(self, arr, row, limit, arrVT):
        if self.kiemTraTrangThaiDich(arr):
            return arr, arrVT
        elif limit == 0: 
            return np.zeros((8,8), dtype=int), []
        else:
            cutof_occurred = False

            for i in range(8):
                stateNew = copy.deepcopy(arr)
                stateNew[row][i] = 1
                vtNew = copy.deepcopy(arrVT)
                if self.trangThaiAnToan(stateNew):
                    if (row + 1) < 8:
                        self.soTT += 1
                        vtNew.append([row, i])
                        result, v = self.RecusiveDLS(stateNew, row + 1, limit - 1, vtNew)
                        if np.array_equal(result, np.zeros((8,8), dtype=int)):
                            cutof_occurred = True
                        elif result is not None: 
                            return result, v
                    elif (row + 1) == 8:
                        self.soTT += 1
                        vtNew.append([row, i])
                        result, v = self.RecusiveDLS(stateNew, row, limit - 1, vtNew)
                        if np.array_equal(result, np.zeros((8,8), dtype=int)):
                            cutof_occurred = True
                        elif result is not None: 
                            return result, v
                    
            if cutof_occurred:
                return np.zeros((8,8), dtype=int), []
            else:
                return None, []
            
    def IterativeDeepening_DLS(self):
        self.soTT = 0
        for depth in range(9):
            result, vt = self.DepthLimitedSearch(np.zeros((8,8), dtype=int), 0, depth)
            if self.kiemTraTrangThaiDich(result):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(self.soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return True
            
        self.controller.setSoTrangThai(self.soTT)
        self.controller.setColor(False)
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        self.controller.dungDemGio()
        return False
            
    def DepthLimitedSearch(self, arr, row, limit):
        return self.RecusiveDLS(arr, row, limit, [])
    
    def IterativeDeepening_DFS(self):
        soTT = 0
        for depth in range(10):
            stack = deque()
            arrBanDau = np.zeros((8,8), dtype=int)
            stack.append((arrBanDau, 0, []))
            while len(stack) != 0:
                state, row, vt = stack.pop()
                
                if self.kiemTraTrangThaiDich(state):
                    self.controller.inBanCo(vt)
                    self.controller.setSoTrangThai(soTT)
                    self.controller.setColor(True)
                    self.controller.dungDemGio()
                    return 
                
                if row == 8:
                    continue

                if row < depth:
                    for j in range(8):
                        stateNew = copy.deepcopy(state)
                        stateNew[row][j] = 1
                        vtNew = copy.deepcopy(vt)
                        if self.trangThaiAnToan(stateNew):
                            if row  <= 7:
                                soTT += 1
                                vtNew.append([row, j])
                                stack.append((stateNew, row + 1, vtNew))                       

        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        self.controller.dungDemGio()
        return None
    
    # NHÓM 2: THUẬT TOÁN TÌM KIẾM CÓ THÔNG TIN 
    def GreedySearch(self):
        queue = PriorityQueue()
        arrBanDau = np.zeros((8,8), dtype=int)
        thuTu = 0
        queue.put((20, thuTu, arrBanDau, 0, []))
        soTT = 0
        while queue.qsize() != 0:
            chiPhi, tt, state, row, vt = queue.get()
            if self.kiemTraTrangThaiDich(state):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return state

            if row == 8:
                continue
            
            for col in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][col] = 1
                vtNew = copy.deepcopy(vt)
                if self.trangThaiAnToan(stateNew):
                    if row <= 7:
                        thuTu += 1
                        soTT += 1
                        vtNew.append([row, col])
                        chiPhiMoi = self.chiPhiHeruristics(row, col)
                        queue.put((chiPhiMoi, thuTu, stateNew, row + 1, vtNew))

        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        self.controller.dungDemGio()
        return None

    def AStarSearch(self):
        queue = PriorityQueue()
        arrBanDau = np.zeros((8,8), dtype=int)
        thuTu = 0
        queue.put((20, thuTu, arrBanDau, 0, 0, 0, []))
        soTT = 0
        while queue.qsize() != 0:
            chiPhi, tt, state, row, x, y, vt = queue.get()
            if self.kiemTraTrangThaiDich(state):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return state 
            
            if row == 8:
                continue

            if 1 not in state[row, :]:
                for col in range(8):
                    stateNew = copy.deepcopy(state)
                    stateNew[row][col] = 1
                    vtNew = copy.deepcopy(vt)
                    if self.trangThaiAnToan(stateNew):
                        if row <= 7:
                            thuTu += 1
                            soTT += 1
                            vtNew.append([row, col])
                            chiPhiMoi = chiPhi + self.chiPhi_PathCost(row, col, x, y) + self.chiPhiHeruristics(row, col)
                            queue.put((chiPhiMoi, thuTu, stateNew, row + 1, row, col, vtNew))

        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        self.controller.dungDemGio()        
        return None
    
    # NHÓM 3: LOCAL SEARCH
    def HillClimbing(self):
        start = np.zeros((8,8), dtype=int)
        row = 0
        cPBanDau = 64
        thuTu = 0
        vt = []
        soTT = 0
        while True:
            queue = PriorityQueue()

            if row == 8:
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(False)
                self.controller.dungDemGio()
                self.controller.loiOrLuuY("Lỗi", "Không thể sinh tiếp trạng thái lân cận")
                return None

            # Sinh các trạng thái lân cận
            for col in range(8):
                state =  copy.deepcopy(start)
                state[row][col] = 1
                vtNew = copy.deepcopy(vt)
                if self.trangThaiAnToan(state):
                    if row <= 7:
                        thuTu += 1
                        soTT += 1
                        vtNew.append([row, col])
                        queue.put((self.chiPhiHeruristics(row, col), thuTu, row+1, state, vtNew))
                    

            if queue.empty():
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(False)
                self.controller.dungDemGio()
                self.controller.loiOrLuuY("Lỗi", "Không thể sinh tiếp trạng thái lân cận")
                return None
            cP, tt, r, stateBest, v = queue.get()
            
            if (self.kiemTraTrangThaiDich(stateBest)):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return True

            if cP < cPBanDau:
                
                start = stateBest
                cPBanDau = cP
                row = r
                vt = v
                
            else:
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(False)
                self.controller.dungDemGio()
                self.controller.loiOrLuuY("Lỗi", "Trạng thái lân cận không tốt hơn\n trạng thái hiện tại.")
                return False

    
    def SimulatedAnnealing(self):
        start = np.zeros((8,8), dtype=int)
        row = 0
        chiPhi = 8*8
        thuTu = 0
        t = 1
        vt = []
        soTT = 0
        while True:
            if self.kiemTraTrangThaiDich(start):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return
            T = self.schedule(t)
            if T == 0:
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(False)
                self.controller.dungDemGio()
                self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
                return
            queue = PriorityQueue()
            l = []
            if row < 8:
                for col in range(8):
                    state = copy.deepcopy(start)
                    state[row][col] = 1
                    vtNew = copy.deepcopy(vt)
                    if self.trangThaiAnToan(state):
                        if row <= 7:
                            thuTu += 1
                            soTT += 1
                            vtNew.append([row, col])
                            chiPhiState = self.chiPhiHeruristics(row, col)
                            queue.put((chiPhiState, thuTu, row + 1, state, vtNew))
                            l.append([chiPhiState,row + 1, state])
                        
                        
            if queue.empty():
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(False)
                self.controller.dungDemGio()
                self.controller.loiOrLuuY("Lỗi", "Không thể sinh tiếp trạng thái lân cận.")
                return 
            
            cp, tt, r, stateBest, v = queue.get()
            
            if (cp - chiPhi) < 0:
                start = stateBest
                row = r
                chiPhi = cp
                vt = v
            else:
                index = random.randint(0, len(l)-1)
                c = l[index][0]
                ro = l[index][1]
                stateBad = l[index][2]
                p = math.e**(-(c-chiPhi)/T)
                p_Random = random.uniform(0,1)
                if p > p_Random:
                    start = stateBad
                    row = ro
                    chiPhi = c
                    vt = v

            t = t + 1

    def BeamSearch(self):
        arrBanDau = np.zeros((8,8), dtype=int)
        queue = deque()
        k = 2
        self.controller.loiOrLuuY("Lưu ý: ", f"Giá trị k = {k}")
        queue.append((20, 0, arrBanDau, []))
        soTT = 0
        while len(queue) != 0:
            chP, row, state, vt = queue.popleft()
            if self.kiemTraTrangThaiDich(state):
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(soTT)
                self.controller.setColor(True)
                self.controller.dungDemGio()
                return
            
            if row == 8:
                continue

            sinhTT = PriorityQueue()
            thuTu = 0
            for col in range(8):
                stateNew = copy.deepcopy(state)
                stateNew[row][col] = 1
                vtNew = copy.deepcopy(vt)
                if self.trangThaiAnToan(stateNew):
                    cP = self.chiPhiHeruristics(row, col)
                    thuTu += 1
                    if row <= 7:
                        vtNew.append([row, col])
                        sinhTT.put((cP, thuTu,row + 1, stateNew, vtNew))
                    
            index = 0
            while index < k and not sinhTT.empty():
                soTT += 1
                c, t, ro, stateBest, v = sinhTT.get()
                queue.append((c, ro, stateBest, v))
                index += 1

        self.controller.inBanCo(vt)
        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        return None
    
    def GeneticAlgorithms(self):
        soTT = 0
        # Khởi tạo ngẫu nhiên một quần thể có 6 cá thể và tính giá trị fitness cho từng cá thể 
        queueQuanThe = self.khoiTaoQuanThe()
        maxGen = 1000
        Gen = 0
        self.controller.loiOrLuuY("Lưu ý: ", f"Số lượng mã Gen tối đa là {maxGen}")
        vt = []
        while Gen < maxGen:
            # Chọn lọc cả thể 
            quanTheChonLoc =  self.chonLocCacCaThe(queueQuanThe)
            # Đem cá thể chọn lọc đi lai
            quanTheMoi = []
            Flag = False
            for i in range(len(quanTheChonLoc)):
                A = copy.deepcopy(quanTheChonLoc[i])
                for j in range(i+1, len(quanTheChonLoc)):
                    B = copy.deepcopy(quanTheChonLoc[j])
                    # bắt đầu quá trình lai 
                    rateLai = 0.65 # tỉ lệ lai 65%
                    for k in range(8):
                        r = random.random()
                        if r < rateLai:
                            soTT += 1
                            temp2D = A[0][:, k]
                            A[0][:, k] = B[0][:, k]
                            B[0][:, k] = temp2D

                            temp1D = A[1][k]
                            A[1][k] = B[1][k]
                            B[1][k] = temp1D

                            tempVT = A[3][k]
                            A[3][k] = B[3][k]
                            B[3][k] = tempVT

                            A[2] = self.doFitness(A[1])
                            B[2] = self.doFitness(B[1])


                    # Bắt đầu đột biến gen với tỉ lệ đột biến là 5%
                    rateDotBien = 0.05
                    for m in range(8):
                        c1 = random.random()
                        c2 = random.random()
                        if c1 < rateDotBien:
                            index = random.randint(0, 7)
                            A[0][:, m] = 0
                            A[0][index][m] = 1
                            
                            A[1][m] = index

                            A[2] = self.doFitness(A[1])

                        if c2 < rateDotBien:
                            index = random.randint(0, 7)
                            B[0][:, m] = 0
                            B[0][index][m] = 1

                            B[1][m] = index

                            B[2] = self.doFitness(B[1])
                    
                    quanTheMoi.append(A)
                    quanTheMoi.append(B)
                    if len(quanTheMoi) == 6:
                        Flag = True
                        break
                if Flag:
                    break
            
            # kiểm tra trong quần thể mới có cá thể mục tiêu không 
            for i in quanTheMoi:
                if self.kiemTraTrangThaiDich(i[0]):
                    self.controller.inBanCo(i[3])
                    self.controller.setSoTrangThai(soTT)
                    self.controller.setColor(True)
                    self.controller.dungDemGio()
                    return 
            queueQuanThe = copy.deepcopy(quanTheMoi)
            Gen += 1

        self.controller.setSoTrangThai(soTT)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        return None
    
    # NHÓM 4: TÌM KIẾM TRONG MÔI TRƯỜNG PHỨC TẠP 
    def RecursiveAndOrTreeSearch_DFS(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Bài toán chỉ tìm trạng thái đặt \n8 quân xe hợp lệ.")
        path = deque()
        self.TT = 0
        result = self.OrSearch((np.zeros((8,8), dtype=int),[]), path)
        if result is not False:
            self.controller.inBanCo(result)
            self.controller.setSoTrangThai(self.TT)
            self.controller.setColor(None)
            self.controller.dungDemGio()
            return 
        
        self.controller.setSoTrangThai(self.TT)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        return False
    def OrSearch(self, state: tuple, path: deque):
        # Kiểm tra trạng thái đích 
        if self.kiemTraTrangThaiDich_Ver2(state[0]):
            return state[1]
        
        # Kiểm tra có chu trình hay không 
        stateTuple = tuple(map(tuple, state[0]))
        if stateTuple in path:
            return False
        
        # Thêm vào path
        path.append(stateTuple)
        
        # Bắt đầu hành động đặt 
        soQuanHienTai = np.sum(state[0] == 1)
        if soQuanHienTai < 8:
                action = soQuanHienTai
                plan = self.AndSearch(self.ResultAndOrTree(state, action), path)
                
                if plan is not False:
                    path.pop()
                    return plan
        
        path.pop()
        return False

    def AndSearch(self, states, path):
        danhDau = None
        for s in states:
            planS = self.OrSearch(s, path)
            if planS is False:
                return False
            danhDau = planS
        return danhDau
    def ResultAndOrTree(self, state: tuple, action):
        states = []
        for row in range(8):
            stateCopy = copy.deepcopy(state[0])
            stateCopy[row][action] = 1
            vtNew = state[1].copy()
            if self.trangThaiAnToan(stateCopy):
                self.TT += 1
                vtNew.append([row, action])
                states.append((stateCopy, vtNew))
        return states
    
    def SearchUnobservable_DFS(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Bài toán tìm tập các trạng thái \nhợp lệ.")
        niemTinBanDau = []
        niemTinBanDau.append((
            [[0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1]], [[0,6], [7,7]]))  
        niemTinBanDau.append((
            [[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1]], [[3,3], [7,7]]))
        
        
        
        niemTinMucTieu = []
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
        self.soTTKN = 0
        giaTriLap = 0
        while len(queue) != 0:
            A = queue.pop()

            if giaTriLap == 1000:
                break

            Flag = True
            for i in A:
                if i[0] not in niemTinMucTieu:
                    Flag = False
                    break
            if Flag:
                self.controller.inBanCo(A[0][1])
                self.controller.setSoTrangThai(self.soTTKN)
                self.controller.setColor(None)
                self.controller.dungDemGio()
                return 
            
            for action in Action:
                state = None
                if action == "Di chuyển":
                    state = self.diChuyen(A)
                elif action == "Đặt":
                    state = self.Dat(A)

                if len(state) > 0 and state != None:
                    self.soTTKN += 1
                    queue.append(state)
            giaTriLap += 1
        
        self.controller.setSoTrangThai(self.soTTKN)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        return None
    
    def PartiallyPbservable_GreedySearch(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Bài toán tìm tập các trạng thái hợp lệ.\n Vị trí đã biết: (0,0) ")
        self.controller.inBanCo([[0,0]])

        niemTinBanDau = []
        niemTinBanDau.append((
            [[1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]], [[0,0]]))
        niemTinBanDau.append((
            [[1,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,1]], [[0,0], [7,7]]))
        
        niemTinMucTieu = []
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
        queue.put((self.Herurictics_PartiallyObservable(niemTinBanDau), thuTu, niemTinBanDau))
        self.soTTKN = 0
        while queue.qsize() != 0:
            cp, tt, A = queue.get()

            Flag = True
            for i in A:
                if i[0] not in niemTinMucTieu:
                    Flag = False
                    break
            if Flag:
                self.controller.inBanCo(A[0][1])
                self.controller.setSoTrangThai(self.soTTKN)
                self.controller.setColor(None)
                self.controller.dungDemGio()
                return 
            
            for action in Action:
                state = None
                if action == "Di chuyển":
                    state = self.diChuyen(A, 0)
                elif action == "Đặt":
                    state = self.Dat(A, 0)
                
                if  len(state) > 0:
                    cpH = self.Herurictics_PartiallyObservable(state)
                    self.soTTKN += 1
                    thuTu += 1
                    queue.put((cpH, thuTu, state))
        self.controller.setSoTrangThai(self.soTTKN)
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        return None
    
    # NHÓM 5: TÌM KIẾM THÕA MÃN RÀNG BUỘC 
    def CSP_Backtracking(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Bài toán chỉ tìm ra trạng thái \nhợp lệ.")
        self.soTT = 0
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
        result = self.Backtracking(tapBien, tapGiaTri, np.zeros((8,8), dtype=int), [])
        if result is not None:
            self.controller.inBanCo(result)
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(None)
            self.controller.dungDemGio()
            return 
        else:
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(False)
            self.controller.dungDemGio()
            self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
            return None

    def Backtracking(self, tapBien, tapGT, arr, vt):

        if self.kiemTraTrangThaiDich_Ver2(arr):
            return vt
        else:
            if len(tapBien) == 0:
                return None
        
        bien = random.randint(0,len(tapBien)-1)

        arrCopy = copy.deepcopy(arr)
        for i in range(len(tapGT)):
            gt = random.randint(0, len(tapGT)-1)
            if arrCopy[tapGT[gt][0]][tapGT[gt][1]] == 0:
                arrCopy[tapGT[gt][0]][tapGT[gt][1]] = tapBien[bien]
                if self.trangThaiAnToan(arrCopy):
                    self.soTT += 1
                    tapBienNew = tapBien[:]
                    tapGTNew = tapGT[:]
                    del tapBienNew[bien]
                    del tapGTNew[gt]
                    vtNew = copy.deepcopy(vt)
                    vtNew.append([tapGT[gt][0], tapGT[gt][1]])
                    result = self.Backtracking(tapBienNew, tapGTNew,arrCopy, vtNew)
                    if result is not None:
                        return result

                arrCopy[tapGT[gt][0]][tapGT[gt][1]] = 0

        return None
    
    def CSP_FORWARDCHECKING(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Bài toán chỉ tìm ra trạng thái \nhợp lệ.")
        self.soTT = 0
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

        result = self.ForwardChecking(tapBien, tapGiaTri, np.zeros((8,8), dtype=int), [])

        if result is not None:
            self.controller.inBanCo(result)
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(None)
            self.controller.dungDemGio()
            return
        else:
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(False)
            self.controller.dungDemGio()
            self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
            return
        
    def ForwardChecking(self, tapBien, tapGT, arr, vt):
        
        if self.kiemTraTrangThaiDich_Ver2(arr):
            return vt
        else:
            if len(tapBien) == 0:
                return None
        
        bien = random.randint(0,len(tapBien)-1)

        arrCopy = copy.deepcopy(arr)
        for i in range(len(tapGT)):
            gt = random.randint(0, len(tapGT)-1)
            if arrCopy[tapGT[gt][0]][tapGT[gt][1]] == 0:
                arrCopy[tapGT[gt][0]][tapGT[gt][1]] = tapBien[bien]
                if self.trangThaiAnToan(arrCopy):
                    self.soTT += 1
                    tapBienNew = tapBien[:]
                    tapGTNew = self.F(tapGT, tapGT[gt][0], tapGT[gt][1])
                    del tapBienNew[bien]
                    vtNew = copy.deepcopy(vt)
                    vtNew.append([tapGT[gt][0], tapGT[gt][1]])
                    result = self.ForwardChecking(tapBienNew, tapGTNew,arrCopy, vtNew)
                    if result is not None:
                        return result

                arrCopy[tapGT[gt][0]][tapGT[gt][1]] = 0

        return None
    
    def ArcConsistencyAlgorithm_3(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Bài toán chỉ tìm ra trạng thái \nhợp lệ.")
        tapGiaTri = [[i, j] for i in range(8) for j in range(8)]
        tB = [(i+1, copy.deepcopy(tapGiaTri)) for i in range(8)]
        self.tapBien = copy.deepcopy(tB)
        self.soTT = 0
        result = self.AC3(tB)
        if result:
            vt = self.Backtracking_AC3(copy.deepcopy(self.tapBien), np.zeros((8,8), dtype=int), [])
            if vt  is not None:
                self.controller.inBanCo(vt)
                self.controller.setSoTrangThai(self.soTT)
                self.controller.setColor(None)
                self.controller.dungDemGio()
                return
        
        self.controller.setColor(False)
        self.controller.dungDemGio()
        self.controller.loiOrLuuY("Lỗi", "Không tìm thấy mục tiêu.")
        return None
    
    def Backtracking_AC3(self, tapBien, arr, vt):
        if self.kiemTraTrangThaiDich_Ver2(arr):
            return vt
        else:
            if len(tapBien) == 0:
                return None
            
        arrCopy = copy.deepcopy(arr)
        bien = random.randint(0,len(tapBien)-1)
        for i in range(len(tapBien[bien][1])):
            gt = random.randint(0, len(tapBien[bien][1])-1)
            if arrCopy[tapBien[bien][1][gt][0]][tapBien[bien][1][gt][1]] == 0:
                arrCopy[tapBien[bien][1][gt][0]][tapBien[bien][1][gt][1]] = 1
                if self.trangThaiAnToan(arrCopy):
                    self.soTT += 1
                    tapBienNew = tapBien[:]
                    del tapBienNew[bien]
                    vtNew = copy.deepcopy(vt)
                    vtNew.append([tapBien[bien][1][gt][0], tapBien[bien][1][gt][1]])
                    result = self.Backtracking_AC3(tapBienNew, arrCopy, vtNew)
                    if result is not None:
                        return result
                    
                arrCopy[tapBien[bien][1][gt][0]][tapBien[bien][1][gt][1]] = 0

        return None

    def AC3(self, tb):
        queue = deque()
        for i in tb:
            for j in tb:
                if i[0] != j[0]:
                    queue.append((i, j))
        
        while len(queue) != 0:
            Xi, Xj = queue.popleft()
            
            if self.revise(Xi, Xj):
                if len(Xi[1]) == 0:
                    return False
                
                for k in tb:
                    if k[0] != Xi[0] and k[0] != Xj[0]:
                        queue.append((k, Xi))

        return True

    def revise(self, Xi: tuple, Xj: tuple):
        revised = False
        to_remove = []
        
        for i in Xi[1]:
            if not self.RangBuoc(i, Xj[1]):
                to_remove.append(i)
                revised = True
        
        for i in to_remove:
            Xi[1].remove(i)
        
        for idx, bien in enumerate(self.tapBien):
            if Xi[0] == bien[0]:
                self.tapBien[idx] = Xi
                break
        
        return revised

    def RangBuoc(self, x, y):
        for j in y:
            arr = np.zeros((8, 8), dtype=int)
            arr[x[0]][x[1]] = 1
            arr[j[0]][j[1]] = 1
            
            if self.trangThaiAnToan(arr):
                return True
        
        return False

    # NHÓM 6: THUẬT TOÁN TÌM KIẾM ĐỐI KHÁNG
    def Minimax_Decision(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Thuật toán Minimax chỉ tìm ra trạng thái \nhợp lệ cho 8 quân xe.")
        self.soTT = 0
        state = (np.zeros((8,8), dtype=int), [], 0) 
        
        best_score = -math.inf
        best_state = None
        
        # MAX bắt đầu đặt xe vào từng cột
        for action in self.Actions(state):
            value, VT = self.Min_Value(self.Result(state, action))
            if value > best_score:
                best_score = value
                best_state = VT
        
        if best_state is not None:
            self.controller.inBanCo(best_state)
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(None)
            self.controller.dungDemGio()
        else:
            self.controller.loiOrLuuY("Lỗi", "Không tìm thấy trạng thái hợp lệ.")
            self.controller.setColor(False)
            self.controller.dungDemGio()

    def Max_Value(self, state):
        if self.Terminal_Test(state):
            return self.Utility(state)
        
        v = -math.inf
        VT = None
        for action in self.Actions(state):
            a, VT = self.Min_Value(self.Result(state, action))
            v = max(v, a)
            
        return v, VT

    def Min_Value(self, state):
        if self.Terminal_Test(state):
            return self.Utility(state)
        
        v = math.inf
        VT = None
        for action in self.Actions(state):
            a, VT = self.Max_Value(self.Result(state, action))
            v = min(v, a)

        return v, VT

    def Terminal_Test(self, state):
        board, vt, score = state
        # Kết thúc khi đã đặt 8 quân hợp lệ hoặc không còn cột nào trống
        return len(vt) == 8 or len(self.Actions(state)) == 0

    def Utility(self, state):
        board, vt, score = state
        if self.kiemTraTrangThaiDich_Ver2(board):
            return 100, vt
        return len(vt) * 10 - self.demXungDot(board) * 20, vt

    def Actions(self, state):
        board, vt, score = state
        actions = []
        for col in range(8):
            # Nếu cột chưa có xe
            if 1 not in board[:, col]:
                actions.append(col)
        return actions

    def Result(self, state, action):
        board, vt, score = state
        states = None
        
        for row in range(8):
            board_copy = copy.deepcopy(board)
            if board_copy[row][action] == 0:
                board_copy[row][action] = 1
                if self.trangThaiAnToan(board_copy):
                    vt_new = copy.deepcopy(vt)
                    vt_new.append([row, action])
                    self.soTT += 1
                    new_score = score + self.chiPhiHeruristics(row, action)
                    states = (board_copy, vt_new, new_score)
                    break
        return states
    
    def demXungDot(self, board):
        """Đếm số cặp xe đang ăn nhau trên cùng hàng hoặc cột."""
        count = 0
        for i in range(8):
            if np.sum(board[i, :]) > 1:  # hàng
                count += 1
            if np.sum(board[:, i]) > 1:  # cột
                count += 1
        return count
    
    
    def AlphaBetaPruning(self):
        self.controller.loiOrLuuY("Lưu ý: ", "Thuật toán AlphaBeta chỉ tìm ra trạng thái \nhợp lệ cho 8 quân xe.")
        self.soTT = 0
        state = (np.zeros((8,8), dtype=int), [], 0) 
        
        best_score = -math.inf
        best_state = None
        
        # MAX bắt đầu đặt xe vào từng cột
        for action in self.Actions(state):
            value, VT = self.Max_Value_AB(self.Result(state, action), -math.inf, math.inf)
            if value > best_score:
                best_score = value
                best_state = VT
        
        if best_state is not None:
            self.controller.inBanCo(best_state)
            self.controller.setSoTrangThai(self.soTT)
            self.controller.setColor(None)
            self.controller.dungDemGio()
        else:
            self.controller.loiOrLuuY("Lỗi", "Không tìm thấy trạng thái hợp lệ.")
            self.controller.setColor(False)
            self.controller.dungDemGio()


    def Max_Value_AB(self, state, alpha, beta):
        if self.Terminal_Test(state):
            return self.Utility(state)
        
        v = -math.inf
        VT = None
        for action in self.Actions(state):
            a, VT = self.Min_Value_AB(self.Result(state, action), alpha, beta)
            v = max(v, a)
            if v >= beta:
                return v, VT
            alpha = max(alpha, v)
        return v, VT

    def Min_Value_AB(self, state, alpha, beta):
        if self.Terminal_Test(state):
            return self.Utility(state)
        
        v = math.inf
        VT = None
        for action in self.Actions(state):
            a, VT = self.Max_Value_AB(self.Result(state, action), alpha, beta)
            v = min(v, a)
            if v <= alpha:
                return v, VT
            beta = min(beta, v)
        return v, VT


    

    