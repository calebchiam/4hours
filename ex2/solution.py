with open('numbers.txt') as numbers_file:
    s = numbers_file.read()


number_string_list = s.split("\n")

new_list = []

for string in number_string_list:
    if len(string) > 0:
        new_list.append(int(string))

print(sum(new_list))


with open('filename.txt') as f:
    contents = f.read()
