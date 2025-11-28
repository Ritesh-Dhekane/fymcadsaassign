import os

for i in range(1, 21):  # 36 to 52 inclusive
    filename = f"a2q{i}.py"
    with open(filename, "w") as f:
        f.write('print("Name = Ritesh Dhekane")\n')
    print(f"Created {filename}")
