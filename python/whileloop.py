#basic while loop
'''n = 1
while n <= 3:
    print(n)
    n+=1'''

#sum of N natural numbers
'''n =int(input("Enter a value of n:"))
sum = 0
while n > 0:
    sum += n
    n -= 1
print(f"Sum is {sum}")'''

# infinite while loop
'''n = 100
while True:
    print(n)
    n-=1'''

#breaking loop
'''while True:
    line = input("Enter a number(type 'q' to quit):")
    if line == 'q':
        break
    print(line)'''

fruits = ['apple','banana','mango','strawberry']
fruits_len = len(fruits)
index = 0

while index < fruits_len:
    if fruits[index] == 'orange':
        print("Orange is availabel.")
        break
    index += 1
else:
    print("Orange is not availabel.")