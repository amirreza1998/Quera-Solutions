import threading
import queue
import time


def input_thread(input_queue):
    # Simulated input values
    inputs = [
        "5 2",  # n and q
        # Additional inputs can be added here if needed
    ]

    for line in inputs:
        input_queue.put(line)
        time.sleep(1)  # Wait for a bit before putting the next line

    # Optionally, put a sentinel value to indicate the end of input
    input_queue.put(None)


def process_input(input_queue):
    # Read n and q
    line = input_queue.get()
    if line is None:
        return False



    ###---------your code----------###
    n, q = map(int, line.split(" "))
    print(f"n: {n}, q: {q}")

    # Read the list a
    line = input_queue.get()
    if line is None:
        return False
    a = list(map(int, line.split(" ")))
    print(f"a: {a}")
    ###----------------------------###

    return True  # Indicate that processing was successful


def main():
    input_queue = queue.Queue()

    # Start the input thread
    thread = threading.Thread(target=input_thread, args=(input_queue,))
    thread.start()

    while True:
        if not process_input(input_queue):
            break  # Exit if the processing indicates an end condition

    thread.join()


if __name__ == "__main__":
    main()