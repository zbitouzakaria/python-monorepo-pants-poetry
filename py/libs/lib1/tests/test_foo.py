import json

from org.lib import Foo


def test_foo() -> None:
    got = json.loads(Foo(name="adrian").json())
    expected = {"name": "adrian"}
    print("changed test lib")
    assert got == expected
