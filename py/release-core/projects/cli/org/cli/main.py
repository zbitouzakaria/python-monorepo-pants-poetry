from org.lib import Foo
from rich import print


def main() -> None:
    print(Foo(name="cli"))


if __name__ == "__main__":
    main()
