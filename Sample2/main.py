from method import *


assert(largestNumber([2,3,1,5,3,7,4])==7)
assert(secondLargestNumber([2,3,1,5,3,7,4])==5)
assert(evenOdd([2,3,1,5,3,7,4])==([2,4],[3,1,5,3,7]))
assert(ifListSSame([1,2,4,3,4],[1,2,3,4])==True)
assert(union([1,2,3],[3,1,4,5])==[1,1,2,3,3,4,5])
assert(intersection([1,2,3],[3,1,4,5])==[1,3])
assert(UnionInterSection([1,2,3],[3,1,4,5])==({1,2,3,4,5},{1,3}))
assert(squareNumberTuples(5)==[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)])
assert(removeDuplicates([1,2,4,2,1,3,5])==([4,2,1,3,5]))
assert(findLongestLenghtWord(["Nidhi","Nidhi S","Nidhi S Rao"])==11)

assert(addKeyValue({"n":"nidhi",1:"a"},"k","kite")==({"n":"nidhi",1:"a","k":"kite"}))
assert(concatDict({1:1,2:4},{3:9})==({1:1,2:4,3:9}))
assert(ifKeyExists({1:1,2:4,3:9},2)==True)
assert(dictionaryOfSquare(4)==({1:1,2:4,3:9,4:16}))
assert(sumValues({1:1,2:4,3:9})==14)
assert(multiplyValues({1:1,2:4,3:9})==36)
assert(removeKey({1:1,2:4,3:9},2)==({1:1,3:9}))
assert(is_empty({})==True)
assert((makeDict([(1,1),(2,4)]))==({1:1,2:4}))
