# 1. Remove All Special Characters from a String

# Online Banking Customer Data Cleaning System

# A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

# Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

# * Alphabets
# * Numbers
# * Spaces

# The cleaned value should be stored back into the original string variable.

# Input:

# Deepika@@ Padukone!! 123
# Output:
# Deepika Padukone 123
# Input:
# Ajay###Singh$$$
# Output:
# AjaySingh

s = input("Entre String: ")

for i in s:
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z") or (i == " ") or (i <= "9" and i >="0"):
        print(i,end="")




# 2. Reverse Sentence + Reverse Each Word

# Secret Military Communication Decoder
# A defense organization stores highly confidential messages in encrypted form.
# To decode the message:

# 1. Reverse the entire sentence.
# 2. Reverse every individual word.
# 3. Store the final result back into the original string variable.

# You must use the split() method.
# Input:

# ```
# Python is powerful
# ```

# Output:

# ```
# lufrewop si nohtyP


s = input("Enter String: ")
s1 = s.split()
result = ""

for i in range(len(s1)-1,-1,-1):
    s2 = s1[i]
    result = result+s2[::-1]+" "


print(result)




# 3. Find the First Non-Repeated Character

# Railway Ticket Fraud Detection System

# The railway department generates ticket reference IDs automatically.

# Sometimes, due to technical issues, many characters get repeated inside the ticket ID.

# The department wants a Python program that finds the first character that appears only once in the string.

# Example 1

# Input:
# aabbccddefg
# Output:

# ```
# e
# ```

s = input("Enter String: ")


for i in s:
    count=0
    for j in s:
        if i in j:
            count+=1
    if count==1:
        print("Output: ",i)
        break



# 4. Program should work for both uppercase and lowercase letters.

#  Find the Shortest Word in a Sentence

# Telecom SMS Cost Optimization System

# A telecom company charges customers based on the length of words used in bulk SMS campaigns.

# The company wants to identify the shortest word in every message for analytics purposes.

# Write a Python program to find the shortest word from a given sentence.

# Input:

# ```
# Python is very easy to learn
# ```

# Output:

# ```
# is
# ```

s = input("Entre String: ")
s1 = s.split()

s2 = s1[0]

for i in range(1,len(s1)):
    if len(s2) > len(s1[i]):
        s2 = s1[i]

print(s2)






# 5. Find the Number of Unique Characters in a String

# Password Strength Analyzer

# A cybersecurity company checks password strength based on the number of unique characters present.

# Passwords containing more unique characters are considered more secure.

# Write a Python program to count the number of unique characters in a string.

# Input:

# ```
# aabbccdde
# ```

# Output:

# ```
5


s = input()
count = 1
first = s[0]
for i in range (1 , len(s)):
    if first == s[i]:
        first = s[i]
    else:
        count+=1
        first = s[i]
print(count)




# 6. Find Occurrence of a Word in a String

# Product Review Analysis System

# An e-commerce company wants to analyze customer reviews.

# The company wants a Python program to count how many times a particular word appears in a review.

# Input Sentence:

# ```
# iphone is good and iphone battery is strong
# ```

# Word:

# ```
# iphone
# ```

# Output:

# ```
# 2
# ```



s = input("Entre String: ")
s1 = input("Entre Find String: ")
s2 = s.split()
count=0

for i in s2:
    if i == s1:
        count+=1

print(count)





# 7. Remove Duplicate Words from a String

# Voice Assistant Noise Correction System

# A voice assistant records spoken commands from users.

# Due to microphone disturbance and network lag, some words are repeated multiple times.

# The company wants a Python program that removes duplicate words while maintaining the original order.

# ``
# hello hello how are are you
# ```

# Output:

# ```
# hello how are you
# ```


s = input("Entre String: ")
s1 = s.split()
result = []


for i in s1:
    if i not in result:
        result.append(i)




print(" ".join(result))


# 8.
# Find the Second Highest Repeating Character in a String

# Social Media Trend Analysis System

# A social media company analyzes hashtags and user comments to identify trending character patterns.

# The analytics team wants a Python program to find the character with the second highest frequency in a given string.

# This helps detect secondary trending patterns in user activity.

# Input:

# aaabbbbccddeee

# Output:

# e

# Explanation:

# b occurs 4 times → highest
# e occurs 3 times → second highest

# Condition:

# Program should work for both uppercase and lowercase letters.
# Spaces should be ignored.
# If no second highest frequency exists, print:
# Second highest repeating character not found


s = input("Enter String: ")


s = s.replace(" ", "")

max1 = 0
max2 = 0
char1 = ""
char2 = ""

i = 0
while i < len(s):

    if s[i] not in s[:i]:

        count = 0
        j = 0

        while j < len(s):
            if s[i] == s[j]:
                count += 1
            j += 1

        if count > max1:
            max2 = max1
            char2 = char1
            max1 = count
            char1 = s[i]

        elif count > max2 and count < max1:
            max2 = count
            char2 = s[i]

    i += 1


if max2 == 0:
    print("Second highest repeating character not found")
else:
    print(char2)