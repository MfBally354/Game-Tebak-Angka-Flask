# 🎮 Tebak Angka Game

Sebuah web game interaktif berbasis Flask untuk menebak angka dengan berbagai tingkat kesulitan.

<img width="1920" height="1080" alt="Screenshot (611)" src="https://github.com/user-attachments/assets/ce278f3c-5c94-4fe0-89ca-221f215e25b8" />


## 📸 Screenshot

Game dengan 3 tingkat kesulitan: Mudah (1-10), Sedang (1-50), dan Sulit (1-100).

## ✨ Fitur

- 🎯 **3 Level Kesulitan**
  - **Mudah**: Tebak angka 1-10 dengan 5 kesempatan
  - **Sedang**: Tebak angka 1-50 dengan 7 kesempatan  
  - **Sulit**: Tebak angka 1-100 dengan 10 kesempatan

- 💡 **Hint Cerdas**: Sistem memberikan petunjuk "terlalu besar" atau "terlalu kecil"
- 📜 **Riwayat Tebakan**: Lihat semua tebakan sebelumnya beserta hintnya
- 📊 **Tracking Percobaan**: Monitor sisa kesempatan menebak
- 🎨 **Responsive Design**: Tampilan menarik dan mobile-friendly
- ✅ **Validasi Input**: Cegah input yang tidak valid

## 🗂️ Struktur Proyek

```
game_flask/
├── app.py                 # Aplikasi Flask utama
├── requirements.txt       # Dependencies Python
├── static/
│   ├── css/
│   │   └── style.css     # Styling aplikasi
│   └── js/
│       └── script.js     # JavaScript untuk animasi
└── templates/
    ├── base.html         # Template dasar
    ├── index.html        # Halaman pemilihan level
    ├── game.html         # Halaman permainan
    └── result.html       # Halaman hasil
```

## 🚀 Instalasi

### Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Langkah Instalasi

1. **Clone atau download repository**
   ```bash
   cd game_flask
   ```

2. **Install dependencies**
   
   **Opsi A: Menggunakan Virtual Environment (Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # atau
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   ```

   **Opsi B: Install langsung ke sistem**
   ```bash
   pip install -r requirements.txt --break-system-packages
   ```

3. **Jalankan aplikasi**
   ```bash
   python app.py
   ```

4. **Buka browser**
   ```
   http://localhost:5000
   ```

## 🎮 Cara Bermain

1. Pilih tingkat kesulitan (Mudah, Sedang, atau Sulit)
2. Masukkan tebakan angka di form input
3. Sistem akan memberikan hint:
   - 📉 "Terlalu kecil!" - coba angka yang lebih besar
   - 📈 "Terlalu besar!" - coba angka yang lebih kecil
4. Terus tebak hingga berhasil atau kesempatan habis
5. Lihat hasil akhir dan main lagi!

## 🛠️ Teknologi yang Digunakan

- **Backend**: Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Session Management**: Flask Session
- **Styling**: Custom CSS dengan Gradient Background

## 📝 API Routes

| Route | Method | Deskripsi |
|-------|--------|-----------|
| `/` | GET | Halaman utama pemilihan level |
| `/game/<mode>` | GET | Memulai game dengan mode tertentu |
| `/guess` | POST | Memproses tebakan user |
| `/reset` | GET | Reset game dan kembali ke menu |

## 🎨 Customization

### Mengubah Tingkat Kesulitan

Edit file `app.py` pada fungsi `game()`:

```python
if mode == 'easy':
    session['max_number'] = 10      # Ubah range angka
    session['max_attempts'] = 5     # Ubah jumlah kesempatan
```

### Mengubah Tampilan

Edit file `static/css/style.css` untuk mengubah warna, font, atau layout.

## 🐛 Troubleshooting

**Problem**: Error "externally-managed-environment"
```bash
# Solusi: Gunakan virtual environment atau flag --break-system-packages
pip install -r requirements.txt --break-system-packages
```

**Problem**: Port 5000 sudah digunakan
```python
# Edit app.py, ubah port
app.run(debug=True, host='0.0.0.0', port=8000)
```

## 📄 License

Project ini dibuat untuk keperluan belajar dan dapat digunakan secara bebas.

## 👨‍💻 Author

Dibuat dengan ❤️ menggunakan Flask dan Vim

## 🤝 Contributing

Kontribusi selalu diterima! Silakan buat issue atau pull request.

## 📞 Support

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.

---

⭐ Jangan lupa beri bintang jika project ini membantu kam
