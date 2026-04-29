def main():
    # Take input from user
    numbers = list(map(int, input("Enter numbers (space-separated): ").split()))
    
    # Sort the list
    numbers.sort()
    
    # Display result
    print("Sorted list:", numbers)


# Run the program
if __name__ == "__main__":
    main()