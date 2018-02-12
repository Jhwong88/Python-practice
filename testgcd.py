'''A solution to find the greatest common divisor of two integers n1 and n2
is as follows: First find d to be the minimum of n1 and n2, then check
whether d, d-1, … d-2, 2, or 1 is a divisor for both n1 and n2 in this order.
The first such common divisor is the greatest common divisor for n1 and n2.
Write a program to implement this solution.'''

n1 = 18
n2 = 30

d = min(n1, n2) # 15

while not ((n1 % d == 0) and (n2 % d == 0)):
    d = d - 1

print(d)

'''
n1 % 15 == 0 # yes
n2 % 15 == 0 # no

n1 % 14 == 0 # no
n2 % 14 == 0 # no
'''
