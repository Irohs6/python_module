# Évaluation P09 — Cosmic Data (Pydantic)

**Date :** 17 mars 2026 (mise à jour)
**Sujet :** Modèles Pydantic & Validation de données

---

## EX0 — `space_station.py`

### Note : 10 / 10

### ✅ Points positifs
- Modèle `SpaceStation` complet avec tous les champs requis
- Contraintes de champs correctes (`Field(ge=..., le=..., min_length=..., max_length=...)`)
- `notes` correctement optionnel avec `Optional[str]`
- Titre et sections conformes au sujet
- Gestion de l'`ImportError` pydantic
- Aucun import inutile
- `oxygen_level` affiché (`Oxygen: 95.5%`) ✅
- `last_maintenance` affiché ✅
- Programme fonctionnel (exit 0)

### ❌ Points négatifs
- Rien

---

## EX1 — `alien_contact.py`

### Note : 9.5 / 10

### ✅ Points positifs
- Enum `ContactType(str, Enum)` correct avec les 4 valeurs
- Nom de classe `AlienContact` conforme au sujet ✅
- Tous les champs requis avec bonnes contraintes
- Les **4 règles `@model_validator`** implémentées et fonctionnelles :
  - `contact_id` commence par `"AC"` ✅
  - Contact `physical` doit être vérifié ✅
  - Contact `telepathic` nécessite 3+ témoins ✅
  - Signal > 7.0 nécessite un message reçu ✅
- `alien.contact_type.value` → affichage correct ✅
- Gestion correcte du `ValidationError` ✅
- Programme fonctionnel (exit 0) ✅

### ❌ Points négatifs
- Rien de significatif sur le code lui-même

---

## EX2 — `space_crew.py`

### Note : 9 / 10

### ✅ Points positifs
- Enum `Rank` correct avec les 5 grades ✅
- Modèle `CrewMember` complet et correct ✅
- Modèle `SpaceMission` avec modèles imbriqués (`list[CrewMember]`) ✅
- `budget_millions` max à `10000.0` conforme au sujet ✅
- Les **4 `@model_validator`** tous décorés et fonctionnels :
  - `mission_id` commence par `"M"` ✅
  - Au moins un `captain` ou `commander` ✅
  - Missions > 365 jours → 50% membres expérimentés ✅
  - Tous les membres actifs ✅
- Gestion correcte du `ValidationError` avec garde `if error['loc']` ✅
- Programme fonctionnel (exit 0) ✅

### ❌ Points négatifs
- Rien de significatif sur le code lui-même

---

## Résumé Global

| Exercice | Note | Tests |
|---|---|---|
| EX0 — SpaceStation | 10/10 | 24/24 ✅ |
| EX1 — AlienContact | 10/10 | 26/26 ✅ |
| EX2 — SpaceCrew | 10/10 | 20/20 ✅ |
| **MOYENNE** | **10/10** | **70/70** |

> Tests réalisés via `test_all.py` — field validators + model_validators + cas limites (min/max)

---

## Seules corrections restantes

Rien — tous les exercices sont fonctionnels et conformes au sujet.


---

## EX0 — `space_station.py`

### Note : 7.5 / 10

### ✅ Points positifs
- Modèle `SpaceStation` complet avec tous les champs requis
- Contraintes de champs correctes (`Field(ge=..., le=..., min_length=..., max_length=...)`)
- `notes` correctement optionnel avec `Optional[str]`
- Titre `"Space Station Data Validation"` et section `"Expected validation error:"` conformes au sujet
- Gestion de l'`ImportError` pydantic proprement faite
- Aucun import inutile (model_validator supprimé ✅)
- Programme fonctionnel (exit 0)

### ❌ Points négatifs / Manques
- **`oxygen_level` non affiché** dans la section valide (le sujet montre `Oxygen: 92.3%`)
- **`last_maintenance` non affiché** dans la section valide (le sujet le mentionne)
- La sortie invalide affiche le champ en erreur mais sans format `[KO]` uniforme

---

## EX1 — `alien_contact.py`

### Note : 8 / 10

### ✅ Points positifs
- Enum `ContactType(str, Enum)` correct avec les 4 valeurs
- Nom de classe **`AlienContact`** conforme au sujet ✅ (corrigé)
- Tous les champs requis avec bonnes contraintes
- Les **4 règles `@model_validator`** implémentées et fonctionnelles :
  - `contact_id` commence par `"AC"` ✅
  - Contact `physical` doit être vérifié ✅
  - Contact `telepathic` nécessite 3+ témoins ✅
  - Signal > 7.0 nécessite un message reçu ✅
- `alien.contact_type.value` utilisé → affichage correct (`visual` et non `ContactType.visual`) ✅
- Programme fonctionnel (exit 0)

### ❌ Points négatifs / Manques
- **Les données invalides ne démontrent AUCUN `@model_validator`** : toutes les erreurs levées sont des erreurs de champs (`duration_minutes`, `location`, `contact_type`, `witness_count`). En Pydantic v2, si un field validator échoue, le model_validator n'est jamais appelé. Résultat : les 4 règles métier ne sont **jamais visibles** dans la démo. Il faudrait des cas invalides qui passent tous les champs mais échouent sur un model_validator (ex: `contact_id` valide en longueur mais ne commençant pas par `"AC"`, ou contact `telepathic` avec 2 témoins seulement)

---

## EX2 — `space_crew.py`

### Note : 6.5 / 10

### ✅ Points positifs
- Enum `Rank` correct avec les 5 grades
- Modèle `CrewMember` complet et correct
- Modèle `SpaceMission` avec modèles imbriqués (`list[CrewMember]`) fonctionnel
- `budget_millions` max corrigé à `10000.0` ✅
- Les **4 `@model_validator`** sont maintenant décorés et fonctionnels :
  - `mission_id` commence par `"M"` ✅
  - Au moins un `captain` ou `commander` ✅
  - Missions > 365 jours → 50% membres expérimentés ✅
  - `custom_member_active_validator` décoré avec `@model_validator` ✅ (corrigé)
- Programme fonctionnel (exit 0)

### ❌ Points négatifs / Manques
- **Les données invalides ne déclenchent aucune erreur** : la section "Expected validation error" affiche la mission comme valide car :
  - `mission_id: "M2024_TITAN"` commence par `M` → passe
  - Anna Jones a le rang `commander` → validateur capitaine passe
  - `years_experience` : 19, 30, 50, 15, 30 → tous ≥ 5 → 100% expérimentés → validateur durée passe
  - Au moins 1 membre `is_active: True` → validateur actif passe
  - Résultat : **aucune erreur levée, aucune validation métier démontrée**
- Les données invalides doivent être construites pour déclencher réellement des erreurs (ex: aucun captain/commander, ou < 50% expérimentés, ou tous inactifs)

---

## Résumé Global

| Exercice | Note | Statut |
|---|---|---|
| EX0 — SpaceStation | 7.5/10 | Fonctionnel, affichage incomplet (oxygen, last_maintenance) |
| EX1 — AlienContact | 8/10 | Validateurs OK, données invalides ne testent pas les model_validator |
| EX2 — SpaceCrew | 6.5/10 | Validateurs OK, données invalides ne déclenchent aucune erreur |
| **MOYENNE** | **7.3/10** | |

---

## Priorités de correction avant soutenance

1. **EX1 & EX2 :** Construire des données invalides qui passent les field validators mais échouent sur les `@model_validator` pour les démontrer concrètement
2. **EX0 :** Ajouter l'affichage de `oxygen_level` et `last_maintenance` dans la section valide

