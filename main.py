#!/usr/bin/env python3
"""Office Artifacts: one-line museum placard for a sticky note."""
import os

LINE = "Votive note, c. 2003, paper and faded ink. Affixed to the shrine of the fridge to mark a lunch never eaten; bequest of K., Desk 14, who never returned for it."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
