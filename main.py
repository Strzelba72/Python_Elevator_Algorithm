class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors                                        #set floor
        self.current_floor = 1                                              #start floor
        self.direction = 0                                                  #0 stay,1 up,-1 down
        self.destinations=set()                                             #destinations as class set()
    
    def __str__(self):
        return f"Floor {self.current_floor} direction {self.direction}"     #display current floor and direction
    
    def req_floor(self, floor):
        if floor == self.current_floor:
            return
        
        self.destinations.add(floor) #add destination
        if not self.direction:
            self.direction = 1 if floor > self.current_floor else -1        #set direction
    
    def move(self):
        if not self.direction:                                              #return if direction is 0
            return
        
        next_floor = self.current_floor + self.direction                    #count next floor
        if next_floor in self.destinations:
            self.destinations.remove(next_floor)                            #if next floor is in destinations, remove
        elif next_floor == self.num_floors or next_floor == 1:
            self.direction = 0                                              #return direction when next_floor is actual floor
        elif not self.destinations:
            self.direction = 0                                              #when destinations is empty
        elif self.direction == 1 and max(self.destinations) < next_floor:
            self.direction = -1                                             #the highest destination floor
        elif self.direction == -1 and min(self.destinations) > next_floor:
            self.direction = 1                                              #the lowest destination floor
       
        
        self.current_floor = next_floor                                     #change current on next
    
    def start(self):
        while 1:
            print(self)
            self.move()
            if not self.direction and not self.destinations: 
                 self.direction=0
                 break                                               #stop if destiation is empty and direction is 0b
               

elevator = Elevator(8)

elevator.req_floor(2)  
elevator.req_floor(5)                                                     #request floor
elevator.start()
#elevator.req_floor(2)
elevator.req_floor(4)
elevator.start()
#elevator.req_floor(5)
#elevator.req_floor(3)
#elevator.start() #start elevator
#elevator.req_floor(1)
#elevator.req_floor(8)
#elevator.start()
print(elevator.destinations)
