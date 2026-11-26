import os

# Rejected Olympic sport: one line, broadcast-plausible, <=200 chars
LINE = "Synchronized parallel parking, scored on speed, style, and how many bystanders quietly move their own cars."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
