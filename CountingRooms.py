import networkx as nx

n, m = map(int, input().split())

room = []
for _ in range(n):
    room.append(input())


deltas = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# print(room)
G = nx.Graph()
for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] == ".":
            G.add_edge((j, i), (j, i))
            for d in deltas:
                x = j + d[0]
                y = i + d[1]
                if 0 <= y < len(room) and 0 <= x < len(room[0]) and room[y][x] == ".":
                    G.add_edge((j, i), (x, y))


sub = nx.number_connected_components(G)
print(sub)
