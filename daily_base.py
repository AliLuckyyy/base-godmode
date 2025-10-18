from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")
filename = f"daily_code_{today}.py"

with open(filename, "w") as f:
    f.write(f"# Auto generated daily code for {today}\n")
    f.write("print('Hello Base Builders!')\n")

print(f"Created {filename}")
