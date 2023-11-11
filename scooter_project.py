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


class User:
    def __init__(self, username, password, age):
        self.username = username
        self.password = password
        self.age = age
        self.logged_in = False

    def login(self, password):
        if password != self.password:
            raise Exception("Incorrect Password")
        
        self.logged_in = True

    def logout(self):
        self.logged_in = False
        

# Example of instances of the User class
user1 = User(username="MegH123", password="Google2023", age=34)
user2 = User(username="userTwo2",password="User123", age=21)

#Login User
try:
    user1.login(password="Google2023")
    print(f"User {user1.username} logged in.")
except Exception as e:
    print(f"Error: {e}")

# Logout a user
user2.logout()
print(f"User {user2.username} logged out")


class ScooterApp:
    def __init__(self):
        self.stations = {
            'Crotona Park Station':[],
            'Boston Rd Station':[],
            'Mott Haven':[],
            'TimeSquare Station':[],
            'Harlem River Station':[],
            'Bronx River Station':[],
            'Yankees Stadium':[]  
        }

        self.registered_users = {}

    def registered_user(self, username, password, age):
        if age < 18:
            raise Exception("Too young to register")
        elif username in self.registered_users:
            raise Exception("Already registered")
        
        user = User(username, password, age)
        self.registered_uses[username] = user
        print(f"User {username} is registered")
        return user
    
    def login_user(self, username, password):
        user = self.registered_users.get(username)
        if not user:
            raise Exception("Username or password is incorrect")
        
        try:
            user.login(password)
            print(f"User {username} is logged in")
        except Exception as e:
            raise Exception("Username or password is incorrect")
        
    
    def logout_user(self, username):
        user = self.registered_users.get(username)
        if not user or not user.logged_in:
            raise Exception("No such user is logged in")
        
        user.logout()
        print(f"User {username} is logged out")

    
    def create_scooter(self, station):
        if station not in self.stations:
            raise Exception('No such station')
        
        scooter = Scooter(station)
        self.station[station].append(scooter)
        scooter.station = station
        print(f"Created new scooter at {station}")
        return scooter 
    
    def dock_scooter(self, scooter, station):
        if station not in self.stations:
            raise Exception("No such station")
        if scooter in self.stations[station]:
            raise Exception("Scooter already at station")
        
        self.stations[station].append(scooter)
        scooter.dock(station)
        print(f"Scooter is docked at {station}")

    
    def rent_scooter(self, scooter, user):
        if not scooter.station:
            raise Exception("Scooter already rented")
        elif scooter.station not in self.stations:
            raise Exception("No such station")
