import streamlit as st
import math

# Konfigurasi Halaman Web
st.set_page_config(page_title="ChemSolv: Smart Solution for Solubility", layout="centered", page_icon="🧪")

# 2. Injeksi CSS Kustom (Sidebar Hijau Pastel, Menu & Tombol Pink Tua)
st.markdown("""
    <style>
    /* Mengubah latar belakang layar utama menjadi Pink Soft/Pastel agar tidak putih kaku */
    [data-testid="stAppViewContainer"] {
        background-color: #fff0f3 !important;
    }
    [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* Mengubah latar belakang Sidebar menjadi HIJAU PASTEL */
    [data-testid="stSidebar"] {
        background-color: #e2f0d9 !important; /* Hijau pastel lembut */
    }
    
    /* Mengubah warna teks judul "Menu Kalkulator" menjadi PINK TUA */
    .judul-menu {
        color: #d81b60 !important; /* Pink tua */
        font-size: 26px;
        font-weight: bold;
        margin-bottom: 25px;
        margin-top: -20px;
    }
    
    /* Mengubah gaya tombol di sidebar (Warna PINK TUA & Membulat) */
    [data-testid="stSidebar"] .stButton>button {
        background-color: #d81b60 !important; /* Pink tua */
        color: white !important;
        border-radius: 15px !important; /* Membuat sudut membulat */
        border: none !important;
        padding: 10px 20px !important;
        font-size: 15px !important;
        font-weight: bold !important;
        width: auto !important; /* Lebar otomatis mengikuti panjang teks */
        display: block !important;
        margin-bottom: -5px !important; /* Jarak antar tombol */
        box-shadow: 0px 4px 6px rgba(0,0,0,0.1);
        transition: 0.2s;
    }
    
    /* Efek saat tombol di sidebar disentuh kursor (Hover) */
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: #c2185b !important; /* Pink lebih gelap saat di-hover */
        transform: scale(1.03);
    }
    
    /* Merapikan tampilan container input di layar utama */
    .stHeader h2 {
        color: #d81b60;
    }
    </style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state: 
    st.session_state['page'] = "Home" 
with st.sidebar:
    st.title("Menu ChemSolv")
    if st.button("Kalkulator Ksp"): 
        st.session_state['page'] = "Kalkulator Ksp"
        
    if st.button("Prediksi Endapan"):
        st.session_state['page'] = 'Prediksi Endapan'
        
    if st.button("Tentang Kami"):
        st.session_state['page'] = 'Tentang Kami'
    page = st.session_state['page'] 
    st.sidebar.divider()

# ==========================================
# FITUR 1: KALKULATOR KELARUTAN & KSP
# ==========================================
if page == "Kalkulator Ksp":
    st.title("🧪 ChemSolv: Kalkulator Kelarutan dan Ksp")
    st.title("🧪 ChemSolv: Kalkulator Kelarutan dan Ksp")
    st.markdown("Hitung **Kelarutan (s)** dari **Ksp**, atau sebaliknya, berdasarkan stoikiometri senyawa.")
    st.divider()

    mode = st.radio("Pilih Jenis Perhitungan:", 
                    ("Hitung Kelarutan (s) dari nilai Ksp", "Hitung Ksp dari nilai Kelarutan (s)"))

    senyawa_type = st.selectbox("Pilih Jenis Senyawa (Berdasarkan Stoikiometri):", 
                                ("AB (Contoh: AgCl, BaSO₄)", 
                                 "AB₂ atau A₂B (Contoh: PbCl₂, Ag₂CrO₄)", 
                                 "AB₃ atau A₃B (Contoh: Al(OH)₃, Ag₃PO₄)", 
                                 "A₂B₃ atau A₃B₂ (Contoh: As₂S₃)"))
    st.divider()

    # Logika Perhitungan: Kelarutan (s) dari Ksp
    if mode == "Hitung Kelarutan (s) dari nilai Ksp":
        ksp_val = st.number_input("Masukkan Nilai Ksp (Gunakan format e, contoh: 1.0e-10):", 
                                  value=1.0e-10, format="%.2e", step=1e-11)
        
        if st.button("Hitung Kelarutan (s)"):
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
        s_val = st.number_input("Masukkan Nilai Kelarutan (s) dalam mol/L (contoh: 1.0e-5):", 
                                value=1.0e-5, format="%.2e", step=1e-6)
        
        if st.button("Hitung Nilai Ksp"):
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

# ==========================================
# FITUR 2: PREDIKSI ENDAPAN (Qsp vs Ksp)
# ==========================================
elif page == "Prediksi Endapan":
    st.title("🧪 ChemSolv: Kalkulator Kelarutan dan Ksp")
    st.subheader("⚖️ Kalkulator Prediksi Endapan")
    st.markdown("Bandingkan nilai **Quotient Reaksi (Qsp)** dengan **Ksp** untuk memprediksi apakah suatu campuran akan menghasilkan endapan.")
    st.divider()

    st.subheader("1. Data Konstanta Ksp")
    ksp = st.number_input("Masukkan nilai Ksp:", format="%e", value=1.0e-10)

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

    if st.button("Hitung & Prediksi"):
        # Menghitung Qsp
        qsp = (konsentrasi_kation ** koefisien_kation) * (konsentrasi_anion ** koefisien_anion)
        
        st.write(f"**Nilai Quotient Reaksi (Qsp) yang dihitung:** {qsp:.2e}")
        st.latex(r"Q_{sp} = [\text{Kation}]^x [\text{Anion}]^y")
        
        # Kesimpulan Prediksi
        if qsp > ksp:
            st.error("Hasil: Qsp > Ksp. **Terjadi Endapan!** ⬇️")
        elif qsp == ksp:
            st.warning("Hasil: Qsp = Ksp. **Larutan Tepat Jenuh** (Belum mengendap). ⚖️")
        else:
            st.success("Hasil: Qsp < Ksp. **Tidak Terjadi Endapan** (Semua larut). 💧")

#OKE#
elif page == "Tentang Kami":
    st.title("⚖️")
    
