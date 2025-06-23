import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    counts = {sum_: 0 for sum_ in range(2, 13)}
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        counts[total] += 1
    probabilities = {sum_: count / num_rolls for sum_, count in counts.items()}
    return probabilities


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"\nСимуляція для {accuracy} кидків:")
        probabilities = simulate_dice_rolls(accuracy)
        print(f"{'Сума':^6} | {'Ймовірність':^12}")
        print("-" * 21)
        for s in sorted(probabilities):
            print(f"{s:^6} | {probabilities[s]*100:>9.2f} %")
