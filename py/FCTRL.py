# https://www.spoj.com/problems/FCTRL/
import sys
import math
sys.stdin = open("FCTRL.txt")
n = int(input())
for i in range(n):
    j = int(input())
    a = 0
    for l in range(1,100):
        a += j // (5 ** l)
    print(a)