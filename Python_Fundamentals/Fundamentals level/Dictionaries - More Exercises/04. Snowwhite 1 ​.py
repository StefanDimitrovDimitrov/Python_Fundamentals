import collections

dwarfs = {}
dwarf_name_hat_color_count = collections.defaultdict(int)

while True:
    data = input()
    if data == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <:>")
    dwarf_physics = int(dwarf_physics)

