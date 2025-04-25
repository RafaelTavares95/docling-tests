from docling.document_converter import DocumentConverter

#coverting
source = "./file.pdf" 
converter = DocumentConverter()
result = converter.convert(source)

#export result to a file
file = open("file.md", "w")
file.write(result.document.export_to_markdown())
file.close()
