# Read from file
file = "d:\\tutorials\\python\\barantcev-training\\barantcev-training\\Learn Python Book\\txt_file.txt"
with open(file) as f_obj:
    content = f_obj.read()
    print(content)
    print()

# print(read) lines from file
with open(file) as f_obj:
    for line in f_obj:
        print(line.strip())

# Create list of strings(lines)
with open(file) as f_obj:
    lines = f_obj.readlines()
print(lines)
for line in lines:
    print(line.rstrip())
text = ''
for line in lines:
    text +=line.rstrip()
print(text)

# Replacing
new_text = []
for line in lines:
    if 'qwe' in line:
        new_text.append(line.replace('qwe', 'asd'))
print(new_text)

# Write in file
file_to_write = "d:\\tutorials\\python\\barantcev-training\\barantcev-training\\Learn Python Book\\savings.txt"
with open(file_to_write, 'a+') as f_obj:
    f_obj.write('The info to be saved1\n')
    f_obj.write('The info to be saved2\n')



