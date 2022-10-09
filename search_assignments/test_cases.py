tests = []

# A list of size 10 rotated 3 times.
tests.append({
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
})

# A list of size 8 rotated 5 times.
tests.append({
    'input': {
        'nums': [6, 7, 9, 11, 13, 1, 3, 5]
    },
    'output': 5
})

# A list that wasn't rotated at all.
tests.append({
    'input': {
        'nums': [2, 4, 6, 8, 10]
    },
    'output': 0
})

# A list that was rotated just once.
tests.append({
    'input': {
        'nums': [12, 2, 4, 6, 8, 10]
    },
    'output': 1
})

# A list that was rotated n-1 times, where n is the size of the list.
tests.append({
    'input': {
        'nums': [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 1]
    },
    'output': 10
})

# A list that was rotated n times, where n is the size of the list
tests.append({
    'input': {
        'nums': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    },
    'output': 0
})

# An empty list.
tests.append({
    'input': {
        'nums': []
    },
    'output': 0
})

# A list containing just one element.
tests.append({
    'input': {
        'nums': [1]
    },
    'output': 0
})
