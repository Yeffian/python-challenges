import time

class CarRecord:
    def __init__(self, vehicle_id, registration, date_of_registration, engine_size, purchase_price) -> None:
        self.VehicleId = vehicle_id
        self.Registration = registration
        self.DateOfRegistration = date_of_registration
        self.EngineSize = engine_size
        self.PurchasePrice = purchase_price

cars = [
    CarRecord('Nissan Fairlady Z', 'VDX18020', time.now(), 100, 5000),
    CarRecord('Mazda Miata', 'GMX7872', time.now(), 140, 70000),
    # insert more cars here
]