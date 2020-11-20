from threading import Thread, Lock

a = 0
mutex = Lock()


def function(arg):
    global a
    for _ in range(arg):
        mutex.acquire()
        a += 1
        mutex.release()


def main():
    threads = []
    for i in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        threads.append(thread)

    [t.join() for t in threads]
    print("----------------------", a)  # ???


main()
