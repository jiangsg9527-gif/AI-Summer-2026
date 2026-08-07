# 使用写入模式打开文件
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("今天学习文件读写。\n")
    file.write("下一步学习 Pandas。\n")

print("TXT文件写入成功！")


# 使用读取模式打开文件
with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("\nTXT文件内容：")
print(content)