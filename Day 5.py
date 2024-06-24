add_status = "1"

if add_status == "1":
    print("1, 2, 3.")
    for task in range(1, 6):
        print(f"QUEUE NAA {task}")
    print("2, 3")
    for station in range(1, 6):
        print(f"STACK NAA {station}")
else:
    print("NAA")
    print("2, 3, 4, 6, 7, 8")

