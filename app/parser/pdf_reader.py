import fitz


class PDFReader:

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def extract_blocks(self):
        document = fitz.open(self.pdf_path)

        extracted_data = []

        for page_number, page in enumerate(document, start=1):

            page_dict = page.get_text("dict")

            for block in page_dict["blocks"]:

                if "lines" not in block:
                    continue

                for line in block["lines"]:

                    line_text = ""
                    font_size = None
                    font_name = None

                    for span in line["spans"]:

                        line_text += span["text"]

                        if font_size is None:
                            font_size = span["size"]

                        if font_name is None:
                            font_name = span["font"]

                    extracted_data.append(
                        {
                            "page": page_number,
                            "text": line_text.strip(),
                            "font_size": font_size,
                            "font_name": font_name,
                            "bbox": block["bbox"],
                        }
                    )

        document.close()

        return extracted_data