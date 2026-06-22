import streamlit as st
import joblib
import pandas as pd

# Memuat model AI
model = joblib.load('model_pcos_track.pkl')

st.title("🩺 PCOS-Track: AI Deteksi Dini")

# Form Input
with st.form("input_form"):
    age = st.number_input("Usia (Tahun)", 18, 50, 25)
    weight = st.number_input("Berat Badan (Kg)", 30.0, 150.0, 50.0)
    height = st.number_input("Tinggi Badan (Cm)", 140.0, 200.0, 160.0)
    
    bmi = round(weight / ((height/100) ** 2), 1)
    st.write(f"**BMI Anda:** {bmi}")
    
    # Mengubah Input menjadi pilihan yang lebih ramah pengguna
    cycle_raw = st.selectbox("Siklus Haid", ["Teratur", "Tidak Teratur"])
    cycle = 1 if cycle_raw == "Teratur" else 0
    
    # Menggunakan Checkbox (True = 1, False = 0)
    weight_gain = 1 if st.checkbox("Mengalami kenaikan berat badan drastis?") else 0
    hair_growth = 1 if st.checkbox("Pertumbuhan rambut berlebih (Hirsutisme)?") else 0
    skin_darkening = 1 if st.checkbox("Kulit menggelap (di lipatan/leher)?") else 0
    hair_loss = 1 if st.checkbox("Rambut rontok berlebih?") else 0
    pimples = 1 if st.checkbox("Jerawat parah?") else 0
    fast_food = 1 if st.checkbox("Sering makan makanan cepat saji?") else 0
    exercise = 1 if st.checkbox("Rutin berolahraga?") else 0
    
    submit = st.form_submit_button("Deteksi Sekarang")

if submit:
    input_data = pd.DataFrame([[age, weight, height, bmi, cycle, weight_gain, hair_growth, 
                                skin_darkening, hair_loss, pimples, fast_food, exercise]],
                              columns=[' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'BMI',
                                       'Cycle(R/I)', 'Weight gain(Y/N)', 'hair growth(Y/N)', 
                                       'Skin darkening (Y/N)', 'Hair loss(Y/N)', 'Pimples(Y/N)', 
                                       'Fast food (Y/N)', 'Reg.Exercise(Y/N)'])
    
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ Hasil: Terdeteksi Risiko Tinggi PCOS. Silakan konsultasi ke dokter SpOG.")
    else:
        st.success("✅ Hasil: Risiko Rendah. Pertahankan gaya hidup sehat!")
    st.markdown("---") # Garis pemisah
    st.markdown("<span style='color:red; font-size:0.8em;'>⚠️ <b>DISCLAIMER:</b> Prediksi ini dihasilkan oleh AI dan memiliki kemungkinan salah. Aplikasi ini hanya ditujukan untuk referensi edukasi dan bukan sepenuhnya pengganti diagnosis medis profesional. Harap segera hubungi dokter untuk pemeriksaan lebih lanjut.</span>", unsafe_allow_html=True)    