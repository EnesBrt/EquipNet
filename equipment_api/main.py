"""
L'API utilise le design pattern DTO (Data Transfer Object) pour :

EquipmentBase (Base DTO)
    ├── EquipmentCreate (Input DTO)
    ├── EquipmentUpdate (Input DTO)
    └── EquipmentResponse (Output DTO)

- La Sépartion des responsabilités :
    - EquipmentBase : Définit la structure de base des données
    - EquipmentCreate : Gère les données d'entrée pour la création
    - EquipmentUpdate : Gère les données d'entrée pour la mise à jour
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



"""

# Importation des modules nécessaires
from fastapi import Depends, FastAPI, HTTPException, APIRouter  # FastAPI pour créer l'API, HTTPException pour gérer les erreurs
from fastapi.middleware.cors import CORSMiddleware  # Import correct pour CORSMiddleware
from requests import Session
from sqlalchemy import create_engine, Column, Integer, String, Enum  # SQLAlchemy pour la gestion de la base de données
from sqlalchemy.ext.declarative import declarative_base  # Pour créer les modèles de base de données
from sqlalchemy.orm import sessionmaker  # Pour créer des sessions de base de données
from pydantic import BaseModel  # Pour la validation des données
from typing import Optional
import uvicorn  # Pour définir des types optionnels
from database import Base, engine
from router.equipment_router import router

# Création de la base de données
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de gestion des équipements", description="API pour gérer les équipements de l'entreprise")

# Configuration des CORS (Cross-Origin Resource Sharing), fonction: permettre aux requêtes d'être envoyées depuis n'importe quelle origine (domaine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ajout des routes au router
app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de gestion des équipements",
            "documentation": "http://localhost:8000/docs"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)