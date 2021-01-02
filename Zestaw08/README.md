## Zestaw08 2021-01-02
#### Opis
Opcja '-saving' przy algorytmach Djikstry oraz Bellmana-Forda powoduje że trasy wygenerowane dla jakiegoś wierzchołka są zapisywane zamiast być szukana za każdym razem(znacząco przyspiesza to działanie)

#### Wywołanie
```
usage: main.py [-h] [-seed SEED] [-routes ROUTES] [-json JSON]
               [-output OUTPUT] [-directed DIRECTED] [-saving SAVING]

optional arguments:
  -h, --help          show this help message and exit
  -seed SEED          seed for random.seed() [default = VxV]
  -routes ROUTES      file with routes to test [deafult = '']
  -json JSON          file for Graph [default = tramwaje.json]
  -output OUTPUT      save routes [deafult = '']
  -directed DIRECTED  is digraph? [deafult = False]
  -saving SAVING      enable djikstra/bellman temp save? [deafult = T]
```
Przykłady:
```
>python main.py
TEST Z ZAPISYWANIEM
Djikstra:: 0.289585454
Bellman-Ford:: 2.1552109760000002
Floyd-Warshall:: 8.382051243

>python main.py -saving=F
TEST BEZ ZAPISYWANIA
Djikstra:: 43.224764549
Bellman-Ford:: 328.013519441
Floyd-Warshall:: 8.569382306000023

>python main.py -seed=123 -output=123.txt

>python main.py -routes=123.txt
TEST Z ZAPISYWANIEM
Djikstra:: 0.30090964899999995
Bellman-Ford:: 3.657082779
Floyd-Warshall:: 8.358419479

>python main.py -routes=all.txt
TEST Z ZAPISYWANIEM
Djikstra:: 0.317065445
Bellman-Ford:: 3.815838185
Floyd-Warshall:: 8.281261228

```