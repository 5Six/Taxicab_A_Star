    def a_star(map):
        explored = []
        to_explore = [(0, 0)]
        g_cost = {(0, 0): 0}
        h_cost = {(0, 0): n + m}
        f_cost = {(0, 0): n + m}
        came_from = {}

        while to_explore:
            closest = to_explore[0]
            for node in to_explore:
                if f_cost[node] < f_cost[closest]:
                    closest = node

            to_explore.remove(closest)
            explored.append(closest)

            if closest == (n, m):
                return g_cost[(n, m)] + 1

            if closest[0] > 0 and map[closest[0] - 1][closest[1]] == 0 and (closest[0] - 1, closest[1]) not in explored:
                if (closest[0] - 1, closest[1]) not in to_explore or g_cost[closest]+1 < g_cost[(closest[0] - 1, closest[1])]:
                    g_cost[(closest[0] - 1, closest[1])] = g_cost[closest] + 1
                    h_cost[(closest[0] - 1, closest[1])] = n + m - (closest[0] - 1) - closest[1]
                    f_cost[(closest[0] - 1, closest[1])] = g_cost[(closest[0] - 1, closest[1])] + h_cost[(closest[0] - 1, closest[1])]
                    came_from[(closest[0] - 1, closest[1])] = closest

                    if (closest[0] - 1, closest[1]) not in explored:
                        to_explore.append((closest[0] - 1, closest[1]))

            if closest[0] < n and (closest[0] + 1, closest[1]) not in explored and map[closest[0] + 1][closest[1]] == 0:
                if (closest[0] + 1, closest[1]) not in to_explore or g_cost[closest] + 1 < g_cost[(closest[0] + 1, closest[1])]:
                    g_cost[(closest[0] + 1, closest[1])] = g_cost[closest] + 1
                    h_cost[(closest[0] + 1, closest[1])] = n + m - (closest[0] + 1) - closest[1]
                    f_cost[(closest[0] + 1, closest[1])] = g_cost[(closest[0] + 1, closest[1])] + h_cost[(closest[0] + 1, closest[1])]
                    came_from[(closest[0] + 1, closest[1])] = closest

                    if (closest[0] + 1, closest[1]) not in explored:
                        to_explore.append((closest[0] + 1, closest[1]))

            if closest[1] > 0 and (closest[0], closest[1] - 1) not in explored and map[closest[0]][closest[1] - 1] == 0:
                if (closest[0], closest[1] - 1) not in to_explore or g_cost[closest] + 1 < g_cost[(closest[0], closest[1] - 1)]:
                    g_cost[(closest[0], closest[1] - 1)] = g_cost[closest] + 1
                    h_cost[(closest[0], closest[1] - 1)] = n + m - closest[0] - (closest[1] - 1)
                    f_cost[(closest[0], closest[1] - 1)] = g_cost[(closest[0], closest[1] - 1)] + h_cost[(closest[0], closest[1] - 1)]
                    came_from[(closest[0], closest[1] - 1)] = closest

                    if (closest[0], closest[1] - 1) not in explored:
                        to_explore.append((closest[0], closest[1] - 1))

            if closest[1] < m and (closest[0], closest[1] + 1) not in explored and map[closest[0]][closest[1] + 1] == 0:
                if (closest[0], closest[1] + 1) not in to_explore or g_cost[closest] + 1 < g_cost[(closest[0], closest[1] + 1)]:
                    g_cost[(closest[0], closest[1] + 1)] = g_cost[closest] + 1
                    h_cost[(closest[0], closest[1] + 1)] = n + m - closest[0] - (closest[1] + 1)
                    f_cost[(closest[0], closest[1] + 1)] = g_cost[(closest[0], closest[1] + 1)] + h_cost[(closest[0], closest[1] + 1)]
                    came_from[(closest[0], closest[1] + 1)] = closest

                    if (closest[0], closest[1] + 1) not in explored:
                        to_explore.append((closest[0], closest[1] + 1))
