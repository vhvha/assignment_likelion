# 1-1

sum = 0
num = 1

while num <= 1000:
    if num % 3 == 0:
        sum += num

    num += 1


print(sum)


# 1-2

num = 10
while num > 0:
    print('*'*num)
    num -= 1


# 1-3

sum = 0
aa = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]


def tra(l):
    a = l.pop()
    return a


while len(aa) > 0:

    sum += tra(aa)

print(sum)


# 2-1

for i in range(1, 101):
    print(i)

# 2-2

sum = 0

b = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for i in b:
    sum += i

print(sum/len(b))


# 2-3

numbers = [1, 2, 3, 4, 5]

res = [n*2 for n in numbers if n % 2 == 1]

print(res)
