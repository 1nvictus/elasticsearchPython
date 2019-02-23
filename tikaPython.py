from tika import parser

file = '/home/fractaluser/Downloads/school.pdf'
# Parse data from file
file_data = parser.from_file(file)
# Get files text content
text = file_data['content']
print(text)

