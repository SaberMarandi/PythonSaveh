# D0040 - مقایسه دو فایل
# بررسی اینکه آیا دو فایل یکسان هستند

file1 = input()
file2 = input()

try:
    with open(file1, 'r', encoding='utf-8') as f1:
        content1 = f1.read()
    
    with open(file2, 'r', encoding='utf-8') as f2:
        content2 = f2.read()
    
    if content1 == content2:
        print("Files are identical")
    else:
        print("Files are different")
except FileNotFoundError:
    print("One or both files not found")
