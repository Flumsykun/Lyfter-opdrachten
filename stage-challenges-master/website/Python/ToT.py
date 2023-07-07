# Read input from input.txt
with open('./Input/input2.txt', 'r') as file:
    input_data = file.readlines()

# Process each line and calculate candies per child
output_data = [
    str(sum(int(x.split(': ')[1]) * y for x, y in zip(group, [3, 4, 5])) // int(group[3].split(': ')[1]))
    for group in (line.strip().split(', ') for line in input_data)
]

# Write output to output3.html
with open('output3.html', 'w') as file:
    file.write('<html>\n')
    file.write('<head>\n')
    file.write('  <title>Trick or Treat Output</title>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('  <h1>Trick or Treat Output</h1>\n')
    file.write('  <ul>\n')
    for candies in output_data:
        file.write('    <li>' + candies + '</li>\n')
    file.write('  </ul>\n')
    file.write('</body>\n')
    file.write('</html>')

