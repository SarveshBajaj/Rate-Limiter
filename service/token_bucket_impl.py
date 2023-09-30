from service.algo import Algo
import threading
import time

class TokenBucketImpl(Algo):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(TokenBucketImpl, cls).__new__(cls)
                cls._instance.tokens = {} 
                threading.Thread(target=cls._instance.refill_tokens).start()
        return cls._instance
        
        
    def serveRequest(self, ipAddress):
        with TokenBucketImpl._lock:
            if ipAddress not in self.tokens:
                self.tokens[ipAddress] = 10
            
            if self.tokens[ipAddress] > 0:
                self.tokens[ipAddress] -= 1
            else:
                print ("Too many requests")
                return "Too many requests (429)"
        
        time.sleep(5)
        return "Serving your request now"
    
    def refill_tokens(self):
        while True:
            time.sleep(1)
            with TokenBucketImpl._lock:
                print("Increasing val")
                for ip in self.tokens:
                    self.tokens[ip] = min(self.tokens[ip] + 1, 10)