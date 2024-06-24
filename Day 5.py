def enter_num(number, queue):
    if number not in queue:
        queue.append(number)
        if len(queue) > 5:
            queue.pop(0)

queue = []

static = []

commands = []
while True:
    command = input("COMMAND: ")
    if command.startswith("3"):
        number = command.split()[-1]
        commands.append(number)
        print(commands)
    elif command == "NAA":
        if commands:
            commands.pop(0)
        print(commands)
    elif command == "WALA":
        if commands:
            commands.pop()   
            print(commands) 
    elif command == "DISPLAY":
        print(commands)
    elif command == "HAWA":
        break
    else:
        commands.append(command)
        print(commands)
