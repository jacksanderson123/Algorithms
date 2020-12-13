# Linked Lists

## Singly Linked List

- Cosrsera

They are like links in a chain.

7 -> 10 -> 4 -> 13

head -> [7, -> [10, -> [4, -> [13, None]]]]

Each link is a node,

Node contains:

- Key/Value
- next pointer

What operations can you do to a linked list?

- add to the front of the list -> O(1)
- return front item of the list -> O(1)
- remove front of the list -> O(1)

Without tail

- add to the back -> O(n)
- return the back item -> O(n)
- remove back item ->O(n)

With tail

- add to the back -> O(1)
- return the back item -> O(1)
- remove back item ->O(n)

- if empty
- add key before or after a given node

Time complexity

- add to the front (Constant Time)

  - create node
  - point new node to the previous head node
  - point head to new node

- Tail pointer remove front -> O(1)
  - create node
  - point previous tail to new tail
  - update the tail it's self
