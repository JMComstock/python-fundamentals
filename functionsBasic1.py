#1
def a():
    return 5
print(a()) #returns 5

#2
def a():
    return 5
print(a()+a()) # returns 10

#3
def a():
    return 5
    return 10
print(a()) #returns 5

#4
def a():
    return 5
    print(10)
print(a()) # returns 5

#5
def a():
    print(5)
x = a()
print(x) # retuens 5

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))  # returns 25

#8
def a():
    b = 100
    print(b) # returns 100
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) # returns 10           

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3)) # returns 7
print(a(5,3)) # returns 14
print(a(2,3) + a(5,3)) # reutrns 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # returns 8

#11 
b = 500
print('1st b ',b) # reutrns 500
def a():
    b = 300
    print('2nd b', b) # retuns 500
print('3rd b', b) # returns 300
a()
print('4th b', b) # returns 500   

#12
c = 500
print('1st c', c) # reutrns 500
def a():
    c = 300
    print('2nd c', c)
    return c # returns 500
print('3rd c', c) # returns 300
a()
print('4th c', c) #returns 500

#13
d = 500
print('1st d', d) # returns 500
def a():
    d = 300
    print('2nd d', d) # returns 500
    return d 
print('3rd d', d) # returns 300
d = a()
print('3rd d', d) # returns 300

#14
def a():
    print('first', 1) # returns 1
    b()
    print('third', 2)
def b():
    print('second', 3)
a() 

#15
def a():
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5 
y = a() # first returns 3 from line 114 and also returns 5 line 115
print(y) # returns 10 from line 112    