import re

def clean_up_words(string):
    cleaned_string = re.sub('[^a-zA-Z]+', ' ', string)  # Remove non-alphabetic characters
    cleaned_string = cleaned_string.strip()  # Remove leading/trailing spaces
    cleaned_string = ' '.join(cleaned_string.split())  # Remove extra spaces between words
    return cleaned_string.lower()

# Read input from input.txt
with open('./input.txtinput.txt', 'r') as file:
    input_data = file.readlines()

# Clean up the words
output_data = []
for line in input_data:
    cleaned_line = clean_up_words(line)
    output_data.append(cleaned_line)

# Write output to output.html
with open('./index.html', 'w') as file:
    file.write('<pre>\n')
    for line in output_data:
        file.write(line + '\n')
    file.write('</pre>')
