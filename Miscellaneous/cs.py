no=0
for a in range(2, 101):
    check = 0
    for b in range(2, a):
        if a%b==0:
            check+=1
    if check==0:
        no+=1
        print(a)
print(no)