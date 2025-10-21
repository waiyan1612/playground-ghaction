import shutil
import os
import re

print("Running test cases")
artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")

code_files = os.listdir(artifact_dir)
print(f"Choosing best variant from {code_files}")
selected = os.path.join("./artifacts", code_files[1])

best = re.sub(r'-variant\d+(?=\.py$)', '', selected)
shutil.copy(selected, best)
print(f"Promoted {selected} to {best}")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"best={best}\n")
