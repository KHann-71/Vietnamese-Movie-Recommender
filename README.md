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
text
Movie-Recsys-VN/
├── data/               
├── experiments/        
│   ├── 01_eda/        
│   ├── 02_benchmarks/ 
│   ├── 03_collab/      
│   └── 04_advanced/    
├── src/               
├── .gitignore          
└── requirements.txt

## 📊 4. Kết quả thực nghiệm
Hệ thống được đánh giá dựa trên tập 1000 người dùng ngẫu nhiên. Kết quả cho thấy sự vượt trội rõ rệt của mô hình Hybrid tích hợp ngôn ngữ.

| Mô hình (Model) | Recall@10 | nDCG@10 | Cải thiện (vs Baseline) |
| :--- | :---: | :---: | :---: |
| Popularity (Baseline) | 0.0350 | 0.1149 | - |
| ALS | 0.0410 | 0.1250 | +8.7% |
| EASE | 0.0520 | 0.1802 | +56.8% |
| **NeuMF (Deep Learning)** | 0.0590 | 0.2115 | +84.1% |
| **BERT-NeuMF (Ours)** | **0.0616** | **0.2720** | **+136.7%** |

> **Nhận xét chính:** Việc sử dụng **PhoBERT** để trích xuất đặc trưng nội dung tiếng Việt giúp mô hình BERT-NeuMF tăng **~28%** hiệu năng so với mô hình NeuMF truyền thống chỉ dựa trên tương tác.



