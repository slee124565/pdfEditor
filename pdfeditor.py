from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.generic import NameObject

reader = PdfReader("form.pdf")
writer = PdfWriter()

page = reader.pages[0]
# fields = reader.get_fields()
txt_fields = reader.get_form_text_fields()

writer.add_page(page)

for key in txt_fields.keys():
    writer.update_page_form_field_values(
        writer.pages[0], {key: f'{key}'}
    )

# write "output" to PyPDF2-output.pdf
with open("filled-out.pdf", "wb") as output_stream:
    writer.write(output_stream)
