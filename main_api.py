"""
L'API utulise le design pattern DTO (Data Transfer Object) pour :

- La Sépartion des responsabilités :
    - EquipmentBase : Définit la structure de base des données
    - EquipmentCreate : Gère les données d'entrée pour la création
    - EquipmentResponse : Gère les données de sortie pour les réponses API

- Validation des données :
    - Les données sont validées à l'entrée et à la sortie de l'API

- Sécurité :
    - Contrôle précis des données exposées
    - Protection contre l'injection de données non désirées
    
- Flexibilité :
    - Facile d'ajouter de nouveaux DTOs pour des cas d'utilisation spécifiques
    - Possibilité de modifier la structure des données sans affecter la base de données
    
- Maintenabilité :
    - Code plus organisé et plus facile à maintenir
    - Séparation claire entre la logique métier et la persistance des données

DTO (Data Transfer Object) :
- EquipmentBase : Modèle de base avec tous les champs
- EquipmentCreate : Modèle pour la création d'un équipement
- EquipmentResponse : Modèle pour la réponse API, inclut l'ID

EquipmentBase (Base DTO)
    ├── EquipmentCreate (Input DTO)
    └── EquipmentResponse (Output DTO)

"""

# Importation des modules nécessaires
from fastapi import Depends, FastAPI, HTTPException  # FastAPI pour créer l'API, HTTPException pour gérer les erreurs
from requests import Session
from sqlalchemy import create_engine, Column, Integer, String, Enum  # SQLAlchemy pour la gestion de la base de données
from sqlalchemy.ext.declarative import declarative_base  # Pour créer les modèles de base de données
from sqlalchemy.orm import sessionmaker  # Pour créer des sessions de base de données
from pydantic import BaseModel  # Pour la validation des données
from typing import Optional  # Pour définir des types optionnels

# Configuration de la connexion à la base de données
# Format: postgresql://utilisateur:motdepasse@hote:port/nom_base
DATABASE_URL = "postgresql://admin:123456@localhost:5432/cmdb"

# Création du moteur de base de données
engine = create_engine(DATABASE_URL)

# Création d'une factory de sessions
# autocommit=False : les changements ne sont pas automatiquement sauvegardés
# autoflush=False : les requêtes ne sont pas automatiquement synchronisées
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Création de la classe de base pour les modèles
Base = declarative_base()

# Définition du modèle SQLAlchemy qui correspond à la table dans la base de données
class Equipment(Base):
    __tablename__ = "equipments_equipments"  # Nom de la table dans PostgreSQL

    # Définition des colonnes
    id = Column(Integer, primary_key=True, index=True)  # Clé primaire auto-incrémentée
    device_name = Column(String, nullable=True)  # Nom de l'appareil, peut être null
    device_type = Column(String)  # Type d'appareil
    host = Column(String)  # Adresse hôte
    username = Column(String)  # Nom d'utilisateur
    password = Column(String)  # Mot de passe
    port = Column(Integer, default=50)  # Port, valeur par défaut 50
    secret = Column(String, nullable=True)  # Secret, peut être null
    status = Column(String, default="Disconnected")  # Statut, valeur par défaut "Disconnected"

# Modèles Pydantic pour la validation des données
# Ces modèles définissent la structure des données pour l'API

# Modèle de base avec tous les champs
class EquipmentBase(BaseModel):
    device_name: Optional[str] = None  # Champ optionnel
    device_type: str
    host: str
    username: str
    password: str
    port: Optional[int] = 50  # Champ optionnel avec valeur par défaut
    secret: Optional[str] = None  # Champ optionnel
    status: str = "Disconnected"  # Champ avec valeur par défaut

# Modèle pour la création d'un équipement
class EquipmentCreate(EquipmentBase):
    pass

# Modèle pour la réponse API, inclut l'ID
class EquipmentResponse(EquipmentBase):
    id: int

    class Config:
        orm_mode = True  # Permet la conversion automatique entre ORM et Pydantic

# Création de l'application FastAPI
app = FastAPI()

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db  # Fournit la session
    finally:
        db.close()  # Ferme la session après utilisation

# Routes CRUD (Create, Read, Update, Delete)

# Route pour créer un nouvel équipement
@app.post("/equipments/", response_model=EquipmentResp)
def create_equipment(equipment: EquipmentCreate, db: Session = Depends(get_db)):
    # Crée une nouvelle instance d'Equipment avec les données reçues
    db_equipment = Equipment(**equipment.dict())
    db.add(db_equipment)  # Ajoute à la session
    db.commit()  # Sauvegarde dans la base de données
    db.refresh(db_equipment)  # Rafraîchit l'objet avec les données de la base
    return db_equipment

# Route pour lister tous les équipements
@app.get("/equipments/", response_model=list[EquipmentResp])
def read_equipments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # Récupère les équipements avec pagination
    equipments = db.query(Equipment).offset(skip).limit(limit).all()
    return equipments

# Route pour obtenir un équipement spécifique
@app.get("/equipments/{equipment_id}", response_model=EquipmentResp)
def read_equipment(equipment_id: int, db: Session = Depends(get_db)):
    # Recherche l'équipement par ID
    equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return equipment

# Route pour mettre à jour un équipement
@app.put("/equipments/{equipment_id}", response_model=EquipmentResp)
def update_equipment(equipment_id: int, equipment: EquipmentCreate, db: Session = Depends(get_db)):
    # Recherche l'équipement à mettre à jour
    db_equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    # Met à jour tous les champs
    for key, value in equipment.dict().items():
        setattr(db_equipment, key, value)
    
    db.commit()  # Sauvegarde les changements
    db.refresh(db_equipment)  # Rafraîchit l'objet
    return db_equipment

# Route pour supprimer un équipement
@app.delete("/equipments/{equipment_id}")
def delete_equipment(equipment_id: int, db: Session = Depends(get_db)):
    # Recherche l'équipement à supprimer
    db_equipment = db.query(Equipment).filter(Equipment.id == equipment_id).first()
    if db_equipment is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    
    db.delete(db_equipment)  # Supprime l'équipement
    db.commit()  # Sauvegarde les changements
    return {"message": "Equipment deleted successfully"}