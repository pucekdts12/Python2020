def cost_path(graph,START,END):
  distance = dict()
  prev = dict()
  for v in graph:
    distance[v] = float('inf')
    prev[v] = None


  distance[START] = 0

  for i in range(len(graph.nodes)-1):
    for u,v,c in graph.edges:
      if distance[u] + c < distance[v]:
        distance[v] = distance[u] + c
        prev[v] = u
  path=END
  cur = prev[END]
  while cur!=None:
    path=f'{cur}->{path}'
    cur = prev[cur]

  return(distance[END],path)


def cost_only(graph,START):
  distance = dict()
  for v in graph:
    distance[v] = float('inf')
  distance[START] = 0
  for i in range(len(graph.nodes)-1):
    for u,v,c in graph.edges:
      if distance[u] + c < distance[v]:
        distance[v] = distance[u] + c
  return distance


def test(graph,routes):
  result={}
  for s,e in routes:
    result[f'{s}=>{e}'] = cost_only(graph,s)[e]
  return result

def test_with_saving(graph,routes):
  result={}
  saved={}
  for s,e in routes:
    if s not in saved:
      saved[s] = cost_only(graph,s)
    result[f'{s}=>{e}'] = saved[s][e]
  return result