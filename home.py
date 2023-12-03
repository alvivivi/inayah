import streamlit as st

st.set_page_config(
    page_title="Portfolio | Inayah",
    page_icon="🍒",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 😼")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("mee.jpg", width= 290)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : INAYATUL AENAH")
   st.caption("NIM : 0402201098")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 19 Juni
            - Alamat               : Sengon Tamjung Brebes
            - Hobi                 : Melihat Langit
            - Cita-cita            : Rich Aunty
            - Hal yang disukai     : Delulu
            - Status               : Milik Kedua Orang Tua
            """
        )
st.header("*Don't Call Me - I'm Busy*")
