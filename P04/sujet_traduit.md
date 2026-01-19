# Archiviste des données — Préservation numérique dans les Cyber Archives

Ce document est une traduction en français du sujet fourni, avec les noms de fichiers, commandes et formats d’affichage conservés pour cohérence lors de l’évaluation.

---

## Accès au coffre — Récupération (exemple de récupération)

Si le coffre est inaccessible, votre programme doit afficher :

ERROR:
Storage vault not found. Run data generator first. Remember: a
good archivist always checks if the vault exists before attempting
access. Trying to read non-existent files is like trying to open a
door that isn’t there—it never ends well.

Objectif attendu : votre programme doit afficher l’en-tête système, l’état d’accès au coffre, les données récupérées avec le bon formatage, puis une confirmation de fin. L’exemple terminal ci-dessous montre le format exact. Vous pouvez ajouter une touche d’« archiviste » tant que les informations essentielles sont présentes.

Exemple de journal de récupération :

```
$> python3 ft_ancient_text.py
=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===
Accessing Storage Vault: ancient_fragment.txt
Connection established...
RECOVERED DATA:
[FRAGMENT 001] Digital preservation protocols established 2087
[FRAGMENT 002] Knowledge must survive the entropy wars
[FRAGMENT 003] Every byte saved is a victory against oblivion
Data recovery complete. Storage unit disconnected.
```

Questions :
- Que se passe-t-il pour le système de stockage si les connexions ne sont pas correctement fermées ?
- Pourquoi le protocole de déconnexion est-il critique ?

---

## Chapitre VII — Exercice 1 : Création d’archive

Exercise1
ft_archive_creation

Répertoire : ex1/
Fichiers à rendre : ft_archive_creation.py
Autorisé : open(), write(), close(), print()

Briefing : Excellent travail sur la récupération ! Le Chef Archiviste est impressionné. Votre prochaine mission : établir un nouveau protocole de préservation en créant de nouvelles entrées d’archives. Il est temps de faire l’histoire plutôt que de simplement la lire !

Protocole de création : Établir une nouvelle unité de stockage nommée new_discovery.txt et y inscrire trois entrées critiques : informations sur une percée en algorithmes quantiques, métriques d’amélioration de performance (gain d’efficacité de 347 %), et identification de l’archiviste. Pensez-y comme une capsule temporelle numérique pour les générations futures.

Rappel : Le mode « préservation » (écriture) crée de nouvelles archives ou remplace les existantes. Contrairement à la lecture, l’écriture est permanente — une fois le coffre scellé, les données intègrent les Archives éternelles.

Objectif attendu : afficher l’en-tête système, l’initialisation de l’unité de stockage, l’inscription des données avec des entrées numérotées, et la confirmation de fin. L’exemple terminal montre le format attendu ; vous pouvez y ajouter vos touches d’archiviste.

Avertissement : Soyez prudent avec les opérations d’écriture ! Dans les Archives réelles, écraser accidentellement des données historiques est un crime contre le savoir. Vérifiez toujours vos noms de fichiers.

Exemple de journal d’archive :

```
$> python3 ft_archive_creation.py
=== CYBER ARCHIVES - PRESERVATION SYSTEM ===
Initializing new storage unit: new_discovery.txt
Storage unit created successfully...
Inscribing preservation data...
[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee
Data inscription complete. Storage unit sealed.
Archive 'new_discovery.txt' ready for long-term preservation.
```

Questions :
- Quelle est la différence critique entre le mode d’extraction (« r ») et le mode de préservation (« w ») ?
- Pourquoi cette distinction est-elle vitale pour les archivistes ?

---

## Chapitre VIII — Exercice 2 : Gestion des flux

Exercise2
ft_stream_management

Répertoire : ex2/
Fichiers à rendre : ft_stream_management.py
Autorisé : sys, sys.stdin, sys.stdout, sys.stderr, input(), print()

Briefing : Travail d’archive remarquable ! Le Chef Archiviste vous confie un nouveau défi. Les Archives fonctionnent via trois canaux de données sacrés actifs depuis les débuts de la civilisation numérique. Ces canaux sont plus anciens qu’Internet — l’équivalent des routes commerciales antiques.

Protocole de communication : Accéder aux trois canaux sacrés — flux d’entrée, canal standard, et canal d’alerte. Collecter l’identifiant de l’archiviste et son statut, puis démontrer une séparation correcte en routant chaque type de message vers son flux approprié.

Métaphore : Considérez les flux comme des fréquences différentes : stdin pour recevoir, stdout pour les messages normaux, et stderr pour les alertes. Chacun a son rôle dans le réseau de communication.

Objectif attendu : afficher l’en-tête système, collecter l’entrée utilisateur (ID archiviste et rapport de statut), puis sortir les messages via les bons flux : messages standard via sys.stdout et alertes via sys.stderr. Terminer par une confirmation de test réussi.

Rappel : Ne mélangez jamais vos flux ! Envoyer une alerte sur le canal standard, c’est crier « FEU ! » en chuchotant dans une bibliothèque — cela annule l’objectif et sème la confusion.

Exemple de journal de communication :

```
$> python3 ft_stream_management.py
=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===
Input Stream active. Enter archivist ID: ARCH_7742
Input Stream active. Enter status report: All systems nominal
[STANDARD] Archive status from ARCH_7742: All systems nominal
[ALERT] System diagnostic: Communication channels verified
[STANDARD] Data transmission complete
Three-channel communication test successful.
```

Questions :
- Pourquoi les Archives maintiennent-elles des canaux séparés pour les données standard et les alertes ?
- Que pourrait-il se passer si ces flux étaient mélangés ?

---

## Chapitre IX — Exercice 3 : Sécurité du coffre

Exercise3
ft_vault_security

Répertoire : ex3/
Fichiers à rendre : ft_vault_security.py
Autorisé : open(), read(), write(), print()

Exigence : Utiliser l’instruction « with » (gestionnaire de contexte) pour garantir une gestion correcte des fichiers. « with » ferme automatiquement les fichiers même en cas d’erreur, évitant la corruption des données et les fuites de ressources.

Briefing : Excellentes compétences de communication ! Le Chef Archiviste remarque votre potentiel et vous promeut aux opérations de Sécurité du coffre. Bienvenue dans la cour des grands — une erreur peut corrompre des siècles de connaissance.

Contexte historique : Après la Grande Corruption des Données de 2089, le protocole ancien « with » a été créé pour garantir la fermeture correcte des connexions lors des défaillances système.

Protocole sacré : Avec « with », trois choses se produisent automatiquement : le coffre s’ouvre, vos opérations s’exécutent sous protection, et le coffre se scelle — même en cas de problème. C’est un garde du corps numérique pour vos fichiers.

Objectif : Implémenter des opérations de fichier sécurisées avec « with » pour la lecture de données classifiées et la préservation de nouvelles informations. Le programme doit démontrer un scellement automatique du coffre, quelle que soit la réussite ou l’échec de l’opération, avec un journal de sécurité professionnel.

Principe clé : C’est l’essence de la gestion sûre des ressources : acquérir, utiliser, relâcher — garanti. Sans « with », vous laissez des portes de coffre ouvertes en pleine tempête numérique.

Exemple de journal de sécurité :

```
$> python3 ft_vaul_security.py
=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===
Initiating secure vault access...
Vault connection established with failsafe protocols
SECURE EXTRACTION:
[CLASSIFIED] Quantum encryption keys recovered
[CLASSIFIED] Archive integrity: 100%
SECURE PRESERVATION:
[CLASSIFIED] New security protocols archived
Vault automatically sealed upon completion
All vault operations completed with maximum security.
```

Questions :
- Comment le protocole « with » empêche-t-il la corruption des données ?
- Quel est le principe RAII et pourquoi est-il crucial pour la sécurité du coffre ?

---

## Chapitre X — Exercice 4 : Réponse à la crise

Exercise4
ft_crisis_response

Répertoire : ex4/
Fichiers à rendre : ft_crisis_response.py
Autorisé : open(), read(), write(), print()

Exigence : Utiliser l’instruction « with » pour la sécurité des fichiers ET des blocs try/except pour la gestion d’erreurs. Vous devez gérer FileNotFoundError, PermissionError et autres exceptions avec grâce, en assurant la fermeture correcte des fichiers même en cas d’erreurs.

Briefing : Travail de sécurité exceptionnel ! Le Chef Archiviste vous confie le test ultime : opérations de Réponse à la crise. C’est l’épreuve où l’on prouve sa capacité à affronter le chaos réel des désastres de données.

Préparation des données :
Exécuter : `python3 tools/data_generator.py` pour créer des fichiers de test, dont standard_archive.txt et d’autres. Votre programme testera l’accès à différents fichiers pour simuler des scénarios de crise.

Protocole de réponse : Développer un système complet de gestion de crise implémentant une fonction de gestionnaire pour les opérations d’archives. Le système doit gérer les échecs d’accès de manière élégante en combinant des protocoles de sécurité avec « with » pour prévenir la corruption pendant les erreurs.

Catégories de crise : Gérer les archives manquantes dans la matrice de stockage, les violations de protocoles de sécurité, les anomalies système inattendues et les opérations réussies. Tester des accès à des archives inexistantes, des coffres à accès restreint, et des opérations de récupération standard.

Objectif attendu : afficher des alertes de crise pour chaque tentative, des réponses adaptées selon le type d’erreur (FileNotFoundError, PermissionError ou autre), des confirmations d’état, puis une sécurité globale. Suivre précisément le format pour la cohérence.

Exemple de journal de crise :

```
$> python3 ft_crisis_response.py
=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===
CRISIS ALERT: Attempting access to 'lost_archive.txt'...
RESPONSE: Archive not found in storage matrix
STATUS: Crisis handled, system stable
CRISIS ALERT: Attempting access to 'classified_vault.txt'...
RESPONSE: Security protocols deny access
STATUS: Crisis handled, security maintained
ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...
SUCCESS: Archive recovered - ``Knowledge preserved for humanity''
STATUS: Normal operations resumed
All crisis scenarios handled successfully. Archives secure.
```

Questions :
- Quelles sont les menaces les plus dangereuses pour les archives numériques ?
- Comment une bonne réponse à la crise prévient-elle la perte de données et maintient-elle la stabilité du système ?

---

## Chapitre XI — Dépôt et rendu

Déposez votre travail dans votre dépôt Git habituel. Seul le contenu à l’intérieur de votre dépôt sera évalué lors de la soutenance. N’hésitez pas à vérifier les noms de vos fichiers.

Pendant l’évaluation, on pourra vous demander d’expliquer les opérations sur fichiers, de démontrer la gestion des erreurs, ou de montrer le fonctionnement de l’instruction « with ». Assurez-vous de bien comprendre ces concepts.

Vous ne devez rendre que les fichiers demandés par le sujet. Concentrez-vous sur un code propre et simple qui démontre clairement votre maîtrise des opérations sur fichiers.
