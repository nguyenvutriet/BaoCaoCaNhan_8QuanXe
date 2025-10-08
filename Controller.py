import Model
import threading

class DatQuanXeController:
    def __init__(self, view):
        self.model = Model.DatQuanXeModel(self)
        self.view = view

    def suKien(self, thuatToan):
        self.view.reSetThongTin()
        if thuatToan == "Breadth First Search":
            self.view.cauHinhThongTin("Breadth First Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.BreadthFirstSearch).start()
            
        elif thuatToan == "Depth First Search":
            self.view.cauHinhThongTin("Depth First Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.DepFirstSearch).start()

        elif thuatToan == "Uniform Cost Search":
            self.view.cauHinhThongTin("Uniform Cost Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.UniformCostSearch).start()

        elif thuatToan == "Depth Limited Search":
            self.view.cauHinhThongTin("Depth Limited Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.DepthLimitedSearch_Ver2).start()

        elif thuatToan == "Iterative Deepening Search With DLS":
            self.view.cauHinhThongTin("Iterative Deepening Search With DLS")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.IterativeDeepening_DLS).start()

        elif thuatToan == "Iterative Deepening Search With DFS":
            self.view.cauHinhThongTin("Iterative Deepening Search With DFS")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.IterativeDeepening_DFS).start()

        elif thuatToan == "Greedy Search":
            self.view.cauHinhThongTin("Greedy Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.GreedySearch).start()

        elif thuatToan == "A* Search":
            self.view.cauHinhThongTin("A* Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.AStarSearch).start()

        elif thuatToan == "Hill Climbing":
            self.view.cauHinhThongTin("Hill Climbing")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.HillClimbing).start()

        elif thuatToan == "Simulated Annealing":
            self.view.cauHinhThongTin("Simulated Annealing")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.SimulatedAnnealing).start()

        elif thuatToan == "Beam Search":
            self.view.cauHinhThongTin("Beam Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.BeamSearch).start()

        elif thuatToan == "Genetic Algorithms":
            self.view.cauHinhThongTin("Genetic Algorithms")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.GeneticAlgorithms).start()

        elif thuatToan == "Recursive And Or Tree Search":
            self.view.cauHinhThongTin("Recursive And Or Tree Search")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.RecursiveAndOrTreeSearch_DFS).start()

        elif thuatToan == "Search in an unobservable environment":
            self.view.cauHinhThongTin("Search in an unobservable environment")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.SearchUnobservable_DFS).start()

        elif thuatToan == "Search In Partially Observable Environment":
            self.view.cauHinhThongTin("Search In Partially Observable Environment")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.PartiallyPbservable_GreedySearch).start()

        elif thuatToan == "CSP BackTracking":
            self.view.cauHinhThongTin("CSP BackTracking")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.CSP_Backtracking).start()

        elif thuatToan == "CSP Forward Checking":
            self.view.cauHinhThongTin("CSP Forward Checking")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.CSP_FORWARDCHECKING).start()

        elif thuatToan == "CSP Ac-3 Art Concistency":
            self.view.cauHinhThongTin("CSP Ac-3 Art Concistency")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.ArcConsistencyAlgorithm_3).start()

        elif thuatToan == "MiniMax Algorithm":
            self.view.cauHinhThongTin("MiniMax Algorithm")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.Minimax_Decision).start()
        
        elif thuatToan == "Alpha-Beta Pruning":
            self.view.cauHinhThongTin("Alpha-Beta Pruning")
            self.view.batDauDemGio()
            threading.Thread(target=self.model.AlphaBetaPruning).start()

        

        

        
        
        


    def getMucTieu(self):
        return self.model.getMucTieu()
    
    def inBanCo(self, arrViTri):
        self.view.inBanCoNguoiChoi(arrViTri)

    def dungDemGio(self):
        self.view.dungDemGio()

    def setSoTrangThai(self, soTT):
        self.view.setSoTrangThai(soTT)

    def loiOrLuuY(self, msg, str_):
        self.view.loiOrLuuY(msg, str_)

    def setColor(self, color):
        self.view.FlagColor = color

    


