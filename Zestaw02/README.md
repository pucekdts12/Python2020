## Zestaw02 2020-10-29
#### Wywołanie
```
python main.py NUMER_ZADANIA [argumenty dla zadania ...]
```
Przykłady:
```
> python main.py 1 [1,2,[3,4,[5,6],5],3,4]
Przed [1, 2, [3, 4, [5, 6], 5], 3, 4]
Po [1, 2, [3, 4, [5, 6, 7], 5], 3, 4]

> python main.py 2 2000
True

> python main.py 2 2300
False

> python main.py 3 "Ala ma kota"
Statistics for: Ala ma kota
{' ': 2, 'A': 1, 'a': 3, 'k': 1, 'l': 1, 'm': 1, 'o': 1, 't': 1}
Number of words: 3

> python main.py 3 "Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae molestiae eos corporis ducimus omnis sint quam, nulla autem perferendis, neque, nam vel minus debitis, veritatis? Voluptatum, odio adipisci illo id?"
Statistics for: Lorem ipsum dolor sit amet consectetur adipisicing elit. Recusandae molestiae eos corporis ducimus omnis sint quam, nulla autem perferendis, neque, nam vel minus debitis, veritatis? Voluptatum, odio adipisci illo id?
{' ': 29,
 ',': 5,
 '.': 1,
 '?': 2,
 'L': 1,
 'R': 1,
 'V': 1,
 'a': 12,
 'b': 1,
 'c': 7,
 'd': 9,
 'e': 19,
 'f': 1,
 'g': 1,
 'i': 24,
 'l': 9,
 'm': 11,
 'n': 10,
 'o': 13,
 'p': 6,
 'q': 2,
 'r': 8,
 's': 16,
 't': 13,
 'u': 12,
 'v': 2}
Number of words: 30

> python main.py 4 1 1 2 3
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]

> python main.py 5 9
9 as bin 1001
Largest gap:  2

> python main.py 5 1024
1024 as bin 10000000000
Largest gap:  0

> python main.py 5 1025
1025 as bin 10000000001
Largest gap:  9
```