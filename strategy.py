from abc import ABC, abstractmethod
from typing import Any


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)


class Context:
    def __init__(self, strategy_name: str) -> None:
        self.strategy = self.get_strategy(strategy_name=strategy_name)

    def get_strategy(self, strategy_name: str) -> Strategy:
        strategy_cls = globals().get(strategy_name)
        if strategy_cls is None:
            raise ValueError(f"Strategy '{strategy_name}' not found")
        return strategy_cls()

    def set_strategy(self, strategy_name: str) -> None:
        self.strategy = self.get_strategy(strategy_name=strategy_name)

    def execute_strategy(self, data: Any):
        return self.strategy.execute(data)


def main():
    context = Context("ConcreteStrategyA")
    result = context.execute_strategy([3, 1, 4])
    print("**** result *** ", result)

    context.set_strategy("ConcreteStrategyB")
    result = context.execute_strategy([3, 1, 4])
    print("**** result *** ", result)


if __name__ == "__main__":
    main()
