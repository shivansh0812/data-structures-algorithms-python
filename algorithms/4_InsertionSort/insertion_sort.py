
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:  #We are not past the beginning (j >= 0), and anchor is smaller than the element at index j.
            elements[j+1] = elements[j]   # Shift the element at j one step to the right
            j = j - 1  # Decrement j to check the previous element. This continues until we find the correct spot for anchor.
        elements[j+1] = anchor  # When the loop ends, j will be one position left of where anchor b

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    insertion_sort(elements)
    print(elements)
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        insertion_sort(elements)
        print(f'sorted array: {elements}')
