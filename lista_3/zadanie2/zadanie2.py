def calkowite(a=1):
    while True:
        yield a
        a +=1

def kwadrat(n=1):
    for i in calkowite(n):
        yield i ** 2

# for a in calkowite():
#     print(a)

for a in kwadrat():
    print(a)