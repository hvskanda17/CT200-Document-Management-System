from app.parser.pdf_reader import PDFReader

reader = PDFReader("data/ct200_manual.pdf")

blocks = reader.extract_blocks()

for block in blocks:
    if "Battery Life" in block["text"]:
        print(block)