def locate_card(query, data=[]):
    print("LINEAR SEARCH")
    data_length = len(data)
    index = 0
    
    while index < data_length:
        if data[index] == query:
            return index
        index = index+1
    
    return -1

