mustbat=open("mustbat.txt","w")
manfiy=open("manfiy.txt","w")

a = [-3, 5, -1, 7, -6]
for i in a:
    if i > 0:
        mustbat.write(f"{i} ")
    elif i<0:
        manfiy.write(f"{i} ")
mustbat.close()
manfiy.close()