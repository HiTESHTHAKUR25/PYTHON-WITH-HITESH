# 1 Find the length of a string.S = "programming"

s = input("Enter String: ")
print(len(s))



# 2 Copy one string to another.



s = input("Enter First String: ")
s1 = input("Enter Second String: ")



print(s+s1)


# 4 Compare two strings (case-sensitive).



s1 = input("Enter First String: ")
s2 = input("Enter Secod String: ")



if s1 == s2:
    print("Both Are Same")
else:
    print("NOt Same")



# 3 Concatenate two strings.


s1 = input("Enter 1st String: ")
s2 = input("Enter 2nd String: ")


print(s1+s2)


# 5 Compare two strings ignoring case.




s1 = input("Enter First String: ").lower()
s2 = input("Enter Secod String: ").lower()



if s1 == s2:
    print("Both Are Same")
else:
    print("NOt Same")

# 6 Convert a string to uppercase.


s = input("Enter String: ")

result = ""

for i in s:
    if s >= "a" and s <= "z":
        upper = ord(i)-32
        result = result + chr(upper) 


print(result)



# 7 Convert a string to lowercase.


s = input("Enter String: ")
result = ""

for i in s:
    if i >= "A" and i <= "Z":
        lower = ord(i)+32
        result = result + chr(lower)


print(result)




# 8 Toggle the case of each character.

s = input("Enter String: ")
result = ""

for i in s:
    if i >= "a" and i <= "z":
        upper = ord(i) -32
        result = result + chr(upper)
    elif i >= "A" and i <= "Z":
        lower = ord(i)+32
        result = result + chr(lower)
    else:
        result = result + i

print(result)




# 9 Check whether a string is empty.


s = input("Enter String1: ")
s1 = input("Enter String: ")



if len(s) ==0 or len(s1) == 0:
    print("anyone string is Empty String")
else:
    print("String HAve Some thing")




# 10 Trim leading, trailing, or extra spaces.

s = input("Enter String: ")
result = ""


for i in range(len(s)):
    if s[i] == " ":
        pass
    elif s[i-1]==" " and (s[i] >= "a" and s[i] <= "z"):
        result = result+" "+s[i]
    else:
        result = result+s[i]


print(result)


# 10 Trim leading, trailing, or extra spaces.

s = input("Enter String: ")
result = ""


for i in range(len(s)):
    if s[i] == " ":
        pass
    elif s[i-1]==" ":
        result = result+" "+s[i]
    else:
        result = result+s[i]


print(result)




# 11 Get the character at a given index.


s = input("Enter String: ")
word = int(input("Entre The Index Number: "))


print(s[word])



# 12 Get the Unicode code point of a character at index.12 Get the Unicode code point of a character at index.


s = input("Enter String: ")
num = int(input("Enter The index of any Word: "))


print(ord(s[num]))




# 13 Get the Unicode code point before index.


s = input("Enter String: ")
num = int(input("Enter String: "))


print(ord(s[num-1]))



# 14 Find the first occurrence of a character.


s = input("Enter String: ")
word = input("Enter Find Word: ")


print(s.index(word))


# 15 Find the last occurrence of a character.


s = input("Enter String: ")
n = len(s)

for i in range(n-1,0,-1):
    if s[i] != " ":
        print(s[i])
        break




# 16 Count total occurrences of a character.


s = input("Entre String: ")
word = input("Entre Word: ")
count = 0 
for i in s:
    if i == word:
        count+=1


print(count)


# 17 Remove occurrences of a character.

s = input("Entre String: ")
word = input("Entre Word: ")
result = ""
for i in s:
    if i == word:
        pass
    else:
        result = result+i


print(result)



# 18 Replace occurrences of a character.


s = input("Enter String: ")
word = input("Entre Replace Word: ")
word1 = input("Enter Repleased word: ")
result = ""

for i in s:
    if i == word:
        result = result+word1
    else:
        result = result+i

print(result)



# 19 Find the highest frequency character.


s = input("Entre String: ")
s1 = ""
count1 = 0

for i in s:
    count=0
    for j in s:
        if i in j:
            count+=1

    if count>count1:
        s1 = i 

print(s1)


# 20 Find the lowest frequency character.



s = input("Entre String: ")
s1 = ""

count1 = 4

for i in s:
    count = 0 
    for j in s:
        if i == j:
            count+=1

    if count<count1:
        s1 = i
        count1 = count


print(s1)

# 21 Find the first non-repeating character.


s = input("Entre String: ")
s1 = ""

count1 = 4

for i in s:
    count = 0 
    for j in s:
        if i == j:
            count+=1

    if count<count1:
        s1 = i
        count1 = count


print(s1)



# 22 Find the last repeating character.



s = input("Enter String: ")
count2 = 5 
result = ""

for i in s:
    count = 0 
    for j in s:
        if i == j:
            count+=1

    
    if count==1:
        result += i



print(result[-1])



# 23 Print all characters that occur exactly twice.


s = input("Enter String: ")
s1 = []

for i in s:
    count = 0
    for j in s:
        if i == j:
            count+=1

    if count == 2:
        if i not in s1:
            s1.append(i)


print(" ".join(s1))



# 24 Check if all characters in a string are unique.


s = input("Entre String: ")
count = 0


for i in s:
    for j in s:
        if i == j:
            count+=1

if count == len(s):
    print("All Character Is unic ")
else:
    print("NOT Unic")



# 25 Count total words in a string.


s = input("Enter String: ")
count = 0
s1 = ""

for i in s:
    if i == " " and count==0:
        pass
    else:
        s1 = s1 + i
        count = 1

count1 = 0

for j in range(len(s1)):
    if s1[j-1] == " " and s1[j] >= "a" and s1[j] <= "z":
        count1+=1
    
print("Total Count: ",count1+1)




#  Find the first occurrence of a every  word.

s = input("Enter String: ")

s1 = s.split()


for i in s1:
    s2  = i
    for j in range(len(s2)):
        if j == 0:
            print(s2[j],end="")




# 26 Find the first occurrence of a word.

s = input("Enter String: ")
word = input("Enter Word: ")
s1 = s.split()

for i in s1:
    if word == i:
        print(s.index(i[1]))




# 27 Find the last occurrence of a word.


s = input("Enter String: ")
word = input("Enter Word: ")
s1 = s.split()

for i in s1:
    if word == i:
        print(s.index(i[len(word)-1])+1)





# 28 Count occurrences of a word.


s = input("Enter String: ").lower()
word = input("Enter Word: ").lower()
s1 = s.split()
count = 0
for i in s1:
    if word == i:
        count+=1


print(count)




# 29 Remove occurrences of a word.


s = input("Entre String: ")
s1 = s.split()
word = input("Entre Word: ")
result = ""

for i in s1:
    if word == i:
        pass
    else:
        result = result+i+" "
        
print(result)



# 30 Replace a word with another word.


s = input("Entre String: ")
s1 = s.split()
word = input("Entre Word you want to reaplace: ")
word1 = input("Enter New word: ")
result = ""

for i in s1:
    if word == i:
        result = result+word1+" "
    else:
        result = result+i+" "


print(result)



# 31 Remove duplicate words.



s = input("Enter String: ")
s1 = s.split()
result =[]

for i in s1:
    if i not in result:
        result.append(i)

print(" ".join(result))



# 32 Count frequency of each word.


s = input("Enter String: ")
s1 = s.split()
result = []


for i in s1:
    count= 0
    for j in s1:
        if i == j:
            count+=1

    if i not in result:
        result.append(i)
        print(f"{i} : {count}")



# 33 Find the longest word.


s = input("Enter String: ")
s1 = s.split()

count1 = s[0]

for i in s1:
    if len(count1) < len(i):
        count1 = i

print("Longest String is: ",count1)



# 34 Find the shortest word.



s =  input("Enter String: ")
s1 = s.split()

s2 = s1[0]

for i in s1:
    if len(s2) > len(i):
        s2 = i

print("Shortest String: ",s2)



# 35 Find the first palindrome word.


s = input("Enter String: ")
s1 = s.split()



for i in s1:
    s2 = i
    s3 = i[::-1]

    if s2 == s3:
        print(s2)
        break
else:
    print("Not Plindrome")



#  Reverse order of words.



s = input("Enter StirnG: ")
s1 = s.split()
s2 = s1[::-1]
result = ""


for i in s2:
    s3 = i[::-1]
    result = result+s3+" "


print(result)




# 36 Reverse order of words.



s = input("Enter StirnG: ")
s1 = s.split()
print(" ".join(s1[::-1]))



# 37 Reverse each word.



s = input("Entre String: ")
s = s+" "
result = ""
result1 = ""
for i in s:
    if i != " ":
        result1 = result1+i

    else: 
        result = result + result1[::-1] + " "
        result1 = ""


print(result)




# 38 Reverse words without split().


s5 = input("Enter String: ")
s = s5[::-1]



s = s+" "
result = ""
result1 = ""
for i in s:
    if i != " ":
        result1 = result1+i

    else: 
        result = result + result1[::-1] + " "
        result1 = ""


print(result)





# 39 Search all occurrences of a character.

s = input("Enter String: ")
word = input("Enter Word: ")


for i in range(len(s)):
    if s[i] == word:
        print(i,end=",")



# 40 Search all occurrences of a word.


s1 = input("Enter String: ")
s = s1.split()
word = input("Enter Word: ")


for i in range(len(s)):
    if s[i] == word:
        print(i,end=",")


# 41 Check if a string contains a substring (without using contains()).


str = input("Enter: ")
str2 = input("Enter: ")

count = 0
for i in range(0,len(str)):
    for j in range(0,len(str2)):
        if str[i+j] != str2[j]:
            break
        else:
            count+=1

if count==len(str2):
    print("Find THe Substring ")
else:
    print("not Found")




# 42 Check if two strings are equal without using equals().



s = input("Enter First String: ")
s1 = input("Enter Second String: ")


s2 = s.split()
s3 = s1.split()
count = 0 
if len(s2) == len(s3):
    for i in range(len(s2)):    
        for j in range(i,i+1):  
            if s2[i] == s3[j]:  
                count+=1    

if count == len(s2):
    print("Those are same ")
else:
    print("Those are diffresnt")



# 43 Check if two strings are rotations of each other.



s = input("Enter First String: ")
s0 = input("Enter Seconf String: ")

n = len(s)//2
result = ""

for i in range(n,len(s)):
    result = result+s[i]

for j in range(n):
    result = result+s[j]


if result == s0:
    print("Strings are Rotations")
else:
    print("String Are Not Rotation")




# 44 Check if two strings are anagrams.

str = input("Enter: ")
str2 = input("Enter: ")

count=0
if len(str)== len(str2):
    for i in str:
        for k in str2:
            if i == k:
                count+=1
                break

if count== len(str):
    print("ANAGRAM")
else:
    print("Not Anagram")


# 45 Check whether a string starts with or ends with another string.


s = input("Enter String: ")


if s[0] >= "a" and s[0] <= "z":
    match = True
else:
    match = False

if s[len(s)-1] >= "a" and s[len(s)-1] <= "z":
    match1 = True
else:
    match1 = False
    
print(f"Stsrt: {match} , End: {match1}")



# 46 Check if a substring appears at both the start and end.



s = input("Entre String: ")
sub = input("Enter Substring: ")

n = len(sub)



if s[0:n] == sub:
    print("Start in Substring")
else:
    print("Not Start With Substring")
if s[len(s)-n:len(s)] == sub:
    print("End in Substring")
else:
    print("Not End With Substring")




# 47 Check if one string is a substring of another using only concatenation.

s = input("Enter String: ")
s1 = s+s
word = input("Enter Word: ")
count=0
for i in range(0,len(s)):
    for j in range(0,len(word)):
        if s1[i+j] != word[j]:
            break
        else:
            count+=1

if count==len(word):
    print("S1 is substring of S2")
else:
    print("Not Substring")





# 48 Remove all vowels.

s = input("Enter String: ")


for i in s:
    if i not in "aeiouAEIOU":
        print(i,end="")


# 49 Replace all consonants with ''.

s = input("Enter String: ")
result = ""
print('"',end="")
for i in s:
    if i in "aeiouAEIOU":
        print(i,end="")
    
print('"')



# 50 Remove all digits.


s = input("Enter String: ")

for i in s:
    if i >= "0" and i <= "9":
        pass
    else:
        print(i,end="")



# 51 Extract only digits.


s = input("Enter String: ")

for i in s:
    if i >= "0" and i <= "9":
        print(i,end="")



# 52 Remove all special characters.


s = input("Enter String: ")


for i in s:
    if (i >= "a" and i <= "z") or (i >= "0" and i <= "9") or (i >= "A" and i <= "Z") or i ==" ":
        print(i,end="")



# 53 Remove all punctuation characters.



s = input("Enter String: ")


for i in s:
    if i not in (".,?!“”’:"):
        print(i,end="")
        



# 54 Replace all duplicate characters with '$'.


s = input("Enter String: ")
s1 = []

for i in s:
    if i not in s1:
        s1.append(i)
    elif i in s1:
        s1.append("$")


print("".join(s1))



# 55 Reverse only vowels.55 Reverse only vowels.


s = input("Enter String: ")
result = ""
result1 = ""
for i in range(len(s)-1,-1,-1):
    if s[i] in "aeiouAEIOU":
        result += s[i] 


n =0
for j in s:
    if j in "aeiouAEIOU":
        result1 += result[n]
        n+=1
    else:
        result1+=j




print(result1)



# 56 Reverse only consonants.

s = input("Enter String: ")
result = ""
for i in range(len(s)-1,-1,-1):
    if s[i] not in "aeiouAEOIU":
        result +=s[i]

result1 = ""
n=0
for j in s:
    if j in "aeiouAEIOU":
        result1 += j
    else:
        result1 = result1+result[n]
        n+=1 

print(result1)



# 57 Merge two strings alternatively (char by char).



s = input("Enter First String: ")
s1 = input("Enter Second String: ")



for i in range(len(s)):
    print(s[i],end="")
    for j in range(i,i+1):
        print(s1[j],end="")




# 58 Rotate characters by 2 positions to the left.

s = input("Enter String: ")
n = int(input("Enter Number: "))
result = ""
for i in range(n,len(s)):
    result+=s[i]
    if i == len(s)-1:
        for j in range(n):
            result += s[j]

print(result)



# 59 Rotate characters by 3 positions to the right.


s = input("Enter String: ")
n = int(input("Enter Number: "))
result = ""
for i in range(n,len(s)):
    result+=s[i]
    if i == len(s)-1:
        for j in range(n):
            result += s[j]

print(result)




# 60 Append two strings but remove duplicate adjacent characters.
# S1 = "miss", S2 = "issippi"
# "misisipi"


s = input("Enter First String: ")
s1 = input("Enter Second String: ")
s2 = s+s1
result = ""

for i in range(len(s2)):
    if s2[i-1] == s2[i]:
        pass
    else:
        result = result+s2[i]

print(result)




# 61 Count total alphabets, digits, and special characters.


s = input("Enter String: ")
count=0
count1=0
count2=0

for i in s:
    if i >= "a" and i <= "z" or i >= "A" and i <= "Z":
        count +=1
    elif i >= "0" and i <= "9":
        count1+=1
    else:
        count2+=1


print("Alphabets: ",count)
print("Digits: ",count1)
print("Special: ",count2)


# 62 Count vowels and consonants.


s = input("Entre String: ")
count=0
count1=0

for i in s:
    if i in "aeiouAEIOU":
        count+=1
    else:
        count1+=1


print("Vowels: ",count)
print("Consonents: ",count1)



# 63 Count frequency of each character.


s = input("Enter String: ")
l = []

for i in s:
    count=0
    for j in s:
        if i == j:
            count+=1


    if i not in l:
        l.append(i)
        print(i,count)




# 64 Count frequency of each vowel.



s = input("Enter String: ")
l = []

for i in s:
    count=0
    if i in "aeiouAEIOU": 
        for j in s:
            if i == j:
                count+=1
        if i not in l:
            l.append(i)
            print(i,count) 



# 65 Count palindromic substrings.


s = input("Enter String: ")
l =[]
for i in range(len(s)):
    for j in range(i,len(s)):
        n = s[i:j+1]
        l.append(n)

print(l)

for i in l:
    i1 = i[::-1]
    if i == i1:
        print(i)




# 66 Count number of sentences in a paragraph.


s = input("Enter String: ")
count=0

for i in s:
    if i == ".":
        count+=1
    

print("Total Number of Peragraph: ",count)




# 67 Count how many times a substring appears.


s = input("Enter String: ")
s1 = input("Enter SubString: ")
l = []
count=0
for i in range(len(s)):
    for j in range(i,len(s)):
        n = s[i:j+1]
        l.append(n)

if s1 in l:
    count+=1
else:
    print("It Is not Substring")

print(count)




# 68 Count the sum of digits present in a string.


s = input("Enter String: ")
sum =0


for i in s:
    if i >= "0" and i <= "9":
        sum = int(i)+sum


print(sum)




# 69 Count how many times 'life' appears in a string.


s = input("Enter String: ")
s1 = "life"
count2 = 0
for i in range(len(s)):
    count=0

    for j in range(len(s1)):
        if s[i+j] != s1[j]:
            break
        else:
            count+=1
            if count == 4:
                count2 +=1

print(count2)



# 70 Compare the number of times 'the' and 'is' appear.


s = input("Enter String :")
s1 = s.split()
count = 0
count1 = 0

for i in s1:
    if i == "the":
        count+=1
    elif i == "is":
        count1+=1


print("The Appear: ",count)
print("Is Appear: ",count1)




# 71 Print all substrings.


s = input("Enter Stroing :")
l = []
for i in range(len(s)):
    for j in range(i,len(s)):
        n = s[i:j+1]
        l.append(n)


print(l)


# 72 Print all substrings of length n.


s = input("Enter String: ")
n1  = int(input("Enter The Length: "))
l = []

for i in range(len(s)):
    for j in range(i,len(s)):
        n = s[i:j+1]
        l.append(n)


for k in l:
    if len(k) == n1:
        print(k)




# 73 Find the longest palindromic substring.


s  = input("Enter String: ")
l = []


for i in range(len(s)):
    for j in range(i,len(s)):
        n = s[i:j+1]
        l.append(n)

s2 = "a"
for i in l:
    s1 = i[::-1]
    if s1 == i:
        if len(s1) > len(s2):
            s2 = s1


print(s2)



# 74 Find the longest substring without repeating characters.



s = input("Enter String: ")
l = []

for i in range(len(s)):
    for j in range(i,len(s)):
        n = s[i:j+1]
        l.append(n)


s1 = l[0]
for i in l:
    match = 1
    for j in range(len(i)):
        for k in range(j+1,len(i)):
            if i[j] == i[k]:
                match = 0
    if match == 1 and len(s1) < len(i):
        s1 = i

print(s1)
            
    




# 75 Find the longest common prefix among strings.

s = input("Enter String: ")
s1 = s.split()

result = ""
s2 = s1[0]

for i in range(len(s2)):
    flag = 0
    for j in range(1, len(s1)):
        if i >= len(s1[j]) or s1[j][i] != s2[i]:
            flag = 1
            break
    if flag == 1:
        break
    result = result + s2[i]

print(result)



# 75 Find the longest common prefix among strings.

s = input("Enter String: ")
s5 = s.split()
s1 = []
for i in s5:
    n = i[::-1]
    s1.append(n)


result = ""
s2 = s1[0]

for i in range(len(s2)):
    flag = 0
    for j in range(1, len(s1)):
        if i >= len(s1[j]) or s1[j][i] != s2[i]:
            flag = 1
            break
    if flag == 1:
        break
    result = result + s2[i]

print(result[::-1])

# 78 Find the longest mirror-image substring at both ends.

s = input("Enter String: ")
s1 = s[::-1]
result = ""

for i in range(len(s)):
    flag = 1
    for j in range(i,i+1):
        if s[i] != s1[i]:
            flag = 0
            break
        else:
            result += s[i]
            break
    if flag == 0:
        break


print(result)

# 79 Divide a string into n equal parts.



s = input("Enter String: ")
num = int(input("Enter How many part YOu want: "))


n = len(s)//num
n1 = n
l = 0
count = 0
for i in s:
    print(s[l:n1])
    l+=n
    n1+=n
    count+=1
    if count == num:
        break

# 80 Print list items containing all characters of a given word.


s = input("Enter String: ")
l = s.split()
word = input("Enter String: ")

result = ""
for i in range(len(l)):
    count=0
    for j in range(len(word)):
        if word[j] in l[i]:
            count+=1
    if count == len(word):
        result += l[i]+" "


print(result)


# 82 Create a string from a character array.


l = ["h","i","i"]

print("".join(l))




# 83 Create a string from a byte array.


num = int(input("Enter Number: "))
l = []
for i in range(1,num+1):
    n = int(input(f"Enter {i} Number: "))
    if (65 <= n <= 91) or  (n >= 97 and n <= 123):
        l.append(n)
    else:
        print("Wrong Value")
        break

l1 = []
for i in l:
    l1.append(chr(i))

print("".join(l1))



# 84 Print ASCII value of each character.


s = input("Enter String: ")

for i in s:
    print(f"{i} = {ord(i)}")


# 85 Convert string into a char array without built-in functions.


s = "test"

l = []
for i in s:
    l.append(i)

print(l)






# 100 Return true if string contains 'abc' not followed by '.'.


s = "abc."

if "abc" in s and "abc." not in s:
    print(True)
else:
    print(False)



