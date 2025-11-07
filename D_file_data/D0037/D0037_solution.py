# D0037 - تقسیم فایل
# تقسیم فایل به چند فایل کوچکتر

filename = input()
n = int(input())

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    file_count = 0
    for i in range(0, len(lines), n):
        file_count += 1
        with open(f'part{file_count}.txt', 'w', encoding='utf-8') as out:
            out.writelines(lines[i:i+n])
    
    print(f"Split into {file_count} files")
except FileNotFoundError:
    print("File not found")
