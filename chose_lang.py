import time

# List of languages to practice coding in
lang = [
    "python",
    "c++",
]

current_time = int(time.time())
days = current_time // (60 * 60 * 24)
# Use current day to chose language - iterate through the list each day
print(lang[(days - 1) % len(lang)])
