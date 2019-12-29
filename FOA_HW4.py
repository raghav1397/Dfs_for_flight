import pandas as pd
import numpy as np
import time

df = pd.read_csv('./Data.csv')

cities = {0:'LAX', 1:'DEN', 2:'PHX', 3:'SEA',4:'SFO', 5:'ORD', 6:'ATL', 7:'IAD', 8:'BOS', 9:'JFK'}
cities1 = {'LAX':0, 'DEN':1, 'PHX':2, 'SEA':3,'SFO':4 , 'ORD':5, 'ATL':6, 'IAD':7, 'BOS':8, 'JFK':9}

for x in range(len(df['Finish_Time'])):
    df['Finish_Time'][x] = df['Finish_Time'][x].rjust(5,'0')
    
df = df.sort_values(by=['Finish_Time'])

routes = {}

for x in range(len(df['Start_Time'])):
    df['Start_Time'][x] = df['Start_Time'][x].rjust(5,'0')
    
for x in range(len(cities1)):
    for y in range(len(cities1)):
        temp_df = df[(df['Source_City']==cities[x])]
        k1 = list(temp_df['Id'])
        k2 = list(temp_df['Start_Time'])
        k3 = list(temp_df['Finish_Time'])
        k4 = list(temp_df['Capacity'])
        k5 = list(temp_df['Source_City'])
        k6 = list(temp_df['Destination_City'])
        k = [k1, k2, k3, k4, k5, k6]
        k = np.asarray(k)
        k = k.T
        routes[str(x)] = k
        
def Ford_Fulkerson(routes, maxFlow):
    visited = [False, False, False, False, False, False, False, False, False, False]
    path = []
    source = routes['0'][0]
    dest_list = routes[str(cities1[source[5]])]
    path.append(source)
    visited[0] = True
    path = DFS(dest_list, source, visited, path, None, None)
    if(len(path) > 0):
        pathFlow = int(path[0][3])
        for i in range(len(path)):
            if pathFlow > int(path[i][3]):
                pathFlow = int(path[i][3])
        maxFlow = maxFlow + pathFlow
        for i in range(len(path)):
            var = routes.get(str(cities1[path[i][4]]))   
            zero_capacity = []
            for x in range(len(var)):
                if var[x][0] == path[i][0]:
                    value = int(var[x][3]) - pathFlow
                    if value == 0:
                        zero_capacity.append(x)
                    else:
                        var[x][3] = str(value)
            for x in range(len(zero_capacity)):
                var = np.delete(var, zero_capacity[x], 0)

            routes.update({str(cities1[path[i][4]]) : var})
        maxFlow = Ford_Fulkerson(routes, maxFlow)
    return maxFlow
        
def DFS(dest_list, source, visited, path, prev, prev1):
    init_length = len(path)
    
    source_end_time = source[2]
    
    if visited[len(cities1) - 1] == True:
        return path

    
    if source[5] == 'JFK':
        visited[len(cities1) - 1] = True
        return path
    
    for x in range(len(dest_list)):
        start_time = dest_list[x][1]
       
        if start_time >= source_end_time and visited[cities1[dest_list[x][5]]] == False:
            
            path.append(dest_list[x])            
            visited[cities1[dest_list[x][4]]] = True
            if dest_list[x][5]=='JFK':
                visited[len(cities1) - 1] = True
            
            source = dest_list[x]
            if prev is not None:
                visited[cities1[prev[5]]] = False
                prev1 = prev
                prev = None
            break
    final_length = len(path)
    
    if final_length == 0:
        return path
    
    if(final_length == init_length):
        to_remove = path[len(path)-1]
        if prev is not None:
            visited[cities1[prev[5]]] = False
        prev = path.pop(len(path)-1)
        if prev1 is not None:
            visited[cities1[prev1[5]]] = True
        visited[cities1[to_remove[4]]] = False
        visited[cities1[to_remove[5]]] = True
        src = routes[str(cities1[source[4]])]
        if len(path) > 0:
            source = path[len(path) - 1]
            dest_list  = src            
        else:
            for i in range(len(src)):
                if visited[cities1[src[i][5]]] == False:
                    source = src[i]
                    dest_list = routes[str(cities1[source[5]])]
                    path.append(source)
                    visited[cities1[src[i][4]]] = True
                    prev = None
                    if cities1[src[i][5]] == len(cities1) - 1:
                        visited[len(cities1) - 1] == True
                    break
            if len(path) == 0:
                return path
    else:
        dest_list = routes[str(cities1[source[5]])]
    path = DFS(dest_list, source, visited, path, prev, prev1)
    return path


maxFlow = 0 

print('Maximum Flow = ' + str(Ford_Fulkerson(routes, maxFlow))) 
