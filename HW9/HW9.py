from cover_letter_processor import CoverLetterProcessor

processor = CoverLetterProcessor(
    folder_path="cover_letters",
    excel_file="so_yeu_ly_lich.xlsx"
)
processor.process_documents()

processor.insert_column(9, "Tên File")

#YC2 : Tìm các trường không có data
processor.tim_truong()

print(f"Số file xử lý thành công: '{processor.success}' Số file lỗi : '{processor.error}'")

processor.auto_ajust_column()
