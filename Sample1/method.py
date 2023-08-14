import random

#Swapping 2 numbers without temp
def swap(a,b):
  c=a+b
  b=c-b
  a=c-b
  return a,b


#Check if the number is positive or negative
def check(a):
  if(a<0):
    return 'Negative number'
  elif(a>0):
   return 'Positive number'
  else:
    return 'Entered number is zero'

#Program to print all numbers in a range divisible by given number
def checkDivisor(n,k):
  a=[]
  for i in range(1,n+1):
    if(i%k==0):
      a.append(i)
  return a

#Program to get quotient and reminder of 2 numbers
def Divide(a,b):
	q=a/b
	r=a%b
	return q,r


#Program to print odd numbers
def oddNumbers(n):
	a=[]
	for i in range(n+1):
		if(i%2!=0):
			a.append(i)
	
	return a

#Program to find sum of digits in a number
def sumOfDegits(n):
	sum=0
	while(int(n)>0):
		sum=sum+n%10
		n=int(n/10)
	return sum

#Program to find smallest divisor of a number
def findSmallestDivisor(n):
	for i in range(2,n):
		if(n%i==0):
			return i
			


#Program to read a number n and then find sum of n+nn+nnn+...
def sumOfSeries(n,k):
	sum=0
	digit=n
	while(k>0):
		sum=sum+n
		n=n*10+digit
		k=k-1
	return sum

#Reverse a number
def reverse(n):
	reverse=0
	while(int(n)>0):
		reverse=reverse*10+n%10
		n=int(n/10)
	return reverse

#Average of numbers in a list
def average(a):
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]
		average=sum/len(a)
	return average

#Count the number of digits in a number
def count(n):
	c=0
	while(int(n)>0):
		c=c+1
		#print(c)
		n=int(n/10)
	return c

#Program to check if number is palindrome
def palindrome(n):
	number=n
	reverse=0
	while(n>0):
		reverse=reverse*10+n%10
		n=int(n/10)
	return (reverse==number)

#Program to check the occurrences of the sub string present int he given string
def ifSubStringFound(a,b):
	c=0
	for i in range(len(a)):
		if(a[i:i+len(b)]==b):
			c=c+1
	return c

#Program to findout the lowest index once the string is found
def indexSubStringFound(a,b):
	for i in range(len(a)-len(b)+1):
		if(a[i:i+len(b)]==b):
			break
	return i

#Program to return false if other than character present
def checkForCharacters(a):
	for i in range(len(a)):
		f=0
		if(96<ord(a[i])<123 or 64<ord(a[i])<92):
			f=0
		else:
			f=1
			break
	if(f==1):
		return False
	else:
		return True
			
		
#Program to replace a with $
def replace(a):
	a_list=list(a)
	for i in range(len(a_list)):
		if(a_list[i]=='a'):
			a_list[i]='$'
	return ''.join(a_list)

#Program to count the number of vowels
def countVowels(n):
	c=0
	for i in range(len(n)):
		if(n[i] in ['a','e','i','o','u','A','E','I','O','U']):
			c+=1
	return c

#Program to replace blank space with a '-'

def replaceBlankSpace(a):
	a_list=list(a)
	for i in range(len(a_list)):
		if(a_list[i]==' '):
			a_list[i]='-'
	return ''.join(a_list)

#Program to find length of string
def findLength(a):
	if(a==''):
		return 0
	else:
		return 1+findLength(a[1:])
	
#Program to find larger string
def findLargerString(a,b):
	n=findLength(a)
	m=findLength(b)
	if(n>m):
		return a
	elif(m>n):
		return b
	else:
		return "Equal"

#Program to count upper case and lower case letters
def countOfUpperLower(a):
	u=0
	l=0
	for i in range(len(a)):
		if(64<ord(a[i])<91):
			u+=1
		elif(96<ord(a[i])<123):
			l+=1
		else:
			"Nothing"
	return u,l

#Program to count characters and digits in a string
def checkDigitORLetter(b):
	if(64<ord(b)<91 or 96<ord(b)<123):
		return True
	else:
		return False
def countCharsDigits(a):
	c=0
	d=0
	for i in range(len(a)):
		if(checkDigitORLetter(a[i])):
			c+=1
		else:
			d+=1
	return c,d


#Program to find if full pattern is present in a string
def fullPattern(a,b):
	if(b in a):
		return True
	else:
		return False
	

#Program to find cumulative sum of list
def cumulative_Sum(a):
	b=[]
	sum=0
	for i in range(len(a)):
		sum=sum+a[i]
		b.append(sum)
	return b

#Program to generate 10 random numbers
def tenRandomNumbers():
	a=[]
	for i in range(10):
		a.append(random.random())
	return a


#Program to generate random numbers between 1 and 20
def tenRandomNumbersRange():
	a=[]
	for i in range(10):
		a.append(random.randint(1,20))
	return a

#Program to generate 5 unique random numbers in a range
def uniqueRandomNumbers():
	a=set()
	for i in range(6):
		a.add(random.randint(1,20))
	return a

#Program to get 10 random numbers between 1 to 100 with condition
a=[]
def randomNumbers():
	n=1
	while(n<101):
		a.append(random.randint(n,n+10))
		n=n+10
	return a

	
