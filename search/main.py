from test_cases import tests
from utilities import execute_with_execution_time
from linear_search import locate_card as linear_locate_card

response_received, execution_time = execute_with_execution_time(locate_card, tests[0]['input']['query'], tests[0]['input']['cards'])
print(response_received)
print("\nExecution Time: ", execution_time, "ms")
