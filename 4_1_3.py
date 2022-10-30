# put your python code here
a = int(input())
b = []
while a > 0:
  b.append(a % 10)
  a = a // 10
b = b[::-1] # так можно развернуть, если бы нам был важен порядок
if b[0] + b[3] == b[1] - b[2]:
    print('ДА')
else:
    print('НЕТ')