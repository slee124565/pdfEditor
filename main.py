from pypdf import PdfReader, PdfWriter
import subprocess

if __name__ == '__main__':
    reader = PdfReader("form.pdf")
    writer = PdfWriter()

    page = reader.pages[0]
    # fields = reader.get_fields()
    txt_fields = reader.get_form_text_fields()

    # writer.add_page(page)
    writer.append(reader)
    writer.set_need_appearances_writer()

    for key in txt_fields.keys():
        if 'Text' in f'{key}':
            value = key.replace('Text', '')
        elif '_' in key:
            value = key.split('_')[1]
        else:
            value = key
        writer.update_page_form_field_values(
            writer.pages[0], {key: f'{value}'}
        )

    # write "output" to PyPDF2-output.pdf
    with open("filled-out.pdf", "wb") as output_stream:
        writer.write(output_stream)

    input('Press any key to continue ...')
    cmd = 'open filled-out.pdf'
    subprocess.run(cmd.split(' '))
