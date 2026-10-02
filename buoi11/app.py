import streamlit as st

with st.form (key = "user_form"):
    name = st.text_input("Họ và tên: ")
    phone = st.text_input("Số điện thoại: ")
    date = st.date_input("Ngày sinh:")
    email = st.text_input("Email:")
    is_student = st.checkbox ("Bạn có phải học sinh không ?")

    submit_button = st.form_submit_button ("Thêm thông tin")