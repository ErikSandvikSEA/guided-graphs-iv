class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Nonexistent vertex")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        # create empty queue
        q = Queue()
        # add starting vertex id
        q.enqueue(starting_vertex_id)
        # create set for visited verts
        visited = set()
        # while queue is not empty
        while q.size() > 0:
            # deque a vert
            v = q.dequeue()
            # if not visited
            if v not in visited:
                # mark as visited
                visited.add(v)
            # add all neighbors to queue
            for neighbor in self.get_neighbors(v):
                q.enqueue(neighbor)

    def bfs(self, starting_vertex_id, target_vertex_id):
        pass

    # Create an empty queue and enqueue A PATH TO the starting vertex ID
    # Create a Set to store visited vertices
    # While the queue is not empty...
    # Dequeue the first PATH
    # Grab the last vertex from the PATH
    # If that vertex has not been visited...
    # CHECK IF IT'S THE TARGET
    # IF SO, RETURN PATH
    # Mark it as visited...
    # Then add A PATH TO its neighbors to the back of the queue
    # COPY THE PATH
    # APPEND THE NEIGHOR TO THE BACK

    def dft_recursive(self, starting_vertex_id, visited=None):
        if visited is None:
            visited = set()
        visited.add(starting_vertex_id)
        print(visited)
        print(starting_vertex_id)
        for neighbor in self.vertices[starting_vertex_id]:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)

    def dfs_recursive(self, starting_vert, ending_vert, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(starting_vert)
        # path = path + [starting_vert] #subtly makes a copy of the path
        # more explicit way ↓
        path = list(path)  # make a copy
        path.append(starting_vert)

        if starting_vert == ending_vert:
            return path

        for neighbor in self.get_neighbors(starting_vert):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, ending_vert, visited, path)
                if new_path is not None:
                    return new_path

        return None  # if no path is found


g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(4, 3)
g.add_edge(3, 6)
g.add_edge(6, 5)
g.add_edge(5, 4)

# print(g.vertices)
# g.bft(3)
# g.dft_recursive(1)
print(g.dfs_recursive(1, 6))


# --------------------------------------- what self.vertices ends up looking like
# self.vertices = {
#     1: set(2),
#     2: set(1)
# }
