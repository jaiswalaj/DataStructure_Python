import time

def execute_with_execution_time(function, query, data):
    start_time = time.time()
    response_received = function(query, data)
    end_time = time.time()

    execution_time = round((end_time-start_time) * 10**3, 5)
    
    return response_received, execution_time

def compare_execution_time(execution_time_matrix, algo_names=[]):
    data_index = 0
    algo_count = len(execution_time_matrix)
    data_count = len(execution_time_matrix[0])
    while data_index < data_count:
        algo_index = 0
        fastest_execution_index = 0
        fastest_execution_time = execution_time_matrix[fastest_execution_index][data_index]
        
        while algo_index < algo_count:
            if execution_time_matrix[algo_index][data_index] < fastest_execution_time:
                fastest_execution_time = execution_time_matrix[algo_index][data_index]
                fastest_execution_index = algo_index
            
            algo_index = algo_index + 1

        print("\nFastest Algo for Test Case #", data_index+1, " is: ", algo_names[fastest_execution_index])
        print("Fastest Execution Time is: ", fastest_execution_time, "ms")

        data_index = data_index + 1

        

