from stack import *
input="([{"
output=")]}"


s1=stack()
def checkForParantheses(input_string):
    f=0
    for i in input_string:
        #For a char in the input string if its in the "input" then that will be pushed to stack
        if i in input:
            s1.push(i)
        elif i in output:
            #If char is in "output" then the last element from stack is popped and compared with index of input, if it matches then goes for next char or else return false
            if not s1.isStackEmpty():
                if(input.index(s1.pop())==output.index(i)):
                   f=0
                else:
                    f=1
                    break
            else:
                f=1
                break
    if(f==1):
        return False
    else:
        return True

def fileCheck(fileName):
    with open(fileName,'r')as f:
        for line in f:
            assert(checkForParantheses(line)==True)

			
assert(checkForParantheses("(({[[{{}}]]}))")==True)       
assert(checkForParantheses("(({{}]]}))")==False)
fileCheck("hello.txt")

