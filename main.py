# Найти число, которое повторяется один раз
a = input().split()

for i in a:
    if a.count(i) <= 1:
        print(i)