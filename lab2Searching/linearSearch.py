def linearSearch(myList, target):
    """
    Performs a linear search to find a target value in a list.

    Args:
        myList: The list to be searched.
        target: The value to search for.

    Returns:
        The index of the target value if found, otherwise returns -1.
    """
    for i in range(len(myList)):
        if myList[i] == target:
            return i
    return -1

def main():
    myList = [4, 7, 1, 9, 3, 6, 8]
    while True:
        try:
            searchValueInput = input("Enter a number to search for or 'n' to quit: ")
            
            if searchValueInput.lower() == 'n':
                print(f"The original list was {myList}. Exiting program.")
                break
            
            searchValue = int(searchValueInput)
            
            index = linearSearch(myList, searchValue)
            
            if index != -1:
                print(f"Success! The number {searchValue} was found at index {index}.")
                break
            else:
                print(f"Sorry, the number {searchValue} was not found in the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'n' to quit.")

if __name__ == "__main__":
    main()