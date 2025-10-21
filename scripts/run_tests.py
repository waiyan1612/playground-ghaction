import os
import re

print("Running test cases")
artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")

code_files = os.listdir(artifact_dir)
with open("test_results.md", "w") as f:
    f.write("| Filename | Passed | Failed |\n| -------- | ------ | ------ |\n")
    for code_file in code_files:
      f.write(f"|{code_file}| xx | yy |\n")

selected = os.path.join("./artifacts", code_files[1])
with open("selected.txt", "w") as f:
    f.write(selected)
print(f"Promoted {selected} to {best}")
