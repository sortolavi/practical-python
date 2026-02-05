import stock

with stock.open("koe.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
print("File content read successfully.")

