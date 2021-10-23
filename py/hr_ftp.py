# https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
n = 0
o = 0
for i in student_marks[query_name]:
    n += 1
    o += i
print(f'{o/n:.2f}')
