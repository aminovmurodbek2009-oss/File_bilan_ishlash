file=open("FizzBuzz.txt","w")
son=int(input())

for i in range(1,son+1):
    if i % 5 == 0 and son % 3 == 0:
        file.write("FizzBuzz ")
    elif i % 3 == 0:
        file.write("Fizz ")
    elif i % 5 == 0:
        file.write("Buzz ")
    else:
        file.write(f"{i} ")
file.close()