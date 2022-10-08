def test_location(mid, query, data):
    if data[mid] < query or (mid-1 >= 0 and data[mid-1] == query):
        return "LEFT"
    elif data[mid] > query:
        return "RIGHT"
    elif data[mid] == query:
        return "FOUND"



def locate_card(query, data=[]):
    print("BINARY SEARCH")
    data_length = len(data)
    lo, hi = 0, data_length - 1

    while lo <= hi:
        mid = (lo+hi) // 2
        result = test_location(mid, query, data)

        if result == "FOUND":
            return mid
        elif result == "LEFT":
            hi = mid - 1
        elif result == "RIGHT":
            lo = mid + 1
    
    return -1