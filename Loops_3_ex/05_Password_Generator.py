n = int(input())
l = int(input())

for i in range(1, n):
    for x in range(1, n):
        for z in range(97, 97 + l):
            for r in range(97, 97 + l):
                for t in range(1, n + 1):
                    z_1 = chr(z)
                    r_1 = chr(r)
                    if t > i and t > x:
                        print(f'{i}{x}{z_1}{r_1}{t}', end=" ")
