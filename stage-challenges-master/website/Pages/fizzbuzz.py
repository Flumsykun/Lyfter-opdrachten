def fizz_buzz(fizz, buzz):
    output = []
    for i in range(1, 101):
        if i % fizz == 0 and i % buzz == 0:
            output.append("FB")
        elif i % fizz == 0:
            output.append("F")
        elif i % buzz == 0:
            output.append("B")
        else:
            output.append(str(i))
    return output

# Provide input values for fizz and buzz
fizz = int(input("Enter the fizz value: "))
buzz = int(input("Enter the buzz value: "))

# Get the Fizz Buzz sequence
sequence = fizz_buzz(fizz, buzz)

# Generate HTML
html = """
<!DOCTYPE html>
<html>
<head>
<title>Fizz Buzz Output</title>
</head>
<body>
<h1>Fizz Buzz Output</h1>
<p>{}</p>
</body>
</html>
""".format(" ".join(sequence))

# Write output to output.html
with open('output2.html', 'w') as file:
    file.write(html)
