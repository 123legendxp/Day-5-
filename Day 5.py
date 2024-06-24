def enter_num(number, queue):
    if number not in queue:
        queue.append(number)
        if len(queue) > 5:
            queue.pop(0)

queue = []

clicks = [0]

commands = []
while True:
    command = input("COMMAND: ")
    if command.startswith("3"):
        num = command.split()[-1]
        commands.append(num)
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
    elif command == "QUIT":
        break
    else:
        commands.append(command)
        print(commands)
