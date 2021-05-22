graph = {
    'a': set(['b', 'c', 'd']),
    'b': set(),
    'c': set('e'),
    'd': set(['e', 'f']),
    'e': set(['a', 'f']),
    'f': set(),
}

# def main_function(current_vertex):
#     visited = set()
#     def print_graph(current_vertex):
#         print(current_vertex)
#         visited.add(current_vertex)
#         # Recurse on the children
#         for neighbor in graph[current_vertex]:
#             if neighbor not in visited:
#                 print_graph(neighbor)

#     print_graph(current_vertex)

def print_graph(current_vertex, visited):
    print(current_vertex)
    visited.add(current_vertex)
    print(visited)
    # Recurse on the children
    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            print_graph(neighbor, visited)


def iterative_dfs(start_vertex, target_vertex):
    stack = []
    stack.append((start_vertex, []))
    visited = set()


    while len(stack) > 0:
        # process vertices on the stack, and queue up other ones
        current_vertex, current_path = stack.pop()
        visited.add(current_vertex)

    current_path.append(current_vertex)

    # Check if the current vertex is our target
    if current_vertex == target_vertex:
        print("Found")
        return current_path

    for neighbor in graph[current_vertex]:
        if neighbor not in visited:
            stack.append((neighbor, current_path.copy))


# print(iterative_dfs('a', 'f'))

def iterative_bfs(start_vertex, target_vertex):
    queue = []
    queue.append((start_vertex, []))
    visited = set()


    while len(queue) > 0:
        # process vertices on the stack, and queue up other ones
        current_vertex, current_path = queue.pop(0)
        # if current_vertex in visited:
        #     continue

    visited.add(current_vertex)
    current_path.append(current_vertex)

    # Check if the current vertex is our target
    if current_vertex == target_vertex:
        print("Found")
        return current_path

    for neighbor in graph[current_vertex]:
        queue.append((neighbor, current_path.copy()))


print(iterative_bfs('a', 'f'))