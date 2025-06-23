def greedy_algorithm(sum, items):
    items = [(name, data) for name, data in items.items()]
    for i in range(len(items)):
        items[i][1]["koef"] = items[i][1]["calories"] / items[i][1]["cost"]
    items = sorted(items, key=lambda x: x[1]["koef"], reverse=True)
    menu = {}
    for el in items:
        count = sum // el[1]["cost"]
        if count > 0:
            menu[el[0]] = sum // el[1]["cost"]
            sum -= el[1]["cost"] * menu[el[0]]
            if sum == 0:
                break
    return menu


def dynamic_programming(amount, items, memo=None):
    if memo is None:
        memo = {}
    if amount == 0:
        return {"total_calories": 0, "combo": {}}
    if amount in memo:
        return memo[amount]
    best_result = {"total_calories": 0, "combo": {}}
    for name, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        if cost <= amount:
            sub_result = dynamic_programming(amount - cost, items, memo)
            total_calories = sub_result["total_calories"] + calories
            if total_calories > best_result["total_calories"]:
                best_result = {
                    "total_calories": total_calories,
                    "combo": sub_result["combo"].copy(),
                }
                best_result["combo"][name] = best_result["combo"].get(name, 0) + 1
    memo[amount] = best_result
    return best_result


def main():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }
    print(greedy_algorithm(805, items))
    print(dynamic_programming(805, items)["combo"])


main()
