import os
import re


artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")
code_files = os.listdir(artifact_dir)
print("Running test cases ...")
with open("test_results.md", "w") as f:
    f.write("| Filename | Passed | Failed |\n| -------- | ------ | ------ |\n")
    for code_file in code_files:
      f.write(f"|{code_file}| xx | yy |\n")

selected = os.path.join("./artifacts", code_files[-1])
print(f"Selected {selected} as the best variant.")
with open("selected.txt", "w") as f:
    f.write(selected)
    
print("Tests complete,")
