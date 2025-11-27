file=open("max.txt","r")

a=file.read()
a=a.split()
a=list(map(int, a))
print(max(a))