# Chapitre V

## Exercice 0 : Sanctuaire Lambda

**Exercice 0**  
**ex0**

- **Dossier** : `ex0/`
- **Fichier a rendre** : `lambda_spells.py`
- **Autorise** : `map`, `filter`, `sorted`, `print()`

Pour cet exercice, vous devez utiliser des expressions `lambda` pour toutes les transformations. N'utilisez pas le mot-cle `def` pour creer des fonctions nommees lorsqu'il s'agit d'operations simples. L'objectif est de maitriser les fonctions anonymes et les modeles de programmation fonctionnelle.

### Le Sanctuaire Lambda : Maitriser les fonctions anonymes

Bienvenue dans le Sanctuaire Lambda, jeune mage ! Ici, on enseigne l'art ancien des fonctions anonymes. Les expressions `lambda` sont comme de rapides incantations : des sorts courts et puissants capables de transformer des donnees sans le ceremonial d'une definition de fonction complete.

**Votre mission** : maitriser l'art des expressions `lambda` en aidant le gardien du Sanctuaire, Sage Lambda, a organiser des artefacts magiques a l'aide de fonctions anonymes. Apprenez a creer des fonctions a la volee pour transformer des donnees.

### Le defi

Maitrisez les arts anciens de la programmation fonctionnelle.

Creez un fichier `lambda_spells.py` qui contient des fonctions demontrant votre maitrise des `lambda`.

### Signatures des fonctions

```python
def artifact_sorter(artifacts: list[dict]) -> list[dict]
def power_filter(mages: list[dict], min_power: int) -> list[dict]
def spell_transformer(spells: list[str]) -> list[str]
def mage_stats(mages: list[dict]) -> dict
```

### Exigences d'implementation

#### `artifact_sorter(artifacts)` - Trier les artefacts magiques

- Utiliser `sorted()` avec une `lambda` pour trier par niveau de `power` en ordre decroissant.
- Chaque artefact est un dictionnaire : `{'name': str, 'power': int, 'type': str}`.
- Retourner la liste triee.

#### `power_filter(mages, min_power)` - Filtrer les mages par puissance

- Utiliser `filter()` avec une `lambda` pour trouver les mages dont la puissance est `>= min_power`.
- Chaque mage est un dictionnaire : `{'name': str, 'power': int, 'element': str}`.
- Retourner une liste des mages filtres.

#### `spell_transformer(spells)` - Transformer les noms de sorts

- Utiliser `map()` avec une `lambda` pour ajouter le prefixe `* ` et le suffixe ` *`.
- Entree : une liste de noms de sorts (chaines de caracteres).
- Retourner une liste des noms transformes.

#### `mage_stats(mages)` - Calculer des statistiques

- Utiliser des `lambda` avec `max()`, `min()` et `sum()` pour trouver :
- Le niveau de puissance du mage le plus puissant.
- Le niveau de puissance du mage le moins puissant.
- Le niveau de puissance moyen, arrondi a 2 decimales.
- Retourner un dictionnaire : `{'max_power': int, 'min_power': int, 'avg_power': float}`.

### Exemple de sortie attendue

```bash
$> python3 lambda_spells.py
Master the Ancient Arts of Functional Programming
Testing artifact sorter...
Fire Staff (92 power) comes before Crystal Orb (85 power)
Testing spell transformer...
* fireball * * heal * * shield *
```

Comment les expressions `lambda` rendent-elles le code plus concis ? Quand faut-il utiliser une `lambda` plutot qu'une definition de fonction classique ?

---

# Chapitre VI

## Exercice 1 : Royaume Superieur

**Exercice 1**  
**ex1**

- **Dossier** : `ex1/`
- **Fichier a rendre** : `higher_magic.py`
- **Autorise** : `callable()`, `print()`

### Le Royaume Superieur : des fonctions qui operent sur d'autres fonctions

Bienvenue dans le Royaume Superieur, ou les fonctions deviennent elles-memes les sujets d'autres fonctions ! Ici, vous apprendrez que les fonctions sont des citoyens de premiere classe : elles peuvent etre passees en argument, retournees par d'autres fonctions et stockees dans des structures de donnees.

**Votre mission** : aider le gardien du Royaume, le Mage Functional, a creer un systeme de fabrication de sorts dans lequel des fonctions peuvent modifier, combiner et renforcer d'autres fonctions. Maitrisez l'art des fonctions d'ordre superieur !

### Le defi

Creez un fichier `higher_magic.py` qui demontre votre maitrise des fonctions d'ordre superieur.

### Signatures des fonctions

```python
def spell_combiner(spell1: callable, spell2: callable) -> callable
def power_amplifier(base_spell: callable, multiplier: int) -> callable
def conditional_caster(condition: callable, spell: callable) -> callable
def spell_sequence(spells: list[callable]) -> callable
```

### Exigences d'implementation

#### `spell_combiner(spell1, spell2)` - Combiner deux sorts

- Retourner une nouvelle fonction qui appelle les deux sorts avec les memes arguments.
- Le sort combine doit retourner un tuple contenant les deux resultats.
- Exemple : `combined = spell_combiner(fireball, heal)`.

#### `power_amplifier(base_spell, multiplier)` - Amplifier la puissance d'un sort

- Retourner une nouvelle fonction qui multiplie le resultat du sort de base par `multiplier`.
- On suppose que le sort de base retourne un nombre (degats, soins, etc.).
- Exemple : `mega_fireball = power_amplifier(fireball, 3)`.

#### `conditional_caster(condition, spell)` - Lancer un sort sous condition

- Retourner une fonction qui ne lance le sort que si `condition` retourne `True`.
- Si la condition echoue, retourner `"Spell fizzled"`.
- `condition` et `spell` recoivent les memes arguments.

#### `spell_sequence(spells)` - Creer une sequence de sorts

- Retourner une fonction qui lance tous les sorts dans l'ordre.
- Chaque sort recoit les memes arguments.
- Retourner une liste contenant tous les resultats des sorts.

### Exemple de sortie attendue

```bash
$> python3 higher_magic.py
Testing spell combiner...
Combined spell result: Fireball hits Dragon, Heals Dragon
Testing power amplifier...
Original: 10, Amplified: 30
```

Comment les fonctions d'ordre superieur permettent-elles la reutilisation et la composition du code ? Qu'est-ce qui fait des fonctions des "citoyens de premiere classe" en Python ?

---

# Chapitre VII

## Exercice 2 : Profondeurs de la Memoire

**Exercice 2**  
**ex2**

- **Dossier** : `ex2/`
- **Fichier a rendre** : `scope_mysteries.py`
- **Autorise** : `nonlocal`, `print()`

### Les Profondeurs de la Memoire : portee lexicale et fermetures

Au plus profond des abysses de la memoire, les anciens secrets de la portee lexicale sont gardes. Ici, les fonctions se souviennent de l'environnement dans lequel elles ont ete creees, capturant des variables dans des fermetures mystiques qui persistent au-dela de leur portee d'origine.

**Votre mission** : aider le Gardien de la Memoire, Sage Closure, a comprendre comment des fonctions peuvent "se souvenir" des variables presentes lors de leur creation. Maitrisez les closures et la portee lexicale pour creer des effets magiques persistants.

### Le defi

Creez un fichier `scope_mysteries.py` qui demontre votre maitrise de la portee lexicale.

### Signatures des fonctions

```python
def mage_counter() -> callable
def spell_accumulator(initial_power: int) -> callable
def enchantment_factory(enchantment_type: str) -> callable
def memory_vault() -> dict[str, callable]
```

### Exigences d'implementation

#### `mage_counter()` - Creer une fermeture compteur

- Retourner une fonction qui compte combien de fois elle a ete appelee.
- Chaque appel doit retourner le compteur actuel, en commencant a `1`.
- Le compteur doit persister entre les appels.
- Utiliser une closure pour conserver l'etat sans variable globale.

#### `spell_accumulator(initial_power)` - Creer un accumulateur de puissance

- Retourner une fonction qui accumule de la puissance au fil du temps.
- Chaque appel ajoute la valeur fournie a la puissance totale.
- Retourner la nouvelle puissance totale apres chaque ajout.
- Commencer avec `initial_power` comme base.

#### `enchantment_factory(enchantment_type)` - Creer des fonctions d'enchantement

- Retourner une fonction qui applique l'enchantement specifie.
- La fonction retournee prend un nom d'objet et retourne une description enchantee.
- Format : `"enchantment_type item_name"` (exemple : `"Flaming Sword"`).
- Chaque fabrique cree des fonctions avec des types d'enchantement differents.

#### `memory_vault()` - Creer un systeme de gestion de memoire

- Retourner un dictionnaire contenant les fonctions `store` et `recall`.
- La fonction `store` prend `(key, value)` et stocke le souvenir.
- La fonction `recall` prend `(key)` et retourne la valeur stockee ou `"Memory not found"`.
- Utiliser une closure pour maintenir un stockage prive en memoire.

### Exemple de sortie attendue

```bash
$> python3 scope_mysteries.py
Testing mage counter...
Call 1: 1
Call 2: 2
Call 3: 3
Testing enchantment factory...
Flaming Sword
Frozen Shield
```

Comment les closures permettent-elles aux fonctions de "se souvenir" de leur environnement de creation ? Quels sont les avantages de la portee lexicale en programmation fonctionnelle ?

---

# Chapitre VIII

## Exercice 3 : Bibliotheque Ancienne

**Exercice 3**  
**ex3**

- **Dossier** : `ex3/`
- **Fichier a rendre** : `functools_artifacts.py`
- **Autorise** : `functools`, `operator`, `print()`

### La Bibliotheque Ancienne : les tresors de functools

Dans la Bibliotheque Ancienne sont conserves les artefacts les plus puissants de la programmation fonctionnelle. Le module `functools` contient des outils legendaires : `reduce`, `partial`, `wraps`, et bien d'autres encore. Ces artefacts peuvent transformer votre facon d'aborder les problemes complexes.

**Votre mission** : aider le conservateur de la bibliotheque, Archivist Functools, a cataloguer et demontrer la puissance de ces anciens artefacts. Apprenez a manier `reduce`, `partial` et les autres tresors de `functools`.

### Le defi

Creez un fichier `functools_artifacts.py` qui demontre votre maitrise de `functools`.

### Signatures des fonctions

```python
def spell_reducer(spells: list[int], operation: str) -> int
def partial_enchanter(base_enchantment: callable) -> dict[str, callable]
def memoized_fibonacci(n: int) -> int
def spell_dispatcher() -> callable
```

### Exigences d'implementation

#### `spell_reducer(spells, operation)` - Reduire des puissances de sorts

- Utiliser `functools.reduce` pour combiner toutes les puissances de sorts.
- Prendre en charge les operations : `"add"`, `"multiply"`, `"max"`, `"min"`.
- Utiliser les fonctions du module `operator` (`add`, `mul`, etc.).
- Retourner la valeur finale reduite.

#### `partial_enchanter(base_enchantment)` - Creer des applications partielles

- Recevoir une fonction d'enchantement de base qui attend `(power, element, target)`.
- Utiliser `functools.partial` pour creer des versions specialisees.
- Retourner un dictionnaire avec les cles : `fire_enchant`, `ice_enchant`, `lightning_enchant`.
- Chacune doit etre une application partielle avec `power=50` et l'element correspondant.

#### `memoized_fibonacci(n)` - Fibonacci avec cache

- Utiliser le decorateur `functools.lru_cache` pour la memorisation.
- Implementer le calcul de la suite de Fibonacci.
- Le cache doit ameliorer les performances lors des appels repetes.
- Retourner le n-ieme nombre de Fibonacci.

#### `spell_dispatcher()` - Creer un systeme de dispatch simple

- Utiliser `functools.singledispatch` pour creer un systeme de sorts.
- Gerer differents types : `int` (sort de degats), `str` (enchantement), `list` (lancement multiple).
- Retourner la fonction de dispatch.
- Chaque type doit avoir un comportement adapte.

### Exemple de sortie attendue

```bash
$> python3 functools_artifacts.py
Master the Ancient Arts of Functional Programming
Testing spell reducer...
Sum: 100
Product: 240000
Max: 40
Testing memoized fibonacci...
Fib(10): 55
Fib(15): 610
```

Comment `functools.reduce` permet-il une aggregation puissante des donnees ? Quels sont les gains de performance de la memorisation avec `lru_cache` ?

---

# Chapitre IX

## Exercice 4 : Tour du Maitre

**Exercice 4**  
**ex4**

- **Dossier** : `ex4/`
- **Fichier a rendre** : `decorator_mastery.py`
- **Autorise** : `functools.wraps`, `staticmethod`, `print()`

### La Tour du Maitre : maitrise des decorateurs et methodes de classe

Au sommet de votre voyage se trouve la Tour du Maitre, ou les mages des fonctions les plus avances apprennent a creer des decorateurs : des enveloppes magiques capables de transformer le comportement de n'importe quelle fonction. Ici, vous maitriserez aussi `@staticmethod` et comprendrez comment les decorateurs fonctionnent avec les classes.

**Votre mission** : prouver votre maitrise au gardien de la tour, Grandmaster Decorator, en creant de puissants decorateurs capables d'ameliorer n'importe quel sort ou methode. C'est votre epreuve finale en tant que Mage des Fonctions.

### Le defi

Creez un fichier `decorator_mastery.py` qui demontre votre maitrise des decorateurs.

### Signatures des fonctions

```python
def spell_timer(func: callable) -> callable
def power_validator(min_power: int) -> callable
def retry_spell(max_attempts: int) -> callable

class MageGuild:
	@staticmethod
	def validate_mage_name(name: str) -> bool

	def cast_spell(self, spell_name: str, power: int) -> str
```

### Exigences d'implementation

#### `spell_timer(func)` - Decorateur de mesure du temps d'execution

- Creer un decorateur qui mesure le temps d'execution d'une fonction.
- Afficher `"Casting function_name..."` avant l'execution.
- Afficher `"Spell completed in time seconds"` apres l'execution.
- Utiliser `functools.wraps` pour preserver les metadonnees de la fonction d'origine.
- Retourner le resultat de la fonction d'origine.

#### `power_validator(min_power)` - Decorateur parametre de validation

- Creer une fabrique de decorateurs qui valide les niveaux de puissance.
- Verifier que le premier argument (`power`) est `>= min_power`.
- Si la valeur est valide, executer la fonction normalement.
- Sinon, retourner `"Insufficient power for this spell"`.
- Utiliser `functools.wraps` correctement.

#### `retry_spell(max_attempts)` - Decorateur de nouvelle tentative

- Creer un decorateur qui relance les sorts en echec.
- Si la fonction leve une exception, recommencer jusqu'a `max_attempts` fois.
- Afficher `"Spell failed, retrying... (attempt n/max_attempts)"`.
- Si toutes les tentatives echouent, retourner `"Spell casting failed after max_attempts attempts"`.
- Si le sort reussit, retourner normalement son resultat.

#### Classe `MageGuild` - Demonstration de `staticmethod`

- `validate_mage_name(name)` : methode statique qui verifie si le nom est valide.
- Un nom est valide s'il comporte au moins 3 caracteres et ne contient que des lettres ou des espaces.
- `cast_spell(self, spell_name, power)` : methode d'instance.
- Cette methode doit utiliser le decorateur `power_validator` avec `min_power=10`.
- Retourner `"Successfully cast spell_name with power power"`.

### Exemple de sortie attendue

```bash
$> python3 decorator_mastery.py
Testing spell timer...
Casting fireball...
Spell completed in 0.101 seconds
Result: Fireball cast!
Testing MageGuild...
True
False
Successfully cast Lightning with 15 power
Insufficient power for this spell
```

Comment les decorateurs permettent-ils de separer les responsabilites ? Quelle est la difference entre `@staticmethod` et une methode d'instance classique ?

---

# Chapitre X

## Rendu et peer-review

Rendez votre travail dans votre depot Git comme d'habitude. Seul le travail present dans votre depot sera evalue pendant la soutenance ou la peer-review. N'hesitez pas a verifier une derniere fois les noms de fichiers afin d'etre sur qu'ils sont corrects.

Pendant la peer-review, on pourra vous demander d'expliquer des concepts de programmation fonctionnelle, de montrer comment les closures fonctionnent ou de demontrer comment les decorateurs transforment les fonctions. Concentrez-vous sur la comprehension des concepts, pas seulement sur l'implementation.

Gardez des implementations simples et centrees sur la demonstration claire des concepts de programmation fonctionnelle. Evitez le sur-ingenierie : le but est de montrer votre maitrise des fonctions d'ordre superieur, des closures et des decorateurs.

Felicitations, Mage des Fonctions ! Vous avez maitrise les arts anciens de la programmation fonctionnelle. Ces techniques rendront votre code plus elegant, reutilisable et puissant. Utilisez-les avec sagesse pour vos futures aventures.