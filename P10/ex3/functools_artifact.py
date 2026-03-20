from functools import reduce, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ope = getattr(operator, operation, None)
    if not ope:
        raise AttributeError
    if all(isinstance(spell, int) for spell in spells):
        return reduce(ope, spells)


def base_enchantement():
    pass


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    pass


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def fibo(n: int, i: int) -> int:
    fibo._calls += 1
    if n < 2:
        return n
    return fibo(n - 1, i + 1) + fibo(n - 2, i + 1)


fibo._calls = 0
fibo.call_info = lambda: (
    f"CacheInfo(hits=0, misses={fibo._calls}, maxsize=None, currsize=0)"
)

@singledispatch
def spell_dispatcher() -> callable:
    return lambda x: f"Default spell cast on {x}"

@spell_dispatcher.register
def _(target: str) -> str:
    return f"String spell cast on {target}"


if __name__ == "__main__":
    print([memoized_fibonacci(n) for n in range(8)])

    print(memoized_fibonacci.cache_info())

    print([fibo(n, n) for n in range(8)])
    print(fibo.call_info())
