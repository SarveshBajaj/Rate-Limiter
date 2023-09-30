from abc import ABC, abstractmethod

class Algo(ABC):
    @abstractmethod
    def serveRequest(self, ipAddress):
        pass