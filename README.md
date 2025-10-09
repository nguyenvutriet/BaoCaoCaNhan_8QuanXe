# Báo Cáo Cá Nhân:
GVHD: Phan Thị Huyền Trang<br>
SVTT: Nguyễn Vũ Triết - MSSV: 23110161
# BÀI TOÁN 8 QUÂN XE

## 1. Giới thiệu bài toán
**Mục tiêu**: Xây dựng ứng dụng giải quyết trò chơi đặt 8 quân xe bằng cách sử dụng các thuật toán tìm kiếm trong AI.<br>
**Hiệu suất**: tìm kiếm ra giải pháp nhanh nhất, các quân xe đặt ở các vị trí không ăn nhau.<br>
**Môi trường**: ma trận 8x8, 8 quân xe.<br>
**Truyền động**: đặt quân xe vào ô hợp lý trên bàn cờ hoặc di chuyển quân xe.<br>
**Cảm biến**: kiểm tra trạng thái an toàn giữa các quân xe, kiểm tra trạng thái mục tiêu của bàn cờ.<br>

## 2. Các thuật toán
⚠️ **Lưu ý**: Do vấn đề về bộ nhớ nên lúc sinh trạng thái trong tất cả các thuật toán được sử dụng hầu như đều sử dụng sinh theo hàng. 
### *2.1.  Nhóm thuật toán tìm kiếm không có thông tin*

1. __Tìm kiếm theo chiều rộng (BFS)__
- Tìm kiếm theo chiều rộng [(Breadth First Search)](https://vi.wikipedia.org/wiki/T%C3%ACm_ki%E1%BA%BFm_theo_chi%E1%BB%81u_r%E1%BB%99ng) sử dụng cấu trúc queue (FIFO) để chứa các trạng thái được sinh ra. 
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, queue.<br>
Đầu ra: Giải pháp tìm thấy trạng thái mục tiêu.<br>
Đưa vào queue trạng thái ban đầu<br>
Loop:
    1. Lấy một trạng thái từ queue ra.
    2. Nếu là trạng thái mục tiêu thì return.
    3. Sinh các trạng thái có thể có từ trạng thái lấy ra từ queue đó.
    4. Đẩy các trạng thái sinh ra vào queue.
    5. Quay lại vòng lặp Loop.

- Kết quả sau áp dụng thuật toán:
![](/Img/BFS.gif)


2. __Tìm kiếm theo chiều sâu (DFS)__
- Tìm kiếm theo chiều sâu [(Depth First Search)](https://vi.wikipedia.org/wiki/T%C3%ACm_ki%E1%BA%BFm_theo_chi%E1%BB%81u_s%C3%A2u) sử dụng cấu trúc stack (LIFO) để chứa các trạng thái sinh ra.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, stack.<br>
Đầu ra: Giải pháp tìm thấy trạng thái mục tiêu.<br>
Đưa vào stack trạng thái ban đầu<br>
Loop:
    1. Lấy một trạng thái từ stack ra.
    2. Nếu là trạng thái mục tiêu thì return.
    3. Sinh các trạng thái có thể có từ trạng thái lấy ra từ stack đó.
    4. Đẩy các trạng thái sinh ra đó vào stack.
    5. Quay lại vòng lặp Loop.

- Kết quả sau áp dụng thuật toán: 
![](/Img/DFS.gif)

3. __Tìm kiếm chi phí đồng đều (UCS)__
- Thuật toán tìm kiếm chi phí đồng đều [(Uninform Cost Search)](https://vi.wikipedia.org/wiki/T%C3%ACm_ki%E1%BA%BFm_chi_ph%C3%AD_%C4%91%E1%BB%81u) sử dụng hàng đợi [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue) để lưu trữ các trạng thái được sinh ra. Tìm kiếm các chi phí trên đường đi có chi phí nhỏ nhất đến trạng thái mục tiêu.
- Chi phí mà UCS sử dụng là Path Cost (chi phí từ trạng thái ban đầu đến trạng thái hiện tại).
- Hướng dẫn UCS:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, priority queue.<br>
Đầu ra: Giải giáp từ trạng thái ban đầu đến trạng thái mục tiêu với chi phí tốt nhất.<br>
Đưa trạng thái ban đầu vào Priority Queue.<br>
Loop:
    1. Lấy từ Priority Queue trạng thái có chi phí tốt nhất (Chí phí nhỏ nhất).
    2. Nếu trạng thái đó là trạng thái mục tiêu thì dừng.
    3. Sinh các trạng thái đồng thời tính chi phí Path Cost cho từng trạng thái đó.
    4. Sau khi sinh xong đưa vào Priority Queue và quay lại Loop.

- Kết quả sau áp dụng thuật toán:
![](/Img/UCS.gif)

4. __Tìm kiếm theo chiều sâu lặp lại (IDS)__
- Thuật toán tìm kiếm theo chiều sâu lặp sâu dần [(Iterative Deepening Search)](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search) là sự kết hợp của thuật toán BFS và DFS. Sử dụng với độ sâu lặp đi lặp lại đến khi nào tìm được trạng thái mục tiêu thì dừng lại.
- Một số sách viết tắt thuật toán theo chiều sâu lặp lại là IDS hoặc IDL. Nhưng thường sử dụng nhất là IDS.
- Thuật toán này có 2 hướng sử dụng: được sử dụng với DFS và BFS hoặc DLS và BFS. 

- Hướng dẫn IDS với DLS:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán DLS.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Loop độ sâu tăng từ 1:
    1. gọi thuật toán DLS và truyền vào độ sâu đang lặp.
    2. nếu trả về mục tiêu thì return
    3. Nếu không trả về mục tiêu thì tiếp tục tăng độ sâu.

- Kết quả sau khi áp dụng thuật toán sử dụng với DLS
![](/Img/IDS_DLS.gif)

- Hướng dẫn IDS với DFS: <br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, stack.<br>
Đầu ra: Giải pháp đi từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Loop 1 độ sâu tăng dầu từ 1:
    1. Đưa trạng thái ban đầu vào stack
    2. Loop 2:
        1. Lấy một trạng thái từ stack (theo cơ chế LIFO).
        2. kiểm tra nếu đạt độ sâu giới hạn thì quan lại Loop 1.
        3. Nếu chưa đạt độ sâu giới hạn thì sinh trạng thái.
        4. Đưa các trạng thái sinh ra đó vào stack và quay lại loop 2.

- Kết quả sau khi áp dụng thuật toán sử dụng với DFS:
![](/Img/IDS_DFS.gif)

5. __Tìm kiếm theo chiều sâu giới hạn (DLS)__
- Thuật toán tìm kiếm theo chiều sâu giới hạn [(Depth Limited Search)](https://www.geeksforgeeks.org/artificial-intelligence/depth-limited-search-for-ai/) là phiên mở rộng của thuật toán DFS.
- Khi gặp cây có độ sâu vô hạn mà mục tiêu chỉ nằm ở giữa thân, trong khi đó DFS sẽ duyệt đến độ sâu cuối cùng cho theo cơ chế LIFO. Nên để để tối ưu với trường hợp trên thuật toán DLS được sử dụng duyệt với độ sâu với hạn cho đến khi tìm được mục tiêu.
- Ưu điểm: có thể trách khỏi tình trạng duyệt vô hạn và tránh được việc ngốn bộ nhớ.
- Nhược điểm: Thuật toán duyệt với độ sâu cố định sẽ gặp phải tình trạng không tìm được mục tiêu vì chỉ duyệt đến độ sâu định sẵn nhưng mục tiêu có thể nằm ở sâu hơn. Thuật toán này cũng khá tốn bộ nhở vì thực hiện gọi đệ quy nhiều lần. 
- Hướng dẫn: <br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, độ sâu.<br>
Đầu ra: giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Thực hiện gọi hàm đệ quy và truyền vào vấn đề của bài toán, trạng thái ban đầu và độ sâu.<br>
Hàm đệ quy:
    1. Nếu trạng thái đạt trạng thái mục tiêu thì dừng.
    2. Nếu như độ sâu giảm về không thì return *"Không tìm thấy"*.
    3. Ngược lại: 
        1. Gán CutOff ← False
        2. Child ← sinh các trạng thái kế tiếp
        3. result ← Hàm đệ quy (Child, độ sâu -1)
        4. Nếu result là *"Không tìm thấy"* thì CutOff ← True
        5. Nếu như result không phải là None thì return result.
    4. Nếu CutOff ← True thì return *"Không tìm thấy"*
    5. Ngược lại return None

- Kết quả sau khi áp dụng thuật toán:
![](/Img/DLS.gif)

6. __Đánh giá các thuật toán trong nhóm tìm kiếm không có thông tin__
![](/Img/DanhGiaN1.gif)

### *2.2.Nhóm thuật toán tìm kiếm có thông tin*
1. __Gready Search__
- Thuật toán [Greedy Search](https://en.wikipedia.org/wiki/Greedy_algorithm) sử dụng cấu trúc Priority Queue để lưu các trạng thái sinh ra từ bàn cờ. Mỗi lần lấy trạng thái ra Greedy chọn trạng thái có chi phí tốt nhất (chi phí thấp nhất). 
- Thuật toán này sử dụng hàm ước lượng chi phí [(Herurictics)](https://vi.wikipedia.org/wiki/Heuristic) để tính chi phí cho các trạng thái sinh ra. 
- Ước lượng chi phí từ trạng thái ban đầu đến trạng thái mục tiêu.
- Thuật tóa Greedy muốn tối ưu đòi hỏi ta phải xây dựng hàm ước lượng chi phí gần đúng nhất so với trạng thái mục tiêu.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán GS, hàm Herurictics.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Đưa vào priorityQueue trạng thái ban đầu kèm chi phí.<br>
Loop:
    1. Lấy từ priorityQueue trạng thái có chi phí thấp nhất.
    2. Nếu trạng thái lấy ra là trạng thái mục tiêu thì return.
    3. Sinh các trạng thái tiếp theo và tính ước lượng chi phí cho các trạng thái sinh ra.
    4. Đưa các trạng thái sinh ra đó vào priorityQueue.
    5. Quay lại vòng lặp Loop.

- Kết quả sau khi áp dụng thuật toán:
![](/Img/GS.gif)

2. __A* Search__
- Thuật toán [A* SSearch](https://vi.wikipedia.org/wiki/Gi%E1%BA%A3i_thu%E1%BA%ADt_t%C3%ACm_ki%E1%BA%BFm_A*) sử dụng cấu trúc lưu trữ và ý tưởng gần giống với thuật toán Gready. Chỉ khác ở bên Greedy chỉ sử dụng hàm Herurictics để tính chi phí còn A* sử dụng hai hàm Herurictics và Path Cost để tính chi phí.
- Thuật toán A* muốn tối ưu phải xây dụng 2 hàm tính chi phí có tính chính xác cao.
- Nếu xây dụng hàm Path Cost và Herurictics chưa chính xác thì thuật toán A* có thể chạy lâu hơn hàm Greedy.
- Hàm tính chi phí: f(x) = g(x) + h(x)
- Trong đó: 1. f(x) là tổng các chi phí
            2. g(x) là chi phí từ trạng thái ban đầu đến hiện tại (Path Cost).
            3. h(x) là chi phí từ trạng thái hiện tại đến mục tiêu (Herurictics).
- Lưu ý: trong một số sách người ta ghi g(x) = f(x) + h(x).
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán AS, các hàm tính chi phí.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Đưa trạng thái ban đầu kèm chi phí vào priorityQueue.<br>
Loop:
    1. Lấy từ priorityQueue trạng thái tốt nhất
    2. Nếu trạng thái lấy ra đó là trạng thái mục tiêu thì return.
    3. Sinh các trạng thái kế tiếp và tính chi phí f(x) cho trạng thái đó.
    4. Đưa trạng các trạng thái sinh ra vào priorityQueue.
    5. Quay lại vòng lặp Loop.

- Kết quả sua khi áp dụng thuật toán:
![](/Img/AS.gif)

3. __Đánh giá nhóm thuật toán tìm kiếm có thông tin__
![](/Img/DanhGiaN2.gif)

### *2.3. Nhóm thuật toán tìm kiếm Local Search*
1. __Hill climbing__
- Thuật toán [Hill Climbing](https://en.wikipedia.org/wiki/Hill_climbing) sử dụng cấu trúc priorityQueue để lưu trữ các trạng thái sinh ra. Nhưng thuật toán này khác với các thuật toán khác trong nhóm thuật toán tìm kiếm có thông tin là mỗi lần sinh trạng thái đưa vào queue và sau khi chọn được trạng thái tốt nhất thì các trạng thái còn lại trong queue không được sử dụng tiếp mà bị xóa đi.
- Thuật toán này rất dễ bị vướng ở cục bộ bởi vị nó chỉ chọn trạng thái tốt nhất từ các trạng thái sinh ra từ trạng thái hiện tại, nếu như trạng thái tốt nhất chọn ra không tốt hơn trạng thái hiện tại thì chương trình bị mắc ở cục bộ.
- Trong thuật toán này có sử dụng hàm herurictics để tính chi phí.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, hàm herurictics, thuật toán Hill Climbing.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Lưu trạng thái ban đầu vào H<br>
Loop:
    1. Kiểm trạn trạng thái H có phải trạng thái mục tiêu không.
    2. Khởi tạo priorityQueue rỗng.
    3. Sinh các trạng thái lân cận từ H, tính chi phí cho các trạng thái lân cận đó và đưa vào priorityQueue.
    4. Nếu priorityQueue là rỗng thì return "Không thể sinh tiếp trạng thái".
    5. Chọn M từ priorityQueue là trạng thái có chi phí thấp nhất.
    6. Nếu chi phí của M > chi phí của H thì return "Không có trạng thái nào tốt hơn trạng thái hiện tại".
    7. Gán H = M và tiếp lục lặp Loop.

- Kết quả sau khi áp dụng thuật toán: 
![](/Img/Hill.gif)

2. __Simulated Annealling__ 
- Thuật toán [Simulated Annealling](https://en.wikipedia.org/wiki/Simulated_annealing) còn được gọi là thuật toán mô phỏng luyện kim. Đây là phiên bản cải tiến hơn của Hill Climbing để tránh việc tìm kiếm trong cục bộ mà đưa dần tiếp kiếm ra toàn  cục với một xác xuất nào đó.
- Thuật toán này được tối ưu khi ta xây dụng hàm tính nhiệt độ một cách chính xác và hàm tính chi phí phải tối ưu. Làm tăng khả năng tìm kiếm ra toàn cục hơn.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán Simulated Annealling, hàm tính chi phí.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến mục tiêu.<br>
Lưu trạng thái ban đầu là H.<br>
Loop t = 1:
    1. Kiểm trạn trạng thái H có phải trạng thái mục tiêu không.
    2. Xây dựng hàm tính tính độ T dựa trên t.
    3. Nếu T giảm về 0 thì return "Không tìm thấy mục tiêu".
    4. Khởi tạo priorityQueue rỗng.
    5. Sinh các trạng thái lân cận từ H, tính chi phí cho các trạng thái lân cận đó và đưa vào priorityQueue.
    6. Nếu priorityQueue là rỗng thì return "Không thể sinh tiếp trạng thái".
    7. Chọn M từ priorityQueue là trạng thái có chi phí thấp nhất.
    8. Nếu chi phí của M > chi phí của H:
        1. Tính xác xuất theo công thức exp(−Δ(chi phí M, chi phí H)/T).
        2. Chọn một xác xuất random.
        3. Nếu xác suất tính theo công thức > xác xuất random thì chấp nhận trạng thái xấu: H = M.
        4. Quay lại vòng lặp Loop.
    9. Gán H = M và tiếp tục lặp Loop.

- Kết quả sau khi áp dụng thuật toán:
![](/Img/SA.gif)

3. __Beam Search__
- Thuật toán [Beam Search](https://en.wikipedia.org/wiki/Beam_search) dựa trên thuật toán tìm kiếm theo chiều rộng nhưng thay vì lấy hết trạng thái sinh ra thì ở đây Beam chỉ lấy k trạng thái tốt nhất. Beam sử dụng hàm Herurictics để tính chi phí và dùng  queue giống như BFS để lưu trạng thái sinh ra.
- Do đó thuật toán này có thể được coi là phiên bản tối ưu của BFS.
- Nhưng để thuật  toán này tối ưu được ta cũng phải xây dựng hàm tính chi phí phải tối ưu.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán BS, hàm herurictics.<br>
Đầu ra: giải pháp từ trạng thái ban đầu đến mục tiêu.<br>
đưa vào queue trạng thái ban đầu.<br>
Loop:
    1. Lấy ra khỏi queue một trạng thái theo cơ  chế (FIFO).
    2. Nếu trạng thái lấy ra là mục tiêu thì return.
    3. Tạo một priorityQueue rỗng.
    4. sinh các trạng thái từ trạng thái lấy ra và tính chi phí cho các trạng thái đó.
    5. Đưa vào priorityQueue các trạng thái sinh ra đó.
    6. Lấy ra khỏi priorityQueue k trạng thái có chi phí thấp nhất.
    7. Đưa k trạng thái tốt nhất đó vào queue và quay lại Loop.

- Kết quả sau khi áp dụng thuật toán:
![](/Img/Beam.gif)

4. __Genetic Algorithms__
- Thuật toán [Genetic ALgorithms](https://aivietnam.edu.vn/blog/giai-thuat-di-truyen#4-crossover-lai-gh%C3%A9p) được thiết lập theo các cơ chế sau: Khởi tạo quần thểm, chọn lọc quần thể, lại ghép và độ biến gen các cá thể trong quần thể.
- Thuật toán này  khó tìm ra mục tiêu nếu các các thể trong quần  thể thiếu tính đa dạng và quần thể ít cá thể.
- Do vậy để thuật toán này tối ưu hơn ta cần tăng số lượng cá thể trong quần thể, tăng tính  đa dạng của quần thể.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, tập quần thể ban đầu, thuật toán GA.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Lưu ý: các quần thể là một tập các trạng thái của bàn cờ.<br>
Khởi tạo quần thể chưa 6 trạng thái bàn cờ ngẫu nhiên<br>
Loop với số lượng mã Gen cố định:
    1. chọn lọc 2 trạng thái tốt và random ngẫu nhiên một trạng thái xấu trong quần thể ban đầu.
    2. Đem các trạng thái chọn lọc đi lai. (lai từng cặp trạng thái khác nhau)
        1. khởi tạo tỉ lệ lai 65%.
        2. với mỗi cột trong trạng thái có một xác xuất random.
        3. nếu xác xuất random < tỉ lệ lai thì ta sẽ hoán đổi các cột giữa 2 trạng thái với nhau.
    3. Đem các trạng thái vừa lai xong đi đột biến.
        1. Khởi tạo tỉ lệ đột biến 5%.
        2. Với mỗi cột trong trạng thái có một giá trị đột biến random.
        3. Nếu giá trị đó < tỉ lệ  đột biến thì đưa tất cả giá trị trong vột về 0 và random ngẫu nhiên một vị trí đặt 1.
    4. Đưa các trạng thái trên vào quần thể mới.
    5. Nếu quần thể mới chưa đủ 6 trạng thái thì tiếp tục quá trình trên.
    6. Nếu quần thể mới đủ 6 trạng thái thì kiểm tra trong quần thể mới có mục tiêu không nếu có thì return.

- Kết quả sau khi áp dụng thuật toán:
![](/Img/GA.gif)

5. __Đánh giá nhóm thuật toán Local Search
![](/Img/DanhGiaN3.gif)

### *2.4. Nhóm thuật toán tìm kiếm trong môi trường phức tạp*
1. __And-Or Tree Search__
- Thuật toán [And-Or Tree Search](https://en.wikipedia.org/wiki/And%E2%80%93or_tree) có thể được sử dụng chung với các nhóm thuật toán có thông tin và không có thông tin. Trong bài toán này thuật toán này được sử dụng chung với thuật toán DFS. Ban đầu thuật toán sẽ gọi hàm Or sẽ xác định việc sinh ra các hành động và đảm bảo bột trong các hành động là mục tiêu thì trả về. Sau khi quyết định được hành động gọi hàm And và truyền vào một tập các trạng thái sinh ra từ hành động đặt và phải thõa mãn các trạng thái sinh ra từ hành động Or phải tìm thấy mục tiêu. 
- Thuật toán là sử dụng ý tưởng giống các phép toán tử logic trong toán học. And trả về đúng nếu cả hai cùng đúng còn Or chỉ đúng khi một trong hai đúng.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán And-Or.<br>
Đầu ra: Giải pháp tìm ra tập mục tiêu hợp lệ.<br>
    1. Gọi hàm Or truyền vào trạng thái ban đầu và đường đi
    2. Hàm Or:
        1. kiểm tra xem trạng thái truyền vào là mục tiêu thì trả về trạng thái đó
        2. Kiểm tra xem có chu trình hay không
        3. Nếu không có chu trình thì thêm trạng thái vào path.
        4. Gọi hàm And và truyền vào tập trạng thái sinh ra từ hành động được chọn.
        5. Nếu giá trị mà hàm And trả về không phải False thì xóa trạng thái đó ra khỏi path và return trạng thái đó.
        6. reuturn False nếu không thể gọi tiếp hàm And.
    3. Hàm And:
        1. Loop mỗi trạng thái trong tập trạng thái được nhận:
            1. Gọi hàm Or truyền vào trạng thái đang xét.
            2. nếu hàm Or trả về False thì return False
        2. return tập trạng thái đều là mục tiêu.

- Kết quả khi áp dụng thuật toán:
![](/Img/ANDOR.gif)

2. __Tìm kiếm trong môi trường không nhìn thấy__
- Thuật toán [tìm kiếm trong môi trường không nhìn thấy](https://staff.agu.edu.vn/nvhoa/AI/lecture2.pdf) ban đầu sẽ không xác định được vị trí hay có thông tin rằng mình đang ở đâu mà phải xây dựng một tập niềm tin ban đầu và muốn biết được kết quả thì cũng xây dựng nên tập niềm tin mục tiêu.
- Ở thuật toán nào khó tìm thấy mục tiêu đối với bài toán 8 quân xe khi mà tập niềm tin mục tiêu đưa vào quá ít, và có thể là không tìm ra được. 
- Đối với thuật toán này muốn tối ưu thuật toán thif ta phải xây dựng niềm tin ban đầu có nhiều trạng thái mục tiêu nhất và niềm tin ban đầu phải có kích thước nhỏ. Để giảm dung lượng bộ nhớ giúp chương trình chạy nhanh hơn.
- khi xây tập niềm tin ban đầu và niềm tin mục tiêu phải bảo đảm các tập có số trạng thái > 2.
- Ở trong chương trình này được xây dựng dựa trên thuật toán DFS.
- Hướng dẫn: <br>
- Đầu vào: bài toán 8 quân xe, niềm tin ban đầu, niềm tin kết thúc.<br>
- Đầu ra: Tập các trạng thái đặt quân xe hợp lệ.<br>
    1. Xây dựng niềm tin ban đầu.
    2. Xây dựng niềm tin kết thúc.
    3. Đưa niềm tin ban đầu vào stack.
    4. Xây dưng tập hành động: di chuyển và đặt
    5. Loop:
        1. Lấy 1 phần tử đầu tiên ra khỏi stack (LIFO).
        2. Kiểm tra các trạng thái trong phần tử: nếu tất cả các trạng thái đều nằm trong niềm tin ban đầu thì dừng.
        3. thực hiện các hành động lên phần tử lấy ra đó.
        4. mội lần thực hiện 1 hành động sinh ra một tập các trạng thái của bàn cờ và đưa vào stack.

- Kết quả thi áp dụng thuật toán: 
![](/Img/UnE.gif)

3. __Tìm kiếm trong môi trường nhìn thấy một phần__
- Thuật toán [tìm kiếm trong môi trường nhìn thấy một phần](https://staff.agu.edu.vn/nvhoa/AI/lecture2.pdf) có thể coi là phiên bản tối ưu của phiên bản tìm kiếm trong môi trường không nhìn thấy. Thay vì không nhìn thấy mà đi tìm kiếm mục tiêu mù quáng thì ở đây sẽ nhìn thấy được một hoặc 2 vị trí hoặc có thể hơn trong niềm tin ban đầu.
- Nhưng ở thuật toán này không sử dụng với thuật toán DFS mà xây dựng dựa trên thuật toán Greedy Search.
- tương tự như Greedy thì để thuật toán tối ưu phải xây dựng hàm ước lượng chi phí một cách tối ưu nhất và ngoài ra ta còn cần xây dựng thêm niềm tin mục tiêu đa dạng hơn.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, niềm tin ban đầu, niềm tin kết thúc, nhìn thấy được một quân xe trên bàn cờ.
Đầu ra: tập các trạng thái đặt 8 quân xe hợp lệ.
    1. Xây dựng niềm tin ban đầu và các trạng thái phải chứa quân xe đã biết trước.
    2. Xây dựng niềm tin mục tiêu.
    3. Xây dựng tập hành động: di chuyển và đặt.
    4. đưa niềm tin ban đầu vao priorityQueue.
    5. Loop:
        1. Lấy phần tử có chi phí thấp nhất ra khởi priorityQueue.
        2. Kiểm tra các trạng thái trong phần tử thuộc trong niềm tin mục tiêu không: nếu tất cả đều thuộc thì dừng.
        3. Từ các hành động sinh các tập trạng thái và ước lượng chi phí cho các tập đó.
        4. Đưa các tập trạng thái sinh ra vào priorityQueue.

- Kết quả khi áp dụng thuật toán: 
![](/Img/POS.gif)

4. __Đánh giá nhóm thuật toán tìm kiếm trong môi trường phức tạp__
![](/Img/DanhGiaN4.gif)


### *2.5. Nhóm thuật toán tìm kiếm thõa mãn ràng buộc*
1. __CSP Backtracking__
- Thuật toán [CSP](https://vi.wikipedia.org/wiki/L%E1%BA%ADp_tr%C3%ACnh_r%C3%A0ng_bu%E1%BB%99c) được sử dụng với [Backtracking](https://en.wikipedia.org/wiki/Backtracking) ban đầu cần tạo các tập biến, tập giá trị và tập ràng buộc sau mới gọi hàm bactracking. 
- Để giảm bớt thời gian chạy và bộ nhớ cũng như tăng khả năng tìm thấy thì thuật toán này không tìm ra một mục tiêu cụ thể nào đó mà chỉ tìm ra một trạng thái đặt 8 quân xe hợp lệ.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, tập biến, tập giá trị, tập ràng buộc.<br>
Đầu ra: Trạng thái đặt xe phù hợp.<br>
    1. Xây dựng tập biến chứa 8 quân xe.
    2. Xây dựng tập giá trị là các vị trí có thể đặt của quân xe.
    3. Xây dựng tập ràng buộc: không đặt cùng hàng và cùng cột.
    4. Gọi hàm Backtracking và truyền vào tập biến, tập giá trị và tập ràng buộc.
    5. Hàm Backtracking:
        1. kiểm tra xem bàn cờ có hợp lệ không nếu hợp lệ thì dừng.
        2. Chọn ngẫu nhiên một quân xe.
        3. Chọn ngẫu nhiên một giá trị từ tập giá trị của quân xe.
        4. Đặt quân xe được chọn ngẫu nhiên lên vị trí có giá trị được chọn ngẫu nhiên.
        5. Gọi Backtracking
        6. nếu giá trị trả về của hàm Backtracking là một trạng thái hợp lệ thì return
        7. return None

- Kết quả khi áp dụng thuật toán:
![](/Img/CSP_BTK.gif)

2. __CSP Forward Checking__
- Thông qua quá trình quan sát thì thuật toán CSP Backtracking sẽ thử hết tất các các giá trị nằm trong miền điều này dễ dẫn tới việc bộ nhớ quá lớn và tốn thời gian. Để giảm thiểu việc này mỗi lần ta đặt quân xe ra sẽ giới hạn lại tập giá trị, khi đặt quân xe lên sẽ giảm các vị trí mà quân xe đã đặt đó tấn công được. Đây được gọi là thuật toán Forward Checking.
- Thuật toán này có thể xem là phiên bản tối ưu hơn của Backtracking.
- Hướng dẫn: <br>
Đầu vào: Bài toán 8 quân xe, tập biến, tập giá trị, tập ràng buộc.<br>
Đầu ra: Trạng thái đặt xe phù hợp.<br>
    1. Xây dựng tập biến chứa 8 quân xe.
    2. Xây dựng tập giá trị là các vị trí có thể đặt của quân xe.
    3. Xây dựng tập ràng buộc: không đặt cùng hàng và cùng cột.
    4. Gọi hàm ForwardChecking và truyền vào tập biến, tập giá trị và tập ràng buộc.
    5. Hàm ForwardChecking:
        1. kiểm tra xem bàn cờ có hợp lệ không nếu hợp lệ thì dừng.
        2. Chọn ngẫu nhiên một quân xe.
        3. Chọn ngẫu nhiên một giá trị từ tập giá trị của quân xe và đặt quân xe lên vị trí có giá trị được chọn.
        4. Gọi hàm F để loại bỏ bớt tập giá trị mà chứa các vị trị bị quân xe đã đặt có thể tấn công được.
        5. Gọi ForwardChecking.
        6. nếu giá trị trả về của hàm ForwardChecking là một trạng thái hợp lệ thì return.
        7. return None

- Kết quả khi áp dụng thuật toán:
![](/Img/CSP_FTK.gif)

3. __AC-3 Art Concistencey__
- Thuật toán [AC-3](https://en.wikipedia.org/wiki/AC-3_algorithm) được xây dựng dựa trên việc tinh giảm miền giá trị trước khi đưa vào quá trình Backtracking. Mỗi quân xe sẽ có một miền giá trị riêng cho mình, thay vì mỗi lần gọi backtracking sau khi đặt thì mới cắt giảm miền giá trị giống Forward Checking thì AC-3 sẽ chọn lọc ra mỗi miền giá trị riêng thuộc về mỗi quân xe bằng việc thõa mãn ràng buộc nào đó.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, tập biến, tập giá trị và các ràng buộc.<br>
Đầu ra: Trạng thái đặt 8 quân xe hợp lý.<br>
    1. Xây dựng tập biến.
    2. Xây dựng tập giá trị cho mỗi biến.
    3. Gọi hàm AC3:
        1. Tạo các cặp quân xe và đưa vào queue.
        2. Gọi hàm revise để kiểm tra: 
            1. Nếu một giá trị của x không thão màn ràng buộc với tất cả giá trị của y trong miền giá trị của y thì sẽ xóa giá trị x đó và trả về True
            2. Nếu có một giá thị x thõa màn ràng buộc với một giá trị của y thì trả về False.
        3. Nếu hàn revise là True thì kiểm tra:
            1. Nếu miền giá trị của x đã bị xóa hết thì return False
            2. Đưa các biến hàng xóm không phải y ghép thành cặp với x và đưa vào queue. 
    4. Sau khi miền giá trị của các quân xe đã bị cắt giảm thì bắt đầu gọi hàm Backtracking để tìm ra mục tiêu.

- Kết quả sau khi áp dụng thuật toán: 
![](/Img/AC3.gif)

4. __Đánh giá nhóm thuật toán tìm kiếm trong môi trường thõa mãn ràng buộc__
![](/Img/DanhGiaN5.gif)

### *2.6. Nhóm thuật toán tìm kiếm đối kháng*
1. __MiniMax Decision__
- Thuật toán [MiniMax Decision](https://vi.wikipedia.org/wiki/Minimax) thuộc nhóm tìm kiếm đối kháng bởi vì nó tồn tại 2 hàm quyết định là Min và Max. Max là luôn tìm kiếm trạng thái tốt nhất trong số các trạng thái mà hàm Min đưa. Còn Min thì chọn các  trạng thái Nhỏ nhất được sinh ra để làm hại Max. 
- Do sự cạnh tranh như vậy nên số trạng thái sinh ra của thuật toán có thể rất lớn.
- Hướng dẫn: <br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu.<br>
Đầu ra: Trạng thái đặt 8 quân xe phù hợp.<br>
    1. Khởi tạo trạng thái ban đầu, điểm đanh giá, lưu vị trí đặt xe.
    2. Loop với mỗi cột có thể đặt:
        1. Gọi hàm Min trả về value đánh giá và mảng lưu vị trí.
        2. Chọn mảng có value cao nhất.
    3. Hàm Min:
        1. Kiểm tra nếu đặt đủ 8 quân xe trả về 100, mảng lưu vị trí nếu không thì trả về điểm đanh giá và vị trí các quân.
        2. khởi tạo v = inf và Loop với mỗi cột có thể đặt
            1. Gọi hàm Min.
            2. Chọn giá trị nhỏ nhất giữa v và giá trị trả về của Max.
        3. Trả về v, mảng lưu vị trí các quân.
    4. Hàm Max:
        1. Kiểm tra nếu đặt đủ 8 quân xe trả về 100, mảng lưu vị trí nếu không thì trả về điểm đanh giá và vị trí các quân.
        2. khởi tạo v = inf và Loop với mỗi cột có thể đặt
            1. Gọi hàm Min.
            2. Chọn giá trị lớn nhất giữa v và giá trị trả về của Min.
        3. Trả về v, mảng lưu vị trí các quân.

- Kết quả sau khi áp dụng thuật toán:
![](/Img/MiniMax.gif)

2. __Alpha-Beta-Pruning__
- Thuật toán [Alpha-Beta Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) giảm số lượng các trạng thái sinh ra của bài toán. Ở thuật toán MiniMax trong khi duyệt hết tất cả trạng thái có thể thì ở đây thay vì nó duyệt hết có chặn các tham số alpha và beta. Nếu giá v trong Min mà nhỏ hơn alpha và v trong Max mà lớn hơn Beta thì trả về v không cần duyệt tiếp.
- Với cách hoạt động như vậy thuật toán giúp giảm đáng kể số lượng trạng thái sinh ra trong chương trình.
- Hướng dẫn:<br>
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu.<br>
Đầu ra: Trạng thái đặt 8 quân xe phù hợp.<br>
    1. Khởi tạo trạng thái ban đầu, điểm đanh giá, lưu vị trí đặt xe.
    2. Loop với mỗi cột có thể đặt:
        1. Khởi tạo Alpha=-inf, Beta=inf
        2. Gọi hàm Max trả về value đánh giá và mảng lưu vị trí.
        3. Chọn mảng có value cao nhất.
    3. Hàm Min:
        1. Kiểm tra nếu đặt đủ 8 quân xe trả về 100, mảng lưu vị trí nếu không thì trả về điểm đanh giá và vị trí các quân.
        2. khởi tạo v = inf và Loop với mỗi cột có thể đặt
            1. Gọi hàm Min.
            2. Chọn giá trị nhỏ nhất giữa v và giá trị trả về của Max.
            3. Nếu v <= Alpha thì return v, vị trí quân xe.
            4. Beta = min(v, Beta).
        3. Trả về v, mảng lưu vị trí các quân.
    4. Hàm Max:
        1. Kiểm tra nếu đặt đủ 8 quân xe trả về 100, mảng lưu vị trí nếu không thì trả về điểm đanh giá và vị trí các quân.
        2. khởi tạo v = inf và Loop với mỗi cột có thể đặt
            1. Gọi hàm Min.
            2. Chọn giá trị lớn nhất giữa v và giá trị trả về của Min.
            3. Nếu v >= Beta thì return v, vị trí quân xe.
            4. Alpha = max(v, Alpha).
        3. Trả về v, mảng lưu vị trí các quân.

- Kết quả sau khi áp dụng thuật toán:
![](/Img/AlphaB.gif)

3. __Đánh giá nhóm thuật toán tìm kiếm đối kháng__
![](/Img/DanhGiaN6.gif)

## 3. Môi trường phát triển
- Ngôn ngữ: Python
- Version: tải python 3.13.7 từ [python.org]( https://www.python.org/)
- Thư viện: cài đặt các thư viện:
tkinter:
    ```python
    pip install tkinter
    ```

    numpy:
    ```python
    pip install numpy
    ```

    Hoặc thư viện pygame thay cho thư viện tkinter:
    ```python
    pip install pygame
    ```
    PIL:
    ```python
    pip install Pillow
    ```
    Matplotlib: 
    ```python
    pip install matplotlib
    ```

    Các thư viện khác cần import: math, queue, random, collections, threading, time. <br>

## 4. Hướng dẫn chạy chương trình
- chạy file **Home.py**

- chọn nút ***Start***
![](/Img/Home.png)

- Sau khi nhấn nút ***Start*** chương trình sẽ đi vào giao diện bên dưới:
![](/Img/CTMain.png)

- Xổ **Combobox** xuống để chọn thuật toán:
![](/Img/CBB.png)

- Nhấn chuột vào thuật toán bạn muốn chọn và nhấn nút ***Chay*** chương trình sẽ hiện ra các thông tin của thuật toán.
![](/Img/Chay.png)

- Sau khi một thuật toán chạy xong có thể chọn các thuật toán khác để chạy tiếp.
![](/Img/Chay1.png)

- Nút ***XemDT*** để hiển thị đánh giá các thuật toán, trục tung là không gian trạng thái, trục hoành là thời gian chạy thuật toán.
![](/Img/DT.png)

- Nút ***Reset*** để *clear* toàn bộ thông tin trên giao diện.

## 5. Một số thông tin khác
- Để dễ quả lý code trong bài trên ta xây dựng theo mô hình MVC (Model-View-Controller)
- View: trong đây chỉ xử lý các đoạn liên quan tới giao diện.
- Model: là phần bên trong của bài toán, nơi chạy các thuật toán AI, chứa bàn cờ là ma trận 0 8x8 kèm theo một số hàm phụ để bổ trợ cho các thuật toán.
- Controller: Kiểm soát việc tương tác giữa View mà Model.
- Hình ảnh Minh hoạc mô hình MVC cho bài toán 8 quân xe:
![](/Img/MVC.png)

- Giải thích cách hoạt động:<br>
    1. Chương trình Home sẽ gọi đến View để hiển thị giao diện.
    2. Nếu Home chọn thuật toán thì View sẽ gửi yêu cầu đến Controller.
    3. Controller nhận diện và truyền lại thông tin này đến Model để chạy thuận toán.
    4. Model chạy xong sẽ báo kết quả đến cho Controller.
    5. Controller gửi lại cho View để hiển thị kết quả cho Home xem.









