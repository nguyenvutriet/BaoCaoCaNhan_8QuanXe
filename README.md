# Báo Cáo Cá Nhân: Nguyễn Vũ Triết - MSSV: 23110161

# BÀI TOÁN 8 QUÂN XE

## 1. Giới thiệu bài toán
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
3. __UCS__

4. __Iterative Deepening Search__

5. __IDL__
6. __IDS__


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
    Các thư viện khác cần import: math, queue, random, collections.


## 4. Hướng dẫn chạy chương trình





