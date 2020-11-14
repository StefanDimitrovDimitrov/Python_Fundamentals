number_oscar = int(input())

if number_oscar < 88 and number_oscar != 86:
    print(f"When will you give Leo an Oscar?")
elif number_oscar > 88:
    print(f"Leo got one already!")
elif number_oscar == 88:
    print(f"Leo finally won the Oscar! Leo is happy")
else:
    print(f"Not even for Wolf of Wall Street?!")