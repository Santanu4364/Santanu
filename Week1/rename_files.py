import os
import re

folder = "week1"

for filename in os.listdir(folder):
    match = re.match(r"L(\d+)\.py", filename)
    if match:
        num = int(match.group(1))
        new_name = f"L{num:02}.py"   # adds leading zero
        old_path = os.path.join(folder, filename)
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")
print("\n all matching files have been renames!")