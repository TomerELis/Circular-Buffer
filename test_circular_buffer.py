from circular_buffer import CircularBuffer

print("Test #1 - pushing negative\n--------------------------------------------------------------------------")

circ = CircularBuffer(1)
circ.pop()      # None (empty pop)
circ.push(-5)   # Push -5
print(circ)  # [-5]

circ.push(20)  # Overwrites -5
print(circ)  # [20]
circ.pop()  # 20
print(circ)  # [None]
circ.pop()  # None (empty again)
print(circ)  # [None]



print("\n\nTest #2 - resize larger&smaller\n--------------------------------------------------------------------------")

circ = CircularBuffer(3)
circ.push(10)
circ.push(20)
circ.peek()  # 10
circ.push(30)
circ.peek()  # 10
circ.pop()   # 10
circ.peek()  # 20
print(circ)  # [10, 20, 30]

circ.push(40)  # Overwrite 10
print(circ)    # [20, 30, 40]
circ.pop()     # 20
print(circ)    # [30, 40]

circ.push(50)
print(circ)  # [30, 40, 50]

# Resize larger
circ.resize(5)
circ.push(60)
circ.push(70)
print(circ)  # [30, 40, 50, 60, 70]

# Resize smaller (cut oldest items, keep youngest)
circ.resize(2)
print(circ)  # Should only keep [60, 70]


circ.push(80)
print(circ)  # [70, 80]
circ.push(90)
circ.push(100)  # Overwrites 80
print(circ)  # [90, 100]


circ.pop()  # 90
circ.pop() # 100
print(circ)  # [None, None]
circ.pop()  # None (buffer empty)



print("\n\nTest #3 - different data types\n--------------------------------------------------------------------------")

circ = CircularBuffer(3)
circ.push('a')
print(circ)  # ['a', None, None]
circ.push('b')
print(circ)  # ['a', 'b', None]
circ.push(1)
print(circ)  # ['a', 'b', 1]
circ.pop()         # removes 'a'
circ.push('d')
print(circ)  # ['b', 1, 'd']
circ.pop()         # removes 'b'
circ.push(2.5)
print(circ)  # [1, 'd', 2.5]


print("\n\nTest #4 - resize to same size and string\n--------------------------------------------------------------------------")

circ = CircularBuffer(3)
circ.push(1)
circ.push(2)
circ.push(3)
print(circ)  # [1, 2, 3]
circ.resize(3)
print(circ)  # [1, 2, 3]
circ.pop()
print(circ)  # [None, 2, 3]
circ.push(4)
print(circ)  # [4, 2, 3]
circ.push('Hello')
print(circ)  # [5, 4, 3]
circ.peek()  # 3


# print("\n\nTest #5 - resize to invalid size \n--------------------------------------------------------------------------")
#
# circ = CircularBuffer(3)
# circ.push(10)
# print(circ)  # [10, None, None]
# circ.resize(0)
# print(circ)  # [10, None, None]
# #if user write 3
# circ.push('a')
# print(circ)  # ['a', 10, None]

#
# print("\n\nTest #6 - invalid starting size \n--------------------------------------------------------------------------")
# circc = CircularBuffer(-5)  #user must enter a valid size
# print(circc)  # [None, None]
# circc.push(10)  # Push 10
# print(circc)  # [10, None]
#
#
# circc = CircularBuffer(3)
# print(circc)  # [None, None]
# circc.push(1)
# print(circc)  # [None, None]
