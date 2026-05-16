import heapq


def min_cost_connect_cables(cables):
    if len(cables) <= 1:
        return 0

    heap = cables[:]
    heapq.heapify(heap)

    total_cost = 0
    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        cost = first + second
        total_cost += cost
        heapq.heappush(heap, cost)
        print(
            f"  З'єднуємо {first} + {second} = {cost}  (загальні витрати: {total_cost})"
        )

    return total_cost


def run():
    cables = [4, 3, 2, 6]

    print("=== Завдання 3 ===")
    print(f"Кабелі: {cables}")
    result = min_cost_connect_cables(cables)
    print(f"Мінімальні загальні витрати: {result}")
