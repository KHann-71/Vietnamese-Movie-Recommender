# 📂 Movie Recommendation Data Management

Thư mục này quản lý quy trình xử lý dữ liệu từ tương tác thô (MovieLens) đến đặc trưng ngữ nghĩa tiếng Việt (PhoBERT).

## 1. Nguồn dữ liệu (Sources)
Dự án kết hợp hai tập dữ liệu quy mô lớn:
* **MovieLens 25M**: Chứa 25 triệu ratings. Tập trung vào tệp `ratings.csv` và `links.csv`. [Link tải](https://www.kaggle.com/datasets/garymk/movielens-25m-dataset/data)
* **TMDB API**: Sử dụng để lấy **Overview** (Tóm tắt phim) và **Poster** dựa trên `tmdbId` từ MovieLens.

## 2. Quy trình tiền xử lý (Pipeline)
Toàn bộ code xử lý nằm trong `experiments/01_eda/eda.ipynb`, bao gồm:
- **Lọc Implicit Feedback**: Chuyển đổi Rating sang nhị phân (1 nếu Rating $\ge$ 4.0, ngược lại 0).
- **Xử lý Cold-start**: Loại bỏ User có ít hơn 20 tương tác để đảm bảo chất lượng huấn luyện.
- **Dịch thuật & Làm giàu**: Sử dụng `googletrans` và `tmdbsimple` để Việt hóa nội dung phim.

## 3. Trích xuất đặc trưng (Feature Engineering)
Chúng tôi sử dụng mô hình ngôn ngữ **PhoBERT (base)** từ VinAI để chuyển đổi văn bản tóm tắt phim thành Vector không gian (Embedding):
- **Input**: Movie Overview (Tiếng Việt).
- **Output**: Vector 768 chiều đại diện cho ngữ nghĩa phim.
- **Mục đích**: Cung cấp thông tin Content-based cho các mô hình lai (Hybrid) như **BERT-NeuMF**.

## 4. Hướng dẫn thiết lập
Do giới hạn dung lượng của GitHub (>100MB), dữ liệu thô không được upload trực tiếp. Bạn cần:
1. Tải bộ ML-25M về máy.
2. Tạo thư mục `data/raw/` và đặt file `.csv` vào đó.
3. Chạy Notebook `01_eda/eda.ipynb` để tạo ra các file đã xử lý (`processed_data.pkl`).

---
*Lưu ý: Đảm bảo đã cài đặt `requirements.txt` ở thư mục gốc trước khi thực hiện tiền xử lý.*