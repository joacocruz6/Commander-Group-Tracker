# Copilot Instructions - Commander Group Tracker

## Project Overview
Commander Group Tracker is a FastAPI-based backend service for tracking Magic: The Gathering Commander play groups. It enables users to manage play groups, players (persons), their decks, and game results.

## Architecture

### Monolithic Backend Structure
- Single FastAPI application (`app/main.py`)
- Modular routing system under `app/routers/`
- Four core domains: playgroups, persons, decks, games
- Each domain is isolated in its own router file with a consistent `APIRouter(prefix=..., tags=[...])`  pattern

### Key Data Model
```
PlayGroup (group of players)
├── Persons (players in the group)
│   └── Decks (each player has multiple decks)
└── Games (match results within the group)
```

## Integration Patterns

### Router Registration
All routers must be manually imported and included in `app/main.py` using `app.include_router()`. Currently this is **not implemented** - only the base `FastAPI()` app exists.

**Fix example**: Add to `main.py` after `app = FastAPI()`:
```python
from app.routers import playgroup, persons, decks, games
app.include_router(playgroup.router)
app.include_router(persons.router)
app.include_router(decks.router)
app.include_router(games.router)
```

### Response Wrapper Format
All endpoints follow a consistent response structure with a `"data"` wrapper:
```python
response = {"data": {...}}  # Single resource
response = {"data": {"items": [...]}}  # Collections
```
Keep this consistent across all new endpoints.

## Critical Issues & Patterns
1. **Endpoint Path Conflicts**: 
   - `decks.py` has overlapping GET endpoints: both `list_person_decks()` and `get_deck()` use `GET /{id}`
   - `games.py` has overlapping GET endpoints: both `get_game()` and `list_playgroup_games()` use `GET /{id}`
   - **Suggested fix**: Refactor to use `/persons/{person_id}/decks` and `/playgroup/{playgroup_id}/games` for list operations
2. **Router Route Ordering**: FastAPI matches routes in definition order. Static routes (like `/admin`, `/participant`) must be defined before dynamic routes (`/{id}`) to work correctly. Playgroup router follows this pattern (fixed).
3. **Empty Dependencies**: `app/dependencies.py` exists but is unused; use this for shared utilities, auth helpers, or database session management as the project grows

## ID Parameter Conventions
Use consistent parameter naming across domains:
- `playgroup_id` - identifies a play group
- `person_id` - identifies a player in a group
- `deck_id` - identifies a deck
- `game_id` - identifies a game/match result

## Development Workflow
- Async handlers required: all endpoint definitions use `async def`
- Tags for OpenAPI docs: tag each router (e.g., `tags=['playgroups']`)
- Request/response validation: planning to add Pydantic models (not yet implemented)
- **Testing**: Run `pytest app/tests/ -v` to execute the test suite (19 tests covering all four routers)
- **Test Structure**: Tests use FastAPI's `TestClient` with fixtures in `app/tests/conftest.py`

## What's Not Yet Implemented
- Database connectivity/ORM (currently mock responses)
- Authentication/authorization
- Pydantic request/response schemas (input validation)
- Error handling beyond basic HTTP exceptions
- Comprehensive error messages and validation errors

Priority roadmap when implementing:
1. Refactor router paths to resolve GET endpoint conflicts (see Critical Issues section)
2. Add Pydantic models for request/response validation
3. Implement database layer (suggested structure: `app/models/` for ORM models, `app/schemas/` for Pydantic, queries in routers or separate data layer)
4. Add authentication middleware
