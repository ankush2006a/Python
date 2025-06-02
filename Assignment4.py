'''Assignment 4 Task 1 '''

try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


'''Assignment 4 Task 2 '''

data = input("Enter data to write to output.txt: ")
with open('output.txt', 'w') as file:
    file.write(data + '\n')
more_data = input("Enter additional data to append to output.txt: ")
with open('output.txt', 'a') as file:
    file.write(more_data + '\n')
print("\nFinal content of 'output.txt':")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
