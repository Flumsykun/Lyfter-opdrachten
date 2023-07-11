def convert_to_roman(num):
    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while num >= value:
            roman_numeral += symbol
            num -= value

    return roman_numeral

# Read input from input.txt
with open('./Input/input3.txt', 'r') as file:
    input_data = file.readlines()

# Convert to Roman numerals
output_data = [convert_to_roman(int(line.strip())) for line in input_data]

# Write output to output.html
with open('./Output/output4.html', 'w') as file:
    file.write(f'''
        <html>
        <head>
            <title>Roman Numerals Output</title>
        </head>
        <body>
            <h1>Roman Numerals Output</h1>
            <ul>
                {"".join(f"                <li>{roman_numeral}</li>\n" for roman_numeral in output_data)}
            </ul>
        </body>
        </html>
    ''')
