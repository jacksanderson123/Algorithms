# Algorithm Complexity / Big-O / Asymptotic analysis

## Harvad CS50: Asymptotic Notation

---

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
