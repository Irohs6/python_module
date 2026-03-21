from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations: dict[str, callable] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if operator.ge(a, b) else b,
        "min": lambda a, b: a if operator.le(a, b) else b,
    }
    if operation not in operations:
        raise ValueError("Unsupported operation")
    if not all(isinstance(spell, int) for spell in spells):
        raise TypeError("All spells must be integers")
    return reduce(operations[operation], spells)


def enchantement():
    pass


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": partial(base_enchantment, 50, "fire"),
        "ice_enchant": partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


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


def spell_dispatcher() -> callable:
    @singledispatch
    def cast(target) -> str | list[str]:
        return f"Mysterious spell cast on {target}"

    @cast.register
    def _(target: int) -> str:
        return f"Damage spell deals {target} points"

    @cast.register
    def _(target: str) -> str:
        return f"Enchantment applied to {target}"

    @cast.register
    def _(target: list) -> list[str]:
        return [cast(item) for item in target]

    return cast


if __name__ == "__main__":
    print([memoized_fibonacci(n) for n in range(8)])

    print(memoized_fibonacci.cache_info())

    print([fibo(n, n) for n in range(8)])
    print(fibo.call_info())
