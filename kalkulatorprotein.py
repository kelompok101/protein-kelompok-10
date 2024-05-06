import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Menu sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Navigasi",
        options=["Perkenalan Kelompok", "Pengetahuan", "Perhitungan", "Tabel Protein"],
        icons=["house", "book", "calculator", "table"],
        menu_icon="menu",
        default_index=0,
    )

# Halaman Pengetahuan
if selected == "Pengetahuan":
    st.title("Pengetahuan Tentang Kadar Protein 🧠🥦💪")
    st.write("Di sini Anda dapat menemukan informasi tentang kadar protein dan pentingnya asupan protein dalam makanan.")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    st.header("Pentingnya Kadar Protein dalam Berbagai Tingkat Aktivitas")

    st.write("Kadar protein yang dibutuhkan tubuh sehari-hari dapat berbeda-beda tergantung pada usia, jenis kelamin, tinggi dan berat badan, serta berbagai faktor pendukung lainnya. Pedoman yang diterbitkan oleh Food and Nutrition Board of the National Academy of Sciences merekomendasikan bahwa orang dewasa membutuhkan sekitar 50 gram protein per hari yang dapat diperoleh dari makanan berprotein. Namun, kebutuhan protein dapat berbeda untuk individu yang memiliki tingkat aktivitas fisik yang lebih tinggi atau memiliki kebutuhan gizi yang lebih besar, seperti ibu hamil yang membutuhkan peningkatan asupan nutrisi selama kehamilan.")

    st.write("Kalkulator kadar protein kami dapat membantu Anda menghitung kadar protein dalam berbagai produk pangan dan membandingkannya dengan kebutuhan harian Anda.")
    st.header("Kadar Protein dan Tingkat Aktivitas")
    st.write("Aktivitas fisik seseorang juga memengaruhi kebutuhan protein harian. Berikut adalah rekomendasi kebutuhan protein berdasarkan tingkat aktivitas:")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.subheader("Aktivitas Rendah:")
    st.write("Orang yang memiliki aktivitas fisik rendah membutuhkan asupan protein yang lebih sedikit dari pada orang yang memiliki tingkat aktivitas fisik yang lebih tinggi.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas rendah adalah sekitar 0,8 gram protein per kilogram berat badan.")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    st.subheader("Aktivitas Sedang:")
    st.write("Orang yang memiliki tingkat aktivitas fisik sedang membutuhkan lebih banyak protein dari pada orang dengan aktivitas fisik yang rendah.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas sedang adalah sekitar 1,0 - 1,2 gram protein per kilogram berat badan.")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.subheader("Aktivitas Tinggi:")
    st.write("Orang yang memiliki aktivitas fisik yang tinggi, seperti atlet atau pekerja fisik, membutuhkan lebih banyak protein untuk memperbaiki dan membangun otot yang rusak selama latihan.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas tinggi adalah sekitar 1,2 - 1,5 gram protein per kilogram berat badan.")

# Halaman Pengantar
elif selected == "Perkenalan Kelompok":
    st.title("🌟 Aplikasi Perhitungan Kadar Protein 🍏🥩")
    st.write("Selamat datang di aplikasi perhitungan kadar protein dalam produk pangan!")
    st.write("Kami hadir untuk membantu Anda menghitung kadar protein dalam berbagai jenis makanan.")
    st.write("Dibuat oleh Kelompok 10 Kelas PMIP Mata Kuliah Logika dan Pemrograman Komputer.")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    nama_kelompok = "Kelompok 10"
    anggota_tim = (
        "1. Adinda Rahmadani (2320501)\n"
        "2. Ajeng Maulida Aprilia (2320503)\n"
        "3. Amalia Syfa Zahra (2320505)\n"
        "4. Anjani Rahmawati (2320508)\n"
        "5. Harits Dzaki Firdani (2320527)"
    )

    st.info(f"👥 Kelompok: {nama_kelompok}")
    st.write("Anggota tim:")
    st.write(anggota_tim.replace("\n", "\n"))

# Halaman Perhitungan
elif selected == "Perhitungan":
    st.title("Perhitungan Kadar Protein dalam Produk Pangan 🥩🍳🌽")
    st.write("Aplikasi ini menghitung kadar protein dalam produk pangan berdasarkan berbagai parameter.")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    daftar_produk = {
        "Daging": ["Daging Sapi", "Daging Ayam", "Daging Kambing", "Daging Babi", "Daging Ikan", 
                   "Daging Domba", "Daging Rusa"],
        "Susu": ["Susu Sapi", "Susu Kambing"],
        "Telur": ["Telur Ayam", "Telur Bebek", "Telur Puyuh"],
        "Kacang-kacangan": ["Kacang Merah", "Kacang Hijau", "Kacang Kedelai"],
        "Sereal": ["Oat", "Beras", "Gandum"],
        "Sayuran": ["Brokoli", "Bayam", "Kangkung"],
        "Buah-buahan": ["Pisang", "Apel", "Jeruk"],
        "Tahu": ["Tahu Putih", "Tahu Kuning"],
        "Tempe": ["Tempe Mendoan", "Tempe Goreng"],
        "Keju": ["Keju Cheddar", "Keju Mozzarella"],
        "Yoghurt": ["Yoghurt Plain", "Yoghurt Buah"],
        "Roti": ["Roti Gandum", "Roti Tawar"],
        "Kentang": ["Kentang Rebus", "Kentang Goreng"],
        "Sosis": ["Sosis Ayam", "Sosis Sapi"],
        "Biskuit": ["Biskuit Gandum", "Biskuit Cokelat"],
        "Nasi": ["Nasi Putih", "Nasi Merah"],
        "Pasta": ["Spaghetti", "Penne"]
    }

    kategori_produk = st.selectbox("Pilih kategori produk:", list(daftar_produk.keys()))

    if daftar_produk[kategori_produk]:
        produk_pilihan = st.selectbox(f"Pilih jenis {kategori_produk.lower()}: ", daftar_produk[kategori_produk])
    else:
        produk_pilihan = kategori_produk
    
    berat_produk = st.number_input(
        "Masukkan berat produk (gram):",
        min_value=0.0,
        step=0.1,
        format="%.1f"
    )

    berat_badan = st.number_input(
        "Masukkan berat badan Anda (kg):",
        min_value=0.0,
        step=0.1,
        format="%.1f"
    )

    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=0, step=1, format="%d")

    kategori_aktivitas = st.selectbox("Pilih kategori aktivitas Anda:", ["Rendah", "Sedang", "Tinggi"])

    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ["Pria", "Wanita"])

    default_protein = {
        "Daging Sapi": 26.0,
        "Daging Ayam": 25.0,
        "Daging Kambing": 27.0,
        "Daging Babi": 25.0,
        "Daging Ikan": 20.0,
        "Susu Sapi": 3.5,
        "Telur Ayam": 12.0,
        "Kacang Merah": 22.0,
        "Tempe": 19.0,
        "Roti Gandum": 8.0,
        "Kedelai": 35.0,
        "Biskuit Gandum": 6.0,
    }

    konsentrasi_protein = st.number_input(
        f"Konsentrasi protein dalam {produk_pilihan} (persentase):",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
        format="%.1f",
        value=float(default_protein.get(produk_pilihan, 0))
    )

    st.write("Konsentrasi protein diukur dalam persentase dari berat total produk.")

    if st.button("Hitung Kadar Protein"):
        if berat_produk <= 0 or konsentrasi_protein < 0 or konsentrasi_protein > 100:
            st.error("Pastikan berat produk lebih dari 0 dan konsentrasi protein antara 0 dan 100.")

        kadar_protein = (berat_produk * konsentrasi_protein) / 100

        st.success(f"Kadar protein dalam {produk_pilihan} adalah {kadar_protein:.2f} gram.")

        # Hitung kebutuhan protein harian dengan batas bawah dan batas atas
        if kategori_aktivitas == "Rendah":
            kebutuhan_protein_bawah = 0.8 * berat_badan
            kebutuhan_protein_atas = 1.0 * berat_badan
        elif kategori_aktivitas == "Sedang":
            kebutuhan_protein_bawah = 1.0 * berat_badan
            kebutuhan_protein_atas = 1.2 * berat_badan
        elif kategori_aktivitas == "Tinggi":
            kebutuhan_protein_bawah = 1.2 * berat_badan
            kebutuhan_protein_atas = 1.5 * berat_badan

        st.info(f"Kebutuhan protein harian Anda berkisar antara {kebutuhan_protein_bawah:.2f} dan {kebutuhan_protein_atas:.2f} gram.")

        if kadar_protein < kebutuhan_protein_bawah:
            st.warning("Kadar protein dalam produk ini kurang dari batas bawah kebutuhan harian Anda.")
        elif kadar_protein > kebutuhan_protein_atas:
            st.warning("Kadar protein dalam produk ini melebihi batas atas kebutuhan harian Anda.")

# Halaman Tabel Protein
elif selected == "Tabel Protein":
    st.title("🍖🥚🧀 Tabel Konsentrasi Protein Berdasarkan Produk 🥜🥛🍗")
# Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    default_protein = {
        "Daging Sapi": 26.0,
        "Daging Ayam": 25.0,
        "Daging Kambing": 27.0,
        "Daging Babi": 25.0,
        "Daging Ikan": 20.0,
        "Daging Domba": 23.0,
        "Daging Rusa": 22.0,
        "Susu Sapi": 3.5,
        "Susu Kambing": 4.0,
        "Telur Ayam": 12.0,
        "Telur Bebek": 13.0,
        "Telur Puyuh": 11.0,
        "Kacang Merah": 22.0,
        "Kacang Hijau": 24.0,
        "Kacang Kedelai": 35.0,
        "Oat": 17.0,
        "Beras": 7.0,
        "Gandum": 13.0,
        "Brokoli": 3.7,
        "Bayam": 2.9,
        "Kangkung": 2.7,
        "Pisang": 1.3,
        "Apel": 0.3,
        "Jeruk": 0.9,
        "Tahu Putih": 19.9,
        "Tahu Kuning": 20.5,
        "Tempe Mendoan": 20.3,
        "Tempe Goreng": 19.0,
        "Keju Cheddar": 25.0,
        "Keju Mozzarella": 22.0,
        "Yoghurt Plain": 3.5,
        "Yoghurt Buah": 3.8,
        "Roti Gandum": 8.0,
        "Roti Tawar": 7.5,
        "Kentang Rebus": 2.0,
        "Kentang Goreng": 3.3,
        "Sosis Ayam": 13.0,
        "Sosis Sapi": 15.0,
        "Biskuit Gandum": 6.0,
        "Biskuit Cokelat": 4.0,
        "Nasi Putih": 2.6,
        "Nasi Merah": 2.9,
        "Spaghetti": 5.0,
        "Penne": 5.1
    }

    df = pd.DataFrame({
        "Produk": list(default_protein.keys()),
        "Konsentrasi Protein (%)": list(default_protein.values())
    })

    st.write("Berikut adalah tabel konsentrasi protein untuk beberapa produk makanan umum:")
    st.dataframe(df)