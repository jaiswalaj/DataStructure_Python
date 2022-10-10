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

tests.append({
    'input': {
        'nums': [5, 6, 9, 0, 2, 3, 4]
    },
    'output': 3
})



# Test Cases for Optional Assignment 2

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]
    },
    'output': 6
})

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [12, 12, 13, 13, 13, 14, 14, 0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 10]
    },
    'output': 7
})

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [12, 12, 12, 12, 12, 12, 12, 12, 13]
    },
    'output': 0
})

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [1, 2, 2, 2, 3, 4, 5, 6, 7]
    },
    'output': 0
})

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [9, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 8, 9]
    },
    'output': 1
})

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [ 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6, 7, 7, 7, 7, 7, 7, 7, 1]
    },
    'output': 19
})

# A list of Repeating Numbers for Assignment 2
tests.append({
    'input': {
        'nums': [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    },
    'output': 0
})