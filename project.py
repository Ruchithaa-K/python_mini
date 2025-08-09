
while True:
    print("\n Mini calculator using python")
    print("1. Arithmetic Operations")
    print("2. Comparison Operations")
    print("3. Logical Operations")
    print("4. Assignment Operations")
    print("5. Bitwise Operations")
    print("6. Membership Operations")
    print("7. list")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        x=int(input("Enter a first number"))
        y=int(input("Enter a first number"))
        print("\nArithmetic Operations:")
        print("x + y =", x + y)
        print("x - y =", x - y)
        print("x * y =", x * y)
        print("x / y =", x / y)
        print("x // y =", x // y)
        print("x % y =", x % y)
        print("x ** y =", x ** y)

    elif choice == "2":
        x=int(input("Enter a first number"))
        y=int(input("Enter a first number"))
        print("\nComparison Operations:")
        print("x == y:", x == y)
        print("x != y:", x != y)
        print("x > y:", x > y)
        print("x < y:", x < y)
        print("x >= y:", x >= y)
        print("x <= y:", x <= y)

    elif choice == "3":
        x=int(input("Enter a first number"))
        y=int(input("Enter a first number"))
        a = bool(x)
        b = bool(y)
        print("\nLogical Operations:")
        print("a and b:", a and b)
        print("a or b:", a or b)
        print("not a:", not a)

    elif choice == "4":
        x=int(input("Enter a first number"))
        y=int(input("Enter a first number"))
        c = x
        print("\nAssignment Operations:")
        c += y
        print("c after += y:", c)
        c -= y
        print("c after -= y:", c)
        c *= y
        print("c after *= y:", c)
        c /= y
        print("c after /= y:", c)

    elif choice == "5":
        x=int(input("Enter a first number"))
        y=int(input("Enter a first number"))
        print("\nBitwise Operations:")
        print("x & y =", x & y)
        print("x | y =", x | y)
        print("x ^ y =", x ^ y)
        print("~x =", ~x)
        print("x << 1 =", x << 1)
        print("x >> 1 =", x >> 1)

    elif choice == "6":
        text = "python"
        print("\nMembership Operations:")
        print("'p' in text:", 'p' in text)
        print("'z' not in text:", 'z' not in text)
    elif choice == "7":
        my_tuple = tuple(map(int, input("Enter numbers separated by space: ").split()))
        print("Tuple:", my_tuple)
        sets=set(my_tuple)
        print("Sets:", sets)

    elif choice == "8":
        print("Exiting program. Goodbye!")
        break

else:
        print("Invalid choice! Please enter a number between 1-8.")

print("hello")