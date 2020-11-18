message = input().split()
new_message = ""
final_message = []
tool=0

for i,item in enumerate(message):
    tool = int(''.join(filter(str.isdigit, item)))
    char = chr(tool)

    new_message = message[i].replace(str(tool),char)
    new_message = list(new_message)
    new_message[1], new_message[-1] = new_message[-1], new_message[1]
    # a = new_message[1]
    # b = new_message[-1]
    # new_message[1] = b
    # new_message[-1] = a
    final_message.append(''.join(new_message))


for i,item in enumerate(final_message):
    print(final_message[i],end=" ")