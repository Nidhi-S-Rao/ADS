def bubbleSort(input):
	for i in range(len(input)-1):
		for j in range(len(input)-1,i,-1):
			if(input[j]<input[j-1]):
				input[j],input[j-1]=input[j-1],input[j]
	return input
	
	
print(bubbleSort([2,1,4,3,7,5,9,8]))



def selectionSort(a):
	for i in range(len(a)-1):
		pos=i
		for j in range(i+1,len(a)):
			if(a[j]<a[pos]):
				pos=j
		a[i],a[pos]=a[pos],a[i]
	return a
	
	
print(selectionSort([2,1,4,3,7,5,9,8]))


def insertionSort(a):
	for i in range(1,len(a)):
		j=i-1
		key=a[i]
		while(j>=0 and key<a[j]):
			a[j+1]=a[j]
			j-=1
		a[j+1]=key
	return a
	
	
print(insertionSort([2,1,4,3,7,5,9,8]))



def mergeSort(a):
	if len(a)==0 or len(a)==1:
		return a
	else:
		mid=len(a)//2
		m=mergeSort(a[:mid])
		n=mergeSort(a[mid:])
		return merge(m,n)
		
def merge(m,n):
	t=[]
	k=len(m)
	l=len(n)
	i=0
	j=0
	while k>0 and l>0:
		if(m[i]<n[j]):
			t.append(m[i])
			i+=1
			k=k-1
		else:
			t.append(n[j])
			j+=1
			l=l-1
	if(k==0):
		t=t+n
	else:
		t=t+m
	return t
				
print(mergeSort([2,1,4,3,7,5,9,8]))	


def mergeSortPop(a):
	if len(a)==0 or len(a)==1:
		return a
	else:
		mid=len(a)//2
		m=mergeSort(a[:mid])
		n=mergeSort(a[mid:])
		return merge(m,n)
		
def mergePop(m,n):
	while len(m)>0 and len(n)>0:
		if(m[i]<n[j]):
			t.append(m[i])
			m.pop(0)
		else:
			t.append(n[j])
			n.pop(0)
	if(len(m)==0):
		t=t+n
	else:
		t=t+m
	return t
				
print(mergeSort([2,1,4,3,7,5,9,8]))	



def quickSort(input):

    start=0

    end=len(input)-1

    _quickSort_(input,start,end)

    return input

def _quickSort_(input,start,end):

    if start<end:  

        mid=_partition_(input,start,end)

        _quickSort_(input,start,mid-1)

        _quickSort_(input,mid+1,end)

def _partition_(input,start,end):

    up=start

    down=end

    pivot=input[start]

    while up<=down:

        while up<=down and input[up]<=pivot:

            up+=1

        while up<=down and input[down]>pivot:

            down-=1
        if(up<=down):
            input[up],input[down]=input[down],input[up]

    input[start],input[down]=input[down],input[start]

    return down

print(quickSort([2,1,4,3,7,5,9,8]))
 




