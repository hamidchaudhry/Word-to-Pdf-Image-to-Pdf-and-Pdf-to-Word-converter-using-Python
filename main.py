import pdf2image
from PIL import Image
import docxtopdf
import io

# Create a menu
print("Select an option:")
print("1. Convert Word file to PDF")
print("2. Convert PDF file to Word")
print("3. Convert Image to PDF")

# Get the user's choice
choice = input("Enter your choice: ")

# Convert Word file to PDF
if choice == "1":
    input_file = input("Enter the full path of the input Word file: ")
    output_file = input("Enter the full path of the output PDF file: ")

    # Convert the Word file to a PDF file
    with open(input_file, "rb") as f:
        doc = docxtopdf.convert(f)

    # Save the PDF file
    with open(output_file, "wb") as f:
        f.write(doc)

    print("Word file converted to PDF successfully!")

# Convert PDF file to Word
elif choice == "2":
    input_file = input("Enter the full path of the input PDF file: ")
    output_file = input("Enter the full path of the output Word file: ")

    # Convert the PDF file to a Word file
    pdf_images = pdf2image.convert_from_path(input_file)

    # Convert the PDF images to a Word document
    doc = docxtopdf.convert(pdf_images)

    # Save the Word document
    with open(output_file, "wb") as f:
        f.write(doc)

    print("PDF file converted to Word successfully!")

# Convert Image to PDF
elif choice == "3":
    input_file = input("Enter the full path of the input image file: ")
    output_file = input("Enter the full path of the output PDF file: ")

    # Convert the image to a PDF file
    image = Image.open(input_file)
    image.save(output_file, "PDF")

    print("Image converted to PDF successfully!")

else:
    print("Invalid choice!")
