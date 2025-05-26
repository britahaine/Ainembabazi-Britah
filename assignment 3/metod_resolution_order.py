
class SingleRoom():
    def display_info(self):
        print( "single Room with premium amenities")

class DoubleRoom():
    def display_info(self):
        print ("Dauble room with luxury")

class Room(SingleRoom,DoubleRoom):
    def display_info(self):
        SingleRoom.display_info(self)
        DoubleRoom.display_info(self)
        
room1=Room()   
room1.display_info()     

    