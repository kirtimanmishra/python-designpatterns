from dataclasses import dataclass


@dataclass(frozen=True)
class A:
    name: str


class B:
    name: str

    def __init__(self, name: str = "b") -> None:
        self.name = name

    def __str__(self) -> str:
        return f"B name:{self.name}"


def main():
    a = A("A")
    print("*** a ** ", a.name)
    print("*** a ** ", str(a))
    # a.name = "A_a"
    b = B(name="B")
    b.name = "B_b"
    print("*** B ** ", b.name)
    print("*** B ** ", str(b))


if __name__ == "__main__":
    main()
