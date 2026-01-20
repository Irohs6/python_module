# Préparation à la Soutenance Orale - P02
## Garden Guardian: Data Engineering for Smart Agriculture

**Date de préparation:** 17 janvier 2026  
**Note globale du projet:** 9.2/10  
**Durée estimée de soutenance:** 20-30 minutes

---

# 🎯 Structure de la Soutenance

## Introduction (2 minutes)
- **Présentation du projet:** Module de gestion des erreurs pour systèmes agricoles intelligents
- **Objectif:** Créer des pipelines de données résilientes et tolérantes aux pannes
- **Technologies:** Python 3.10+, gestion d'exceptions natives
- **Contexte:** 6 exercices progressifs (Ex0 à Ex5)

---

# 📚 Exercice par Exercice

## Exercise 0: Agricultural Data Validation Pipeline
### 🎤 Présentation (3-4 minutes)

#### Objectif du module:
"Valider les données de température provenant de capteurs agricoles en filtrant les données corrompues avant qu'elles n'affectent les analyses."

#### Concepts Clés à Expliquer:

**1. Try/Except/Else**
```python
try:
    temp: int = int(temp_str)  # Tentative de conversion
except ValueError:
    print("Erreur")  # Gestion si échec
else:
    # Exécuté seulement si try réussit
    if temp > 40: ...
```

**Point à retenir:** 
- `try` = zone à risque
- `except` = gestion d'erreur
- `else` = exécuté UNIQUEMENT si try réussit (pas d'exception levée)

**2. ValueError**
- Exception levée quand `int("abc")` échoue
- Type d'erreur: données invalides pour conversion

#### Questions Probables de l'Évaluateur:

**Q: Pourquoi utiliser else au lieu de mettre le code après try/except?**  
**R:** "Le bloc `else` garantit que le code ne s'exécute QUE si aucune exception n'est levée. C'est plus clair et sépare la logique de validation de la gestion d'erreur. Si on mettait le code après except, il s'exécuterait même après une erreur."

**Q: Que se passe-t-il si on ne catch pas ValueError?**  
**R:** "Le programme crash avec un traceback. L'exception remonte la pile d'appels jusqu'à trouver un except ou terminer le programme. C'est pourquoi on utilise try/except pour une gestion gracieuse."

**Q: Pourquoi utiliser type hints?**  
**R:** "Les type hints améliorent la lisibilité, permettent la détection d'erreurs statiques avec mypy, et documentent le code. Ici `temp_str: str` indique clairement qu'on attend une string."

#### Démonstration:
```bash
python ft_first_exception.py
# Montrer: input d'une valeur valide, puis invalide
```

**Points forts à mentionner:**
- ✅ Gestion robuste des erreurs
- ✅ Messages explicites pour l'utilisateur
- ✅ Type hints complets
- ⚠️ Version interactive au lieu de tests automatiques (point d'amélioration)

---

## Exercise 1: Different Types of Problems
### 🎤 Présentation (3-4 minutes)

#### Objectif du module:
"Démontrer la gestion de différents types d'erreurs courantes dans un système de jardin, et montrer comment capturer plusieurs types d'exceptions."

#### Concepts Clés à Expliquer:

**1. Types d'Exceptions Standards**

| Exception | Cause | Exemple |
|-----------|-------|---------|
| **ValueError** | Données invalides | `int("abc")` |
| **ZeroDivisionError** | Division par zéro | `10 / 0` |
| **FileNotFoundError** | Fichier inexistant | `open("missing.txt")` |
| **KeyError** | Clé absente dans dict | `dict["missing_key"]` |

**2. Gestion Multi-Exceptions**
```python
except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
    # Capture N'IMPORTE laquelle de ces exceptions
    print("Erreur capturée!")
```

**Point crucial:** Le tuple d'exceptions permet de gérer plusieurs types avec un seul except.

#### Questions Probables:

**Q: Pourquoi Python a-t-il différents types d'exceptions?**  
**R:** "Ça permet une gestion fine et spécifique. On peut traiter une ValueError (données invalides) différemment d'une FileNotFoundError (ressource manquante). Ça rend le code plus robuste et les messages d'erreur plus pertinents pour l'utilisateur."

**Q: Quelle est la différence entre `except Exception` et `except (ValueError, KeyError)`?**  
**R:** "`except Exception` capture TOUTES les exceptions (trop large). `except (ValueError, KeyError)` est spécifique et ne capture que ces deux types. C'est une meilleure pratique car ça évite de masquer des erreurs inattendues."

**Q: L'ordre des except est-il important?**  
**R:** "Oui! Python évalue les except dans l'ordre. Il faut mettre les exceptions spécifiques AVANT les générales. Sinon, l'exception générale capture tout et les spécifiques ne seront jamais atteintes."

#### Points forts:
- ✅ 4 types d'erreurs bien démontrés
- ✅ Gestion multi-exceptions
- ✅ Programme continue après chaque erreur
- ✅ Conforme à l'exemple du sujet

---

## Exercise 2: Making Your Own Error Types
### 🎤 Présentation (4-5 minutes)

#### Objectif du module:
"Créer des exceptions personnalisées spécifiques au domaine du jardin pour rendre le code plus clair et maintenable."

#### Concepts Clés à Expliquer:

**1. Hiérarchie d'Exceptions**
```
Exception (built-in Python)
    └── GardenError (notre base)
            ├── PlantError (spécifique aux plantes)
            └── WaterError (spécifique à l'arrosage)
```

**2. Pourquoi créer ses propres exceptions?**
- **Clarté sémantique:** `PlantError` est plus parlant que `ValueError`
- **Gestion hiérarchique:** `except GardenError` capture tous les problèmes de jardin
- **Extensibilité:** Facile d'ajouter de nouveaux types d'erreurs

**3. Héritage d'Exceptions**
```python
class GardenError(Exception):
    pass  # Exception de base pour tout le jardin

class PlantError(GardenError):
    pass  # Hérite de GardenError

# Avantage:
try:
    raise PlantError("Plante malade")
except GardenError:  # ← Capture PlantError aussi!
    print("Problème de jardin")
```

#### Questions Probables:

**Q: Pourquoi hériter d'Exception et pas créer une classe normale?**  
**R:** "Exception est la classe de base de toutes les exceptions Python. Hériter d'Exception permet à notre classe d'être utilisée avec try/except et de bénéficier de tous les mécanismes d'exception Python (traceback, raise, etc.)."

**Q: Quand créer une exception personnalisée vs utiliser ValueError?**  
**R:** "On crée une exception personnalisée quand on a une logique métier spécifique. Par exemple, `PlantError('Plante fanée')` est plus descriptif que `ValueError`. Ça permet aussi une gestion ciblée : on peut catch toutes les `GardenError` sans capturer d'autres ValueError du système."

**Q: Pourquoi GardenError hérite d'Exception et pas directement de BaseException?**  
**R:** "`BaseException` est pour les exceptions système (KeyboardInterrupt, SystemExit). `Exception` est pour les exceptions d'application. Hériter d'Exception est la bonne pratique pour nos erreurs métier."

#### Démonstration Live:
```python
# Montrer que GardenError capture PlantError
try:
    raise PlantError("Test")
except GardenError as e:  # ← Fonctionne grâce à l'héritage!
    print(f"Capturé: {e}")
```

#### Points forts:
- ✅ Architecture claire avec héritage
- ✅ Démo complète des 3 types d'exceptions
- ✅ Montre la capture par type parent (GardenError)
- ✅ Classes Plant avec méthodes qui lèvent les erreurs

---

## Exercise 3: Finally Block - Always Clean Up
### 🎤 Présentation (4-5 minutes)

#### Objectif du module:
"Garantir le nettoyage des ressources (fermeture du système d'arrosage) même quand une erreur se produit."

#### Concepts Clés à Expliquer:

**1. Le Bloc Finally**
```python
try:
    # Code à risque
    water_plant()
except ValueError:
    # Gestion d'erreur
    print("Erreur!")
finally:
    # ← TOUJOURS exécuté, erreur ou pas
    print("Fermeture système")
```

**Règle d'OR:** `finally` s'exécute **TOUJOURS**, même si:
- Aucune erreur n'est levée
- Une exception est levée et capturée
- Une exception est levée et NON capturée
- Il y a un `return` dans try ou except

**2. Cas d'Usage Réels**
- Fermeture de fichiers
- Déconnexion de bases de données
- Libération de ressources système
- **Ici:** Fermeture du système d'arrosage

#### Questions Probables:

**Q: Pourquoi ne pas simplement mettre le cleanup après try/except?**  
**R:** "Si une exception non capturée est levée, le code après try/except ne sera jamais exécuté. Avec `finally`, le cleanup est **garanti** même en cas d'erreur imprévue. C'est critique pour éviter les fuites de ressources."

**Q: Peut-on avoir finally sans except?**  
**R:** "Oui! `try/finally` est valide. C'est utile quand on veut garantir le cleanup mais laisser l'exception se propager. Par exemple:
```python
try:
    file = open('data.txt')
    process(file)
finally:
    file.close()  # Garanti même si process() crash
```"

**Q: Que se passe-t-il si finally lui-même lève une exception?**  
**R:** "L'exception de finally remplace l'exception originale du try. C'est pourquoi le code dans finally doit être le plus sûr possible, souvent avec son propre try/except."

#### Démonstration Live:
```bash
python ft_finally_block.py
# Montrer les deux cas:
# 1. Liste valide → cleanup exécuté
# 2. Liste avec None → erreur + cleanup quand même exécuté
```

**Pointer du doigt dans le terminal:**
- "Voyez ici: erreur levée"
- "Et là: 'Closing watering system' quand même exécuté"
- "C'est la puissance du finally!"

#### Points forts:
- ✅ Démo claire des deux scénarios (succès/échec)
- ✅ Finally garanti dans tous les cas
- ✅ Messages pédagogiques
- ✅ Type hints corrects

---

## Exercise 4: Raising Your Own Errors
### 🎤 Présentation (3-4 minutes)

#### Objectif du module:
"Valider des données d'entrée et lever des erreurs explicites quand les paramètres sont invalides."

#### Concepts Clés à Expliquer:

**1. Le Keyword `raise`**
```python
if not plant_name:
    raise ValueError("Plant name cannot be empty!")
    # ← Crée et lève une exception

# Équivalent à ce que Python fait en interne:
# int("abc") → Python fait: raise ValueError("invalid literal...")
```

**2. Pourquoi lever ses propres exceptions?**
- **Validation métier:** Vérifier que water_level ∈ [1,10]
- **Fail fast:** Détecter les erreurs tôt plutôt que laisser se propager
- **Messages clairs:** Dire exactement ce qui est invalide

**3. Conception de Validations**
```python
# 3 validations dans check_plant_health:
if not plant_name:           # → ValueError
if water_level < 1 or > 10:  # → ValueError
if sunlight < 2 or > 12:     # → ValueError
```

#### Questions Probables:

**Q: Quelle exception choisir pour raise?**  
**R:** "Ça dépend du contexte:
- `ValueError`: données invalides (wrong value)
- `TypeError`: mauvais type (expected int, got str)
- `RuntimeError`: état invalide du programme
- Ou exception personnalisée pour logique métier spécifique

Ici j'utilise `ValueError` car les valeurs numériques sont hors des bornes acceptables."

**Q: Pourquoi ne pas simplement retourner False au lieu de lever une exception?**  
**R:** "Les exceptions sont plus explicites et forcent l'appelant à gérer l'erreur. `return False` peut être ignoré silencieusement. L'exception garantit que l'erreur sera traitée ou fera crasher le programme. C'est le principe 'fail fast' - mieux vaut échouer visiblement que continuer avec des données invalides."

**Q: Comment créer un bon message d'erreur?**  
**R:** "Un bon message doit:
1. Dire CE qui est invalide (`Water level 15`)
2. Dire POURQUOI c'est invalide (`is too high`)
3. Dire quelle est la LIMITE (`max 10`)

Exemple: `'Water level 15 is too high (max 10)'` - complet et actionnable."

#### Points forts:
- ✅ 3 types de validations bien séparées
- ✅ Messages d'erreur explicites et formatés
- ✅ Fonction de test complète
- ✅ Tous les cas (valide + 3 invalides) testés

---

## Exercise 5: Garden Management System (INTÉGRATION)
### 🎤 Présentation (6-8 minutes) - **EXERCICE LE PLUS IMPORTANT**

#### Objectif du module:
"Intégrer TOUS les concepts d'error handling dans un système complet de gestion de jardin."

#### Concepts Intégrés:

**1. Exceptions Personnalisées (Ex2)**
```python
class GardenError(Exception): pass
class PlantError(GardenError): pass
class WaterError(GardenError): pass
class HealthError(GardenError): pass
```

**2. Méthode add_plant() - Try/Except/Return**
```python
def add_plant(self, plant):
    try:
        if not plant.name:
            raise PlantError("...")  # ← Raise (Ex4)
        self.plants.append(plant)
        return "Success"
    except PlantError as e:  # ← Catch personnalisé (Ex2)
        return str(e)
```

**3. Méthode water_plant() - Try/Except/Finally**
```python
def water_plant(self):
    try:
        # Arrosage avec validation
        if self.water_tank < 5:
            raise WaterError("...")  # ← Raise (Ex4)
        # ... arroser ...
    except WaterError as e:  # ← Catch (Ex1)
        print(f"Caught: {e}")
    finally:  # ← Finally (Ex3)
        print("Closing watering system")
```

**4. Recovery après Erreur**
```python
# Test 1: Ajout avec erreur
print(alice.add_plant(invalid_plant))  # ← Erreur catchée

# Test 2: Système continue!
alice.water_plant()  # ← Fonctionne quand même!
```

#### Architecture Complète:

**Classes:**
- `Plant` - Base class avec attributs (name, height, water_level, sunlight)
- `FloweringPlant(Plant)` - Héritage avec couleur
- `PrizeFlower(FloweringPlant)` - Héritage double avec score
- `GardenManager` - Classe principale de gestion

**Méthodes de GardenManager:**
1. `add_plant()` - Validation + PlantError
2. `water_plant()` - Try/except/finally + WaterError
3. `check_plant_health()` - Validations multiples + HealthError
4. `validate_height()` - Méthode statique utilitaire
5. `create_garden_network()` - Class method pour factory pattern

**Classe Nested:**
- `GardenStat` - Statistiques (total_growth, count_type)

#### Questions Probables de l'Évaluateur (CRUCIALES):

**Q: Comment toutes ces techniques d'error handling travaillent ensemble?**  
**R:** "C'est une architecture en couches:
1. **Bottom:** Exceptions personnalisées (GardenError, PlantError, etc.) définissent le vocabulaire d'erreurs
2. **Middle:** Les méthodes valident et `raise` des erreurs spécifiques quand détection de problème
3. **Top:** try/except capturent les erreurs et permettent le recovery
4. **Finally:** Garantit le cleanup des ressources

Ensemble, ça crée un système résilient où chaque erreur est gérée gracieusement sans crash."

**Q: Qu'est-ce que le "error recovery" et pourquoi c'est important?**  
**R:** "Error recovery signifie que le système continue de fonctionner après une erreur. Dans `test_garden_management()`:
- On essaie d'ajouter une plante invalide → **erreur catchée**
- Le programme **continue** et peut arroser les autres plantes
- On force une pénurie d'eau → **erreur catchée**
- Le système **continue** et peut faire d'autres opérations

C'est essentiel en production : un capteur défaillant ne doit pas crasher tout le système agricole!"

**Q: Pourquoi utiliser @staticmethod pour check_plant_health?**  
**R:** "Cette méthode ne dépend pas de l'état de GardenManager (pas de `self` utilisé). C'est une fonction utilitaire qui valide n'importe quelle plante. `@staticmethod` indique clairement qu'elle peut être appelée sans instance et améliore la réutilisabilité."

**Q: Différence entre @staticmethod et @classmethod?**  
**R:** 
- `@staticmethod`: Fonction simple dans la classe, pas d'accès à l'instance ni à la classe
- `@classmethod`: Reçoit la classe (cls) en premier param, utilisé pour factory patterns
- Exemple: `create_garden_network()` est classmethod car il crée des instances de la classe"

#### Démonstration Commentée:
```bash
python ft_garden_management.py
```

**Points à commenter pendant l'exécution:**
1. "Ajout de plantes valides → succès"
2. "Tentative d'ajout de plante sans nom → **erreur catchée**, message clair"
3. "Arrosage avec finally → **cleanup garanti**"
4. "Vérification santé → lettuce a trop d'eau → **erreur catchée**"
5. "Test recovery → pénurie d'eau → **erreur catchée, système continue**"
6. "**Aucun crash**! C'est le but: résilience totale"

#### Points forts à mettre en avant:
- ✅ Intégration complète de tous les concepts (Ex0-Ex4)
- ✅ Architecture solide avec héritage multiple
- ✅ Error recovery démontré clairement
- ✅ Type hints partout
- ✅ Docstrings complètes
- ✅ Fonction `test_garden_management()` bien structurée
- ✅ Messages d'erreur explicites

#### Points d'amélioration à mentionner (montrer que vous êtes critique):
- ⚠️ Messages légèrement différents de l'exemple (espaces autour du tiret)
- ⚠️ add_plant retourne l'objet exception au lieu de str(e) (mineur)

---

# 🎓 Concepts Théoriques à Maîtriser

## 1. Hiérarchie des Exceptions Python

```
BaseException
  ├── SystemExit
  ├── KeyboardInterrupt
  └── Exception
        ├── ValueError
        ├── TypeError
        ├── ZeroDivisionError
        ├── FileNotFoundError
        ├── KeyError
        └── [Nos exceptions personnalisées]
              └── GardenError
                    ├── PlantError
                    ├── WaterError
                    └── HealthError
```

**À retenir:** Toujours hériter d'`Exception`, jamais de `BaseException` directement.

## 2. Flux d'Exécution Try/Except/Else/Finally

```python
try:
    # 1. Exécuté en premier
    risky_code()
except ValueError:
    # 2. Exécuté SI ValueError levé
    handle_error()
else:
    # 3. Exécuté SI aucune exception
    success_code()
finally:
    # 4. TOUJOURS exécuté
    cleanup()
```

**Ordre garanti:**
1. try
2. except (si exception) OU else (si pas d'exception)
3. finally (toujours)

## 3. Bonnes Pratiques

**✅ À FAIRE:**
- Capturer des exceptions spécifiques: `except ValueError`
- Utiliser finally pour cleanup: `finally: file.close()`
- Créer des exceptions custom pour logique métier
- Messages d'erreur explicites et actionnables
- Type hints sur toutes les fonctions

**❌ À ÉVITER:**
- `except Exception` (trop large)
- `except:` sans type (capture TOUT, même KeyboardInterrupt)
- Ignorer silencieusement les erreurs: `except: pass`
- Utiliser exceptions pour le contrôle de flux normal
- Lever Exception directe au lieu d'une subclass

## 4. Fail Fast Principle

**Principe:** "Il vaut mieux échouer tôt et visiblement que continuer avec des données corrompues."

**Application dans P02:**
- Ex4: `check_plant_health()` valide immédiatement et lève si invalide
- Ex5: `add_plant()` refuse les plantes sans nom dès l'ajout
- Résultat: Erreurs détectées à la source, pas propagées silencieusement

---

# 🎯 Questions Transversales Probables

## Q: "Quelle est la différence entre un crash et une exception?"

**R:** "Un **crash** est l'arrêt non contrôlé du programme. Une **exception** est un événement géré qui peut être capturé avec try/except. Notre projet démontre justement comment transformer des situations de crash potentiel en gestions gracieuses d'erreurs."

## Q: "Pourquoi ce projet s'appelle 'Data Engineering for Smart Agriculture'?"

**R:** "En agriculture intelligente, on collecte des données de capteurs (température, humidité, etc.). Ces données peuvent être corrompues (capteurs défaillants, transmission échouée). Notre code démontre comment construire des pipelines de données **résilients** qui:
- Valident les entrées (Ex0)
- Gèrent différents types d'erreurs (Ex1)
- Maintiennent le fonctionnement malgré les erreurs (Ex5)

C'est exactement ce dont on a besoin en production pour des systèmes critiques."

## Q: "Quel exercice a été le plus difficile et pourquoi?"

**R:** "L'exercice 5 car il fallait intégrer TOUS les concepts précédents de manière cohérente. Il ne suffit pas de savoir utiliser try/except séparément - il faut les orchestrer ensemble dans une architecture réelle. La difficulté était de créer une classe qui:
- Utilise des exceptions personnalisées (Ex2)
- Lève ses propres erreurs (Ex4)
- Garantit le cleanup (Ex3 - finally)
- Récupère après erreurs (recovery)

C'est la différence entre connaître la théorie et l'appliquer en pratique."

## Q: "Si vous deviez refaire ce projet, que changeriez-vous?"

**R:** "Deux choses:
1. **Ex0:** Implémenter les tests automatiques au lieu d'input() interactif pour être 100% conforme au sujet
2. **Ex5:** Créer une classe de logging pour tracer toutes les erreurs dans un fichier, utile pour le debugging en production

Mais globalement, l'architecture actuelle est solide et extensible."

---

# 📊 Tableau Récapitulatif des Exercices

| Ex | Concept Principal | Difficulté | Note | Point Clé |
|----|-------------------|------------|------|-----------|
| **0** | try/except/else | ⭐️⭐️ | 7/10 | Validation d'input |
| **1** | Multi-exceptions | ⭐️⭐️ | 9.5/10 | 4 types d'erreurs |
| **2** | Exceptions custom | ⭐️⭐️⭐️ | 10/10 | Héritage |
| **3** | finally | ⭐️⭐️⭐️ | 9.5/10 | Cleanup garanti |
| **4** | raise | ⭐️⭐️⭐️ | 9.5/10 | Validations métier |
| **5** | **INTÉGRATION** | ⭐️⭐️⭐️⭐️ | 9/10 | **Tout ensemble** |

---

# 🗣️ Conseils pour la Soutenance

## Avant la Soutenance:
1. ✅ **Relire le code** de chaque exercice
2. ✅ **Tester** tous les programmes avant
3. ✅ **Préparer** des exemples de modifications live si demandé
4. ✅ **Réviser** les concepts théoriques (hiérarchie exceptions, flux try/except)

## Pendant la Soutenance:

### ✅ À FAIRE:
- **Parler clairement** et éviter le jargon inutile
- **Montrer le code** et l'exécution live
- **Expliquer les choix** de conception ("J'ai choisi ValueError car...")
- **Être honnête** sur les limitations (Ex0 interactif)
- **Montrer l'enthousiasme** pour le sujet

### ❌ À ÉVITER:
- Dire "je ne sais pas" sans réfléchir
- Blâmer le sujet si quelque chose ne marche pas
- Lire le code sans expliquer
- Ignorer les questions de l'évaluateur

## Structure de Réponse Idéale:

**Question complexe → Méthode STAR:**
1. **Situation:** Contexte du problème
2. **Task:** Ce qu'il fallait faire
3. **Action:** Ce que j'ai implémenté
4. **Result:** Résultat obtenu

**Exemple:**
> Q: "Expliquez votre gestion des erreurs dans Ex5"
> 
> R: "**Situation:** Le système doit gérer des opérations risquées (ajout plante, arrosage).  
> **Task:** Continuer à fonctionner même si une opération échoue.  
> **Action:** J'ai créé des exceptions personnalisées (PlantError, WaterError) et encapsulé chaque opération dans try/except.  
> **Result:** Le système peut ajouter une plante invalide (erreur catchée) puis continuer à arroser les autres. C'est le recovery."

---

# 🎬 Conclusion de la Soutenance

## Message de Clôture (1 minute):

"Ce projet m'a permis de maîtriser la gestion d'erreurs en Python, compétence essentielle pour créer des applications robustes en production. J'ai appris que gérer les erreurs ne consiste pas seulement à éviter les crashes, mais à concevoir des systèmes **résilients** qui:
- Détectent les problèmes tôt (fail fast)
- Informent clairement l'utilisateur
- Continuent de fonctionner malgré les erreurs (recovery)
- Garantissent le nettoyage des ressources (finally)

L'exercice 5 démontre l'intégration de tous ces concepts dans une architecture réelle, applicable à des systèmes agricoles intelligents ou tout autre domaine critique."

## Points Forts du Projet à Réitérer:
✅ Tous les concepts d'error handling maîtrisés  
✅ Code de qualité production (type hints, docstrings)  
✅ Aucun programme ne crash  
✅ Architecture extensible et maintenable  
✅ **Note globale: 9.2/10**

---

# 📝 Checklist Finale Avant Soutenance

- [ ] Tous les programmes testés et fonctionnels
- [ ] Code relu et compris en profondeur
- [ ] Concepts théoriques révisés (hiérarchie, flux)
- [ ] Réponses préparées pour questions probables
- [ ] Exemples de modifications live prêts
- [ ] Attitude positive et professionnelle
- [ ] Temps de présentation calculé (20-30 min)

---

**Bonne chance pour ta soutenance! 🍀**

**Rappel:** Tu as un excellent projet (9.2/10). Sois confiant, explique clairement tes choix, et démontre ta compréhension des concepts. Les évaluateurs cherchent à vérifier que tu comprends ce que tu as codé - et c'est clairement le cas ici.
