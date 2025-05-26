character = input("Enter a single character: ")

def check_case(character):
    if character.isupper():
        return "uppercase"
    elif character.islower():
        return "lowercase"
    else:
        return "not uppercase or lowercase"

result = check_case(character)
print(f"The character is {result}.")