from cover_letter_processor import CoverLetterProcessor

processor = CoverLetterProcessor(
    folder_path="buoi8/cover_letters",
    excel_file="buoi8/so_yeu_ly_lich.xlsx"
)
processor.process_documents()
# YC1: 