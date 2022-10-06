import time

def execute_with_execution_time(function, query, data):
    start_time = time.time()
    response_received = function(query, data)
    end_time = time.time()

    execution_time = round((end_time-start_time) * 10**3, 5)
    
    return response_received, execution_time