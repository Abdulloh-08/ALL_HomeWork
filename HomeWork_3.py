from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_delivery_cost(self, weight, distance):
        pass

class Bike(Transport):
    def calculate_delivery_cost(self, weight, distance):
        return distance * 0.5

class Car(Transport):
    def calculate_delivery_cost(self, weight, distance):
        return (distance * 1.0) + (weight * 0.2)

class Truck(Transport):
    def calculate_delivery_cost(self, weight, distance):
        return (distance * 1.5) + (weight * 0.5)

class DeliveryService:
    def __init__(self):
        self.transports = []

    def add_transport(self, transport):
        self.transports.append(transport)

    def calculate_total_cost(self, weight, distance):
        costs = {}
        for transport in self.transports:
            costs[type(transport).__name__] = transport.calculate_delivery_cost(weight, distance)
        return costs

weight = 100
distance = 50

bike = Bike()
car = Car()
truck = Truck()

delivery_service = DeliveryService()
delivery_service.add_transport(bike)
delivery_service.add_transport(car)
delivery_service.add_transport(truck)

costs = delivery_service.calculate_total_cost(weight, distance)
for transport_, cos in costs.items():
    print(f"Стоимость доставки с помощью {transport_}: {cos} сом")
    
