from service.algo import Algo
from collections import defaultdict
import threading
import time

class FixedWindowCounterImpl(Algo):
    _instance = None
    _threshold = 5
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FixedWindowCounterImpl, cls).__new__(cls)
            cls._instance.request_counts = defaultdict(lambda: defaultdict(int)) 
        return cls._instance
    
    
    def serveRequest(self, ipAddress):
        current_window_start = int(time.time()) // 10 * 10  #window size 10 seconds
        
        user_request_count = self.request_counts[ipAddress][current_window_start]
        
        if user_request_count > self._threshold:
            print ("Too many requests")
            return "Too many requests (429)"
        
        self.request_counts[ipAddress][current_window_start] += 1
        time.sleep(5)
        return "Serving your request now"
