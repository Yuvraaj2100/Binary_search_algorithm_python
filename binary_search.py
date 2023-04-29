
L = [1, 2, 3, 4, 5]


target = int(input("Enter a number: "))


start = 0
end = len(L) - 1
print(end)

while start <= end:

    middle = (start + end) // 2


    if L[middle] == target:
        print("Element found at index", middle)
        break

    elif L[middle] < target:
        start = middle + 1
        
    else:
        end = middle - 1
else:
    print("Element not found")
