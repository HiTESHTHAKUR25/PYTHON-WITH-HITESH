'''2.
Digit Threshold Break Analyzer

A monitoring system analyzes numeric IDs to detect high-value digits. 
The system keeps adding digits one by one, but stops processing as soon as the running sum exceeds a given threshold.

Write a program to:

Accept a number and a threshold value
Traverse digits from right to left
Keep adding digits to a running sum
Display each digit added
The moment sum exceeds the threshold, stop using break
Display:
- Digits processed
- Final sum
- Count of digits processed
If threshold is never exceeded, print Threshold Not Reached

Use loops and break wherever required.

Input:
57294
Threshold = 10

Output:
Digits Processed: 4 9
Sum = 13
Count = 2
Threshold Exceeded

Input:
1234
Threshold = 15

Output:
Digits Processed: 4 3 2 1
Sum = 10
Count = 4
Threshold Not Reached
'''


num = int(input("Enter Numbre: "))
thres = int(input("Enttre THreshold: "))

count = 0
sum = 0
print("Digit Processed: ",end=" ") 
while num>0:
	num1 = num%10
	sum = sum+num1
	if thres<=sum:
		print("\nThreshold Exceeded")
		sum = sum-num1
		break
	
	print(num1,end=" ")
	count+=1
	num = num//10
else:
	print("\nThreshold Not Reached")
	

print("Sum: ",sum)
print("Count: ",count)




