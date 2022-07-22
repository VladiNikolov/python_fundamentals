import re
pattern = r"(?P<day>\d{2})(?P<separator>[\.\-\/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

input_text = input()
searched_pattern = [obj.groupdict() for obj in re.finditer(pattern, input_text)]
for pattern in searched_pattern:
    print(f"Day: {pattern['day']}, Month: {pattern['month']}, Year: {pattern['year']}")
