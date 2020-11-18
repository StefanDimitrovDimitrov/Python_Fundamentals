tail = input()
body = input()
head = input()

meerket =[tail,body, head]

meerket[0], meerket[2] = meerket[2], meerket[0]

print(meerket)