from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Equipment
from schemas import EquipmentCreate, EquipmentUpdate, EquipmentResponse


# Création de l'application FastAPI
router = APIRouter()


# Routes CRUD (Create, Read, Update, Delete)

# Route pour créer un nouvel équipement
@router.post("/equipments/", response_model=EquipmentResponse)
def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    # Crée une nouvelle instance d'Equipment avec les données reçues
    db_equipment = Equipment(**equipment.model_dump())
    db.add(db_equipment)  # Ajoute à la session
    db.commit()  # Sauvegarde dans la base de données
    db.refresh(db_equipment)  # Rafraîchit l'objet avec les données de la base
    return db_equipment

# Route pour lister tous les équipements
@router.get("/equipments/", response_model=list[EquipmentResponse])
def read_equipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Récupère les équipements avec pagination
    equipments = db.query(Equipment).offset(skip).limit(limit).all()
    return equipments

# Route pour obtenir un équipement spécifique
@router.get("/equipments/{equipment_id}", response_model=EquipmentResponse)
def read_equipment(equipment_id: int, db: Session = Depends(get_db)):
    # Recherche l'équipement par ID
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

# Route pour mettre à jour un équipement
@router.put("/equipments/{equipment_id}", response_model=EquipmentResponse)
def update_equipment(equipment_id: int, equipment: EquipmentUpdate, db: Session = Depends(get_db)):
    # Recherche l'équipement à mettre à jour
    db_equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    # Met à jour tous les champs
    for key, value in equipment.model_dump().items():
        setattr(db_equipment, key, value)
    
    db.commit()  # Sauvegarde les changements
    db.refresh(db_equipment)  # Rafraîchit l'objet
    return db_equipment

# Route pour supprimer un équipement
@router.delete("/equipments/{equipment_id}")
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    # Recherche l'équipement à supprimer
    db_equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    db.delete(db_equipment)  # Supprime l'équipement
    db.commit()  # Sauvegarde les changements
    return {"message": "Equipment deleted successfully"}