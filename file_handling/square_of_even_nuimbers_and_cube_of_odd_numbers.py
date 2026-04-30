with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

even_squares= [num**2 for num in numbers if num % 2 == 0]
odd_cubes=[num**3 for num in numbers if num %2!=0]

with open('double.txt', 'w') as file:
    for square in even_squares:
        file.write(str(square)+'\n')

with open('triple.txt', 'w') as file:
    for cube in odd_cubes:
        file.write(str(cube)+'\n')

print(f"Square of even numbers written to doubke.txt: {len(even_squares)} numbers")
print(f"Cubes of odd numbers written to triple.txt: {len(odd_cubes)} numbers")