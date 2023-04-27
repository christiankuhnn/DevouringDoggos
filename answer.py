def knapsack(items, capacity):
    n_items = len(items)
    table = [[0 for _ in range(capacity + 1)] for _ in range(n_items + 1)]

    for i in range(1, n_items + 1):
        item_name, item_weight, item_value = items[i - 1]
        for w in range(1, capacity + 1):
            if item_weight > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w], item_value + table[i - 1][w - item_weight])

    # Backtrack to find which items were selected
    selected_items = []
    w = capacity
    for i in range(n_items, 0, -1):
        if table[i][w] != table[i - 1][w]:
            item_name, item_weight, item_value = items[i - 1]
            selected_items.append(item_name)
            w -= item_weight

    # Print the result
    for item in reversed(selected_items):
        print(item)
    print(table[n_items][capacity])

if __name__ == '__main__':
    n_items = int(input())
    capacity = int(input())
    items = []
    for _ in range(n_items):
        line = input().split()
        item_name = line[0]
        item_weight = int(line[1])
        item_value = int(line[2])
        items.append((item_name, item_weight, item_value))
    knapsack(items, capacity)
