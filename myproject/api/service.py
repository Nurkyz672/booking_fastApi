from fastapi import APIRouter,HTTPException,Depends
from myproject.database.models import Service
from myproject.database.schema import ServiceInputSchema,ServiceOutSchema
from myproject.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


service_router = APIRouter(prefix='/service',tags=['Service'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


@service_router.post('/', response_model=ServiceOutSchema)
async def service_create(
    service: ServiceInputSchema,
    db: Session = Depends(get_db)):
    service_db = Service(**service.dict())
    db.add(service_db)
    db.commit()
    db.refresh(service_db)
    return service_db



@service_router.get('/',response_model=List[ServiceOutSchema])
async def service_list(db: Session = Depends(get_db)):
    return db.query(Service).all()




@service_router.get('/{service_id}',response_model=ServiceOutSchema)
async def service_detail(service_id:int,db: Session = Depends(get_db)):
    service_db = db.query(UserProfile).filter(Service.id == service_id).first()

    if not service_db:
        raise HTTPException(detail='Мындай сервис жок',status_code=404)
    return service_db


@service_router.put('/{service_id}', response_model=dict)
async def update_service(service_id: int,service: ServiceInputSchema, db: Session = Depends(get_db)):
    service_db = db.query(Service).filter(Service.id == service_id).first()
    if not service_db:
        raise HTTPException(
            status_code=404,
            detail='Мындай сервис жок')

    for service_key, service_value in service.dict().items():
        setattr(service_db,service_key,service_value)

    db.commit()
    db.refresh(service_db)

    return {'message': 'Сервис озгорулду'}

@service_router.delete('/{service_id}/', response_model=dict)
async def delete_service(service_id: int,db: Session = Depends(get_db)):
    service_db = db.query(Service).filter(Service.id == service_id).first()
    if not service_db:
        raise HTTPException( status_code=404,detail='Мындай профайл жок')

    db.delete(service_db)
    db.commit()
    return {'message': 'Сервис  удалена'}