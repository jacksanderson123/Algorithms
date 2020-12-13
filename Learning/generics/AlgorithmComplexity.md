# Algorithm Complexity / Big-O / Asymptotic analysis

> Below Is my Notes

## Mathematical explanation of Big O Notation

<details>
<summary>Notes</summary>
### Math Proof

I didn't take notes on this

### What this mean for Computer science

t = time
n = input size

Hypothetical

T(n) = 4n^2 + 16n + 2

    for i in n:
        for j in n:
            # Do 4 constant time instructions
    for i in n:
        # Do 16 constant time instructions
    # Do 2 constant time instructions

As N get's very large the dominating term is the n^2

</details>

## Derek Banas: Big O Notation YT

<details>
<summary>Notes</summary>
    Treat code as psudo code
    Big O Notation:A mesure how how well computer code scales as input increases. Not always a mesure of speed by scalabiltiy.

    > 45^3 + 20n^2 + 19

        If N is 1 then it's = 84
        If N is 2 then it's = 459
        If N is 10 then it's = 47,019

        45^3 = 45,000
        20n^2 = 2,000
        19 = 19

        At this point the + 19 dosen't have a large effect on the final number. The n^2 has a very minimal effect. This eqation has an order
        of  O(N^3)

    ### O(1) - Contant time

    An alogrithm that executes in the same no matter how big the input size

    - Adding an item into an array

    names.append("Jack")

    - Getting a value
    len(names)

    ### O(N) - linear time

    Time to complete grows propotionaly with input size

    - Printing Array

    ```
    for i in items:
        print(i)`
    ```

    - Searching array

    ```
    found = False
    for name in names:
        if name == "jack":
            found = True
    print(found)
    ```

    ### O(N^2) - Quadratic Time

    Time to complete is proportional to the square of the amount of data

    - Bubble sort

    ```
    def bubblesort():
        for i in range(len(names)):
            for j in range(len(names-i)):
                if names[j] > names[j+1]:
                    # swap values
    ```

    ### O(log n)

    This is when data being used is decreased by aproximately 50% each time the data is evaluated during the algorithms. Typicaly for divide an conquer algorithms like binary search.

    As N increase the increase in log N is dramatically smaller.

    ```
    def binary_search(names, value):
        lowIndex = 0
        highIndex = len(names) - 1

        while (lowIndex <= highIndex):
            middleIndex = (highIndex + lowIndex / 2)
            if (names[middleIndex] < value):
                lowIndex = middleIndex + 1
            elif (names[middleIndex] > value):
                highIndex = middleIndex - 1
            else:
                print("found a match")
                break
    ```

    Every time the algorithm rules out half of the value options halfing the amount of comparsions.

    ### O(n log n)

    comparisions = n log n

    - Quick Sort

    ```
    def quickSort(left, right):
        if (right - left <= 0):
            return;
        else:
            pivot = names[right]
            pivotLocation = partitionArray(left, right, pivot)
            quickSort(left, pivotLocation -)
            quickSort(pivorLocation + 1, right)

    def partitionArray(left, right, pivot):
        leftPointer = left - 1;
        rightPointer = right

        while(true){
            while(names[++leftPointer] < pivot>):

            while(rightPointer > 0 && names[-rightPointer] > pivot):


            if (leftPointer >= rightPointer){
                break
            else:

        }
    ```

</details>

## Harvad CS50: Asymptotic Notation

<details>
<summary>Notes</summary>
    What does it mean for an algorithms to be fast?

    ### Asymptotic Complexity and Big O Notation

    ---

    As the size of your input incrase towards infinity how does the size of a program run time grow?

    #### Upper and lower bounds

    Best case and worst case complexity

    Binary Search

        Worst Case Big O(log n)
        Best Case: Omega(1)

    Linear Search

        Worst Case: Big(n)
        Best Case: Omega(1)

    Theta is used if the best case and worst case is the same.

    #### Linear time - O(n)

    **Cat algorithm**

        str_ = "cat"
        count = 0

        for char in str_:
            count += 1

        print(count)

    The time required to run this algorithm, is propotionate to the length of the string so counting 3 characters is going to take 3 times as long as counting 1 charcter.

    #### Constant time - O(1)

    **Cat algorithm**

        str_ = "cat"
        larg_str_ = "big cat"
        len(str_)
        len(larg_str_)`

    The time required to get both lengths is the same even though the string length is difffrent. As len is retreaving a stored varible of the length of the string. All we need to do is read the value, regardless of the size of the string reading the value is always
    done in constant time.

    The draw back is storing the varible takes up more memory you spend more time initilizing the string as you store the length when you initilise.

    > Does big O(1) mean the code runs in 1 step?

    No it's irelavant how many steps a give line of code takes to be big 1 of 1. The imporantce is regarless of the input size it will always take the same amounts of steps.

    #### Quadratic timeO(n^2)

    Can really end up

    #### Logarithmic time O(log n)

    Typically divide and conquer algorithms for example binary search.

    Time goes up linearly while n goes up exponentially so if it takes 1 second to compute 10 elements it will take 2 seconds to compute 100 elements. Doubling n will increase the run time by 1.

    n = 8 -> 3 operations

        (log(2) 8)

    n = 16 -> 4 operations

        (log(2) 16)

</details>
