

def create_array(full_name):
    """Create an array of unique letters from the full name."""
    letters = []

    for name in full_name.split():

        if not name.isalpha():
            print(f"Excluded: {name}")
            continue

        for letter in name.upper():

            if letter not in letters:
                letters.append(letter)

    return letters


def insertion_sort(array):
    """Return a sorted copy of the array using Insertion Sort."""
    result = array.copy()

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result


def main():
    full_name = input("Enter your full name: ")

    unsorted_array = create_array(full_name)

    if not unsorted_array:
        print("No valid names to sort.")
        return

    sorted_array = insertion_sort(unsorted_array)

    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:  ", sorted_array)


if __name__ == "__main__":
    main()

