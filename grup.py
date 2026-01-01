import streamlit as st
import math

# Setting tampilan halaman
st.set_page_config(page_title="BBFS Grup & Harga", page_icon="🔢")

st.title("🔢 Pembagi Grup BBFS")
st.markdown("Aplikasi khusus untuk membagi angka dan hitung biaya otomatis.")

# --- INPUT AREA ---
data_input = st.text_area("Tempel Baris Angka Kamu di Sini (*)", height=250, placeholder="Contoh: 110*112*113...")

col1, col2 = st.columns(2)
with col1:
    jumlah_grup = st.number_input("Bagi jadi berapa grup?", min_value=1, value=2, step=1)
with col2:
    nominal = st.number_input("Nominal Kelipatan (#)", min_value=1, value=1000, step=1000)

# --- PROSES LOGIKA ---
if st.button("PROSES & HITUNG SEKARANG", use_container_width=True):
    if not data_input:
        st.error("Data masih kosong! Silakan tempel angka dulu.")
    else:
        # Pembersihan data (split berdasarkan bintang)
        daftar_angka = [a.strip() for a in data_input.split('*') if a.strip()]
        total_data = len(daftar_angka)
        
        # Hitung Harga (410 per 1000)
        harga_per_item = 410 * (nominal / 1000)
        total_biaya = total_data * harga_per_item
        
        # Tampilkan Ringkasan
        st.success(f"**Total:** {total_data} angka | **Biaya Total:** Rp {total_biaya:,.0f}")
        
        # Pembagian Grup
        ukuran_grup = math.ceil(total_data / jumlah_grup)
        
        st.subheader("Hasil Pembagian Grup")
        for i in range(0, total_data, ukuran_grup):
            grup_ke = (i // ukuran_grup) + 1
            grup = daftar_angka[i:i + ukuran_grup]
            harga_grup = len(grup) * harga_per_item
            
            # Format teks akhir dengan tanda pagar
            teks_akhir = "*".join(grup) + f"#{nominal}"
            
            # Tampilan Box per Grup
            with st.container():
                st.markdown(f"**GRUP {grup_ke}** ({len(grup)} angka) — *Harga: Rp {harga_grup:,.0f}*")
                # Box teks yang mudah di-copy (ada tombol copy di pojok kanan box)
                st.code(teks_akhir, language="text")
                st.divider()