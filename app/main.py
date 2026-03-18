from fastapi import FastAPI
from app.routers import playgroup, persons, decks, games

app = FastAPI()

# Register routers
app.include_router(playgroup.router)
app.include_router(persons.router)
app.include_router(decks.router)
app.include_router(games.router)