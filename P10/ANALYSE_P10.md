# Analyse P10 — État actuel par exercice (mise à jour 27/03/2026 — v2)

---

## Ex0 — `lambda_spells.py` ✅ Fonctionnel

### Sortie réelle
```
Testing artifact sorter...
[{'name': 'Shadow Blade', 'power': 111, ...}, ...]

Testing filter
[{'name': 'Morgan', 'power': 92, ...}, ...]

Testing spell transformer
['* meteor *', '* tsunami *', '* lightning *', '* fireball *']

Testing mage stats
{'max_power': 97, 'min_power': 65, 'avg_power': 85.8}
```

### Problèmes restants

**`main()` : affichage brut des listes, pas le format narratif du sujet**
Le sujet attend un affichage lisible comme :
```
Shadow Blade (111 power) comes before Storm Crown (87 power)
```
Actuellement `print(artifact_sorter(artifacts))` affiche la liste brute. Pas bloquant si l'évaluateur accepte les prints bruts.

### Ce qui est correct ✓
- `artifact_sorter` : `sorted()` + `lambda key` ✓
- `power_filter` : `filter()` + `lambda` ✓
- `spell_transformer` : `map()` + `lambda`, format `* spell *` ✓
- `mage_stats` : `max(..., key=lambda)`, `min(..., key=lambda)`, `sum(map(lambda ...))` ✓
- `main()` présent avec données de test ✓

---

## Ex1 — `higher_magic.py` ✅ Fonctionnel

### Sortie réelle
```
Testing spell combiner...
Combined spell result ('Fireball hits Dragon!', 'Heal Dragon!')

Testing power amplifier...
Original: 10, Amplified: 30

Testing conditional spell...
Fireball hits Goblin!
Spell fizzled

Testing spell sequence...
['Fireball hits Dragon!', 'Heal Dragon!']
```

### Problèmes restants

**Aucun problème fonctionnel majeur.** Le format d'affichage est légèrement différent du sujet (ex: `Combined spell result (...)` au lieu de `Combined spell result: ...`) mais pas bloquant.

### Ce qui est correct ✓
- `spell_combiner` : retourne un tuple des deux résultats ✓
- `power_amplifier` : `base_spell * multiplier`, `power_spell` retourne bien un `int` ✓
- `conditional_caster` : retourne `"Spell fizzled"` si condition False ✓
- `spell_sequence` : retourne une liste de résultats ✓
- `main()` complet avec tous les cas de test ✓

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
for i in range(3):
    print(f"Call {i}: {counter()}")   # i part de 0

# ATTENDU :
for i in range(1, 4):
    print(f"Call {i}: {counter()}")   # i part de 1
```

**2. Typo : `"Testing sepll acumulator..."` → `"Testing spell accumulator..."`**

**3. `memory['store']` retourne `None`**
`store()` ne retourne rien → `print(memory['store']('lapin', 5), ...)` affiche `None 5`.
À corriger : soit ne pas printer le retour de `store`, soit `return value` dans `store`.

### Ce qui est correct ✓
- `mage_counter` : `nonlocal`, un seul compteur créé hors de la boucle ✓
- `spell_accumulator` : `nonlocal initial_power`, accumule correctement ✓
- `enchantment_factory` : format `"type item"` via `chr(32)` ✓
- `memory_vault` : retourne dict `{store, recall}`, `"Memory not found"` si absent ✓
- `main()` présent et fonctionnel ✓

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
Il manque les sections :
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

**2. `memoized_fibonacci` utilise `maxsize=1000` au lieu de `maxsize=None`**
`@lru_cache(maxsize=None)` = cache illimité, plus idiomatique pour Fibonacci.

**3. Affichage `Fib(8)CacheInfo(...)` collé (pas d'espace/newline)**
```python
print(f"Fib(8){memoized_fibonacci.cache_info()}")   # ← collé
# ATTENDU :
print(f"Fib(8): {memoized_fibonacci.cache_info()}")
```

### Note : `fibo()` est intentionnel ✓
`fibo()` sans `@lru_cache` et son `call_info` sont là pour le **comparatif avec/sans cache**.
La sortie montre bien la différence : `hits=12, misses=8` (avec cache) vs `hits=0, misses=67` (sans cache). C'est voulu.

### Ce qui est correct ✓
- `spell_reducer` : `reduce` + `operator` pour les 4 opérations, gestion d'erreurs ✓
- `partial_enchanter` : `functools.partial` avec `power=50` et les 3 éléments ✓
- `memoized_fibonacci` : `@lru_cache` ✓
- `fibo` : version sans cache pour la comparaison ✓
- `spell_dispatcher` : `@singledispatch` avec cas `int`, `str`, `list` ✓
- `__main__` teste `spell_reducer` et Fibonacci ✓

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
Spell failed, retrying... (attempt 1/3)
Spell failed, retrying... (attempt 2/3)
Spell failed, retrying... (attempt 3/3)
```

### Problèmes restants

**1. `validate_mage_name` appelée avec un `tuple` via `zip()`**
```python
for name in zip(mage_names, invalid_names):   # zip → produit des tuples ("Alex", "Jo")
    print(morgan.validate_mage_name(name))     # name = tuple → toujours False
```
C'est pour ça que les 4 lignes affichent `False`. À corriger en itérant séparément :
```python
for name in mage_names:
    print(morgan.validate_mage_name(name))
for name in invalid_names:
    print(morgan.validate_mage_name(name))
```

**2. `power_validator` utilise `<=` au lieu de `<`**
```python
if power_value <= min_power:   # bloque power == min_power → ex: power=10 avec @power_validator(10)

# ATTENDU :
if power_value < min_power:
```
Avec `power=15` ça marche, mais `power=10` retournerait `"Insufficient power"` à tort.

**3. `spell_timer` contient une vérification `kwargs` qui lui appartient pas**
```python
def wrapper(*args, **kwargs):
    if not kwargs:                        # ← logique de validation, pas du timer
        raise SyntaxError("...")
```
Si `spell_timer` est utilisé seul (sans `power_validator`), il rejette tout appel sans kwargs. Cette logique appartient uniquement à `power_validator`.

### Ce qui est correct ✓
- `spell_timer` : `@wraps`, mesure et affiche le temps ✓
- `power_validator` : structure decorator-factory, `*args` pour passer `self` ✓
- `retry_spell` : boucle `max_attempts`, messages corrects, retour final correct ✓
- `cast_spell(spell_name=..., power=...)` : appel correct ✓
- `@power_validator(10)` + `@spell_timer` stackés sur `cast_spell` ✓
- `validate_mage_name` : `@staticmethod`, accepte lettres + espaces ✓

---

## Résumé global

| Exercice | Problèmes critiques | Problèmes mineurs |
|---|---|---|
| **ex0** | `mage_stats` ne respecte pas l'exigence lambda | `print(__getattribute__)` parasite, format `main()` incorrect |
| **ex1** | Format `main()` incorrect | `power_amplifier` testé avec str au lieu d'int |
| **ex2** | **Pas de `main()` → aucune sortie à l'exécution** | `store` ne retourne rien |
| **ex3** | Fonction `enchantement()` vide, `fibo()` hors-sujet, format `__main__` incorrect | `partial_enchanter` dépend de la signature de `base_enchantment` |
| **ex4** | **BUG `<=` au lieu de `<`**, retour `cast_spell` incorrect, `validate_mage_name` rejette les espaces | Format `main()` incomplet, code hors-sujet |

### Actions prioritaires avant soutenance

1. **ex4** — Corriger `<=` → `<` dans `power_validator`
2. **ex4** — Corriger le `return` de `cast_spell` : `f"Successfully cast {spell_name} with {power} power"`
3. **ex4** — Corriger `validate_mage_name` pour accepter les espaces
4. **ex2** — Ajouter un `main()` avec la sortie attendue
5. **ex0** — Corriger `mage_stats` pour utiliser `lambda` avec `max()`/`min()`/`sum()`
6. **ex3** — Supprimer `enchantement()` et `fibo()`
7. **ex0/ex1/ex3** — Corriger les `main()` pour correspondre au format du sujet
