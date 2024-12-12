
RIGHT = 1
LEFT = -1
FORWARD = 1
REVERSE = 0

#gears and allowable speeds are as follows:
#zero (reverse) (speed -1 to -10). Max reverse speed of car is -10
#one (speed 0 to 10)
#two (speed 10 to 20)
#three (speed 20 to 30)
#four (speed 30 to 45)
#five (speed 45 to 80). Max speed of car is 80
#gears change automatically, one gear at a time
#direction values are similar to numbers on clock face,
#imagine the car sitting on an old style clock face.
#0 = 12 = straight on. All other directions = 1-11
#direction indicate the direction the front of the car is pointing


class Car:
   def __init__(self):
      self._speed = 0
      self._gear = 1
      self._direction = 0 #front of car
      self._ForR = 1
      self._broken = False #indicates whether car is broken
      self._simulation = []
      self._simulation_loaded = False



   def accelerate(self, direction_change):
      #check if car is broken – do nothing if it is
      if self._broken:
         return
      print()
      print("Accelerating... ")
      #check if we are in reverse or in forward gear

      #modify speed (increase 5 miles an hour)
      if self._gear == 0:
         self._speed -= 5
      else:
         self._speed += 5

      #if speed to high (>80 or < -10) limit to either 80 or -10
      if self._speed > 80:
         self._speed = 80
      if self._speed < -10:
         self._speed = -10

      #change gear if necessary (automatic)
      self._change_gear()
      #display status
      self.display_stats()


   def brake(self, direction_change):
      #check if car is broken – do nothing if it is
      if self._broken:
         return
      #check if we are in reverse or in forward gear

      #modify speed (decrease 5 miles and hour)
      print("Breaking... ")
      if direction_change == "BRAKE" and self._speed < 0:
            self._speed += 5
            if self._speed > 0:
               self._speed = 0
      else:
         self._speed -= 5
         if self._speed < 0:
            self._speed = 0

      #change gear if necessary (automatic)
      self._change_gear()
      #display status
      self.display_stats()


   def turn_steering_wheel(self, direction_change):
   #check if car is broken – do nothing if it is

      if self._broken:
         return
      
   #check to see if car is in reverse

   #modify direction based on direction change and direction
   #-1 = left, 0 = straight on, 1 = right if going forward
      if self._gear > 0:
         if direction_change == LEFT:
            self._direction -= 1
            if self._direction == -12:
               self._direction += 12
         elif direction_change == RIGHT:
            self._direction += 1
            if self._direction == 12:
               self._direction -= 12

      else:
         self._gear == 0
         if direction_change == LEFT:
            self._direction += 1
            if self._direction == 12:
               self._direction -= 12
         elif direction_change == RIGHT:
            self._direction -= 1
         if self._direction == -12:
            self._direction += 12
   #1 = left, 0 = straight on, -11 = right if going in reverse
      
      self.display_stats()

   def select_forward_or_reverse(self, direction_change):

      #selected_gear is either FORWARD or REVERSE
      if self._speed != 0:
         self._broken = True 
         print()
         print("Your car has broken due to incorrect direction change!")
         print("Exiting Simulation...")
         return

      if direction_change == FORWARD and self._speed == 0:
         self._ForR = 1
         self._gear = 1
      elif direction_change == REVERSE and self._speed == 0:
         self._ForR = 0
         self._gear = 0
      
      self.display_stats()
      #check to see if car is stationary. Car breaks if it is not.
      #change gear


   def _change_gear(self):
      #private: only called by other methods
      #check to see if car is broken – do nothing if it is
      #work out what gear you need to be in based on car’s speed
      if self._speed < 0:
         self._gear = 0
      elif self._speed <= 10:
         self._gear = 1
         print()
         print("Changing gear...")
         print(f"You are in Gear: {self._gear} ")
      elif self._speed <= 20 > 10:
         self._gear = 2
         print()
         print("Changing gear...")
         print(f"You are in Gear: {self._gear} ")
      elif self._speed <= 30 > 20:
         self._gear = 3
         print()
         print("Changing gear...")
         print(f"You are in Gear: {self._gear} ")
      elif self._speed <= 45 > 30:
         self._gear = 4
         print()
         print("Changing gear...")
         print(f"You are in Gear: {self._gear} ")
      elif self._speed <= 80 > 45:
         self._gear = 5
         print()
         print("Changing gear...")
         print(f"You are in Gear: {self._gear} ")
      #Loop one gear at a time, either changing up or down, to get to required gear
      




   def display_stats(self):
   #display car stats
      print(f"Speed: {self._speed} mph | Gear: {self._gear} | Direction: {self._direction}")


   def load_simulation(self, filename: str):
      
      #load data from file
      placeholder_list = [] #empty list for stock sold data

      file = open(filename) #open file
      line = file.readline().strip() #take data from file line by line
      while line != "": #while there is text to read the loop will run
         placeholder_list.append(line) #take the data from the file and moves it to the list
         line = file.readline().strip() #moves to next line to continue the loop
      file.close() #closes file
      self._simulation = placeholder_list
      self._simulation_loaded = True
      


   def run_simulation(self):

      if not self._simulation_loaded:
         print("Error! Simulation not loaded...")
         return

      #apply loaded data to car simulator line by line
      for action in self._simulation:
         if action == "FORWARD":
            direction_change = FORWARD
            self.select_forward_or_reverse(direction_change)
         elif action == "REVERSE":
            direction_change = REVERSE
            self.select_forward_or_reverse(direction_change)
         elif action == "ACCELERATE":
            direction_change = "ACCELERATE"
            self.accelerate(direction_change)
         elif action == "LEFT":
            direction_change = LEFT
            self.turn_steering_wheel(direction_change)
         elif action == "RIGHT":
            direction_change = RIGHT
            self.turn_steering_wheel(direction_change)
         elif action == "BRAKE":
            direction_change = "BRAKE"
            self.brake(direction_change)



if __name__ == '__main__':
   my_car = Car()
   loaded_data = my_car.load_simulation("simulation.txt")
   my_car.run_simulation()
