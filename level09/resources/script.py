import sys

arg = sys.argv[1]
result = ""

for i in range(len(arg)):
    result += chr(ord(arg[i]) - i)

print(result)