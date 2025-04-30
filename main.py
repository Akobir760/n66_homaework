from functions import add, sub, mult, div



def main():
    print("""
1. add numbers
2. substract numbers
3. multiplay numbers
4. division number
5. exit""")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice ==3:
        mult()
    elif choice == 4:
        div()
    elif choice == 5:
        print("Exit")
        return
    else:
        print("Invalid choice!")
        return main
    main()
    

if __name__ == "__main__":
    main()