from stack import *
def reverse(file):
    s1=stack()
    with open(file,'r')as input_file:
        for line in input_file:
            s1.push(line)
    input_file.close()
    with open(file,'w') as output_file:
        while not s1.isStackEmpty():
            output_file.write(s1.pop())
    output_file.close()

reverse('sample.txt')