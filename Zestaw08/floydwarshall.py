def cost_only(graph):
  import copy
  prev = {}
  for l1 in graph:
    prev[l1] = {}
    for l2 in graph:
      if graph[l2] in graph[l1]._edges:
        prev[l1][l2] = graph[l1][ graph[l2] ]
      else:
        prev[l1][l2] = float('inf')
    prev[l1][l1] = 0

  for current in graph:
    next={}
    for l1 in graph:
      next[l1] = {}
      for l2 in graph:
        if current in (l1,l2):
          next[l1][l2] = prev[l1][l2]
        else:
          tmp = prev[l1][current] + prev[current][l2]
          if tmp < prev[l1][l2]:
            next[l1][l2] = tmp
          else:
            next[l1][l2] = prev[l1][l2]
    prev = copy.deepcopy(next)

  return prev

def test(graph,routes):
  costs = cost_only(graph)
  result={}
  for s,e in routes:
    result[f'{s}=>{e}'] = costs[s][e]
  return result

