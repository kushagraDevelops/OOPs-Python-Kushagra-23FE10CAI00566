# 18. Separate the string into comma (,) separated values. X= “ India.is.my.country”
X='India.is.my.country'
tempX=X.split('.')
newX=','.join(tempX)
print(newX)

# 19. Remove a given character from the string Y=”M.A.N.I.P.A.L” 
Y='M.A.N.I.P.A.L'
tempY=Y.split('.')
c=str(input("Enter character to remove: "))
for char in tempY:
    if char==c.upper():
        tempY.remove(char)
newY='.'.join(tempY)
print(newY)

# 20. Remove the (.) dots from the string Y=”M.A.N.I.P.A.L” 
Y='M.A.N.I.P.A.L'
tempY=Y.split('.')
newY=''.join(tempY)
print(newY)

# 21. Sort strings alphabetically in python. 
n=int(input("Enter number of strings: "))
strings=[]
for i in range(n):
    char=str(input(f'Enter string {i+1}: '))
    strings.append(char)
sorted_strings=sorted(strings)
print(sorted_strings)

# 22. Reverse a given string.
string = str(input("Enter String: "))
reversed_string = ''
for char in string:
    reversed_string = char + reversed_string
print(reversed_string)

# 23. Check if string contains only digits.
string = str(input("Enter String: "))
print("The string contains only digits.") if string.isdigit() else print("The string contains characters other than digits.")

# 24. Number of vowels in the string.
string = str(input("Enter String: "))
count=0
for char in string.lower():
    if (char=='a'or char=='e' or char=='i' or char=='o' or char=='u'):
        count+=1
print(count, "vowels")