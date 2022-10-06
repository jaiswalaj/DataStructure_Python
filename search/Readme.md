# Search Algorithms (DSA)

<br/>

## QUESTION 1

<br/>

Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.

<br/>

## Systematic Strategy for Solving Problems

<br/>

1. State the problem clearly. Identify the input & output formats. 
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

<br/>

## Solution

<br/>

### 1. State the problem clearly. Identify the input & output formats.

<br/>

>### Problem <br/>
>We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.

>### Inputs <br/>
>`cards`: A list of numbers sorted in decreasing order. <br/> E.g. [13, 11, 10, 7, 4, 3, 1, 0] <br/>
>`query`: A number, whose position in the array is to be determined. <br/>E.g. 7

>### Output <br/>
>`position`: The position of `query` in the list cards. <br/>
E.g. 3 in the above case (counting from 0)

<br/>

### 2. Come up with some example inputs & outputs. Try to cover all edge cases.

<br/>

>### Test Cases
>
>Creating test cases beforehand allows you to identify different variations and edge cases in advance so that can make sure to handle them while writing code. Sometimes, you may start out confused, but the solution will reveal itself as you try to come up with interesting test cases.
>
>1. The number `query` occurs somewhere in the middle of the list `cards`.
>2. `query` is the first element in `cards`.
>3. `query` is the last element in `cards`.
>4. The list `cards` contains just one element, which is `query`.
>5. The list `cards` does not contain number `query`.
>6. The list `cards` is empty.
>7. The list `cards` contains repeating numbers but not `query`.
>8. The number `query` occurs at more than one position in `cards`.
>
>Note: Don't stress it if you can't come up with an exhaustive list of test cases though. You can come back to this section and add more test cases as you discover them. Coming up with good test cases is a skill that takes practice.

>### Missing Information 
>
>The problem statement does not specify what to do if the list `cards` does not contain the number `query`.
>1. Read the problem statement again, carefully.
>2. Look through the examples provided with the problem.
>3. Ask the interviewer/platform for a clarification.
>4. Make a reasonable assumption, state it and move forward.
>
>We will assume that our function will return -1 in case `cards` does not contain `query`.

<br/>

### 3. Come up with a correct solution for the problem. State it in plain English.

<br/>

Our first goal should always be to come up with a correct solution to the problem, which may necessarily be the most efficient solution. The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the brute force solution.

<br/>

>### Brute Force Solution
>
>In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one, till he find a card with the given number on it. Here's how we might implement it:
>
>1. Create a variable position with the value 0.
>2. Check whether the number at index position in card equals query.
>3. If it does, position is the answer and can be returned from the function
>4. If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
>5. If the number was not found, return -1.
>
>This particular algorithm is called `linear search algorithm`, since it involves searching through a list in a linear fashion i.e. element after element.

<br/>

An algorithm is simply a list of statements which can be converted into code and executed by a computer on different sets of inputs. 

<br/>

### 4. Implement the solution and test it using the test cases designed. Fix bugs, if any.

<br/>

In this step we actually code our functions to test the algorithm we wrote in previous steps. Then we will test our function with the test cases designed, and will improve it if there are any failed test cases. Once the bugs are fixed we will again test the function for all the test cases to make sure that no new bug has been introduced while fixing the previous bug.

<br/>

### 5. Analyze the algorithm's complexity and identify inefficiencies, if any.

<br/>

>### Complexity
>Complexity of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size e.g. N. Unless otherwise stated, the term complexity always refers to the worst-case complexity (i.e. the highest possible time/space taken by the program/algorithm to process an input).

>### Big O Notation
>Worst-case complexity is often expressed using the Big O notation. In the Big O, we drop fixed constants and lower powers of variables to capture the trend of relationship between the size of the input and the complexity of the algorithm i.e. if the complexity of the algorithm is cN^3 + dN^2 + eN + f, in the Big O notation it is expressed as O(N^3)

<br/>

### 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

<br/>

At the moment, we're simply going over cards one by one, and not even utilizing the face that they're sorted. This is called a brute force approach.

The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called binary search.

<br/>

### 7. Come up with a correct solution for the problem. State it in plain English.

<br/>

>Here's how binary search can be applied to our problem:
>1. Find the middle element of the list.
>2. If it matches queried number, return the middle position as the answer.
>3. If it is less than the queried number, then search the first half of the list
>4. If it is greater than the queried number, then search the second half of the list
>5. If no more elements remain, return -1.

<br/>

### 8. Implement the solution and test it using example inputs. Fix bugs, if any.

<br/>

### 9. Analyze the algorithm's complexity and identify inefficiencies, if any.

<br/>
