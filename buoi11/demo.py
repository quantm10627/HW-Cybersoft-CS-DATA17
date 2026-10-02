import streamlit as st

#Nhóm 1 thahf phần để hiển thị
st.title("Hello streamlit")
st.header("Nhập thông tin người dùng")
# st.write()
# st.success()
# st.error()

#Nhóm 2 : Widget dùng để nhận output -> widget trả về một giá trị
name = st.text_input("Nhập họ và tên: ")
st.write(name)

age = st.slider("Nhập tuổi của bạn: ", min_value = 0, max_value = 100, value = 20) # Nhập tuổi dạng thanh kéo
st.write(age)

date = st.date_input ("Nhập ngày: ")

phone = st.text_input("Nhập số điện thoại", value = "0123456789")

is_student = st.checkbox ("Bạn có phải học sinh không ?")

language = st.selectbox ("Chọn ngôn ngữ", ["Tiếng Việt", "Tiếng Anh", "Tiếng Nhật"])
# phone = st.number.input("Nhập số điện thoại: ")