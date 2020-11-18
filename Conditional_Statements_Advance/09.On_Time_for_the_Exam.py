hour_test = int(input())
minutes_test = int(input())
hour_arrived = int(input())
minutes_arrived = int(input())

late = "Late"
on_time = "On time"
early = "Early"

test_time = hour_test * 60 + minutes_test
arrival_time = hour_arrived * 60 + minutes_arrived

total_min_diff = arrival_time - test_time

student_arrival = late

if total_min_diff < - 30:
    student_arrival = early
elif total_min_diff <= 0:
    student_arrival = on_time

result = ""

if total_min_diff != 0:
    hours_diff = abs(total_min_diff) // 60
    minutes_diff = abs(total_min_diff) % 60
    if hours_diff > 0:
        result = f'{hours_diff}:{minutes_diff:02} hours '
    else:
        result = f'{minutes_diff} minutes '

    if total_min_diff < 0:
        result = result + "before the start"
    else:
        result = result + "after the start"

print(student_arrival)
if result:
    print(result)
