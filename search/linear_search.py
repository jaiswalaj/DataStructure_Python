
def locate_card(query, data=[]):
    data_length = len(data)
    index = 0
    while index < data_length:
        if data[index] == query:
            return index
        index = index+1
        
        

# linear_search(tests)

