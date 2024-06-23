from hello import hello

def test_hello():
    assert hello("David") == "hello, David":


def test_default():
    assert hello() == "hello, world"

def test_arguments():

    for name in ["Harry", "Hermoine", "Ron"]:
        assert hello(name) == f"hello, {name}"
