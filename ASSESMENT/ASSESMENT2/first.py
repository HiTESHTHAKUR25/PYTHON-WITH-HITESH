s = input("Enter String: ")
word = input("Enter Word: ")

count = 0


for i in  range(len(s)-len(word)):
    count1 = 1
    for j in  range(len(word)):
        if s[i+j] != word[j]:
            count1 = 0
            break


    if count1 == 1:
        count = count+1

print(count+1)
