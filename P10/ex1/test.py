def test(n: int):
    def test1(y: int):
        return n + y
    return test1


if __name__ == "__main__":
    f = test(6)(7)
    print(f)