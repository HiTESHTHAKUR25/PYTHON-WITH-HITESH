# 1.  Bank Customer Account Privacy System

# A national bank is developing a secure customer portal where account
# numbers should not be displayed completely on the screen. For security
# reasons, the system should hide all digits except the last four digits
# before showing them to users.

# Conditions: - Display only the last 4 digits - Replace all previous
# characters with *

# Input: Enter account number: 123456789012

# Output: Masked Account: ********9012



s = input("Enter Account Number: ")

if len(s)==12:
    print(f"Masked Account: ********{int(s)%10000}")
else:
    print("Wrong Account Number")



# 2.  Corporate Employee Short ID Generator

# A multinational company wants to automatically generate short IDs for
# employees while creating official email accounts. The system should take
# the employee’s full name and create an ID using the first character of
# each word.

# Conditions: - Take first character of every word - Convert all
# characters to uppercase

# Input: Enter employee name: ajay singh thakur

# Output: Employee Short ID: AST

s = input("Enter String: ")

s1 = s.split()
result = ""


for i in range(0,len(s1)):
    s2 = s1[i]
    for j in s2:
        if j >= "a" and j <= "z":
            upper = ord(j)-32
            result = result+chr(upper)
            break


print(result)





# 3.  Smart Chat Message Cleaner

# A social media company noticed that users often enter messages with
# unnecessary spaces. To improve readability and storage efficiency, the
# system should remove extra spaces and keep only a single space between
# words.

# Input: Enter message: Java is easy

# Output: Cleaned Message: Java is easy


s = input("Enter String: ")
s2 = s.split()
s3 = ""
for i in range(0,len(s2)):
    s3 = s3+s2[i]+" "

print(s3)





# 4.  Instant Messaging Word Encryption System

# A messaging application wants to temporarily encrypt messages during
# transmission. The encryption rule is to reverse every word individually
# while keeping the word positions unchanged.

# Input: Enter message: java is powerful

# Output: Encrypted Message: avaj si lufrewop



s = input("Enter String: ")

result = ""
rev = ""

for i in s:
    if i == " " :
        result = result+rev[::-1]+" "
        rev = ""
    else:
        rev = rev+i



print(result+rev[::-1])



# 5. Website URL Verification System

# A software company is developing an automated website registration
# portal. Before saving a website address, the system must verify whether
# the URL follows the required company format.

# Conditions: - Must start with www - Must end with .com

# Input: Enter website: www.amazon.com

# Output: Valid Website


s = input("Enter String: ")
count=0

if s[0:4] == "www.":
    count+=1
if s[len(s)-4:len(s)+1]==".com":
    count+=1

if count==2:
    print("Valid Website")
else:
    print("Invalid Website")




# QNO 7:
#  Advanced Smart Chat Compression Expansion System

# A messaging application stores repeated characters in compressed form to
# reduce storage space. Before displaying messages to users, the system
# should reconstruct the original message.

# The application team has introduced additional rules.

# Conditions: - Alphabet followed by number - Repeat character according
# to the number - If alphabet is uppercase convert expanded characters
# into lowercase - Ignore special symbols - Display expanded string -
# Display total character count

# Test Case 1 Input: Enter compressed message: a3

# Output: Expanded Message: aaa

# Total Characters: 3

# Test Case 2 Input: Enter compressed message: A4b5

# Output: Expanded Message: aaaabbbbb

# Total Characters: 9

# Test Case 3 Input: Enter compressed message: x2Y3

# Output: Expanded Message: xxyyy

# Total Characters: 5

# Test Case 4 Input: Enter compressed message: m5@n2P4

# Output: Expanded Message: mmmmmnnpppp

# Total Characters: 11

# Test Case 5 Input: Enter compressed message: R3S2t5

# Output: Expanded Message: rrrssttttt

# Total Characters: 10




s = input("Enter Value: ").lower()

result = ""
count=0

for i in s:
    if i >= "a" and i <= "z":
        result = result+i
        previous = i
    elif i >= "0" and i <= "9":
        count = count+int(i)
        result = result+previous*(int(i)-1)
    else:
        pass








print("Expanded Message: ",result)
print("Total Characters: ",count)


while True:
    print('''
1. Reverse Complete String
2. Reverse Every Word
3. Reverse Word Order
4. Exit
''')

    choice = int(input("Choose A Number: "))

    # ========================= CASE 1 =========================
    if choice == 1:
        s = input("Enter String: ")
        
        # Step 1: Extract only characters (ignore special)
        letters = []
        for ch in s:
            if ch.isalnum():
                letters.append(ch)

        # Step 2: Reverse manually
        rev_letters = []
        i = len(letters) - 1
        while i >= 0:
            rev_letters.append(letters[i])
            i -= 1

        # Step 3: Put back special characters
        result = ""
        j = 0
        for ch in s:
            if ch.isalnum():
                result += rev_letters[j]
                j += 1
            else:
                result += ch

        print(result)

    # ========================= CASE 2 =========================
    elif choice == 2:
        s = input("Enter String: ")
        words = s.split()
        result = ""

        for word in words:
            has_digit = False

            # Check digit
            for ch in word:
                if ch >= '0' and ch <= '9':
                    has_digit = True
                    break

            if has_digit:
                result += word + " "
            else:
                # Reverse manually
                rev = ""
                i = len(word) - 1
                while i >= 0:
                    rev += word[i]
                    i -= 1

                # Capitalize first letter
                first = chr(ord(rev[0]) - 32)
                rev = first + rev[1:]

                result += rev + " "

        print(result.strip())

    # ========================= CASE 3 =========================
    elif choice == 3:
        s = input("Enter String: ")
        words = s.split()

        result = []
        seen = []

        # Traverse from end (reverse order)
        i = len(words) - 1
        while i >= 0:
            word = words[i]
            lower = word.lower()

            if lower not in seen:
                seen.append(lower)
                result.append(word)

            i -= 1

        print(" ".join(result))

    # ========================= EXIT =========================
    elif choice == 4:
        print("Program Closed Successfully")
        break

    else:
        print("Invalid Choice")



        