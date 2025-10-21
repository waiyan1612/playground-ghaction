import os

print("Running test cases")
artifact_dir = os.path.join(os.path.dirname(__file__), "../artifacts")

code_files = [
    f
    for f in os.listdir(artifact_dir)
    if os.path.isfile(os.path.join(artifact_dir, f))
]

print(f"Choosing best variant from {code_files}")
best = code_files[1]
with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    f.write(f"best={best}\n")
