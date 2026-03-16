# Cosmic Data
## Découvrir les Modèles Pydantic & la Validation

> **Résumé :** Maîtrisez la validation de données Pydantic à travers des exercices sur le thème de l'espace. Apprenez à créer des modèles robustes, à implémenter une validation personnalisée, et à gérer des structures imbriquées tout en traitant des flux de données cosmiques.
>
> **Version :** 2.0

---

## Table des Matières

- [I. Introduction](#i-introduction)
- [II. Instructions sur l'IA](#ii-instructions-sur-lia)
- [III. Instructions Générales](#iii-instructions-générales)
  - [III.1 Exigences Techniques](#iii1-exigences-techniques)
  - [III.2 Outils Disponibles](#iii2-outils-disponibles)
  - [III.3 Concepts Clés de Pydantic](#iii3-concepts-clés-de-pydantic)
- [IV. Exercice 0 : Données de Station Spatiale](#iv-exercice-0--données-de-station-spatiale)
  - [IV.1 Contexte](#iv1-contexte)
  - [IV.2 Exigences](#iv2-exigences)
- [V. Exercice 1 : Journaux de Contact Alien](#v-exercice-1--journaux-de-contact-alien)
  - [V.1 Contexte](#v1-contexte)
  - [V.2 Exigences](#v2-exigences)
- [VI. Exercice 2 : Gestion de l'Équipage Spatial](#vi-exercice-2--gestion-de-léquipage-spatial)
  - [VI.1 Contexte](#vi1-contexte)
  - [VI.2 Exigences](#vi2-exigences)
- [VII. Soumission et Évaluation par les Pairs](#vii-soumission-et-évaluation-par-les-pairs)

---

## I. Introduction

Bienvenue à l'**Observatoire de Données Cosmiques**, la principale installation de traitement de données de la galaxie ! En tant qu'Ingénieur Données junior, vous avez été affecté à la validation des flux de données provenant de diverses missions spatiales, de rapports de contact alien, et des systèmes de surveillance des stations.

**Votre mission :** Apprendre Pydantic, la bibliothèque de validation de données la plus puissante de Python, à travers des scénarios cosmiques concrets. Vous progresserez des modèles basiques vers des règles de validation complexes, garantissant l'intégrité des données à travers l'univers connu.

### Le Thème Cosmique

Tout au long de cette activité, vous travaillerez avec des données sur le thème de l'espace pour rendre l'apprentissage plus engageant :

- 🚀 **Stations Spatiales :** Fondamentaux de la validation de données de base
- 👽 **Contacts Aliens :** Règles et logiques de validation personnalisées
- 👨‍🚀 **Gestion d'Équipage :** Modèles imbriqués et relations complexes

Chaque exercice s'appuie sur le précédent, introduisant progressivement de nouveaux concepts Pydantic.

> 💡 **Astuce Pro :** Pydantic convertit automatiquement les types compatibles (comme les chaînes vers datetime) et fournit des messages d'erreur détaillés en cas d'échec de validation. C'est parfait pour construire des APIs robustes et des systèmes de traitement de données !

---

## II. Instructions sur l'IA

### ● Contexte

Durant votre apprentissage, l'IA peut vous aider dans de nombreuses tâches différentes. Prenez le temps d'explorer les diverses capacités des outils d'IA et comment ils peuvent soutenir votre travail. Cependant, abordez-les toujours avec prudence et évaluez les résultats de manière critique. Que ce soit du code, de la documentation, des idées ou des explications techniques, vous ne pouvez jamais être certain que votre question était bien formulée ou que le contenu généré est exact. Vos pairs sont une ressource précieuse pour vous aider à éviter les erreurs et les angles morts.

### ● Message Principal

- ☛ Utilisez l'IA pour réduire les tâches répétitives ou fastidieuses.
- ☛ Développez des compétences en prompting — tant en codage qu'en dehors — qui bénéficieront à votre future carrière.
- ☛ Apprenez comment les systèmes d'IA fonctionnent pour mieux anticiper et éviter les risques courants, les biais et les problèmes éthiques.
- ☛ Continuez à développer vos compétences techniques et comportementales en travaillant avec vos pairs.
- ☛ N'utilisez que le contenu généré par l'IA que vous comprenez pleinement et dont vous pouvez prendre la responsabilité.

### ● Règles pour l'Apprenant

- Vous devez prendre le temps d'explorer les outils d'IA et comprendre leur fonctionnement, afin de les utiliser de manière éthique et de réduire les biais potentiels.
- Vous devez réfléchir à votre problème avant de formuler un prompt — cela vous aide à écrire des prompts plus clairs, plus détaillés et plus pertinents avec un vocabulaire précis.
- Vous devez développer l'habitude de systématiquement vérifier, réviser, questionner et tester tout ce qui est généré par l'IA.
- Vous devez toujours solliciter une révision par les pairs — ne vous fiez pas uniquement à votre propre validation.

### ● Résultats Attendus de la Phase

- Développer des compétences de prompting générales et spécifiques au domaine.
- Booster votre productivité grâce à une utilisation efficace des outils d'IA.
- Continuer à renforcer la pensée computationnelle, la résolution de problèmes, l'adaptabilité et la collaboration.

### ● Commentaires et Exemples

- Vous rencontrerez régulièrement des situations — examens, évaluations, etc. — où vous devrez démontrer une vraie compréhension. Soyez préparé, continuez à développer vos compétences techniques et interpersonnelles.
- Expliquer votre raisonnement et débattre avec vos pairs révèle souvent des lacunes dans votre compréhension. Faites de l'apprentissage entre pairs une priorité.
- Les outils d'IA manquent souvent de votre contexte spécifique et ont tendance à fournir des réponses génériques. Vos pairs, qui partagent votre environnement, peuvent offrir des insights plus pertinents et précis.
- Là où l'IA génère la réponse la plus probable, vos pairs peuvent apporter des perspectives alternatives et des nuances précieuses. Comptez sur eux comme point de contrôle qualité.

| ✅ **Bonne pratique** | ❌ **Mauvaise pratique** |
|---|---|
| Je demande à l'IA : "Comment tester une fonction de tri ?" Elle me donne quelques idées. Je les essaie et révise les résultats avec un pair. Nous affinons l'approche ensemble. | Je demande à l'IA d'écrire une fonction entière, je la copie-colle dans mon projet. Lors de l'évaluation par les pairs, je ne peux pas expliquer ce qu'elle fait ni pourquoi. Je perds en crédibilité — et je rate mon projet. |
| J'utilise l'IA pour aider à concevoir un parseur. Ensuite, je parcours la logique avec un pair. Nous détectons deux bugs et le réécrivons ensemble — mieux, plus proprement, et entièrement compris. | Je laisse Copilot générer mon code pour une partie clé de mon projet. Ça compile, mais je ne peux pas expliquer comment il gère les pipes. Lors de l'évaluation, je ne parviens pas à justifier et je rate mon projet. |

---

## III. Instructions Générales

### III.1 Exigences Techniques

- Python 3.10 ou ultérieur
- **Qualité du Code :** Votre code doit respecter les standards du linter flake8
- **Annotations de Types :** Toutes les fonctions et méthodes doivent inclure des annotations de types
- Gestionnaire de paquets `pip`
- Environnement virtuel (recommandé : `venv`, `virtualenv` ou `conda`)
- Pydantic 2.x (sera installé via pip)

### III.2 Outils Disponibles

Cette activité comprend des outils de génération de données pour vous aider à tester vos modèles Pydantic :

- `data_generator.py` — Générer des données de test réalistes pour tous les exercices
- `data_exporter.py` — Exporter des données aux formats JSON, CSV et Python
- `generated_data/` — Jeux de données pré-générés prêts à l'emploi

> ⚠️ **Imports autorisés :** Vous pouvez importer des données JSON et CSV depuis le répertoire des outils. Les modules de la bibliothèque standard (`json`, `csv`, `datetime`, etc.) sont autorisés.

> ⚠️ **Important :** Cette activité se concentre sur la syntaxe Pydantic v2. Évitez les décorateurs dépréciés comme `@validator` — utilisez `@model_validator` pour la validation personnalisée à la place.

### III.3 Concepts Clés de Pydantic

#### `BaseModel`
La base de tous les modèles Pydantic. Héritez de `BaseModel` pour créer des classes de données validées.

#### `Field`
Utilisez `Field(...)` pour ajouter des contraintes de validation, des descriptions et des valeurs par défaut aux attributs d'un modèle.

#### `model_validator`
Utilisez le décorateur `@model_validator(mode='after')` pour une logique de validation personnalisée qui s'exécute après la validation intégrée de Pydantic. Ceci remplace le décorateur `@validator` déprécié de Pydantic v1.

---

## IV. Exercice 0 : Données de Station Spatiale

> **Répertoire :** `ex0/`
> **Fichiers à soumettre :** `space_station.py`
> **Autorisations :** Aucune
>
> **Objectif :** Apprendre la création de modèles Pydantic de base avec `BaseModel` et la validation par `Field`.

### IV.1 Contexte

L'Observatoire de Données Cosmiques surveille des centaines de stations spatiales à travers la galaxie. Chaque station rapporte des statistiques vitales incluant la taille de l'équipage, les niveaux d'énergie et le statut opérationnel. Votre première tâche est de créer un système de validation pour ces données critiques.

### IV.2 Exigences

#### Modèle `SpaceStation`

Créez un modèle Pydantic avec ces champs validés :

| Champ | Type | Contraintes |
|---|---|---|
| `station_id` | `str` | 3 à 10 caractères |
| `name` | `str` | 1 à 50 caractères |
| `crew_size` | `int` | 1 à 20 personnes |
| `power_level` | `float` | 0.0 à 100.0 % |
| `oxygen_level` | `float` | 0.0 à 100.0 % |
| `last_maintenance` | `datetime` | Champ datetime |
| `is_operational` | `bool` | Défaut : `True` |
| `notes` | `str` (optionnel) | Max 200 caractères |

#### Fonction de Démonstration

Incluez une fonction `main()` qui :

- Crée une instance de station spatiale valide
- Affiche les informations de la station clairement
- Tente de créer une station invalide (ex. : `crew_size > 20`)
- Affiche le message d'erreur de validation

#### Exemple de Sortie Attendue

```
Space Station Data Validation
========================================
Valid station created:
ID: ISS001
Name: International Space Station
Crew: 6 people
Power: 85.5%
Oxygen: 92.3%
Status: Operational
========================================
Expected validation error:
Input should be less than or equal to 20
```

> 🤔 **Réfléchissez :** Comment fonctionne la conversion automatique de types de Pydantic ? Que se passe-t-il lorsque vous passez un timestamp sous forme de chaîne à un champ datetime ?

---

## V. Exercice 1 : Journaux de Contact Alien

> **Répertoire :** `ex1/`
> **Fichiers à soumettre :** `alien_contact.py`
> **Autorisations :** Aucune
>
> **Objectif :** Maîtriser la validation personnalisée avec `@model_validator` pour des règles métier complexes.

### V.1 Contexte

L'Observatoire reçoit des rapports de contact alien provenant de toute la galaxie. Ces rapports sensibles nécessitent des règles de validation sophistiquées qui vont au-delà des simples contraintes de champs. Les différents types de contact ont des exigences différentes, et certaines combinaisons de données indiquent des rapports potentiellement frauduleux.

### V.2 Exigences

#### Enum `ContactType`

Définissez les types de contact : `radio`, `visual`, `physical`, `telepathic`

#### Modèle `AlienContact`

Créez un modèle Pydantic avec ces champs :

| Champ | Type | Contraintes |
|---|---|---|
| `contact_id` | `str` | 5 à 15 caractères |
| `timestamp` | `datetime` | Date et heure du contact |
| `location` | `str` | 3 à 100 caractères |
| `contact_type` | `ContactType` | Enum de type de contact |
| `signal_strength` | `float` | 0.0 à 10.0 |
| `duration_minutes` | `int` | 1 à 1440 (max 24h) |
| `witness_count` | `int` | 1 à 100 personnes |
| `message_received` | `str` (optionnel) | Max 500 caractères |
| `is_verified` | `bool` | Défaut : `False` |

#### Règles de Validation Personnalisées

Implémentez `@model_validator(mode='after')` avec ces règles métier :

- L'ID de contact doit commencer par `"AC"` (Alien Contact)
- Les rapports de contact physique doivent être vérifiés
- Un contact télépathique nécessite au moins 3 témoins
- Les signaux forts (> 7.0) doivent inclure des messages reçus

#### Fonction de Démonstration

Montrez des rapports de contact valides et invalides avec des messages d'erreur clairs.

#### Exemple de Sortie Attendue

```
Alien Contact Log Validation
======================================
Valid contact report:
ID: AC_2024_001
Type: radio
Location: Area 51, Nevada
Signal: 8.5/10
Duration: 45 minutes
Witnesses: 5
Message: 'Greetings from Zeta Reticuli'
======================================
Expected validation error:
Telepathic contact requires at least 3 witnesses
```

> 💡 **Astuce Avancée :** Le décorateur `@model_validator` vous permet de valider l'ensemble du modèle après que tous les champs ont été validés. N'oubliez pas de retourner `self` à la fin de votre fonction de validation.

---

## VI. Exercice 2 : Gestion de l'Équipage Spatial

> **Répertoire :** `ex2/`
> **Fichiers à soumettre :** `space_crew.py`
> **Autorisations :** Aucune
>
> **Objectif :** Maîtriser les modèles Pydantic imbriqués et les relations de données complexes.

### VI.1 Contexte

Les missions spatiales nécessitent une gestion attentive de l'équipage. Chaque mission comporte plusieurs membres d'équipage avec des grades, des spécialisations et des niveaux d'expérience différents. L'Observatoire a besoin de valider que les équipages de mission respectent les exigences de sécurité et opérationnelles avant l'approbation du lancement.

### VI.2 Exigences

#### Enum `Rank`

Définissez les grades d'équipage : `cadet`, `officer`, `lieutenant`, `captain`, `commander`

#### Modèle `CrewMember`

Membre d'équipage individuel avec ces champs :

| Champ | Type | Contraintes |
|---|---|---|
| `member_id` | `str` | 3 à 10 caractères |
| `name` | `str` | 2 à 50 caractères |
| `rank` | `Rank` | Enum de grade |
| `age` | `int` | 18 à 80 ans |
| `specialization` | `str` | 3 à 30 caractères |
| `years_experience` | `int` | 0 à 50 ans |
| `is_active` | `bool` | Défaut : `True` |

#### Modèle `SpaceMission`

Mission avec liste d'équipage et ces champs :

| Champ | Type | Contraintes |
|---|---|---|
| `mission_id` | `str` | 5 à 15 caractères |
| `mission_name` | `str` | 3 à 100 caractères |
| `destination` | `str` | 3 à 50 caractères |
| `launch_date` | `datetime` | Date de lancement |
| `duration_days` | `int` | 1 à 3650 jours (max 10 ans) |
| `crew` | `List[CrewMember]` | 1 à 12 membres |
| `mission_status` | `str` | Défaut : `"planned"` |
| `budget_millions` | `float` | 1.0 à 10000.0 millions de dollars |

#### Règles de Validation de Mission

Implémentez `@model_validator(mode='after')` avec ces exigences de sécurité :

- L'ID de mission doit commencer par `"M"`
- Doit avoir au moins un `Commander` ou `Captain`
- Les missions longues (> 365 jours) nécessitent 50% de membres expérimentés (5+ ans)
- Tous les membres de l'équipage doivent être actifs

#### Fonction de Démonstration

Montrez une mission valide avec les détails de l'équipage et une mission invalide qui échoue à la validation.

#### Exemple de Sortie Attendue

```
Space Mission Crew Validation
=========================================
Valid mission created:
Mission: Mars Colony Establishment
ID: M2024_MARS
Destination: Mars
Duration: 900 days
Budget: $2500.0M
Crew size: 3
Crew members:
- Sarah Connor (commander) - Mission Command
- John Smith (lieutenant) - Navigation
- Alice Johnson (officer) - Engineering
=========================================
Expected validation error:
Mission must have at least one Commander or Captain
```

> 🤔 **Réfléchissez :** Comment Pydantic gère-t-il la validation de modèles imbriqués ? Que se passe-t-il lorsqu'un `CrewMember` échoue à la validation au sein d'une `SpaceMission` ?

---

## VII. Soumission et Évaluation par les Pairs

Soumettez votre devoir dans votre dépôt Git comme d'habitude. Seul le travail présent dans votre dépôt sera évalué lors de la soutenance. N'hésitez pas à vérifier deux fois les noms de vos fichiers pour vous assurer qu'ils sont corrects.

> ⚠️ Vous devez retourner **uniquement les fichiers demandés** par le sujet de cette activité.
