# 生成器

a = []
for i in range(10):
    a.append(i ** 2)
print(a)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


def f():
    for n in range(10):
        b = n
        yield b


p = f()
if __name__ == '__main__':
    for i in range(4):
        print(next(p))
