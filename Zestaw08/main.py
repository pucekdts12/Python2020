import json
import argparse
import ast
from timeit import Timer
import itertools as it
import random

from Graph import NonGraph
from Graph import Graph


# import djikstra as dj
# import bellmanford as bf
# import floydwarshall  as fw

import djikstra
import bellmanford
import floydwarshall


def speed_test(fn,graph,routes,times=1):
  t1 = Timer(lambda: fn(graph,routes))
  return t1.timeit(number = times)
  


arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-seed",help="seed for random.seed() [default = VxV]",type=int,default=-1)
arg_parser.add_argument("-routes",help="file with routes to test [deafult = '']",type=str,default="")
arg_parser.add_argument("-json",help="file for Graph [default = tramwaje.json]",type=str,default="tramwaje.json")
arg_parser.add_argument("-output",help="save routes [deafult = '']",type=str,default="")
arg_parser.add_argument("-directed",help="is digraph? [deafult = False]",type=bool,default=False)
arg_parser.add_argument("-saving",help="enable djikstra/bellman temp save? [deafult = T]",type=str,default='T')

args = arg_parser.parse_args()


data = json.load(open(args.json,"r",encoding='utf-8'))

if args.directed:
  graph = Graph()
else:
  graph = NonGraph()
 

# Kontrukcja grafu z wczytanego JSON'a
for t in data["tramwaje"]:
  przystanki = t['tprzystanki']
  for j in range(len(przystanki)-1):
    l1 = przystanki[j]['name']
    l2 = przystanki[j+1]['name']
    graph.addEdge(l1,l2,1)


if args.routes!="":
  f = open(args.routes,"r")
  routes = ast.literal_eval(f.read())
else:
  routes = list(it.permutations(graph.nodes.keys(),r=2)) # 
  if args.seed!=-1:
    random.seed(args.seed)
    random.shuffle(routes)
    routes = routes[:len(routes)//4]

if args.output!="":
  f = open(args.output,"w")
  f.write(str(routes))
  f.close()
  exit()



if args.saving=='T':
  print('TEST Z ZAPISYWANIEM')
  print('Djikstra::',speed_test(djikstra.test_with_saving,graph,routes))
  print('Bellman-Ford::',speed_test(bellmanford.test_with_saving,graph,routes))
  print('Floyd-Warshall::',speed_test(floydwarshall.test,graph,routes))
else:
  print('TEST BEZ ZAPISYWANIA')
  print('Djikstra::',speed_test(djikstra.test,graph,routes))
  print('Bellman-Ford::',speed_test(bellmanford.test,graph,routes))
  print('Floyd-Warshall::',speed_test(floydwarshall.test,graph,routes))