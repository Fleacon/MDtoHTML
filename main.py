import converter
import os

if not os.path.exists('./out'):
    os.makedirs('./out', exist_ok=True)

input_file = input("Enter the Markdown file path: ")
converter.convert_to_html(input_file)
print("HTML file created")