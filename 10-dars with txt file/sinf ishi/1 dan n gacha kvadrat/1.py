kvadrat=open("kavdrat.txt","w")
kub=open("kub.txt","w")
n=int(input())
for i in range(1,n+1):
    kvadrat.write(f"{i**2} ")
    kub.write(f"{i**3} ")
kvadrat.close()
kub.close()