import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Read Data from File
def read_file(filename):
    with open(filename, 'r') as file:
        count = int(file.readline().strip())
        data = list(map(int, file.readline().strip().split()))
    return data

# Measure Sorting Time
def measure_sorting_time(data, sort_function):
    start_time = time.time()
    sorted_data = sort_function(data.copy())
    end_time = time.time()
    return end_time - start_time

# Main Function
def main():
    # File paths
    file1 = 'a2_task1_input1.txt'
    file2 = 'a2_task1_input2.txt'

    # Read data
    data1 = read_file(file1)
    data2 = read_file(file2)

    # Measure time for Bubble Sort
    bubble_time1 = measure_sorting_time(data1, bubble_sort)
    bubble_time2 = measure_sorting_time(data2, bubble_sort)

    # Measure time for Quick Sort
    quick_time1 = measure_sorting_time(data1, quick_sort)
    quick_time2 = measure_sorting_time(data2, quick_sort)

    # Print results
    print("Sorting Results for a2_task1_input1.txt:")
    print(f"Bubble Sort Time: {bubble_time1:.5f} seconds")
    print(f"Quick Sort Time: {quick_time1:.5f} seconds")
    print("Quick Sort was faster!" if quick_time1 < bubble_time1 else "Bubble Sort was faster!")

    print("\nSorting Results for a2_task1_input2.txt:")
    print(f"Bubble Sort Time: {bubble_time2:.5f} seconds")
    print(f"Quick Sort Time: {quick_time2:.5f} seconds")
    print("Quick Sort was faster!" if quick_time2 < bubble_time2 else "Bubble Sort was faster!")

if __name__ == "__main__":
    main()
