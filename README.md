# TODO
[] poetry.toml
[] Enforce types (mypy)
[] Formatting (black)
[] Linting (ruff)
[] Setup tests (pytest)

# DSA
1. Create the data structure
2. Read and Write


## Arrays
Structuring data inside of RAM, variables are all stored in RAM

Common for computers to have 8GB of RAM which is ~10^9 bytes.

Know GB to Bytes which equals 8 bits.

Integers are commonly stored a 4 bytes or 32 bits

RAM has two components: a value and a distinct location

Arrays will always be contiguous memory i.e. memory is stored together block-like

Addresses increment by the size of the value i.e. data type

Arrays are fixed size and we don't always get to decide where we store our values in RAM. Random Access Memory

Chars take 1 byte (ASCII chars)

Create an array: O(n)
Read an array if you have the index: O(1)
Write to an array if you have the index: O(1)

Inserting or removing at any random position not at the end of the array is O(n)

Pushing to an array adds it to the end, internal implementation has a pointer that points to the last pushed item which can be used to get the length of the array. Popping the value removes the last value

Dynamic array creates a new array with double the size when it originally runs out of space, copy all orginal values into the second array and then add a new value then deallocate the original array

Pushing is O(1)* (amortized) because on average it is O(1) but sometimes it's O(n) when the array runs out of space and needs to be doubled

R / W i-th element = O(1)
Push / Pop = O(1)
Insert / remove middle = O(n)

### Stacks
Think of stacks as vertical and a cookie jar
LIFO = Last In, First Out
Push = O(1)
Pop = O(1)
Peek = O(1)

## Linked Lists

### Queues

# Python

| Language | Default Behavior | Notes |
|----------|-----------------|-------|
| **C** | Pass by value | Must use pointers explicitly for mutation |
| **C++** | You choose | Can pass by value, reference, or pointer |
| **Python** | Pass by object reference | Mutable objects can be modified |
| **JavaScript** | Pass by object reference | Same as Python |
| **Java** | Pass by value | Objects: pass value of reference |
| **Rust** | Move by default | Ownership system, must explicitly borrow |
| **Go** | Pass by value | Slices/maps/channels are reference types |