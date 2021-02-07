def count_min_cost(N, price:list):
    cost = [float("-inf"), price[1], price[1]+price[2]] + [0]*(N-2)
    for i in range(3, N+1):
        cost[i] = price[i] + min(cost[i-1], cost[i-2])
    return cost[N]

print(count_min_cost(6, [1, 2, 2, 3, 4, 40, 70, 112]))