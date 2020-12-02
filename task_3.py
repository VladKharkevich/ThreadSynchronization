from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class Counter:
    calculated_value = 0


mutex = Lock()


def incrementor(number_of_increments, counter):
    for _ in range(number_of_increments):
        with mutex:
            counter.calculated_value += 1


def main():
    count_of_workers = 5
    counter = Counter()
    with ThreadPoolExecutor(max_workers=count_of_workers) as executor:
        for _ in range(count_of_workers):
            executor.submit(incrementor, 1000000, counter)
    print("----------------------", counter.calculated_value)  # ???


main()
