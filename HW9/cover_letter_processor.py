# Xây dựng chuyên gia xử lý hồ sơ tên CoverLetterProcessor
# Nhiệm vụ: Đọc file word, Trích xuất dữ liệu, Làm việc với Excel, Lưu kết quả 

import os # làm việc file, foler, đường dẫn
import re # xử lý regular expression 

from openpyxl import Workbook, load_workbook # Dùng để đọc và ghi excel 
from docx import Document # Xử lý file word

class CoverLetterProcessor:
    def __init__(self, folder_path, excel_file):
        self.folder_path = folder_path
        self.excel_file = excel_file
        self.success = 0
        self.error = 0
        self.wb = None
        self.ws = None
        self.headers = [
            "Họ và tên",
            "Giới tính",
            "Ngày sinh",
            "Nơi sinh",
            "Nguyên quán",
            "Hộ khẩu thường trú",
            "Chỗ ở hiện nay",
            "Điện thoại",
        ]

        self.patterns = {
            "Họ và tên": r"Họ và tên\s*:\s*(.*?)\s+Nam/Nữ\s*:",
            
            "Giới tính": r"Nam/Nữ\s*:[ \t]*([^\n]*)",
            
            "Ngày sinh": r"Sinh ngày\s*:\s*(.*?)\s+Nơi sinh\s*:",
            
            "Nơi sinh": r"Nơi sinh\s*:[ \t]*([^\n]*)",
            
            "Nguyên quán": r"Nguyên quán\s*:[ \t]*([^\n]*)",
            
            "Hộ khẩu thường trú":
                r"Nơi đăng ký hộ khẩu thường trú\s*:[ \t]*([^\n]*)",
            
            "Chỗ ở hiện nay":
                r"Chỗ ở hiện nay\s*:[ \t]*([^\n]*)",
            
            "Điện thoại":
                r"Điện thoại(?: liên hệ)?\s*:[ \t]*([^\n]*)",
                
        }
    # Phương thức 1: Khởi tạo, mở excel -> initialize_excel()
    def initialize_excel(self):
        if os.path.exists(self.excel_file):
            self.wb = load_workbook(self.excel_file)
            self.ws = self.wb.active
        else:
            self.wb = Workbook()
            self.ws = self.wb.active

            self.ws.title = "Thông tin người dùng"
            self.ws.append(self.headers)

    # Phương thức 2: Read Docx
    def read_docx(self, file_path):
        doc = Document(file_path)

        doc_content = [
            paragraph.text
            for paragraph in doc.paragraphs
        ]

        doc_full = "\n".join(doc_content)
        return doc_full

    # Phương thứ 3: Trích xuất thông tin 
    def extract_info(self, text):
        info = {}

        for key, pattern in self.patterns.items():
            match = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if match:
                value = match.group(1).strip()
                value = re.sub(r"\s+", " ", value)

                info[key] = value
            else:
                info[key] = ""

        return info

    def process_documents(self):
        self.initialize_excel()

        doc_files = os.listdir(self.folder_path) # Lấy danh sách tất cả file bên trong folder
        sum = len(doc_files)
        for file_name in doc_files:
            if not file_name.lower().endswith(".docx"):
                continue
            file_path = os.path.join(self.folder_path, file_name)

            document_text = self.read_docx(file_path)
            data = self.extract_info(document_text) # Trả ra dictionary 
            values = [
                data.get(header, "") 
                for header in self.headers
            ]
            self.success += 1
            self.ws.append(values)
        self.error = sum - self.success
        self.wb.save(self.excel_file)
        print("Xử lý thành công")        


        # Thêm cột "Tên File"
    def insert_column (self, col_index, header_name):
        self.initialize_excel()
        self.ws.insert_cols(col_index)
        self.ws.cell(row = 1, column = col_index, value = header_name)
        doc_files = os.listdir(self.folder_path) # Lấy danh sách tất cả file bên trong folder
        i = 2
        for file_name in doc_files:
            if not file_name.lower().endswith(".docx"):
                continue
        
            self.ws.cell(row = i, column = col_index, value = file_name )
            i+=1
        self.wb.save(self.excel_file)
        print("Thêm cột thành công")
    def auto_ajust_column (self):
        self.initialize_excel()
        for col in self.ws.iter_cols():
            col_word = col[0].column_letter #Lấy header
            max_size = 0

            for cell in col:
                if cell.value is not None:
                    cell_len = len(str(cell.value))
                    if cell_len > max_size:
                        max_size = cell_len
            self.ws.column_dimensions[col_word].width = max_size + 3 #Tránh trường hợp chữ quá sát
        self.wb.save(self.excel_file)
        print("Điều chỉnh độ rộng cột thành công")




    def tim_truong (self):
        doc_files = os.listdir(self.folder_path)

        for file_name in doc_files:
            if not file_name.lower().endswith(".docx") or file_name.startswith("~$"):
                continue
            file_path = os.path.join(self.folder_path, file_name)
            document = self.read_docx(file_path) 
            data = self.extract_info(document)

            for header, values in data.items():
                if values == "" or values is None:
                    print(f"File '{file_name}' - Trường '{header}' không được tìm thấy")

  
    
     # {
        # "Họ và tên": "Lê Văn C",
        # "Giới tính": "Nam",
        # "Ngày sinh": "20/08/2003",
        # "Nơi sinh": "Đà Nẵng",
        # "Nguyên quán": "Quảng Nam",
        # "Hộ khẩu thường trú": "...",
        # "Chỗ ở hiện nay": "...",
        # "Điện thoại": "090..."
        # }

        # Khối 1: initialize_excel() -> mở hoặc tạo excel
        # Khối 2: read_docx() -> đọc word và trả về text
        # Khối 3: extract_info() -> nhận text -> trích xuất thông tin -> trả về dictionary

        # Pipeline:
        # B1: Khởi tạo excel
        # B2: Lấy danh sách file word
        # B3: Duyệt từng file
        # B4: Đọc file
        # B5: Trích xuất thông tin
        # B6: Đưa dữ liệu vào excel
        # B7: Lưu excel 
