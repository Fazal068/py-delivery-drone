class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight

from __future__ import annotations


class Bike:
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        self.brand = brand
        self.model = model
        self.max_speed = max_speed

    @classmethod
    def from_dict(cls, bike_dict: dict) -> Bike:
        return cls(**bike_dict)


class MountainBike(Bike):
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        super().__init__(brand=brand, model=model, max_speed=max_speed)


class RoadBike(Bike):
    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        super().__init__(brand=brand, model=model, max_speed=max_speed)
