import os

current_directory = os.getcwd()
folder_with_files = 'Text files'
full_path = os.path.join(current_directory, folder_with_files)
list_files = []
for files in os.listdir(full_path):
    list_files.append(files)
print(list_files)
a = {}
for file in list_files:
    with open(os.path.join(current_directory, folder_with_files, file), 'r', encoding='utf-8') as f:
        count = 0
        b =[]
        for line in f:
            count += 1
            b.append(line)
            a[file] = [count, b]
with open('Final file.txt', 'w'):
    pass
print(a)
while a != {}:
    for z, v in a.items():
        min_text = min(a.values())
        if v == min_text:
            n = v[1][0:]
            with open('Final file.txt', 'a', encoding='utf-8') as d:
                d.write(f'{z} \n{v[0]}\n')
                d.writelines(n)
                d.write('\n\n')
                del a[z]
                break