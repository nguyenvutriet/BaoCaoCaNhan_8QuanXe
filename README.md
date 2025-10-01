# Báo Cáo Cá Nhân:
GVHD: Phan Thị Huyền Trang
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
    3. sinh các trạng thái có thể có từ trạng thái lấy ra từ queue đó.

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
    3. sinh các trạng thái có thể có từ trạng thái lấy ra từ queue đó.

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
    1. Lấy từ Priority Queue trạng thái có chi phí tốt nhất.
    2. Nếu trạng thái đó là trạng thái mục tiêu thì dừng.
    3. Sinh các trạng thái đồng thời tính chi phí cho từng trạng thái đó.
    4. Sau khi sinh xong đưa vào Priority Queue và quay lại Loop.

- Kết quả sau áp dụng thuật toán:


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

- Hướng dẫn IDS với DLS:
Đầu vào: Bài toán 8 quân xe, trạng thái ban đầu, thuật toán DLS.<br>
Đầu ra: Giải pháp từ trạng thái ban đầu đến trạng thái mục tiêu.<br>
Loop độ sâu tăng từ 1:
    1. gọi thuật toán DLS và truyền vào độ sâu đang lặp.
    2. nếu trả về mục tiêu thì return
    3. Nếu không trả về mục tiêu thì tiếp tục tăng độ sâu.

- Kết quả sau khi áp dụng thuật toán sử dụng với DLS



### *2.2.Nhóm thuật toán tìm kiếm có thông tin*
1. __Gready Search__

2. __A* Search__

### *2.3. Nhóm thuật toán tìm kiếm Local Search*
1. __Hill climbing__
2. __Simulated Annealling__ 
3. __Beam Search__
4. __Genetic Algorithms__

### *2.4. Nhóm thuật toán tìm kiếm trong môi trường phức tạp*
1. __And-Or Tree Search__
2. __Tìm kiếm trong môi trường không nhìn thấy__
3. __Tìm kiếm trong môi trường nhìn thấy một phần__

### *2.5. Nhóm thuật toán tìm kiếm thõa mãn ràng buộc*
1. __CSP Backtracking__
2. __CSP Forward Checking__
3. __AC-3 Art Concistencey__

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
    Các thư viện khác cần import: math, queue, random, collections, time. <br>

    Hoặc thư viện pygame thay cho thư viện tkinter:
    ```python
    pip install pygame
    ```





## 4. Hướng dẫn chạy chương trình





