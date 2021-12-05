n = int(input("Enter the number of elements: "))

a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
print("\nList is: ", a)