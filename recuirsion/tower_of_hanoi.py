def tower_of_hanoi(n, start, end, midle):
    if n == 1:
        print(f"Move disk {n} from {start} to {end}")
        return
    tower_of_hanoi(n-1, start, midle, end)
    print(f"Move disk {n} from {start} to {end}")
    tower_of_hanoi(n-1, midle, end, start)


tower_of_hanoi(3, "A", "C", "B")
