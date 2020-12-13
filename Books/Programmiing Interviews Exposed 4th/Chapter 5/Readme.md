# Linked Lists

## Singly Linked Lists

Typically what an interview will mean by linked list.

- Head Pointer (The first Node in the list)
- Tail either empty or null referance(The last Node in a list)
- Node
  - Value
  - Pointer to next item in the list

A Singly linked list can only be traversed from to top-> down

```
# Simplest form of linked list
typedef struct ListElement {
    struct ListElement *next;
} ListElement;
```

This isn't useful as it contains no value's

```
# Linkedlist with intages
typedef struct IntElement {
    struct ListElement *next;
    int                 data;
} IntElement;
```

```
# A singly linked list in C++

class IntElement {
    public: IntElement ( int value): next(NULL), data(value){}
    -IntElement() {}
    IntElement(){}
    IntElement *getNext() const { return next; }
    int value() const { return next; }
    void setNext (IntElement *elem) { next = elem; }
    void setValue(int value) { data = value; }

    private:
        IntElement *next;
        int         data;
};
```

```
# A python Linked List

class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
```

## Doubly Linked Lists

A doubly linked list each element has a link to the previous element, with the head having empty or null for the previous element.
