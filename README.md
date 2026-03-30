# 🎬 Movie-Recsys-VN: Hybrid Recommendation System
### *Tích hợp Mô hình Ngôn ngữ (PhoBERT) dành cho Người dùng Việt Nam*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.10+-ee4c2c.svg)](https://pytorch.org/)
[![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-yellow.svg)](https://huggingface.co/docs/transformers/index)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📌 1. Tổng quan dự án
Đồ án này nghiên cứu và phát triển một hệ thống gợi ý phim (Top-K Recommendation) lai giữa **Lọc cộng tác (Collaborative Filtering)** và **Lọc dựa trên nội dung (Content-based)**.

**Thách thức bài toán:**
- Xử lý dữ liệu tương tác thô cực lớn (MovieLens 25M).
- Giải quyết vấn đề "khởi động lạnh" (Cold-start) cho người dùng mới.
- Tối ưu hóa nội dung phim dành riêng cho ngữ cảnh người dùng Việt Nam.

**Giải pháp:** Chúng tôi sử dụng mô hình ngôn ngữ **PhoBERT (VinAI)** để trích xuất đặc trưng ngữ nghĩa từ tóm tắt phim tiếng Việt, giúp hệ thống đạt độ chính xác xếp hạng cao vượt trội.

## 🚀 2. Tính năng nổi bật
* **Đa dạng mô hình**: Triển khai từ Baseline (Popularity, ALS) đến SOTA (EASE, SASRec, NeuMF).
* **Làm giàu dữ liệu**: Kết nối MovieLens 25M với TMDB API để lấy Metadata (Overview, Genres, Poster) tiếng Việt.
* **Xử lý ngôn ngữ tự nhiên**: Sử dụng PhoBERT để mã hóa (embedding) vector ngữ nghĩa 768 chiều.
* **Kiến trúc Hybrid**: Kết hợp đặc trưng người dùng và đặc trưng nội dung trong mạng Neural (NeuMF).

## 🏗️ 3. Cấu trúc dự án
Dự án được tổ chức theo tiêu chuẩn nghiên cứu khoa học:
```text
Movie-Recsys-VN/
├── data/               # Quản lý dữ liệu (Hướng dẫn tải ML-25M & TMDB)
├── experiments/        # Lộ trình nghiên cứu & thực nghiệm
│   ├── 01_eda/         # Phân tích dữ liệu & Tiền xử lý (Rating >= 4.0)
│   ├── 02_benchmarks/  # Các mô hình đối chứng (Popularity, EASE)
│   ├── 03_collab/      # Lọc cộng tác (ALS, lite-SASRec)
│   └── 04_advanced/    # Trùm cuối: PhoBERT + NeuMF (Hybrid Model)
├── src/                # Mã nguồn tiện ích (Hàm tính Recall@K, nDCG@K)
├── .gitignore          # Chặn các file rác và dữ liệu nặng (>100MB)
└── requirements.txt    # Danh sách thư viện cần cài đặt
