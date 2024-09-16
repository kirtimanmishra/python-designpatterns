from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Observer(ABC):
    name: str

    @abstractmethod
    def notify(self, value: str) -> None:
        pass


@dataclass
class ConcreteObserver(Observer):
    def notify(self, value: str) -> None:
        print(f"{self.name} is notfied with {value}")


@dataclass
class Subject:
    observers: list[Observer] = field(default_factory=list)
    # used for handling using mutable default arguments (like a list or a dictionary)
    # def __init__(self, observers=[]):
    #     self.observers = observers
    # The list observers=[] is created once when the function is defined, not each time the function is called.
    # So, every time a new instance of Subject is created, it reuses the same list for observers

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        if observer not in self.observers:
            return ValueError(f"{observer.name} not found")
        self.observers.remove(observer)

    def notify(self, value: str):
        for observer in self.observers:
            observer.notify(value=value)


def main():
    subject = Subject()
    observer1 = ConcreteObserver("observer1")
    observer2 = ConcreteObserver("observer2")
    subject.attach(observer1)
    subject.attach(observer2)
    subject.notify("updated")


if __name__ == "__main__":
    main()
