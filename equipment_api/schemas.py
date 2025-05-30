from pydantic import BaseModel
from typing import Optional


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


class EquipmentUpdate(EquipmentBase):
    device_name: Optional[str] = None
    device_type: Optional[str] = None
    host: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    port: Optional[int] = None
    secret: Optional[str] = None
    status: Optional[str] = None


# Modèle pour la réponse API, inclut l'ID


class EquipmentResponse(EquipmentBase):
    id: int

    class Config:
        # Permet la conversion automatique entre ORM et Pydantic (Pydantic V2)
        from_attributes = True
