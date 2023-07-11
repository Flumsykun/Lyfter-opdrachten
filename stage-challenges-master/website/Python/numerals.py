def convert_to_roman(num):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
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
output_data = []
for line in input_data:
    num = int(line.strip())
    roman_numeral = convert_to_roman(num)
    output_data.append(roman_numeral)

# Write output to output.html
with open('output4.html', 'w') as file:
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('  <title>Roman Numerals Output</title>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('  <h1>Roman Numerals Output</h1>\n')
    file.write('  <ul>\n')
    for roman_numeral in output_data:
        file.write('    <li>' + roman_numeral + '</li>\n')
    file.write('  </ul>\n')
    file.write('</body>\n')
    file.write('</html>')