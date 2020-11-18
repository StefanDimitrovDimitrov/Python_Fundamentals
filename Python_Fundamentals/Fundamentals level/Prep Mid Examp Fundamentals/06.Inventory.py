def collect(items, insturction):
    if not instruction in items:
        items.append(instruction)


def drop(items, instruction):
    if instruction in items:
        items.remove(instruction)


def combine_items(items,instruction):
    old_item = instruction.split(":")[0]
    new_item = instruction.split(":")[1]

    for i,item in enumerate(items):
        if item == old_item:
            items.insert(i+1,new_item)
            break



def renew(items,instruction):
    if instruction in items:
        items.remove(instruction)
        items.append(instruction)


items = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        break

    commands = command.split(" - ")[0]
    instruction = command.split(" - ")[1]

    if commands == "Collect":
        collect(items, instruction)
    elif commands == "Drop":
        drop(items, instruction)
    elif commands == "Combine Items":
        combine_items(items,instruction)
    elif commands == "Renew":
        renew(items,instruction)

final_list = ", ".join(items)

print(final_list)