# Week 1 review

# Coding Challenge Review

road_trip = {}

def add_stop(stop_number, destination):
    if road_trip.get(stop_number) == None:
        road_trip[stop_number] = destination
        print(f"Added stop {stop_number} - {destination}")
    else:
        if input("That stop already exists, type 'y' to overwrite:") == 'y':
            road_trip[stop_number] = destination
        else:
            print("The data was not changed")


while True:
    stop = int(input("Stop Number: "))
    dest = input("Destination: ")
    add_stop(stop, dest)
    if input("Would you like to add another stop? Type 'y' for yes.") != 'y':
        break

print(road_trip)

'''
BONUS: 
Instead of printing an error for existing stops, ask the user if they would like to overwrite the existing stop
 - If they do, allow them to overwrite the existing stop
'''
