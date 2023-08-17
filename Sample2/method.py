#Program to sort elements
def sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if(a[i]<a[j]):
                t=a[i]
                a[i]=a[j]
                a[j]=t
    return a

#Program to Find the Largest Number in a List
def largestNumber(a):
    b=sort(a)
    return b[-1]

#Program to find second largest number
def secondLargestNumber(a):
    b=sort(a)
    return b[-2]

#Program to separate even odd numbers
def evenOdd(a):
    even=[]
    odd=[]
    for i in range(len(a)):
        if(a[i]%2==0):
            even.append(a[i])
        else:
            odd.append(a[i])
    return even,odd

#Program to check if 2 lists are same
def ifListSSame(a,b):
    f=0
    for i in a:
        if i in b:
            f=1
    if(f==1):
        return True
    else:
        return False
    
#Program to find union of 2 list
def union(a,b):
    c=[]
    for i in a:
        c.append(i)
    for i in b:
        c.append(i)
    return sort(c)

#Program to find intersection of 2 list
def intersection(a,b):
    c=[]
    for i in a:
        if i in b:
            c.append(i)
    return c

#Program to find union and intersection without repetition
def UnionInterSection(a,b):
    unionList=set(union(a,b))
    intersectionList=set(intersection(a,b))
    return unionList, intersectionList


#Program to create list of 2 tuples 1st number and the square of the number
def squareNumberTuples(n):
    a=[]
    for i in range(1,n+1):
        a.append((i,i**2))
    return a


#Program to remove duplicates from list
def removeDuplicates(a):
    index = 0
    while index < len(a):
        element = a[index]
        if a.count(element) > 1:
            a.remove(element)
        else:
            index += 1
    return a


#Program to find the longest lenght word in a list and return the length
def findLongestLenghtWord(word_list):
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

#Program to add key value pair to dictionary
def addKeyValue(dictionary, key, value):
    dictionary[key] = value
    return dictionary

#Program to concatenate 2 dictionaries
def concatDict(dict1, dict2):
    concatenated_dict = {**dict1, **dict2}
    return concatenated_dict

#Program to check if key exists in dictionary
def ifKeyExists(dict,key):
    if key in dict:
        return True
    else:
        False

#Program to generate dictionary in i, i^2 format
def dictionaryOfSquare(n):
    dict={}
    for i in range(1,n+1):
        dict[i]=i**2
    return dict

#Program to sum all values in a dictionary
def sumValues(dict):
    total = sum(dict.values())
    return total

#Program to multiply all values
def multiplyValues(dict):
    product = 1
    for value in dict.values():
        product *= value
    return product

#Program to remove a key
def removeKey(dict, key):
    if key in dict:
        del dict[key]
    return dict
    
#Program to check if dictionary is empty
def is_empty(my_dict):
    return not bool(my_dict)

#Program to create dictionary from tuples
def makeDict(tuple):
    dict = {}
    for key, value in tuple:
        dict[key] = value
    return dict