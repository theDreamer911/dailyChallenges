import random


# def divide_chunks(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]


# opening file
file = open('class.txt', 'r')

# looping through text file
for line in file:
    # split comas
    fields = line.split(', ')
    random.shuffle(fields)

file.close()

n = 2
x = [fields[i * n:(i+1)*n] for i in range((len(fields)+n-1)//n)]
# x = list(divide_chunks(fields, n))
# print(fields)

print(x)
