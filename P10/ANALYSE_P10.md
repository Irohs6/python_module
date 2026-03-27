# Analyse P10 — État actuel par exercice (mise à jour 27/03/2026 — v3)

---

## Ex0 — `lambda_spells.py` ✅ Correct

### Sortie réelle
```
Testing artifact sorter...
Shadow Blade (111 power) comes before Storm Crown (87 power)
Storm Crown (87 power) comes before Shadow Blade (74 power)
Shadow Blade (74 power) comes before Ice Wand (61 power)

Testing power filter (min 85)...
Morgan qualifies with 92 power
Kai qualifies with 97 power
Jordan qualifies with 91 power

Testing spell transformer...
* meteor * * tsunami * * lightning * * fireball *

Testing mage stats...
Max power: 97, Min power: 65, Avg power: 85.8
```

### Ce qui est correct ✓
- `artifact_sorter` : `sorted()` + `lambda key` ✓
- `power_filter` : `filter()` + `lambda` ✓
- `spell_transformer` : `map()` + `lambda`, format `* spell *` ✓
- `mage_stats` : `max(..., key=lambda)`, `min(..., key=lambda)`, `sum(map(lambda ...))` ✓
- `main()` : affichage formaté et narratif ✓

### Aucun problème bloquant ✓

---

## Ex1 — `higher_magic.py` ✅ Correct

### Sortie réelle
```
Testing spell combiner...
Combined spell result: Fireball hits Dragon!, Heal Dragon!

Testing power amplifier...
Original: 10, Amplified: 30

Testing conditional spell...
Fireball hits Goblin!
Spell fizzled

Testing spell sequence...
Fireball hits Dragon!
Heal Dragon!
```

### Ce qui est correct ✓
- `spell_combiner` : retourne un tuple dépaquetté à l'affichage ✓
- `power_amplifier` : `base_spell * multiplier`, `power_spell` retourne un `int` ✓
- `conditional_caster` : retourne `"Spell fizzled"` si condition False ✓
- `spell_sequence` : résultats affichés ligne par ligne ✓
- `main()` complet avec tous les cas de test, affichage formaté ✓

### Aucun problème bloquant ✓

---

## Ex2 — `scope_mysteries.py` ⚠️ Bugs mineurs dans `main()`

### Sortie réelle
```
Testing mage counter...
Call 0: 1
Call 1: 2
Call 2: 3

Testing sepll acumulator...
11
12

Testing enchantment factory...
fire sword

Testing memory vault...
None 5
```

### Problèmes restants

**1. Compteur commence à `Call 0:` au lieu de `Call 1:`**
```python
# ACTUEL :
for i in range(3):
    print(f"Call {i}: {counter()}")   # i part de 0 → "Call 0: 1"

# ATTENDU :
for i in range(1, 4):
    print(f"Call {i}: {counter()}")   # i part de 1 → "Call 1: 1"
```

**2. Typo : `"Testing sepll acumulator..."` → `"Testing spell accumulator..."`**

**3. `memory['store']` retourne `None`**
`store()` ne retourne rien → `print(memory['store']('lapin', 5), memory['recall']('lapin'))` affiche `None 5`.
Fix : appeler `store` et `recall` séparément, ne pas printer le retour de `store`.

### Ce qui est correct ✓
- `mage_counter` : `nonlocal`, un seul compteur créé hors de la boucle ✓
- `spell_accumulator` : `nonlocal initial_power`, accumule correctement (10→11→12) ✓
- `enchantment_factory` : format `"type item"` via `chr(32)` ✓
- `memory_vault` : retourne dict `{store, recall}`, `"Memory not found"` si absent ✓

---

## Ex3 — `functools_artifacts.py` ⚠️ `__main__` incomplet

### Sortie réelle
```
Testing spell reducer...
Sum: 33
Product: 3600
Max: 12

[0, 1, 1, 2, 3, 5, 8, 13]
Fib(8)CacheInfo(hits=12, misses=8, maxsize=1000, currsize=8)
Original FiboCacheInfo(hits=0, misses=67, maxsize=None, currsize=0)
```

### Problèmes restants

**1. `__main__` ne teste pas `partial_enchanter` ni `spell_dispatcher`**
À ajouter :
```python
print("Testing partial enchanter...")
enchanter = partial_enchanter(some_base_enchantment)
print(enchanter["fire_enchant"]("sword"))

print("Testing spell dispatcher...")
cast = spell_dispatcher()
print(cast("sword"))
print(cast(42))
print(cast([1, "shield"]))
```

**2. Affichage collé sans séparateur**
```python
print(f"Fib(8){memoized_fibonacci.cache_info()}")    # → "Fib(8)CacheInfo(...)"
print(f"Original Fibo{fibo.call_info()}")             # → "Original FiboCacheInfo(...)"
# ATTENDU :
print(f"Fib(8): {memoized_fibonacci.cache_info()}")
print(f"Original Fibo: {fibo.call_info()}")
```

**3. `memoized_fibonacci` utilise `maxsize=1000` au lieu de `maxsize=None`**
`@lru_cache(maxsize=None)` est plus idiomatique pour Fibonacci (cache illimité).

### Note : `fibo()` est intentionnel ✓
`fibo()` sans `@lru_cache` est là pour le **comparatif avec/sans cache**.
La sortie montre la différence : `hits=12, misses=8` (avec) vs `hits=0, misses=67` (sans). C'est voulu.

### Ce qui est correct ✓
- `spell_reducer` : `reduce` + `operator` pour les 4 opérations, gestion d'erreurs ✓
- `partial_enchanter` : `functools.partial` avec `50` et les 3 éléments ✓
- `memoized_fibonacci` : `@lru_cache` ✓
- `fibo` : version sans cache pour comparaison ✓
- `spell_dispatcher` : `@singledispatch` avec cas `int`, `str`, `list` ✓

---

## Ex4 — `decorator_mastery.py` ⚠️ Bugs restants

### Sortie réelle
```
Casting cast_spell...
Spell completed in 0.0000 seconds
tornado and power : 15
False
False
False
False
Spell failed, retrying...
(attempt 1/3)
Spell failed, retrying...
(attempt 2/3)
Spell failed, retrying...
(attempt 3/3)
```

### Problèmes restants

**1. `validate_mage_name` appelée avec un `tuple` via `zip()`**
```python
for name in zip(mage_names, invalid_names):    # → tuples ("Alex", "Jo")
    print(morgan.validate_mage_name(name))     # isalpha() sur tuple → False systématique
```
Fix : itérer séparément sur chaque liste.

**2. `power_validator` utilise `<=` au lieu de `<`**
```python
if power_value <= min_power:   # power=10 avec @power_validator(10) → "Insufficient power" à tort
# ATTENDU :
if power_value < min_power:
```

**3. `spell_timer` contient une validation `kwargs` hors de son rôle**
```python
def wrapper(*args, **kwargs):
    if not kwargs:               # ← logique de validation, pas de timing
        raise SyntaxError("...")
```
Si `spell_timer` est utilisé seul sans `power_validator`, il refuse tout appel sans kwargs.

**4. Message de `retry_spell` affiché sur deux lignes**
```python
print(f"Spell failed, retrying... \n(attempt {attempt}/{max_attempts})")
# ← \n parasite, le message devrait tenir sur une ligne
```

### Ce qui est correct ✓
- `spell_timer` : `@wraps`, mesure et affiche le temps ✓
- `power_validator` : decorator-factory, `*args` pour passer `self` ✓
- `retry_spell` : boucle `max_attempts`, retour final correct ✓
- `cast_spell(spell_name=..., power=...)` : appel correct ✓
- `@power_validator(10)` + `@spell_timer` stackés sur `cast_spell` ✓
- `validate_mage_name` : `@staticmethod`, logique lettres + espaces correcte ✓
