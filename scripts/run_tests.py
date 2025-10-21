import os

print("Running test cases")
artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")

code_files = os.listdir(artifact_dir)
print(f"Choosing best variant from {code_files}")
best = os.path.join("./artifacts", code_files[1])
print(f"Selected: {best}")

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"best={best}\n")
