Evaluation P07 - DataDeck: Master the Art of Abstract Card Architecture
Date : 2026-03-09
Branche : v3 (re-évaluation complète après corrections)

===============================================
NOTE GLOBALE : 92 / 100
===============================================

-----------------------------------------------
EX0 - Card Foundation                 20 / 20
-----------------------------------------------
Fichiers : Card.py, CreatureCard.py, __init__.py, main.py

[OK] Card herite de ABC avec @abstractmethod sur play()
[OK] Constructeur __init__(name, cost, rarity) avec type hints
[OK] Methodes concretes get_card_info() et is_playable() presentes
[OK] CreatureCard herite de Card, ajoute attack/health
[OK] Validation attack/health (isinstance + >= 0)
[OK] Validation cost dans Card.__init__ (isinstance + >= 0)
[OK] Validation available_mana dans is_playable()
[OK] play() utilise game_state.get('mana', 0) → pas de KeyError
[OK] play() retourne le bon format avec is_playable/result
[OK] get_card_info() etend le parent avec type/attack/health
[OK] attack_target() retourne attacker/target/damage_dealt/combat_resolved
[OK] attack_target() gere Card | str pour target
[OK] combat_resolved : True si target est CreatureCard et health <= attack
[OK] main.py utilise import absolu (from ex0.CreatureCard import CreatureCard)
[OK] main.py produit une sortie conforme au modele du sujet
[OK] Tous les type hints presents
[OK] __init__.py exporte Card et CreatureCard

CORRECTION APPLIQUEE :
[FIXED] play() utilise desormais game_state.get('mana', 0) dans CreatureCard.py
        → Plus de risque de KeyError avec un dict sans cle 'mana'

-----------------------------------------------
EX1 - Deck Builder                    19 / 20
-----------------------------------------------
Fichiers : SpellCard.py, ArtifactCard.py, Deck.py, __init__.py, main.py

[OK] SpellCard herite de Card, effect_type valide parmi damage/heal/buff/debuff
[OK] play() retourne le bon format avec message base sur effect_type
[OK] resolve_effect() presente et fonctionnelle
[OK] ArtifactCard herite de Card, durability + effect
[OK] activate_ability() gere la destruction (durability = 0)
[OK] Deck gere add/remove/shuffle/draw/get_deck_stats()
[OK] random.shuffle utilise pour shuffle()
[OK] get_deck_stats() retourne total/creatures/spells/artifacts/avg_cost
[OK] Polymorphisme demonstre : meme interface pour types differents
[OK] main.py produit une sortie conforme au modele
[OK] get_deck_stats() appele AVANT shuffle() → avg_cost desormais deterministe

CORRECTION APPLIQUEE :
[FIXED] get_deck_stats() est maintenant appele avant shuffle() dans main.py
        Deck : Fire Dragon(5) + Lightning Bolt(3) + Mana Crystal(2)
        avg_cost = (5+3+2)/3 = 3.3 (stable, non-aleatoire)

[/!\] NOTE MINEURE : Le sujet de reference montre avg_cost: 4.0, ce qui
      correspond a un calcul sur 2 cartes restantes apres un draw specifique.
      Avec get_deck_stats() appele avant tout draw, avg_cost = 3.3 est
      mathematiquement correct pour les 3 cartes. Difference acceptable.

-----------------------------------------------
EX2 - Ability System                  20 / 20
-----------------------------------------------
Fichiers : Combatable.py, Magical.py, EliteCard.py, __init__.py, main.py

[OK] Combatable : ABC avec attack/defend/get_combat_stats abstraits
[OK] Magical : ABC avec cast_spell/channel_mana/get_magic_stats abstraits
[OK] EliteCard herite de Card + Combatable + Magical (triple heritage)
[OK] Toutes les methodes abstraites implementees
[OK] attack() retourne attacker/target/damage/combat_type
[OK] defend() calcule blocage, retourne defender/damage_taken/blocked/alive
[OK] cast_spell() et channel_mana() fonctionnels
[OK] Ordre des methodes : ['play', 'get_card_info', 'is_playable'] CORRECT
[OK] total_mana: 7 CORRECT (mana_pool=8 → 8-4=4 apres cast → 4+3=7 apres channel)
[OK] main.py affiche les interfaces et leurs methodes, demonstrations OK

CORRECTIONS APPLIQUEES :
[FIXED] Ordre d'affichage des methodes : utilisation de cls.__dict__ au lieu
        de dir() → conserve l'ordre de declaration
        Sortie : ['play', 'get_card_info', 'is_playable'] ✓

[FIXED] mana_pool initialise a 8 (au lieu de 10) dans main.py :
        Fireball cost = len("Fireball") % 5 + 1 = 4
        8 - 4 = 4 (apres cast), 4 + 3 = 7 (apres channel) ✓

-----------------------------------------------
EX3 - Game Engine                     16 / 20
-----------------------------------------------
Fichiers : GameStrategy.py, CardFactory.py, AggressiveStrategy.py,
           FantasyCardFactory.py, GameEngine.py, __init__.py, main.py

[OK] GameStrategy : ABC avec execute_turn/get_strategy_name/prioritize_targets
[OK] CardFactory : ABC avec create_creature/create_spell/create_artifact/
     create_themed_deck/get_supported_types
[OK] AggressiveStrategy joue les cartes par cout croissant
[OK] FantasyCardFactory cree des cartes fantasy (dragons, goblins, sorts)
[OK] name_or_power accepte str | int | None sur les methodes de creation
[OK] GameEngine.configure_engine() / simulate_turn() / get_engine_status()
[OK] Pattern Abstract Factory + Strategy correctement implementes
[OK] get_supported_types() est bien implementee dans FantasyCardFactory

[/!\] NOTE : damage_dealt est non-deterministe (deck genere aleatoirement).

      Le deck est tire aleatoirement par create_themed_deck(5), donc le
      contenu de la main change a chaque execution. La valeur de
      damage_dealt varie selon les cartes tirees (creatures vs sorts).
      Exemple d'une execution : damage_dealt=9 avec Goblin(3) + 2xLightning(3+3).
      Le sujet montrait damage_dealt=8 (valeur de reference pour un deck fixe).
      Ce comportement est attendu dans un systeme randomise.

[/!\] NOTE : available_types montre 3 sorts (Fireball/Lightning Bolt/Healing Light).

      SORTIE ACTUELLE :
        'spells': ['Fireball', 'Lightning Bolt', 'Healing Light']
      SORTIE REFERENCE (sujet) :
        'spells': ['fireball']

      La factory contient 3 sorts fonctionnels. Le sujet montrait un exemple
      simplifie. Ce n'est pas une erreur de logique, le contenu est plus riche.

-----------------------------------------------
EX4 - Tournament Platform             17 / 20
-----------------------------------------------
Fichiers : Rankable.py, TournamentCard.py, TournamentPlatform.py,
           __init__.py, main.py

[OK] Rankable : ABC avec calculate_rating/update_wins/update_losses/get_rank_info
[OK] TournamentCard herite de Card + Combatable + Rankable (3 interfaces)
[OK] Toutes les methodes abstraites implementees
[OK] ELO-like : +16 par victoire, -16 par defaite
[OK] get_tournament_stats() retourne name/rating/record/interfaces
[OK] TournamentPlatform completement implemente
[OK] Valeurs numeriques verifiees : winner_rating: 1216, loser_rating: 1134,
     avg_rating: 1175  -> IDENTIQUES au sujet

[/!\] ERREUR : Format des IDs de carte (non corrige).

      SORTIE ACTUELLE :
        Fire Dragon (ID: fire_dragon_001)
        Ice Wizard  (ID: ice_wizard_001)

      SORTIE ATTENDUE (sujet) :
        Fire Dragon (ID: dragon_001)
        Ice Wizard  (ID: wizard_001)

      CAUSE RACINE dans TournamentPlatform.py (register_card) :
        base = card.name.lower().replace(' ', '_')
        card_id = f"{base}_{count:03d}"
        # "Fire Dragon" -> "fire_dragon_001"  <- code actuel
        # Le sujet attend "dragon_001" = juste le DERNIER MOT du nom

      Solution (1 ligne) :
        base = card.name.lower().split()[-1]
        # "Fire Dragon" -> "dragon_001"  CORRECT
        # "Ice Wizard"  -> "wizard_001"  CORRECT

===============================================
EXIGENCES GENERALES
===============================================
[OK] Python 3.10+
[OK] Type hints presents sur toutes les fonctions et methodes
[OK] ABC et @abstractmethod utilises correctement
[OK] Imports absolus utilises dans tous les exercices
[OK] __init__.py present dans chaque exercice
[OK] Execution via python3 -m exN.main fonctionnelle pour tous les ex
[OK] get_supported_types() implementee dans FantasyCardFactory (ex3)
[OK] flake8 : code globalement propre, quelques longues lignes mineures

===============================================
CORRECTIONS RESTANTES AVANT SOUTENANCE
===============================================

1. [EX4] TournamentPlatform.register_card() : utiliser le dernier mot
   du nom pour l'ID (1 ligne de code)
     base = card.name.lower().split()[-1]
   Impact : "dragon_001" au lieu de "fire_dragon_001"

===============================================
RECAPITULATIF
===============================================
EX0 : 20/20 - Parfait. game_state.get('mana', 0) deja applique, import OK
EX1 : 19/20 - Tres bon. get_deck_stats() avant shuffle → avg_cost stable (3.3)
EX2 : 20/20 - Parfait. mana_pool=8 → total_mana=7 ✓, ordre methodes ✓
EX3 : 16/20 - Bon. Logique correcte, deck aleatoire → damage non-deterministe
EX4 : 17/20 - Tres bon. 1 seule correction restante : format ID (last word)

Points forts :
- Heritage abstrait et patterns design maitrises sur tous les exercices
- Tous les exercices s'executent sans erreur
- Type hints complets, code propre et lisible
- ex0, ex2 et ex4 produisent des sorties numeriquement identiques au sujet
- Corrections ex0/ex1/ex2 toutes appliquees

