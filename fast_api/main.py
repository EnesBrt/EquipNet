# Configuration de Django
import os
import uvicorn

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CMDB.settings")
import django

django.setup()

from cmdb_app.models import NetworkEquipment
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


@app.get("/equipments/")
def root():
    equipments = NetworkEquipment.objects.all()
    result = []
    for equipment in equipments:
        result.append(
            {
                "device_name": equipment.device_name,
                "device_type": equipment.device_type,
                "host": equipment.host,
            }
        )
    return result


class Update(BaseModel):
    new_location: str


@app.put("/equipment/{equipment_id}/location")
def update(equipment_id: int, new_data: Update):
    equipment = NetworkEquipment.objects.get(equipment_id=id)
    equipment.location = new_data.new_location
    equipment.save()
    return {
        "message": f"updated successfully for equipment {equipment_id}",
        "new_location": new_data.new_location,
    }


class Create(BaseModel):
    device_name: str
    device_type: str
    ip_address: str
    host: str
    username: str
    password: str
    location: str
    port: int


@app.post("/equipment/")
def create(equipment_data: Create):
    new_equipment = NetworkEquipment(
        device_name=equipment_data.device_name,
        device_type=equipment_data.device_type,
        ip_address=equipment_data.ip_address,
        host=equipment_data.host,
        username=equipment_data.username,
        password=equipment_data.password,
        location=equipment_data.location,
        port=equipment_data.port,
    )
    new_equipment.save()
    return {"message": "Equipment created successfully", "id": new_equipment.id}


@app.delete("/equipment/{equipment_id}/")
def delete(equipment_id: int):
    equipment = NetworkEquipment.objects.get(id=equipment_id)
    equipment.delete()
    return {"message": f"Equipment with id {equipment_id} has been deleted"}
