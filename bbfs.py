import tkinter as tk
from tkinter import messagebox, scrolledtext
import math

def proses_bagi():
    # 1. Ambil data dari input
    data_input = input_teks.get("1.0", tk.END).strip()
    
    try:
        jumlah_grup = int(entry_grup.get())
        nominal_input = int(entry_nominal.get()) # Contoh: 1000, 2000
        
        # Logika harga: 410 adalah harga per 1000
        # Jadi kalau nominal 2000, harganya jadi 820 per angka
        pengali_nominal = nominal_input / 1000
        harga_per_item = 410 * pengali_nominal
        
    except ValueError:
        messagebox.showerror("Error", "Jumlah Grup dan Nominal harus berupa angka!")
        return

    if not data_input:
        messagebox.showwarning("Peringatan", "Masukkan baris angka terlebih dahulu!")
        return

    # 2. Proses Angka
    daftar_angka = [a.strip() for a in data_input.split('*') if a.strip()]
    total_data = len(daftar_angka)
    total_harga_semua = total_data * harga_per_item
    
    if total_data == 0:
        messagebox.showerror("Error", "Format data salah!")
        return

    ukuran_grup = math.ceil(total_data / jumlah_grup)
    
    # 3. Output Hasil
    output_teks.delete("1.0", tk.END)
    output_teks.insert(tk.END, f"=== RINGKASAN TAGIHAN ===\n")
    output_teks.insert(tk.END, f"Total Data  : {total_data} angka\n")
    output_teks.insert(tk.END, f"Setting     : #{nominal_input}\n")
    output_teks.insert(tk.END, f"Total Bayar : Rp {total_harga_semua:,.0f}\n")
    output_teks.insert(tk.END, "="*45 + "\n\n")

    for i in range(0, total_data, ukuran_grup):
        grup_ke = (i // ukuran_grup) + 1
        grup = daftar_angka[i:i + ukuran_grup]
        harga_grup = len(grup) * harga_per_item
        
        # Gabungkan angka dengan bintang dan tambah #nominal di akhir
        hasil_baris = "*".join(grup) + f"#{nominal_input}"
        
        output_teks.insert(tk.END, f"GRUP {grup_ke} ({len(grup)} angka) - Rp {harga_grup:,.0f}\n")
        output_teks.insert(tk.END, hasil_baris + "\n")
        output_teks.insert(tk.END, "-"*45 + "\n\n")

# --- UI SETUP ---
root = tk.Tk()
root.title("Pembagi Grup Angka & Kalkulator Harga")
root.geometry("750x800")
root.configure(bg="#ececec")

# Input Area
tk.Label(root, text="MASUKKAN BARIS ANGKA (*)", font=("Arial", 10, "bold"), bg="#ececec").pack(pady=(10,0))
input_teks = scrolledtext.ScrolledText(root, height=12, width=85, font=("Consolas", 10))
input_teks.pack(pady=5, padx=15)

# Control Frame
frame_input = tk.Frame(root, bg="#ececec")
frame_input.pack(pady=10)

# Input Jumlah Grup
tk.Label(frame_input, text="Bagi Grup:", bg="#ececec").grid(row=0, column=0, padx=5)
entry_grup = tk.Entry(frame_input, width=5, font=("Arial", 11))
entry_grup.insert(0, "2")
entry_grup.grid(row=0, column=1, padx=10)

# Input Nominal (1000, 2000, dst)
tk.Label(frame_input, text="Nominal (#):", bg="#ececec").grid(row=0, column=2, padx=5)
entry_nominal = tk.Entry(frame_input, width=10, font=("Arial", 11))
entry_nominal.insert(0, "1000")
entry_nominal.grid(row=0, column=3, padx=10)

# Button
btn_proses = tk.Button(root, text="PROSES & HITUNG", command=proses_bagi, 
                       bg="#28a745", fg="white", font=("Arial", 10, "bold"), width=20)
btn_proses.pack(pady=10)

# Output Area
tk.Label(root, text="HASIL EKSPOR", font=("Arial", 10, "bold"), bg="#ececec").pack()
output_teks = scrolledtext.ScrolledText(root, height=20, width=85, font=("Consolas", 10), bg="#ffffff")
output_teks.pack(pady=5, padx=15)

root.mainloop()