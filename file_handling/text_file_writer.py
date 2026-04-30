file_name='my_text.txt'

with open(file_name, mode='w') as file:
    while True:
        line = input('Enter a line: ')
        file.write(line+'\n')
        if line == 'quit':
            response=input('Do you want to write a new line? (y/n): ').lower()
            if response != 'y':
               break

print(f"Content written to {file_name}")