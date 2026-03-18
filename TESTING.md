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
- **app/tests/test_decks.py**: 4 tests for Deck endpoints (create, get, delete, response structure)
- **app/tests/test_games.py**: 4 tests for Game endpoints (create, get, update, response structure)

**Total: 17 tests**

## Known Issues Resolved

The previous routing conflicts in decks and games routers have been resolved:
- **Decks**: Removed `list_person_decks()` endpoint. Now only `create_deck()`, `get_deck()`, and `delete_deck()` exist.
- **Games**: Removed `list_playgroup_games()` endpoint. Now only `create_game()`, `get_game()`, and `update_game()` exist.
- **Auto-generated IDs**: Both `create_game()` and `create_deck()` now generate UUIDs server-side instead of accepting them as parameters.
