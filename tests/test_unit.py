import pytest

from pydantic import ValidationError
from src.models import Apartment, Tenant 


def test_apartment_fields():
    data = Apartment(
        key="apart-test",
        name="Test Apartment",
        location="Test Location",
        area_m2=50.0,
        rooms={
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    )
    assert data.key == "apart-test"
    assert data.name == "Test Apartment"
    assert data.location == "Test Location"
    assert data.area_m2 == 50.0
    assert len(data.rooms) == 2


def test_apartment_from_dict():
    data = {
        "key": "apart-test",
        "name": "Test Apartment",
        "location": "Test Location",
        "area_m2": 50.0,
        "rooms": {
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    }
    apartment = Apartment(**data)
    assert apartment.key == data["key"]
    assert apartment.name == data["name"]
    assert apartment.location == data["location"]
    assert apartment.area_m2 == data["area_m2"]
    assert len(apartment.rooms) == len(data["rooms"])

    data['area_m2'] = "25m2" # Invalid field
    with pytest.raises(ValidationError):
        wrong_apartment = Apartment(**data)



def test_tenant_creation_direct():
   
    tenant = Tenant(
        name="Jan Kowalski",
        apartment="apart-polanka",
        room="room-1",
        rent_pln=1500,
        deposit_pln=2000,
        date_agreement_from="2026-01-01",
        date_agreement_to="2026-12-31"
    )
    
    
    assert tenant.name == "Jan Kowalski"
    assert tenant.apartment == "apart-polanka"
    assert tenant.room == "room-1"
    assert tenant.rent_pln == 1500
    assert tenant.deposit_pln == 2000
    assert tenant.date_agreement_from is not None 