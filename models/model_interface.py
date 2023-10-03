from abc import ABC, abstractmethod

class ModelInterface(ABC):
    @abstractmethod
    def interact(self, prompt):
        pass

    @abstractmethod
    def getName(self):
        pass