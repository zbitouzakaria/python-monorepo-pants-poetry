from time import sleep

import orjson
from org.lib import Foo

import django

def main(max_iters: float | None) -> None:
    print(django.VERSION)
    iter = 0
    if max_iters is None:
        max_iters = float("inf")
    while iter < max_iters:
        iter += 1
        print(orjson.dumps(Foo(name="app").dict()).decode())
        sleep(1)


if __name__ == "__main__":
    main()
