from fastapi import APIRouter,HTTPException,Depends
from myproject.database.models import Room
from myproject.database.schema import RoomInputSchema,RoomOutSchema
from myproject.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


room_router = APIRouter(prefix='/room',tags=['Room'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


@room_router.post('/', response_model=RoomOutSchema)
async def service_create(
    room: RoomOutSchema,
    db: Session = Depends(get_db)):
    room_db = Room(**room.dict())
    db.add(room_db)
    db.commit()
    db.refresh(room_db)
    return room_db



@room_router.get('/',response_model=List[RoomOutSchema])
async def room_list(db: Session = Depends(get_db)):
    return db.query(Room).all()




@room_router.get('/{room_id}',response_model=RoomOutSchema)
async def room_detail(room_id:int,db: Session = Depends(get_db)):
    room_db = db.query(Room).filter(Room.id == room_id).first()

    if not room_db:
        raise HTTPException(detail='Мындай сервис жок',status_code=404)
    return room_db


@room_router.put('/{room_id}', response_model=dict)
async def update_room(room_id: int,room: RoomInputSchema, db: Session = Depends(get_db)):
    room_db = db.query(Room).filter(Room.id == room_id).first()
    if not room_db:
        raise HTTPException(
            status_code=404,
            detail='Мындай сервис жок')

    for room_key, room_value in room.dict().items():
        setattr(room_db,room_image_key,room_value)

    db.commit()
    db.refresh(service_db)

    return {'message': 'Сервис озгорулду'}

@room_router.delete('/{room_id}/', response_model=dict)
async def delete_room(room_id: int,db: Session = Depends(get_db)):
    room_db = db.query(RoomImage).filter(Room.id == room_id).first()
    if not room_db:
        raise HTTPException( status_code=404,detail='Мындай сурот комната жок')

    db.delete(room_db)
    db.commit()
    return {'message': 'Комната картина  удалена'}