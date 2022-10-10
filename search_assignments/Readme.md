# Search Algorithm Assignments

<br/>

## Assignment 1

<br/>

You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where `N` is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.

We define `"rotating a list"` as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`.

`"Sorted list"` refers to a list where the elements are arranged in the increasing order e.g. `[1, 3, 5, 7]`.

<br/>

## Solution of Assignment 1

<br/>

### 1. We need to write a function which takes the rotated list as input, find out minimum number of times the original sorted list has to be rotated to achieve this rotated list, and return this minimum count as output. 

<br/>

>`Input`: A rotated list <br/>
>`Output`: The minimum number of times the original sorted list was rotated to obtain the given list

<br/>

### 2. Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible test cases we might encounter:

<br/>

>1. A list of size 10 rotated 3 times.
>2. A list of size 8 rotated 5 times.
>3. A list that wasn't rotated at all.
>4. A list that was rotated just once.
>5. A list that was rotated n-1 times, where n is the size of the list.
>6. A list that was rotated n times (do you get back the original list here?)
>7. An empty list.
>8. A list containing just one element.

<br/>

### 3. Solution in plain English: 

<br/>

>It has been observed that after rotating the original list which was sorted in ascending order, the first element of the original list is moved to the position index which is equal to the number of times the list was rotated. Additionally the first element of the original list is the only element in the rotated list whose predecessor is greater that itself. Hence, we can write a function to search for an element whose predecessor is greater that the element itself, in order to find out the first element of the original list, and then we can return the position index of that element which is the number of times the original list was rotated to obtain the given rotated list.

<br/>

### 4. The Brute Force/First solution coming in your mind:

<br/>

>Here we can simply search all the elements of the given rotated list one by one (linearlly) to find out the element whose predecessor is greater that the element itself.

<br/>

### 5. Implement the solution given in previous step and check it for the test cases designed in step 2.

<br/>

### 6. Analyze the algorithm's complexity and identify inefficiencies, if any.

<br/>

### 7. Apply the right technique to overcome the inefficiency. Repeat steps 5 to 7.

<br/> <br/>

## Optional Assignment 2

<br/>

So far we've assumed that the numbers in the list are unique. What if the numbers can repeat? E.g. `[5, 6, 6, 9, 9, 9, 0, 0, 2, 3, 3, 3, 3, 4, 4]`. Can you modify your solution to handle this special case?

<br/> <br/>

## Optional Assignment 3

<br/>

You are given list of numbers, obtained by rotating a sorted list an unknown number of times. You are also given a `target` number. Write a function to find the position of the `target` number within the rotated list. You can assume that all the numbers in the list are unique.

Example: In the rotated sorted list `[5, 6, 9, 0, 2, 3, 4]`, the `target` number `2` occurs at position `5`.