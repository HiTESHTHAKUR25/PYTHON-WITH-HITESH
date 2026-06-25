# 1.
# Find the Longest Substring Without Repeating Characters
# Cybersecurity Session Tracking System
# 
# A cybersecurity company monitors user session IDs generated during secure login sessions.
# 
# To detect suspicious repeated patterns, the company wants a Python program that finds the longest substring containing no repeated characters.
# 
# Input:
# abcabcbb
# Output:
# abc
# 



s = input("Entre String: ")


s2 = ""

for i in range(len(s)):
    s1 = ""
    for j in range(i, len(s)):
        if s[j] not in s1:
            s1 = s1 + s[j]
        else:
            break

    if len(s1) > len(s2):
        s2 = s1
        
        
print(s2)














# 2.
# Find the Most Frequently Occurring Word
# News Channel Keyword Analyzer

# A news agency analyzes breaking news headlines to identify the most repeated keyword in a report.

# Write a Python program to find the word with the highest frequency.

# Input:
# india won the match and india created history
# Output:
# india



s = input("Enter String: ")
s1 = s.split()
result = []

for i in s1:
    count = 0
    for j in s1:
        if i == j:
            count+=1
    if count>= 2:
        if i not in result:
            result.append(i)

n = len(result)-1
print(result[n])
            



            