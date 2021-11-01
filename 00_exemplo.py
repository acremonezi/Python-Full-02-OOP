# Isso aqui:
x = []

for i in range(0, 10):
    if i % 2 == 0:
        x.append(i)

# É igual a:

x = [i for i in range(0,10) if i % 2 == 0]