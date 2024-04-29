def find_num():
    N = int(input("Enter the number of elements (N): "))
    
    numbers = []
    for i in range(N):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)
    
    X = int(input("Enter the number to search for (X): "))
    
    index = -1
    for i, num in enumerate(numbers):
        if num == X:
            index = i + 1
            break
    
    if index == -1:
        print("-1")
    else:
        print(f" {X} is at index : {index}")

find_num()
