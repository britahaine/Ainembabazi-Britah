
class Room:
    def display_info(self):
        print( "Standard Room - $500 per night")

class LuxuryRoom(Room):
    def display_info(self):  
        print("Luxury Room - $150 per night, with a pool table and Mini Bar")


room1 = Room()
luxury = LuxuryRoom()

room1.display_info() 
luxury.display_info()  