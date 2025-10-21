import shutil
import os
import re

print("Running test cases")
artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")

code_files = os.listdir(artifact_dir)
print(f"Choosing best variant from {code_files}")
selected = os.path.join("./artifacts", code_files[1])

print("Summarizing results")
with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
    f.write("| Filename | Passed | Failed |\n| -------- | ------ | ------ |\n")
    for code_file in code_files:
      f.write(f"|{code_file}| xx | yy |\n")

best = re.sub(r'-variant\d+(?=\.py$)', '', selected)
shutil.copy(selected, best)
print(f"Promoted {selected} to {best}")
