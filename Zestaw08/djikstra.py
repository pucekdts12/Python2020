def cost_path(graph,START,END):
  costs = { k:float('inf') for k in graph }
  done = {}
  paths = { k:[] for k in graph }

  paths[START].append(START)
  costs[START] = 0

  # print(paths)
  while len(costs)>0:

    parent = min(costs,key=costs.get)
    cost = costs.pop(parent)
    done[parent]=cost
    for s,t,c in graph[parent].edges():
      try:
        if (cost+c)<costs[t]:
          costs[t]=cost+c
          paths[t]=paths[parent] + [t]
      except:
        pass

  
  return(done[END],'->'.join(paths[END]))
  
def cost_only(graph,START):
  costs = { k:float('inf') for k in graph }
  done = {}
  costs[START] = 0
  while len(costs)>0:
    parent = min(costs,key=costs.get)
    cost = costs.pop(parent)
    done[parent]=cost
    for s,t,c in graph[parent].edges():
      try:
        if (cost+c)<costs[t]:
          costs[t]=cost+c
      except:
        pass
  return done


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