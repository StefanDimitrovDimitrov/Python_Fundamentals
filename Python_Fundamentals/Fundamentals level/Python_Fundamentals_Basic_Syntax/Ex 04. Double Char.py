command = str(input())
final_command = ""
for i in range(len(command)):
    final_command += command[i] * 2
print(final_command)