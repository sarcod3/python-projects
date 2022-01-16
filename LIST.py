L = [1, 2, 6]
M = [6, 1, 2, 3]
O = [13, 6, 1, 2, 3]
t = 0
for i in range(len(L)):
    t


'''
l = [3, 1, 4]
m = [1, 5, 9]
t = []
for i  in range(len(l)):
    t.append(l[i]+m[i])
print(t)

from random import randint

l = []
l = l + [randint(1, 100)]
l.sort()
print(l * 50)

print('-------------')
from random import randint

l = []
for i in range(50):
    l.append(randint(1, 100))
l.sort()
print(l)

input()
l = [100, 400, 500, 600, 1200, 800]
del (l[1])
print(l)
input()
l = [100, 400, 500, 600, 1200, 800]
x = l.pop(2)
print(x)
print(l)
input()

l = [100, 400, 500, 600, 1200, 800]
l.insert(4, 900)
print(l)
input()
l = [100, 400, 500, 600, 1200, 800]
print(l[-3:])
print(l * 5)
l[2] = 100
print(l)
print(l.count(100))
input()
score = [45, 90, 66, 23, 56, 87, 42]
score.sort()
print(score)
print(score[-2:])
print(score[0:2])
print('two largest', score[-1], 'and', score[-2])
print('two lowest ', score[0], 'and', score[1])
print('-----------')
score_list = []
for i in range(len(score)):
    if score[i] > 50:
        score_list.append(score[i])
print(score_list)
input()
a = 10
b = 15
c = 20
numlist = []
numlist.append(a)
numlist.append(b)
numlist.append(c)
print(numlist)
# append() adds to the end of the list
# sort() sorts the list alphabetically
# count(x) count how many times x occure in the list
# index(x) returns th first occurence of x in the list
# remove() reverses the list
# remove(x) it removes first occurence of x in the list
# insert(x,p) it inputes a value p after x in the list
# pop(x) removes the item at the specified index but if index not specified it removes the last item in the list
input()
l = ['taiwo', 'kehinde']
t = l[:], 'this copies the items in l'
print(t)
input()
print(min([2, 5, 7]))
input()
print(min([2, 5, 7]))
input()
print(sum([2, 5, 7]))
input()
m = 70, 41, 22, 90, 57
print(list(m)), 'this puts the item in a list'
input()
m = 70, 41, 22, 90, 57
print(sum(m)), 'this outputs the sum of th items in the list'
input()
m = 70, 41, 22, 90, 57
print(max(m)), 'this output the highest number in the list'
input()

m = 70, 41, 22, 90, 57
print(min(m)), 'this output the lowest number in the list'
input()
m = 70, 41, 22, 90, 57
print(len(m))

input()
cars = ['benz', 'acura', 'range', 'toyota']
for i in range(len(cars)):
    if 'e' in cars[i]:
        print(cars[i])
print('------------')
for item in cars:
    if 'e' in item:
        print(item)
print('------------')
M = [70, 41, 22, 90, 57]
count = 0
for i in range(len(M)):
    if M[i] > 50:
        count = +1
print(count)
print('------------')

M = [1, 9, 4, 5]
for i in range(len(M)):
    M[i] = M[i] ** 2
print(M)
print('------------')

M = [1, 9, 4, 5]
for item in M:
    print(item)
print('------------')
M = [1, 9, 4, 5]
for i in range(len(M)):
    print(M[i])
print('------------')

M = [1, 9, 4, 5]
for i in range(len(M)):
    if M[i] == 9:
        print(i)
print('------------')

'ADDITION ADDS ONE LIST TO THE END OF ANOTHER AND MULTIPLICATION REPEATS VALUES OF LIST'
print([7, 8] + ['abc'] + [3, 4, 4])
print([7, 8] * 3)
print([0] * 5)
print('------------')

'slicing allows you to carry a certain amount of value'
L = [6, 7, 8, 9]
print(L[0])
print(L[:3])
print(L.index(8))
print(L.count(6))
input()

L = [1, 2, 3]
if 2 in L:
    print('your list contains the number 2.')
if 0 not in L:
    print('your list has no zeroes.')
input()

L = [1, 2.718, 'abc', [5, 6, 7]]
print(L[-1])
print(L[0])
print(L[1])
print(L[3][1]), 'to pick from the list in the list'
print(L[2][1])
input()
'''
