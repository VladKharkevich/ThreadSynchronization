from concurrent.futures import ThreadPoolExecutor
from threading import Lock


class A:
    a = 0


mutex = Lock()


def function(arg, a):
    for _ in range(arg):
        with mutex:
            a.a += 1


def main():
    count_of_workers = 5
    a = A()
    with ThreadPoolExecutor(max_workers=count_of_workers) as executor:
        for _ in range(count_of_workers):
            executor.submit(function, 1000000, a)
    print("----------------------", a.a)  # ???


main()
