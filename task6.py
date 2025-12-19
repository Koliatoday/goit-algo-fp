"""Using greedy and dynamic programming algorithms to solve the
   knapsack problem"""


def dynamic_programming(data: dict, max_cost: int) -> tuple[list[str], int, int]:
    """Choose dishes with maximum calories using dynamic programming approach"""
    # Convert dictionary to list for DP
    names = list(data.keys())
    costs = [data[name]["cost"] for name in names]
    calories = [data[name]["calories"] for name in names]
    n = len(names)

    # DP table: dp[i][c] = max calories using first i items with cost limit c
    dp = [[0] * (max_cost + 1) for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):
        for c in range(max_cost + 1):
            if costs[i-1] <= c:
                dp[i][c] = max(dp[i-1][c], dp[i-1][c - costs[i-1]] + calories[i-1])
            else:
                dp[i][c] = dp[i-1][c]

    # Recover selected items
    products = []
    total_calories = dp[n][max_cost]
    total_cost = 0

    c = max_cost
    for i in range(n, 0, -1):
        # If value comes from using this item
        if dp[i][c] != dp[i-1][c]:
            products.append(names[i-1])
            c -= costs[i-1]
            total_cost += costs[i-1]

    # To restore original order
    products.reverse()

    return products, total_cost, total_calories


def greedy_algorithm(data: dict, max_cost: int) -> tuple[list[str], int, int]:
    """Choose dishes with maximum calories to cost ratio using greedy approach"""
    ret_cost = 0
    products = []
    ret_calories = 0

    # Add ratio field to the data dictionary
    for key in data.keys():
        data[key]["ratio"] = data[key]["calories"]/data[key]["cost"]

    # Sort data by ratio in descending order
    sort_data = sorted(data.items(), key=lambda val: val[1]["ratio"], reverse=True)

    for el in sort_data:
        el_cost = el[1]["cost"]
        if el_cost < max_cost:
            products.append(el[0])
            max_cost -= el_cost
            ret_cost += el_cost
            ret_calories += el[1]["calories"]

    return products, ret_cost, ret_calories


def main():
    """Demonstrates greedy and dynamic programming approaches"""

    items = {
        "pizza":     {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog":   {"cost": 30, "calories": 200},
        "pepsi":     {"cost": 10, "calories": 100},
        "cola":      {"cost": 15, "calories": 220},
        "potato":    {"cost": 25, "calories": 350}
    }

    max_cost = 114

    prod, tot_cost, calories = greedy_algorithm(items, max_cost)
    print("Greedy approach results:")
    print(f"With {max_cost} cents your choice is {prod} with total "
          f"cost = {tot_cost}, total calories = {calories}")

    print("Dynamic approach results:")
    prod, tot_cost, calories = dynamic_programming(items, max_cost)
    print(f"With {max_cost} cents your choice is {prod} with total "
          f"cost = {tot_cost}, total calories = {calories}")


if __name__ == "__main__":
    main()
