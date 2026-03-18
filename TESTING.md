# Running Tests

## Setup

Install test dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:
```bash
pytest app/tests/ -v
```

Run tests for a specific module:
```bash
pytest app/tests/test_playgroup.py -v
pytest app/tests/test_persons.py -v
pytest app/tests/test_decks.py -v
pytest app/tests/test_games.py -v
```

Run a specific test:
```bash
pytest app/tests/test_playgroup.py::TestPlaygroupRouter::test_create_playgroup -v
```

## Test Coverage

- **app/tests/test_playgroup.py**: 5 tests for PlayGroup CRUD endpoints
- **app/tests/test_persons.py**: 4 tests for Person CRUD endpoints  
- **app/tests/test_decks.py**: 5 tests for Deck CRUD endpoints
- **app/tests/test_games.py**: 5 tests for Game CRUD endpoints

**Total: 19 tests**

## Known Issues Documented in Tests

1. **Decks Router**: GET endpoints conflict - `/decks/{id}` matches both `list_person_decks()` and `get_deck()`. Suggested fix: Use `/persons/{person_id}/decks` for listing.

2. **Games Router**: GET endpoints conflict - `/games/{id}` matches both `get_game()` and `list_playgroup_games()`. Suggested fix: Use `/playgroup/{playgroup_id}/games` for listing or add query parameter.

Tests are written to document the current behavior while noting where refactoring is needed.
