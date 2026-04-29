with open('numbers.txt','r') as file:
    numbers={int(line.strip()) for line in file.readlines()}

even_numbers=[num for num in numbers if num%2==0]
odd_numbers=[num for num in numbers if num%2!=0]

with open('even.txt','w') as file:
    for num in even_numbers:
        file.write(str(num)+'\n')

with open ('odd.txt','w') as file:
    for num in odd_numbers:
        file.write(str(num)+'\n')

print(f"Even numbers written to even.txt:{len(even_numbers)}numbers")
print(f"Odd numbers written to odd.txt:{len(odd_numbers)}numbers")