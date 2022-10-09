from test_cases import tests
import time

def linear_search_method(data):
    index = 1
    data_length = len(data)

    # If list contains only one element
    if data_length <= 1:
        return 0

    # If list contains more than one element
    while index < data_length:
        # If the element is less than its previous element
        if data[index] < data[index-1]:
            return index

        index = index + 1

    return 0


def binary_search_method(data):
    data_length = len(data)
    
    if data_length <= 1:
        return 0

    lo, hi, mid = 0, data_length-1, data_length // 2

    while lo < hi:
        mid = (lo+hi) // 2
        if data[mid] < data[mid-1]:
            return mid
        elif data[mid] > data[mid+1]:
            return mid+1
        elif data[mid] > data[hi]:
            lo = mid
        else:
            hi = mid

    return 0



def main(dataset):
    counter = 0
    for data in dataset:
        start_time = time.time()
        
        # Change the method to be called according to the algorithm you want to use
        actual_output = binary_search_method(data['input']['nums'])

        end_time = time.time()
        expected_output = data['output']
        execution_time = round((end_time-start_time) * 10**3, 5)
        
        print("\nTest Case Data: ", data['input']['nums'])
        print("Expected Output: ", expected_output)
        print("Acutal Output: ", actual_output)
        print("Execution Time: ", round((end_time-start_time) * 10**3, 5), "ms")
        
        if actual_output == expected_output:
            print("Test Case #", counter, ": ", "PASSED")
        else:
            print("Test Case #", counter, ": ", "FAILED")
        
        counter = counter + 1


main(tests)