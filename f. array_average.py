numbers = []
count = 0

while count < 5:
    count += 1
    value = float(input(f"Enter number: "))
    numbers.append(value)

average = sum(numbers) / 5
print(f"Average of numbers is {average}")