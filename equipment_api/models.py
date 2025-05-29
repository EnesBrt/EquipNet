from sqlalchemy import Column, Integer, String
from database import Base

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
