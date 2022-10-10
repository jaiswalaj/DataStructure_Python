import time

tests = []

tests.append({
    'input': {
        'nums': [5, 6, 9, 0, 2, 3, 4],
        'target': 2
    },
    'output': 5
})

tests.append({
    'input': {
        'nums': [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'target': 20
    },
    'output': -1
})


def binary_target_search(data, target):
    data_length = len(data)
    lo, hi = 0, data_length-1

    while lo <= hi:
        mid = (lo+hi) // 2

        if data[lo] == target:
            return lo+1
        elif data[hi] == target:
            return hi+1
        elif data[mid] == target:
            return mid+1
        elif data[mid] < data[mid-1]:
            if target > data[mid-1]:
                break
            elif target > data[lo] and target <= data[mid-1]:
                hi = mid-1
            else:
                lo = mid+1
        elif target < data[mid]:
            hi = mid-1
        else: 
            lo = mid+1
            
    return -1


# Alternative Way to implement Binary Search
# def binary_target_search(data, target):
#     data_length = len(data)
#     lo, hi = 0, data_length-1

#     while lo <= hi:
#         mid = (lo+hi) // 2

#         if data[lo] == target:
#             return lo+1
#         elif data[hi] == target:
#             return hi+1
#         elif data[mid] == target:
#             return mid+1
#         elif data[hi] < target and data[mid] < target:
#             hi = mid-1
#         elif data[hi] > target and data[mid] < target:
#             lo = mid+1
#         elif data[mid] > target:
#             hi = mid-1
#         elif data[mid] < target:
#             lo = mid+1
        
#     return -1


def main(dataset):

    for data in dataset:
        start_time = time.time()
        actual_output = binary_target_search(data['input']['nums'], data['input']['target'])
        end_time = time.time()
        expected_output = data['output']

        print("\nTest Case Data: ", data['input']['nums'])
        print("Expected Output: ", expected_output)
        print("Actual Output: ", actual_output)
        print("Execution Time: ", round((end_time-start_time) * 10**3, 5), "ms")

        if actual_output == expected_output:
            print("Test Case PASSED")
        else:
            print("Test Case FAILED")


main(tests)