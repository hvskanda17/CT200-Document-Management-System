from app.parser.pdf_reader import PDFReader


reader = PDFReader("data/ct200_manual.pdf")

blocks = reader.extract_blocks()

for block in blocks[:20]:
    print(block)