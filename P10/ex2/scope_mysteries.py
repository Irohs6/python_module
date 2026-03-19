

def mage_counter() -> callable
    counter: int = 0
    def counter_():
        nonlocal counter
        counter =+ 1
        return counter
    return counter_

 
def spell_accumulator(initial_power: int) -> callable

    def accumualte_power(add: int):

        nonlocal initial_power
        initial_power += add
        return  initial_power
    
    return  accumualte_power



def enchantment_factory(enchantment_type: str) -> callable
    
    def apply_enchantement(item_name: str):
        return enchantment_type + chr(32) + item_name


def memory_vault() -> dict[str, callable]
    pass