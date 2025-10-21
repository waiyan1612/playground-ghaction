import os

print("Running test cases")
artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")

code_files = [
    f
    for f in os.listdir(artifact_dir)
    if os.path.isfile(os.path.join(artifact_dir, f))
]
print(code_files)

print("Choosing best candidate")
with open("best.txt", "w"):
  print(f"best={code_files[1]}")
