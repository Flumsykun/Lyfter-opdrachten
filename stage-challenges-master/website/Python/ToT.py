def distribute_candy(vampires, zombies, witches, houses):
    total_candies = vampires * 3 + zombies * 4 + witches * 5
    candies_per_child = total_candies // houses
    return candies_per_child

# Read input from input.txt
with open('./Input/input2.txt', 'r') as file:
    input_data = file.readlines()

# Process each line and calculate candies per child
output_data = []
for line in input_data:
    group = line.strip().split(', ')
    vampires = int(group[0].split(': ')[1])
    zombies = int(group[1].split(': ')[1])
    witches = int(group[2].split(': ')[1])
    houses = int(group[3].split(': ')[1])
    candies_per_child = distribute_candy(vampires, zombies, witches, houses)
    output_data.append(str(candies_per_child))

# Write output to output.html
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
