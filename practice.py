char  = input("Enter Name: ")
char.split()
lis = print(" ".join(char))
total = 0
chara = ""
for i in lis[0]:
    for j in lis[1]:
        for k in lis[2]:
            if i == j and j == k :
                total+=1
                chara+=k

print(total)         
if total>0:
    print(chara)
else:
    print("There is no common prefix among the input strings.")
