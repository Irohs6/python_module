import sys
import os
from pydantic import ValidationError

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ex0"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ex1"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ex2"))

from space_station import SpaceStation  # noqa: E402
from alien_contact import AlienContact, ContactType  # noqa: E402
from space_crew import SpaceMission, CrewMember, Rank  # noqa: E402

passed = 0
failed = 0


def test(label, should_pass, model_cls, data):
    global passed, failed
    try:
        model_cls(**data)
        if should_pass:
            print(f"  ✅ PASS | {label}")
            passed += 1
        else:
            print(f"  ❌ FAIL | {label} → devait échouer mais a passé")
            failed += 1
    except ValidationError as e:
        if not should_pass:
            msgs = [err["msg"] for err in e.errors()]
            print(f"  ✅ PASS | {label} → {msgs[0]}")
            passed += 1
        else:
            msgs = [err["msg"] for err in e.errors()]
            print(f"  ❌ FAIL | {label} → erreur inattendue: {msgs[0]}")
            failed += 1
    except Exception as e:
        print(f"  ❌ FAIL | {label} → exception inattendue: {e}")
        failed += 1


# ─────────────────────────────────────────────
# EX0 — SpaceStation
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("EX0 — SpaceStation")
print("=" * 60)

BASE_STATION = {
    "station_id": "ISS001",
    "name": "International Space Station",
    "crew_size": 6,
    "power_level": 85.5,
    "oxygen_level": 92.3,
    "last_maintenance": "2024-01-15T10:30:00",
    "is_operational": True,
    "notes": None,
}

# --- Valides ---
print("\n[Valides]")
test("Station valide de base", True, SpaceStation, BASE_STATION)
test(
    "is_operational=False valide",
    True,
    SpaceStation,
    {**BASE_STATION, "is_operational": False},
)
test(
    "notes max 200 chars",
    True,
    SpaceStation,
    {**BASE_STATION, "notes": "x" * 200},
)
test("crew_size min=1", True, SpaceStation, {**BASE_STATION, "crew_size": 1})
test("crew_size max=20", True, SpaceStation, {**BASE_STATION, "crew_size": 20})
test(
    "power_level=0.0", True, SpaceStation, {**BASE_STATION, "power_level": 0.0}
)
test(
    "power_level=100.0",
    True,
    SpaceStation,
    {**BASE_STATION, "power_level": 100.0},
)
test(
    "oxygen_level=0.0",
    True,
    SpaceStation,
    {**BASE_STATION, "oxygen_level": 0.0},
)
test(
    "oxygen_level=100.0",
    True,
    SpaceStation,
    {**BASE_STATION, "oxygen_level": 100.0},
)
test(
    "station_id min=3 chars",
    True,
    SpaceStation,
    {**BASE_STATION, "station_id": "ABC"},
)
test(
    "station_id max=10 chars",
    True,
    SpaceStation,
    {**BASE_STATION, "station_id": "ABCDEFGHIJ"},
)
test(
    "datetime en string auto-converti",
    True,
    SpaceStation,
    {**BASE_STATION, "last_maintenance": "2023-07-11T00:00:00"},
)

# --- Invalides ---
print("\n[Invalides — field validators]")
test(
    "station_id trop court (<3)",
    False,
    SpaceStation,
    {**BASE_STATION, "station_id": "AB"},
)
test(
    "station_id trop long (>10)",
    False,
    SpaceStation,
    {**BASE_STATION, "station_id": "ABCDEFGHIJK"},
)
test("crew_size=0 (<1)", False, SpaceStation, {**BASE_STATION, "crew_size": 0})
test(
    "crew_size=21 (>20)",
    False,
    SpaceStation,
    {**BASE_STATION, "crew_size": 21},
)
test(
    "power_level=-1 (<0)",
    False,
    SpaceStation,
    {**BASE_STATION, "power_level": -1.0},
)
test(
    "power_level=101 (>100)",
    False,
    SpaceStation,
    {**BASE_STATION, "power_level": 101.0},
)
test(
    "oxygen_level=-1 (<0)",
    False,
    SpaceStation,
    {**BASE_STATION, "oxygen_level": -1.0},
)
test(
    "oxygen_level=101 (>100)",
    False,
    SpaceStation,
    {**BASE_STATION, "oxygen_level": 101.0},
)
test("name vide", False, SpaceStation, {**BASE_STATION, "name": ""})
test(
    "name trop long (>50)",
    False,
    SpaceStation,
    {**BASE_STATION, "name": "x" * 51},
)
test(
    "notes trop long (>200)",
    False,
    SpaceStation,
    {**BASE_STATION, "notes": "x" * 201},
)
test(
    "last_maintenance invalide",
    False,
    SpaceStation,
    {**BASE_STATION, "last_maintenance": "pas-une-date"},
)

# ─────────────────────────────────────────────
# EX1 — AlienContact
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("EX1 — AlienContact")
print("=" * 60)

BASE_CONTACT = {
    "contact_id": "AC_001",
    "timestamp": "2024-01-20T00:00:00",
    "location": "Area 51, Nevada",
    "contact_type": "radio",
    "signal_strength": 5.0,
    "duration_minutes": 45,
    "witness_count": 5,
    "message_received": None,
    "is_verified": False,
}

# --- Valides ---
print("\n[Valides]")
test("Contact valide de base", True, AlienContact, BASE_CONTACT)
test(
    "Type visual",
    True,
    AlienContact,
    {**BASE_CONTACT, "contact_type": "visual"},
)
test(
    "Physical vérifié",
    True,
    AlienContact,
    {**BASE_CONTACT, "contact_type": "physical", "is_verified": True},
)
test(
    "Telepathic avec 3 témoins",
    True,
    AlienContact,
    {**BASE_CONTACT, "contact_type": "telepathic", "witness_count": 3},
)
test(
    "Signal >7 avec message",
    True,
    AlienContact,
    {
        **BASE_CONTACT,
        "signal_strength": 8.0,
        "message_received": "Hello from space",
    },
)
test(
    "contact_id exactement 5 chars",
    True,
    AlienContact,
    {**BASE_CONTACT, "contact_id": "AC001"},
)
test(
    "contact_id exactement 15 chars",
    True,
    AlienContact,
    {**BASE_CONTACT, "contact_id": "AC_2024_001_XXX"},
)
test(
    "duration_minutes=1 (min)",
    True,
    AlienContact,
    {**BASE_CONTACT, "duration_minutes": 1},
)
test(
    "duration_minutes=1440 (max)",
    True,
    AlienContact,
    {**BASE_CONTACT, "duration_minutes": 1440},
)
test(
    "witness_count=1 (min)",
    True,
    AlienContact,
    {**BASE_CONTACT, "witness_count": 1},
)
test(
    "witness_count=100 (max)",
    True,
    AlienContact,
    {**BASE_CONTACT, "witness_count": 100},
)

# --- Invalides field validators ---
print("\n[Invalides — field validators]")
test(
    "contact_id trop court (<5)",
    False,
    AlienContact,
    {**BASE_CONTACT, "contact_id": "AC01"},
)
test(
    "contact_id trop long (>15)",
    False,
    AlienContact,
    {**BASE_CONTACT, "contact_id": "AC_2024_001_XXXX"},
)
test(
    "location trop courte (<3)",
    False,
    AlienContact,
    {**BASE_CONTACT, "location": "AB"},
)
test(
    "signal_strength < 0",
    False,
    AlienContact,
    {**BASE_CONTACT, "signal_strength": -0.1},
)
test(
    "signal_strength > 10",
    False,
    AlienContact,
    {**BASE_CONTACT, "signal_strength": 10.1},
)
test(
    "duration_minutes=0 (<1)",
    False,
    AlienContact,
    {**BASE_CONTACT, "duration_minutes": 0},
)
test(
    "duration_minutes=1441 (>1440)",
    False,
    AlienContact,
    {**BASE_CONTACT, "duration_minutes": 1441},
)
test(
    "witness_count=0 (<1)",
    False,
    AlienContact,
    {**BASE_CONTACT, "witness_count": 0},
)
test(
    "witness_count=101 (>100)",
    False,
    AlienContact,
    {**BASE_CONTACT, "witness_count": 101},
)
test(
    "contact_type invalide",
    False,
    AlienContact,
    {**BASE_CONTACT, "contact_type": "unknown"},
)
test(
    "message_received trop long (>500)",
    False,
    AlienContact,
    {**BASE_CONTACT, "message_received": "x" * 501},
)

# --- Invalides model_validator ---
print("\n[Invalides — model_validator]")
test(
    "contact_id ne commence pas par AC",
    False,
    AlienContact,
    {**BASE_CONTACT, "contact_id": "XX001"},
)
test(
    "Physical non vérifié",
    False,
    AlienContact,
    {**BASE_CONTACT, "contact_type": "physical", "is_verified": False},
)
test(
    "Telepathic avec 2 témoins",
    False,
    AlienContact,
    {**BASE_CONTACT, "contact_type": "telepathic", "witness_count": 2},
)
test(
    "Signal=8.0 sans message",
    False,
    AlienContact,
    {**BASE_CONTACT, "signal_strength": 8.0, "message_received": None},
)

# ─────────────────────────────────────────────
# EX2 — SpaceMission
# ─────────────────────────────────────────────
print("\n" + "=" * 60)
print("EX2 — SpaceMission")
print("=" * 60)

CREW_CAPTAIN = {
    "member_id": "CM001",
    "name": "Sarah Connor",
    "rank": "captain",
    "age": 40,
    "specialization": "Mission Command",
    "years_experience": 10,
    "is_active": True,
}
CREW_CADET = {
    "member_id": "CM002",
    "name": "John Smith",
    "rank": "cadet",
    "age": 25,
    "specialization": "Navigation",
    "years_experience": 1,
    "is_active": True,
}
CREW_VETERAN = {
    "member_id": "CM003",
    "name": "Alice Jones",
    "rank": "officer",
    "age": 35,
    "specialization": "Engineering",
    "years_experience": 6,
    "is_active": True,
}

BASE_MISSION = {
    "mission_id": "M2024_MARS",
    "mission_name": "Mars Colony Mission",
    "destination": "Mars",
    "launch_date": "2024-06-01T00:00:00",
    "duration_days": 90,
    "crew": [CREW_CAPTAIN, CREW_CADET],
    "mission_status": "planned",
    "budget_millions": 2500.0,
}

# --- Valides ---
print("\n[Valides]")
test("Mission valide de base", True, SpaceMission, BASE_MISSION)
test(
    "Avec commander au lieu de captain",
    True,
    SpaceMission,
    {
        **BASE_MISSION,
        "crew": [{**CREW_CAPTAIN, "rank": "commander"}, CREW_CADET],
    },
)
test(
    "Mission longue avec 50% vétérans",
    True,
    SpaceMission,
    {
        **BASE_MISSION,
        "duration_days": 400,
        "crew": [CREW_CAPTAIN, CREW_VETERAN],
    },
)
test(
    "budget_millions=1.0 (min)",
    True,
    SpaceMission,
    {**BASE_MISSION, "budget_millions": 1.0},
)
test(
    "budget_millions=10000.0 (max)",
    True,
    SpaceMission,
    {**BASE_MISSION, "budget_millions": 10000.0},
)
test(
    "duration_days=1 (min)",
    True,
    SpaceMission,
    {**BASE_MISSION, "duration_days": 1},
)
test(
    "duration_days=3650 (max)",
    True,
    SpaceMission,
    {
        **BASE_MISSION,
        "duration_days": 3650,
        "crew": [CREW_CAPTAIN, CREW_VETERAN, CREW_VETERAN],
    },
)

# --- Invalides field validators ---
print("\n[Invalides — field validators]")
test(
    "mission_id trop court (<5)",
    False,
    SpaceMission,
    {**BASE_MISSION, "mission_id": "M123"},
)
test(
    "mission_id trop long (>15)",
    False,
    SpaceMission,
    {**BASE_MISSION, "mission_id": "M" + "X" * 15},
)
test(
    "budget_millions < 1",
    False,
    SpaceMission,
    {**BASE_MISSION, "budget_millions": 0.5},
)
test(
    "budget_millions > 10000",
    False,
    SpaceMission,
    {**BASE_MISSION, "budget_millions": 10001.0},
)
test(
    "duration_days=0 (<1)",
    False,
    SpaceMission,
    {**BASE_MISSION, "duration_days": 0},
)
test(
    "duration_days=3651 (>3650)",
    False,
    SpaceMission,
    {**BASE_MISSION, "duration_days": 3651},
)
test("crew vide", False, SpaceMission, {**BASE_MISSION, "crew": []})
test(
    "membre age < 18",
    False,
    SpaceMission,
    {**BASE_MISSION, "crew": [{**CREW_CAPTAIN, "age": 17}, CREW_CADET]},
)
test(
    "membre name trop court (<2)",
    False,
    SpaceMission,
    {**BASE_MISSION, "crew": [{**CREW_CAPTAIN, "name": "A"}, CREW_CADET]},
)

# --- Invalides model_validator ---
print("\n[Invalides — model_validator]")
test(
    "mission_id ne commence pas par M",
    False,
    SpaceMission,
    {**BASE_MISSION, "mission_id": "X2024_MARS"},
)
test(
    "Aucun captain ni commander",
    False,
    SpaceMission,
    {
        **BASE_MISSION,
        "crew": [CREW_CADET, {**CREW_CADET, "member_id": "CM003"}],
    },
)
test(
    "Mission longue < 50% vétérans",
    False,
    SpaceMission,
    {
        **BASE_MISSION,
        "duration_days": 400,
        "crew": [
            CREW_CAPTAIN,
            CREW_CADET,
            {**CREW_CADET, "member_id": "CM003"},
        ],
    },
)
test(
    "Tous membres inactifs",
    False,
    SpaceMission,
    {
        **BASE_MISSION,
        "crew": [
            {**CREW_CAPTAIN, "is_active": False},
            {**CREW_CADET, "is_active": False},
        ],
    },
)

# ─────────────────────────────────────────────
# Résumé
# ─────────────────────────────────────────────
total = passed + failed
print("\n" + "=" * 60)
print(f"RÉSULTAT FINAL : {passed}/{total} tests passés")
score = round((passed / total) * 10, 1) if total > 0 else 0
print(f"NOTE GLOBALE   : {score}/10")
print("=" * 60)
