# muốn đọc file cover_letter/Le_Van_C.docx

from docx import Document

file_path = "buoi8/cover_letters/le_van_c.docx"
doc = Document(file_path)
print(doc)
print(doc.paragraphs[3].text)

# Cấu trúc: Document -> Paragraphs -> List các paragraph object -> Paragraph.text -> nội dung dạng string

# doc_content = []

# for paragraph in doc.paragraphs:
#     doc_content.append(paragraph.text)

# print(doc_content)

