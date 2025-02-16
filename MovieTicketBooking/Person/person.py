from abc import ABC,abstractmethod


class Iperson(ABC):

    @abstractmethod
    def get_name(self):
        pass

