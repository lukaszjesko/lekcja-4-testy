from src.models import Apartment
from src.manager import Manager
from src.models import Parameters


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key



def test_integration_tenants_loaded():
    params = Parameters()
    manager = Manager(parameters=params)
    
    assert len(manager.tenants) > 0, "Błąd: Manager nie wczytał żadnych najemców!"
    
    expected_names = ["Jan Nowak", "Adam Kowalski", "Ewa Adamska"]
    
    loaded_names = [tenant.name for tenant in manager.tenants.values()]
    
    for expected_name in expected_names:
        assert expected_name in loaded_names, f"Błąd integracji: Brakuje najemcy {expected_name}!"