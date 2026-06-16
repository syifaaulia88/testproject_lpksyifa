import streamlit as st
import math

# Halaman Web
st.set_page_config(page_title="ChemSolv: Smart Solution for Solubility", layout="wide", page_icon="🧪")

# CSS Kustom (Warna judul menu gelap awal, emotikon sejajar, dan tombol seragam)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #fff0f3 !important;
    }

    [data-testid="stSidebar"] {
        background-color: #e2f0d9 !important; /* Hijau pastel lembut */
    }
    
    /* Menyamakan posisi atas (padding) antara main area dan sidebar */
    .block-container {
        padding-top: 2.5rem !important;
    }
    [data-testid="stSidebarUserContent"] {
        padding-top: 2.5rem !important;
    }
    
    /* Tulisan Menu ChemSolv warna gelap awal & emotikon sejajar sempurna */
    .judul-menu {
        color: #31333F !important; 
        font-size: 24px; 
        font-weight: bold;
        margin-bottom: 20px;
        margin-top: 5px;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 8px; 
        white-space: nowrap; 
    }
    
    /* Gaya untuk semua tombol di sidebar agar seragam dan rapi */
    [data-testid="stSidebar"] div[data-testid="stButton"] button {
        background-color: #d81b60 !important;
        color: white !important;
        border-radius: 15px !important;
        border: none !important;
        padding: 10px 20px !important;
        font-size: 15px !important;
        font-weight: bold !important;
        width: 100% !important; 
        display: block !important;
        margin-bottom: 5px !important;
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        transition: 0.2s;
    }
    
    [data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
        background-color: #c2185b !important;
        transform: scale(1.03);
    }
    
    .stHeader h2 {
        color: #d81b60;
    }
    </style>
""", unsafe_allow_html=True)

# Inisialisasi session state untuk halaman jika belum ada
if 'page' not in st.session_state: 
    st.session_state['page'] = "Home" 

# --- KONTROL SIDEBAR ---
with st.sidebar:
    st.markdown('<div class="judul-menu">✨ Menu ChemSolv ✨</div>', unsafe_allow_html=True)
    
    if st.button("Home", use_container_width=True): 
        st.session_state['page'] = "Home"
    
    if st.button("Kalkulator Ksp", use_container_width=True): 
        st.session_state['page'] = "Kalkulator Ksp"
        
    if st.button("Prediksi Endapan", use_container_width=True):
        st.session_state['page'] = 'Prediksi Endapan'
        
    if st.button("Tentang Kami", use_container_width=True):
        st.session_state['page'] = 'Tentang Kami'
        
    st.sidebar.divider()

page = st.session_state['page']

# --- KONTEN HALAMAN ---
if page == "Home":
    st.title("🧪 ChemSolv: Smart Solution for Solubility")
    st.subheader("Selamat Datang di aplikasi ChemSolv!!")
    st.markdown("Klik pada setiap kotak di bawah ini untuk melihat deskripsi lengkap:")
    st.divider()
    
    # 1. Box Lipat: Deskripsi Web
    with st.expander("Apa Itu ChemSolv?", expanded=False):
        st.write("""
        Dalam kimia fisik dan kimia analisis, memahami serta menghitung kesetimbangan larutan merupakan keterampilan dasar yang sangat penting. Materi kesetimbangan, mulai dari menentukan kelarutan suatu zat hingga memprediksi kapan endapan akan mulai terbentuk, menjadi bagian tak terpisahkan dari praktikum maupun kegiatan analisis di laboratorium. Namun, tidak jarang pelajar atau praktisi merasa kesulitan ketika harus melakukan perhitungan ini secara manual, apalagi saat menghadapi rumus stoikiometri ion yang berbeda-beda serta perhitungan eksponen yang cukup rumit.
        
        Sebagai respons terhadap kebutuhan tersebut, kami menghadirkan **ChemSolv - Kalkulator Ksp**, sebuah aplikasi berbasis web yang dirancang khusus untuk membantu pengguna dalam melakukan berbagai perhitungan kesetimbangan kimia larutan dengan cepat dan akurat.
        """)
        
    # 2. Box Lipat: Deskripsi Fitur ke 1
    with st.expander("📲 Fitur Kalkulator Kelarutan & Ksp", expanded=False):
        st.write("""
        Fitur ini dirancang untuk memudahkan pengguna dalam melakukan konversi dan perhitungan otomatis antara nilai Kelarutan ($s$) dan nilai Konstanta Hasil Kali Kelarutan ($K_{sp}$).
        
        * **Hitung Kelarutan (s) dari Ksp:** Membantu mencari konsentrasi maksimum zat yang dapat larut dalam kondisi jenuh.
        * **Hitung Ksp dari Kelarutan (s):** Menghitung nilai konstanta kesetimbangan berdasarkan data eksperimen kelarutan senyawa secara instan.
        """)
        
    # 3. Box Lipat: Deskripsi Fitur ke 2
    with st.expander("⬇️ Fitur Prediksi Endapan", expanded=False):
        st.write("""
        Fitur ini berfungsi untuk memprediksi apakah suatu campuran larutan kation dan anion akan menghasilkan endapan baru atau tidak. Perhitungan dilakukan secara otomatis dengan membandingkan nilai **Quotient Reaksi ($Q_{sp}$)** terhadap nilai **$K_{sp}$** senyawa bawaan.
        
        * Jika $Q_{sp} < K_{sp}$: Belum Terjadi Endapan (Semua Larut).
        * Jika $Q_{sp} = K_{sp}$: Larutan Tepat Jenuh.
        * Jika $Q_{sp} > K_{sp}$: Terjadi Endapan (Lewat Jenuh).
        """)
        

# FITUR 1: KALKULATOR KELARUTAN & KSP
elif page == "Kalkulator Ksp":
    st.title("🧪 ChemSolv: Smart Solution for Solubility")
    st.subheader("📲 Kalkulator Kelarutan dan Ksp")
    st.markdown("Hitung **Kelarutan (s)** dari **Ksp**, atau sebaliknya, berdasarkan stoikiometri senyawa.")
    st.divider()

    mode = st.radio("**Pilih Jenis Perhitungan:**", 
                    ("Hitung Kelarutan (s) dari nilai Ksp", "Hitung Ksp dari nilai Kelarutan (s)"))

    senyawa_type = st.selectbox("**Pilih Jenis Senyawa (Berdasarkan Stoikiometri):**", 
                                ("AB (Contoh: AgCl, BaSO₄)", 
                                 "AB₂ atau A₂B (Contoh: PbCl₂, Ag₂CrO₄)", 
                                 "AB₃ atau A₃B (Contoh: Al(OH)₃, Ag₃PO₄)", 
                                 "A₂B₃ atau A₃B₂ (Contoh: As₂S₃)"))
    st.divider()

    # Logika Perhitungan: Kelarutan (s) dari Ksp
    if mode == "Hitung Kelarutan (s) dari nilai Ksp":
        ksp_val = st.number_input("**Masukkan Nilai Ksp {Gunakan format e (e adalah × 10 pangkat), contoh: 1.0e-10}:**", 
                                   value=1.0e-10, format="%.2e", step=1e-11)
        
        if st.button("Hitung Kelarutan (s)", use_container_width=True):
            if "AB " in senyawa_type:
                s = math.sqrt(ksp_val)
                rumus = r"K_{sp} = s^2 \implies s = \sqrt{K_{sp}}"
            elif "AB₂" in senyawa_type:
                s = (ksp_val / 4.0) ** (1.0 / 3.0)
                rumus = r"K_{sp} = 4s^3 \implies s = \sqrt[3]{\frac{K_{sp}}{4}}"
            elif "AB₃" in senyawa_type:
                s = (ksp_val / 27.0) ** (1.0 / 4.0)
                rumus = r"K_{sp} = 27s^4 \implies s = \sqrt[4]{\frac{K_{sp}}{27}}"
            elif "A₂B₃" in senyawa_type:
                s = (ksp_val / 108.0) ** (1.0 / 5.0)
                rumus = r"K_{sp} = 108s^5 \implies s = \sqrt[5]{\frac{K_{sp}}{108}}"
            
            st.success(f"**Kelarutan (s) = {s:.4e} mol/L**")
            st.info("Rumus yang digunakan:")
            st.latex(rumus)

    # Logika Perhitungan: Ksp dari Kelarutan (s)
    else:
       s_val = st.number_input(
            "Masukkan Nilai Kelarutan (s) dalam mol/L (contoh: 1 × 10⁻⁵):",
            value=1.0e-5,
            format="%.2e",
            step=1e-6
       )
       
       if st.button("Hitung Nilai Ksp", use_container_width=True):
            if "AB " in senyawa_type:
                ksp = s_val ** 2
                rumus = r"K_{sp} = s^2"
            elif "AB₂" in senyawa_type:
                ksp = 4 * (s_val ** 3)
                rumus = r"K_{sp} = 4s^3"
            elif "AB₃" in senyawa_type:
                ksp = 27 * (s_val ** 4)
                rumus = r"K_{sp} = 27s^4"
            elif "A₂B₃" in senyawa_type:
                ksp = 108 * (s_val ** 5)
                rumus = r"K_{sp} = 108s^5"
                
            st.success(f"**Nilai Ksp = {ksp:.4e}**")
            st.info("Rumus yang digunakan:")
            st.latex(rumus)

# FITUR 2: PREDIKSI ENDAPAN (Qsp vs Ksp)
elif page == "Prediksi Endapan":
    st.title("🧪 ChemSolv: Smart Solution for Solubility")
    st.subheader("⬇️ Prediksi Endapan")
    st.markdown("Bandingkan nilai **Quotient Reaksi (Qsp)** dengan **Ksp** untuk memprediksi apakah suatu campuran akan menghasilkan endapan.")
    st.divider()

    st.subheader("1. Data Konstanta Ksp")
    ksp = st.number_input("**Masukkan nilai Ksp {Gunakan format e (e adalah × 10 pangkat), contoh: 1.0e-10}:**", format="%e", value=1.0e-10)

    st.subheader("2. Konsentrasi Ion dalam Campuran")
    kolom_kation, kolom_anion = st.columns(2)

    with kolom_kation:
        st.markdown("**Kation (Ion Positif)**")
        konsentrasi_kation = st.number_input("Konsentrasi Kation (M):", format="%e", value=1.0e-5)
        koefisien_kation = st.number_input("Pangkat/Koefisien Kation:", min_value=1, value=1)

    with kolom_anion:
        st.markdown("**Anion (Ion Negatif)**")
        konsentrasi_anion = st.number_input("Konsentrasi Anion (M):", format="%e", value=1.0e-5)
        koefisien_anion = st.number_input("Pangkat/Koefisien Anion:", min_value=1, value=1)

    st.divider()

    if st.button("Hitung & Prediksi", use_container_width=True):
        # Menghitung Qsp
        qsp = (konsentrasi_kation ** koefisien_kation) * (konsentrasi_anion ** koefisien_anion)
        
        st.write(f"**Nilai Quotient Reaksi (Qsp) yang dihitung:** {qsp:.2e}")
        st.latex(r"Q_{sp} = [\text{Kation}]^x [\text{Anion}]^y")
        
        # Kesimpulan Prediksi
        if qsp > ksp:
            st.error("Hasil: Qsp > Ksp. **Terjadi Endapan!** ⬇️")
        elif qsp == ksp:
            st.warning("Hasil: Qsp = Ksp. **Larutan Tepat Jenuh** (Belum mengendap). ❌")
        else:
            st.success("Hasil: Qsp < Ksp. **Tidak Terjadi Endapan** (Semua larut). 💧")

# PAGE TENTANG KAMI PERKENALAN NAMA ANGGOTA KELOMPOK
elif page == "Tentang Kami":
    st.title("🧪 ChemSolv: Smart Solution for Solubility")
    st.write("""
👨‍💻 Tim Pengembang
Aplikasi ini merupakan hasil Proyek Tugas Website untuk mata kuliah Logika Pemrograman Komputer.

👥 Anggota Kelompok:
- Athiyah Amini Azzahra — 2560587 
- Ryel Fandralaro — 2560766 
- Syifa Aulia Farani Pasha — 2560792 
- Zahra Fitria Sukmawan — 2560809 
- Zalika Imani Hamida — 2560810 

Kelas: 1D
🎓 Program Studi: Analisis Kimia
🏛️ Politeknik AKA Bogor
    """)
    
