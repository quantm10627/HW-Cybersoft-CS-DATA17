from cover_letter_processor import CoverLetterProcessor

processor = CoverLetterProcessor(
    folder_path="cover_letters",
    excel_file="so_yeu_ly_lich.xlsx"
)
processor.process_documents()

# Các hàm thực hiện đều là các phương thức và được viết trong file cover_letter_processorr 
# Yêu cầu 1 : Thêm cột tên file và insert dữ liệu
processor.insert_column(9, "Tên File")

# Yêu cầu 2: Tìm các trường không có data
# Lưu ý trong file cover_letter (file data) đã xóa thông tin của một file để minh họa
processor.tim_truong()

# Yêu cầu 3 và 4: In ra các file xử lý thành công và file lỗi
# Ý tưởng: Tạo 2 thuộc tính trong lớp đối tượng CoverLetterProcessor là success và error để đếm file thành công và file lỗi
# Trong quá trình insert data của hàm processo_document, file nào ok thì tăng success
# Số file lỗi = Tổng file - số file success
print(f"Số file xử lý thành công: '{processor.success}' Số file lỗi : '{processor.error}'")

# Yêu cầu 5: Tự động điều chỉnh độ rộng cột trong excel
processor.auto_ajust_column()

