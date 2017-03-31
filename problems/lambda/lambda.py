def make_incrementor (n): return lambda x: x + n
f = make_incrementor(2)
g = make_incrementor(6)
print f(42), g(42)
#44 48
print make_incrementor(22)(33)
#55

#python collections:

from collections import OrderedDict, deque
#show example on ipython
stack = [1,2,3,4,5]

queue = deque([1,2,3,4,5])
queue.popleft()

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
list3 = list1 + list2
#or
list1.extend(list2)
list1.append(list2) #will append 2nd list as an element of 1st list


#Some useful functions and libraries:

from ast import literal_eval
from datetime import datetime
from collections import OrderedDict

#remove duplicates
list1 = list(set(list1))

li.sort()
#Ordering a dict by key: or use OrderedDict directly
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

#Ordering a dict by value:
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

#Common useful functions:
max()
min()
len()
for key ,val in dict1.iteritems()
range and xrange
#list of even nos in range of [0,50)
list1 = [x for x in range(50) if x%2==0]
#using counter
for n, val in enumerate(list1):
    print n, val

##map1
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

##map2
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

##filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

##reduce
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

##File handling
f = open("abc.txt","r")
f.close()

with open("abc.txt","r") as f:
    #foo baar
