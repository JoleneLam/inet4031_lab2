import sys

data = []

for line in sys.stdin:
    line = line.strip()
    if line.startswith("#"):
        print(f"{line} is skipped because it starts with a hashtag (is commented out)")
        continue
    info = line.split(':')
    data.append(info)

print("Printing out User Data:\n")
for info in data:
        print(f"The user {info[0]} has a password of {info[1]} and has userid {info[2]} and groupid {info[3]}")
print("\nEnd of User Data\n")
