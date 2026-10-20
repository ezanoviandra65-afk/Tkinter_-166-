import tkinter as tk
from tkinter import ttk

# ====== Warna tema ======
BG = "#3F3F9F"
FG = "white"
ENTRY_BG = "#5A5AB5"
ACCENT = "#7DF9FF"

# ====== Window utama ======
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("460x720")
root.configure(bg=BG)
root.resizable(False, False)

# Kolom 0 dan 2 melebar agar isi form berada di tengah
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=0)
root.columnconfigure(2, weight=1)

# ====== 1. Label judul ======
label_judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Segoe UI", 16, "bold"),
    bg=BG,
    fg=FG,
)
label_judul.grid(row=0, column=0, columnspan=3, pady=(25, 20))



