from service.algo import Algo

class FixedWindowCounterImpl(Algo):
    def serveRequest(self, ipAddress):
        return "serving"
    
