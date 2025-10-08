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
⚠️ **Lưu ý**: Do vấn đề về bộ nhớ nên lúc sinh trạng thái trong tất các các thuật toán được sử dụng hầu như đều sử dụng sinh theo hàng. 
### *2.1.  Nhóm thuật toán tìm kiếm không có thông tin*

1. __Tìm kiếm theo chiều rộng (BFS)__
- Tìm kiếm theo chiều rộng [(Breadth First Search)](https://vi.wikipedia.org/wiki/T%C3%ACm_ki%E1%BA%BFm_theo_chi%E1%BB%81u_r%E1%BB%99ng) sử dụng cấu trúc queue (FIFO) để chứa các trạng thái được sinh ra. 
- Hướng dẫn BFS:<br>
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
- Hướng dẫn DFS:<br>
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


4. __Tìm kiếm theo chiều sâu giới hạn (DLS)__
- Thuật toán tìm kiếm theo chiều sâu giới hạn [(Depth Limited Search)](https://www.geeksforgeeks.org/artificial-intelligence/depth-limited-search-for-ai/) là phiên mở rộng của thuật toán DFS.
- Khi gặp cây có độ sâu vô hạn mà mục tiêu chỉ nằm ở giữa thân, trong khi đó DFS sẽ duyệt đến độ sâu cuối cùng cho theo cơ chế LIFO. Nên để để tối ưu với trường hợp trên thuật toán DLS được sử dụng duyệt với độ sâu với hạn cho đến khi tìm được mục tiêu.
- Ưu điểm: có thể trách khỏi tình trạng duyệt vô hạn và tránh được việc ngốn bộ nhớ.
- Nhược điểm: Thuật toán duyệt với độ sâu cố định sẽ gặp phải tình trạng không tìm được mục tiêu vì chỉ duyệt đến độ sâu định sẵn nhưng mục tiêu có thể nằm ở sâu hơn. Thuật toán này cũng khá tốn bộ nhở vì thực hiện gọi đệ quy nhiều lần. 
- Hướng dẫn DLS: <br>
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

5. __Tìm kiếm theo chiều sâu lặp lại (IDS)__
- Thuật toán tìm kiếm theo chiều sâu lặp sâu dần [(Iterative Deepening Search)](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search) là sự kết hợp của thuật toán BFS và DFS. Sử dụng với độ sâu lặp đi lặp lại đến khi nào tìm được trạng thái mục tiêu thì dừng lại.
- Một số sách viết tắt thuật toán theo chiều sâu lặp lại là IDS hoặc IDL. Nhưng thường sử dụng nhất là IDS.
- Thuật toán này có 2 hướng sử dụng: được sử dụng với DFS và BFS hoặc DLS và BFS. 
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

- Hướng dẫn IDS với DLS:
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán DLS.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Loop độ sâu tăng từ 1:
    1. gọi thuật toán DLS và truyền vào độ sâu đang lặp.
    2. nếu trả về mục tiêu thì return
    3. Nếu không trả về mục tiêu thì tiếp tục tăng độ sâu.

- Kết quả sau khi áp dụng thuật toán sử dụng với DLS
![](/Img/IDS_DLS.gif)

6. __Đánh giá các thuật toán trong nhóm tìm kiếm không có thông tin__
![](/Img/DanhGiaN1.gif)

### *2.2.Nhóm thuật toán tìm kiếm có thông tin*
1. __Gready Search__
- Thuật toán [Greedy Search](https://en.wikipedia.org/wiki/Greedy_algorithm) sử dụng cấu trúc Priority Queue để lưu các trạng thái sinh ra từ bàn cờ. Mỗi lần lấy trạng thái ra Greedy chọn trạng thái có chi phí tốt nhất (chi phí thấp nhất). 
- Thuật toán này sử dụng hàm ước lượng chi phí [(Herurictics)](https://vi.wikipedia.org/wiki/Heuristic) để tính chi phí cho các trạng thái sinh ra. 
- Ước lượng chi phí từ trạng thái ban đầu đến trạng thái mục tiêu.
- Thuật tóa Greedy muốn tối ưu đòi hỏi ta phải xây dựng hàm ước lượng chi phí gần đúng nhất so với trạng thái mục tiêu.
- Hướng dẫn GS:
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
- Hướng dẫn AS:
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
- Hướng dẫn HCS:
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
- Hướng dẫn SA:
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
- Hướng dẫn BS:
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
- Hướng dẫn GA:
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
2. __Tìm kiếm trong môi trường không nhìn thấy__
3. __Tìm kiếm trong môi trường nhìn thấy một phần__

### *2.5. Nhóm thuật toán tìm kiếm thõa mãn ràng buộc*
1. __CSP Backtracking__
2. __CSP Forward Checking__
3. __AC-3 Art Concistencey__

### *2.6. Nhóm thuật toán tìm kiếm đối kháng*
1. __MiniMax Decision__
2. __Alpha-Beta-Pruning__

## 3. Môi trường phát triển
- Ngôn ngữ: Python
- Version: tải python 3.13.7 từ [python.org]( https://www.python.org/)
- Thư viện: cài đặt thư viện 
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

    ```python
    pip install Pillow
    ```
    ```python
    pip install matplotlib
    ```

    Các thư viện khác cần import: math, queue, random, collections, threading, time. <br>

## 4. Hướng dẫn chạy chương trình






