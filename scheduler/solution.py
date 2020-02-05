import heapq
import time


# Alternative to threading.Timer
class Scheduler:
    def __init__(self, interval_millis=10):
        self.__tasks = []
        self.__interval = interval_millis / 1000

    def schedule(self, f, delay):
        heapq.heappush(self.__tasks, (self.__current_time_millis() + delay, f))

    def run(self):
        while self.__tasks:
            if self.__tasks[0][0] <= self.__current_time_millis():
                # TODO: Run in separate thread?
                fn = heapq.heappop(self.__tasks)[1]
                try:
                    fn()
                except Exception as e:
                    print(str(e))
            else:
                time.sleep(self.__interval)

    @staticmethod
    def __current_time_millis():
        return int(round(time.time() * 1000))
