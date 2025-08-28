import img2pdf

image_files = ['C:/Users/husse/Downloads/OIP-232202922.jpg','C:/Users/husse/Downloads/OIP-1784839050.jpg']

output_pdf = "output.pdf" 

with open(output_pdf, "wb") as f:
    f.write(img2pdf.convert(image_files))