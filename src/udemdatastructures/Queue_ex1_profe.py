import threading
from collections import deque
import random
import time

call_center_queue = deque()
queue_lock = threading.Lock()

def call_center():
    call_id = 1

    while call_id <= 10:
        time.sleep(random.uniform(0.5, 1.5))
        with queue_lock:
            call_center_queue.append(f"Call {call_id}")
            print(f"Call {call_id} added to the queue")
        call_id += 1

def consumer():
    while True:
        with queue_lock:
            if call_center_queue:
                current_call = call_center_queue.popleft()
                print(f"Handling {current_call} from Call Center")

        time.sleep(0.1)

def main():
    call_center_thread  = threading.Thread(target=call_center)
    consumer_thread = threading.Thread(target=consumer, daemon=True)

    call_center_thread.start()
    consumer_thread.start()

if __name__ == "__main__":
    main()