import queue
import random
import time


requests_queue = queue.Queue()

request_id = 1

def generate_request():
    global request_id

    new_request = f"Request #{request_id}"
    request_id += 1

    requests_queue.put(new_request)
    print(f"Заявка {new_request} додана до черги")

def process_request():
    if not requests_queue.empty():
        current_request = requests_queue.get()
        print(f"Обробляється {current_request}")
    else:
        print("Чергa пуста, немає заявок для обробки")

def main():
    while True:
        for _ in range(random.randint(0, 2)):
            generate_request()
        
        process_request()
        
        time.sleep(1)


if __name__ == "__main__":
    main()
