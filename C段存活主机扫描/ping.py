import threading
import Queue
import subprocess
import sys

class Ping(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        result = []
        while not self._queue.empty():
            ip = self._queue.get()
            result = subprocess.Popen('ping -n 2 %s'%ip,stdout=subprocess.PIPE)
            data = result.stdout.read().decode('gbk')
            if "TTL" in data:
                print(ip)


def main():
    threads = []
    threads_count = 50
    queue = Queue.Queue()

    for i in range(1,255):
        queue.put('106.75.137.' + str(i))

    for i in range(threads_count):
        threads.append(Ping(queue))

    for i in threads:
        i.start()

    for i in threads:
        i.join()

if __name__ == "__main__":
    main()
