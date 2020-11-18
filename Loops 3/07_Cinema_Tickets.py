film = ""
seeds = 0
tickets = 0
total_tickets = 0
student_count = 0
standard_count = 0
kid_count = 0
free_seeds = 0
is_cinema_open = True

while is_cinema_open:
    film = input()
    seeds = 0
    tickets = 0
    if film == "Finish":
        is_cinema_open = False
        break
    free_seeds = int(input())
    seeds += free_seeds
    while free_seeds != 0:
        ticket = input()
        free_seeds -= 1
        if ticket == "student":
            student_count += 1
        elif ticket == "standard":
            standard_count += 1
        elif ticket == "kid":
            kid_count += 1
        elif ticket == "End":
            break
        tickets += 1
        total_tickets += 1
    total_capacity = tickets / seeds * 100
    print(f"{film} -{total_capacity: .2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{student_count / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_count / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_count / total_tickets * 100:.2f}% kids tickets.")
