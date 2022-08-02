from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.get("/videogames", response_model=List[schemas.VideoGameOut])
def get_videogames(db: Session = Depends(get_db)):
    games = db.query(models.VideoGame).all()
    return games

@router.post("/videogames", status_code=status.HTTP_201_CREATED, response_model=schemas.VideoGame)
def create_videogame(game: schemas.VideoGame, db: Session = Depends(get_db)):
    new_game = models.VideoGame(**game.dict())
    db.add(new_game)
    db.commit()
    db.refresh(new_game)
    return new_game

@router.get("/videogames/{id}", response_model=schemas.VideoGameOut)
def get_videogame(id: int, db: Session = Depends(get_db)):
    game = db.query(models.VideoGame).filter(models.VideoGame.id == id).first()
    if not game:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video game with id: {id} was not found")
    return game

@router.delete("/videogames/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_videogame(id: int, db: Session = Depends(get_db)):
    game = db.query(models.VideoGame).filter(models.VideoGame.id == id)

    if game.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video game with id: {id} was not found")

    game.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/videogames/{id}", response_model=schemas.VideoGameOut)
def update_videogame(id: int, updated_game: schemas.VideoGame, db: Session = Depends(get_db)):
    game_query = db.query(models.VideoGame).filter(models.VideoGame.id == id)
    game = game_query.first()

    if game == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Video game with id: {id} was not found")

    game_query.update(updated_game.dict(), synchronize_session=False)
    db.commit()

    return game_query.first()