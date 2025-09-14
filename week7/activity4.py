from __future__ import annotations
from abc import ABC, abstractmethod
import threading
from dataclasses import dataclass

# ---------- Domain ----------
@dataclass(frozen=True)
class Cargo:
    id: str
    kind: str          # container, timber, fuel...
    weight_t: float    # tons

@dataclass(frozen=True)
class Route:
    name: str          # "ROAD" | "SEA"
    origin: str
    destination: str

# ---------- Product families (Factory will create these) ----------
class Vehicle(ABC):
    @abstractmethod
    def move(self, cargo: Cargo, route: Route) -> str: ...

class Crane(ABC):
    @abstractmethod
    def load(self, cargo: Cargo) -> str: ...
    @abstractmethod
    def unload(self, cargo: Cargo) -> str: ...

class Truck(Vehicle):
    def move(self, cargo: Cargo, route: Route) -> str:
        return f"Truck→ {route.origin} -> {route.destination} with {cargo.id} ({cargo.weight_t}t)"

class Barge(Vehicle):
    def move(self, cargo: Cargo, route: Route) -> str:
        return f"Barge≈ {route.origin} => {route.destination} with {cargo.id} ({cargo.weight_t}t)"

class RoadCrane(Crane):
    def load(self, cargo: Cargo) -> str:  return f"RoadCrane loads {cargo.id}"
    def unload(self, cargo: Cargo) -> str:return f"RoadCrane unloads {cargo.id}"

class SeaCrane(Crane):
    def load(self, cargo: Cargo) -> str:  return f"SeaCrane loads {cargo.id}"
    def unload(self, cargo: Cargo) -> str:return f"SeaCrane unloads {cargo.id}"

# ---------- Factory ----------
class AssetFactory:
    _registry = {
        "truck": Truck,
        "barge": Barge,
        "road_crane": RoadCrane,
        "sea_crane": SeaCrane,
    }
    @classmethod
    def create(cls, name: str):
        key = name.strip().lower()
        if key not in cls._registry:
            raise ValueError(f"Unsupported asset: {name}")
        return cls._registry[key]()

# ---------- Singleton (global gateway / dispatcher) ----------
class PortGateway:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def dispatch(self, cargo: Cargo, route: Route) -> list[str]:
        logs = []
        if route.name.upper() == "ROAD":
            crane = AssetFactory.create("road_crane")
            vehicle = AssetFactory.create("truck")
        elif route.name.upper() == "SEA":
            crane = AssetFactory.create("sea_crane")
            vehicle = AssetFactory.create("barge")
        else:
            raise ValueError("route must be ROAD or SEA")

        logs.append(crane.load(cargo))
        logs.append(vehicle.move(cargo, route))
        logs.append(crane.unload(cargo))
        return logs

# ---------- Demo ----------
if __name__ == "__main__":
    gw1, gw2 = PortGateway(), PortGateway()
    print("Singleton?", gw1 is gw2)  # True

    timber = Cargo("C-001", "timber", 22.5)
    fuel   = Cargo("C-002", "fuel",   15.0)

    road_route = Route("ROAD", "North Yard", "City Depot")
    sea_route  = Route("SEA",  "East Wharf", "South Bay")

    for line in gw1.dispatch(timber, road_route): print(line)
    for line in gw1.dispatch(fuel,   sea_route):  print(line)
