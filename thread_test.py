from threading import Thread


def main():
    thread = Thread(target=thread_process1())
    thread.start()



def thread_process1():
    print("thread p 1")
    thread = Thread(target=thread_process2())
    thread.start()


def thread_process2():
    print("thread p 2")


if __name__ == "__main__":
    main()