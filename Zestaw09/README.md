## Zestaw09 2021-01-31
#### Opis


#### Wywołanie
```
usage: main.py [-h] [-N N] [-K K] [-save SAVE] {A,B,C,D,E}

positional arguments:
  {A,B,C,D,E}  A - int numbers from 0 to N-1 in random order
               B - int numbers from 0 to N-1 in almost ordered
               C - B reversed
               D - N float numbers gauss
               E - N repeated int numbers from k length set

optional arguments:
  -h, --help   show this help message and exit
  -N N         [default = 10]
  -K K         set length [default = 3]
  -save SAVE   save input/output to files [default = F]
```
Przykłady:
```
>python main.py A -N=10
Before: [0, 8, 9, 7, 2, 1, 5, 6, 4, 3]
 After: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>python main.py B -N=10 -K=1 # tablica nie zostanie przetasowana
Before: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 After: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>python main.py B -N=10
Before: [0, 1, 3, 2, 6, 5, 9, 4, 8, 7]
 After: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>python main.py C -N=10
Before: [8, 6, 7, 9, 5, 4, 2, 0, 3, 1]
 After: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>python main.py D -N=10
Before: [-0.0658379046059718, 0.5159946437235483, -1.62426530665278, -1.1684230381314429, 1.7092178710888142, 0.6663348144557101, 1.0468357364250145, 0.8330002079786998]
 After: [-1.62426530665278, -1.1684230381314429, -0.0658379046059718, 0.5159946437235483, 0.6663348144557101, 0.8330002079786998, 1.0468357364250145, 1.7092178710888142]

>python main.py E -N=15 -K=4
Before: [6007, 9870, 6007, 5482, 9870, 6007, 5482, 2416, 9870, 2416, 5482, 2416, 6007, 2416, 9870]
 After: [2416, 2416, 2416, 2416, 5482, 5482, 5482, 6007, 6007, 6007, 6007, 9870, 9870, 9870, 9870]

```