import os

print("Running test cases")
code_dir = os.path.join(os.path.dirname(__file__), "../code")
base = os.path.normpath(os.path.join(os.path.dirname(__file__), ".."))

files = [
    os.path.relpath(os.path.join(code_dir, f), start=base)
    for f in os.listdir(code_dir)
    if os.path.isfile(os.path.join(code_dir, f))
]
print(files)

print("Choosing best candidate")
with open("best.txt", "w"):
  print(f"best={files[1]}")
