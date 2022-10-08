from test_cases import tests
from utilities import execute_with_execution_time, compare_execution_time
from linear_search import locate_card as linear_locate_card
from binary_search import locate_card as binary_locate_card

def search(locate_card_function, dataset):
    print("\n********************* START *********************\n")
    counter = 0
    execution_time_list = []
    
    for test in dataset:
        cards = test['input']['cards']
        query = test['input']['query']
        expected_output = test['output']
        actual_output, execution_time = execute_with_execution_time(locate_card_function, query, cards)
        print("Expected Output: ", expected_output)
        print("Actual Output: ", actual_output)
        
        if expected_output == actual_output:
            test_status = "PASSED"
            execution_time_list.append(execution_time)
        else:
            test_status = "FAILED"
            execution_time_list.append(-1)

        print("Test Case #", counter, "Status: ", test_status)
        print("Execution Time: ", execution_time, "ms\n")
        counter = counter + 1

    print("\n********************* END *********************\n")

    return execution_time_list


def main(locate_card_functions, dataset, algo_names=[]):
    execution_time_matrix = []
    for locate_card_function in locate_card_functions:
        execution_time_list = search(locate_card_function, dataset)
        execution_time_matrix.append(execution_time_list)
    
    compare_execution_time(execution_time_matrix, algo_names)
    
    print("\nAlgo Names: ", algo_names)
    print("\nAlgo execution time for each data in the dataset: \n", execution_time_matrix)
    

main([linear_locate_card, binary_locate_card], tests, algo_names=["Linear Search", "Binary Search"])
