(1)
# Program to reverse a string
string = "Hello, World!"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

OUTPUT: Reversed string: !dlroW ,olleH

(2)
# Program to count vowels in a string
text = "Python Programming"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

OUTPUT: Number of vowels: 4

(3)
# Program to check prime number
num = 29
is_prime = True
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False

print(num, "is prime" if is_prime else "is not prime")

OUTPUT: 29 is prime

(4)
# Program to merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

OUTPUT: Merged dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

(5)
# Program to find squares of elements in a list
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print("Squares:", squares)

OUTPUT: Squares: [1, 4, 9, 16, 25]
