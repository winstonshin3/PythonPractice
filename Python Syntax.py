# Multiple Assignments
n, m = 0, "abc"

n, m, z = 0.125, "abc", False

# Increment
n = n + 1   #good
n += 1      #good
#n++        #bad

# If statements don't need parentheses
n = 1
if n > 2:
    n -= 1
elif n == 2:
    n *= 2
else:
    n += 2

# Parentheses needed for multi-line conditions.
# and = &&
# or = ||
n, m = 1, 2
if ((n > 2 and n != m) or n == m):
    n += 1

# While loops are similar
n = 0
while n < 5:
    print(n)
    n += 1
print(n)

# For loops
for i in range(5):
    print(i)

for i in range(1, 6, 2):
    print(i)

# Division is decimal by default
print(5/2)
# Double slash rounds down
print(5//2)
# CAREFUL: most languages round towards 0 by default so negative numbers will round down
print(-3//2)
# A workaround for rounding towards zero is to use decimal division and then convert to int.
print(int(-3/2))

# Modding is similar to most languages
print(10%3)
# Except for negative values
print(-10%3)
# To be consistent with other languages modulo
import math
print(math.fmod(-10,3))
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infimite so they never overflow
print(math.pow(2,200))

# Arrays
arr = [1, 2, 3]
print(arr)

# Can be used as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)
arr.insert(1,7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

# Initialize arr of size n with default value of 1 for each element
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# Careful: -1 is not out of bounds. It's the last value.
arr = [1, 2, 3]
print(arr[-1])

# Sublists (aka slicing)
arr = [1, 2, 3, 4]
print(arr[1:3]) # prints[2,3]

# Loop through arrays
nums = ["a", "b", "c"]
# Using index
for i in range(len(nums)):
    print(nums[i])
# Without using index
for i in nums:
    print(i)
# With index and value
for i, n in enumerate(nums):
    print(i, n)
# Loop through multiple arrays simultaneously with unpacking
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
# Reverse
nums = [1, 2, 3]
nums.reverse()
# Sorting
arr = [5, 3, 2, 1]
arr.sort()
# Custom sort
arr = ["bob", "sue", "alice"]
arr.sort(key=lambda x: len(x))
print(arr)

# List Comprehension
arr = [i for i in range(5)]
print(arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
arr = [[0] * 4] * 4 # This doesn't work as four arrays all reference the same array

# Strings are similar to arrays, but they are immutable
s = "abc"
print(s[0:2])
s += "def"
print(s)

# Valid numeric strings can be converted.
print(int("123") + int("123"))
print(str(123) + str(123))

# Combine a list of strings (with an empty string delimitor)
strings = ["ab", "cd", "ef"]
print("".join(strings))

# Queues
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()
print(queue)

queue.appendleft(1)
queue.pop()
print(queue)

# HashSet
mySet = set()

mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

# List to set
print(set([1,2,3]))

# Set comprehension
mySet = { i for i in range(5)}
print(mySet)

# HashMap (aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
myMap["bob"] = 77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)
myMap.pop("alice")
print("alice" in myMap)

myMap = {"alice": 90, "bob": 70}

# Dict comprehension
myMap { i: 2*i for i in range(3)}

# Looping through maps
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key,val)

# Tuples
tup = (1,2,3)
print()
# CAn be used as key for hash map/set
myMap = { (1,2) : 3}
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# Lists can't be keys
myMap[[3,4]] = 5

# Heaps
import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by default, work around is to use min heap and multiply by -1 when push & pop.

# Build heap from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr) # This is in constant time

# Functions
def myFunc(n, m):
    return n *m

print(myFunc(3,4))

# Nested function have access to outer variables
def outer(a, b):
    c = "c"
    def inner():
        return a + b + c
    return inner()
print(outer("a", "b"))

# One thing about nested functions is that is can
# modify objects but not reassign unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        # will only modify val in the helper scope
        # val *= 2
        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)

nums = [1, 2]
val = 3
double(nums, val)


class MyClass:
    # Constructor
    # self is kinda like "this" in other languages
    # the following constructor seems to take in an array as a parameter
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)

    # self key word required as param
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2 * self.getLength()