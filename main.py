# Import PyPDF2 library
import PyPDF2

# Create a list of two PDF file names
pdfiles = ['1.pdf', '2.pdf']

# Initialize a PdfMerger object
merger = PyPDF2.PdfMerger()

# Iterate over each file name in the list
for filename in pdfiles:
    # Open the file in read binary mode
    pdfFile = open(filename, 'rb')

    # Create a PdfReader object using PyPDF2
    pdfReader = PyPDF2.PdfReader(pdfFile)

    # Append the PdfReader object to the PdfMerger object
    merger.append(pdfReader)

    # Close the file
    pdfFile.close()

# Write the merged PDF to a new file named "merged.pdf"
merger.write('merged.pdf')
