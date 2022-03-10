from q2 import *
from q3 import *
# Tests:
if __name__ == '__main__':
#-------------q2------------------
    print(f1(2))
    print(f1(2))
    print(f1(2))
    print(f1(3))
    print(f1(3))

    print(f2(2))
    print(f2(2))
    print(f2(3))
    print(f2(3))

    print(sort([3,8,6,9,1]))
    print(sort([3,8,6,9,1]))
    print(sort(['t','e','h','i','l','a']))
    print(sort(['t','e','h','i','l','a']))

#output shuld be:
#f1
#4
#I already told you that the answer is 4
#I already told you that the answer is 4
#9
#I already told you that the answer is 9

#f2
#4
#I already told you that the answer is 4
#5
#I already told you that the answer is 5

#sort int
#[1, 3, 6, 8, 9]
#I already told you that the answer is [1, 3, 6, 8, 9]

#sort string
#['a', 'e', 'h', 'i', 'l', 't']
#I already told you that the answer is ['a', 'e', 'h', 'i', 'l', 't']



#-----------------------q3-------------------------------
lst = List([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
])
# prints 1
print(lst[0,0,0])
# prints 11
print(lst[1,1,1])
# prints 5
print(lst[0,1,1])
lst[0,0,0] = 10
#[[[10, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
print(lst)
#[[[10, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], 50]
lst.append(50)
print(lst)
lst.reverse()
#[50, [[7, 8, 9], [10, 11, 12]], [[10, 2, 3], [4, 5, 6]]]
print(lst)