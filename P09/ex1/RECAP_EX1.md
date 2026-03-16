# Recap — Exercise 1: Alien Contact Logs

## ✅ What Is Correct

| Element | Status | Details |
|---|---|---|
| `BaseModel` inheritance | ✅ | Correctly inherits from `BaseModel` |
| `ContactType` enum | ✅ | Defined with `str, Enum` — all 4 values present |
| `contact_type: ContactType` | ✅ | Correctly typed with the enum |
| `Field` constraints | ✅ | `min_length`, `max_length`, `ge`, `le` used correctly |
| `contact_id` length | ✅ | `min_length=5, max_length=15` — matches the subject |
| `timestamp: datetime` | ✅ | Correct type |
| `location` constraints | ✅ | `min_length=3, max_length=100` — matches the subject |
| `signal_strength` constraints | ✅ | `ge=0.0, le=10.0` — matches the subject |
| `duration_minutes` constraints | ✅ | `ge=1, le=1440` — matches the subject |
| `witness_count` constraints | ✅ | `ge=1, le=100` — matches the subject |
| `message_received` field name | ✅ | Typo fixed |
| `message_received` optional | ✅ | `Optional[str]` with `max_length=500` — matches the subject |
| `is_verified` default | ✅ | Defaults to `False` — matches the subject |
| `@model_validator(mode='after')` | ✅ | Correct decorator usage (Pydantic v2 syntax) |
| `contact_id` starts with `"AC"` | ✅ | Uppercase check — matches the subject |
| Error message case | ✅ | Fixed — now says `'AC'` |
| `custom_signal_validator` | ✅ | Logic is correct |
| Enum comparison (`==`) | ✅ | Fixed — now uses `==` instead of attribute access |

---

## ✅ Final Verdict

**All issues have been fixed.** The model is fully compliant with the subject requirements (excluding `main()`).
