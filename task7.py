"""Simulates rolling two dice multiple times and shows frequency
   distribution"""

import random
import matplotlib.pyplot as plt


def dice(repeat: int) -> dict:
    """Simulates rolling two dice multiple times
    Args:
        repeat (int): Number of times to roll two dices
    Returns:
        dict: Dictionary with the sum of the two dices as the key
              and the frequency of the sum as the value.
    """
    result = {x: 0 for x in range(2, 13)}
    for _ in range(repeat):
        val = [random.randint(1, 6) for _ in range(2)]
        result[sum(val)] += 1

    result = {k: v * (100 / repeat) for k, v in result.items()}

    return result


def main():
    """Main function to simulate rolling two dice multiple times
    and show frequency distribution"""

    ref_data = {2: 2.78,  3: 5.56,  4: 8.33,  5: 11.11, 6: 13.89,
                7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56,
                12: 2.78}
    repeat = 1000
    random.seed(42)
    result = dice(repeat)

    # Prepare data for plotting
    x = list(range(2, 13))
    result_percents = [result[k] for k in x]
    ref_percents = [ref_data[k] for k in x]

    plt.figure(figsize=(10, 6))
    plt.plot(x, result_percents, marker='o', label='Simulated')
    plt.plot(x, ref_percents, marker='s', label='Theoretical')
    plt.xlabel('Sum of Two Dice')
    plt.ylabel('Frequency (%)')
    plt.title(f'Distribution of Dice Sums ({repeat} Repeats)')
    plt.xticks(x)
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
