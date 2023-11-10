class Scooter:
    next_serial = 0 # class variable to track the next serial number

    def __init__(self, station, charge):
        self.station = station
        self.user = None
        self.serial = Scooter.next_serial
        Scooter.next_serial += 1
        self.charge = charge
        self.is_broken = False

    def rent(self, user):
        if self.is_broken:
            raise Exception("Scooter needs repair")
        elif self.charge < 20:
            raise Exception("Scooter needs to charge")
        
        self.user = user
        self.station = None

    def dock(self, station):
        self.station = station
        self.user = None


# Create instances of the Scooter class
scooter1 = Scooter(station="Station1", charge=50)
scooter2 = Scooter(station="Station2", charge=15)

# Rent a Scooter
try:
    scooter1.rent(user="Alice")
    print(f"Scooter {scooter1.serial} rented by {scooter1.user}")
except Exception as e:
    print(f"Error: {e}")


#Dock a scooter
scooter2.dock(station="Station3")
print(f"Scooter {scooter2.serial} docked at {scooter2.station}")