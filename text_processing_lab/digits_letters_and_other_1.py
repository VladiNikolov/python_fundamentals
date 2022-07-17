def digits_func(text):
    return "".join([str(ch) for ch in text if ch.isdigit()])

def alpha_func(text):
    return "".join([ch for ch in text if ch.isalpha()])

def other_func(text):
    return "".join([ch for ch in text if not ch.isalpha() and not ch.isdigit()])

text = input()
print(digits_func(text))
print(alpha_func(text))
print(other_func(text))