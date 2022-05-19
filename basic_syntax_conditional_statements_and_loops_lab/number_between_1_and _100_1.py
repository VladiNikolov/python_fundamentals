import sys

for i in range(sys.maxsize):
    current_number = float(input())
    if current_number < 1 or current_number > 100:
        continue
    else:
        print(f"The number {current_number} is between 1 and 100")
        break



