#Function to test the Event Class. 
#Uses raw data as inputs at the moment. Early prototype. 
from Event import *


def main():
    events = []
    new_event = Event('Sailboat race', '21-02-2023', '10:00', '11:00', 5)
    events.append(new_event)

    volunteers = ["Jack Jones", 'Jane Doe', 'Richie David' , 'Saul Horwood', 'Ellie Connor', 'Roger Dodger']

    for volunteer in volunteers:
        if new_event.register_volunteer(volunteer):
            print(f"{volunteer} has been registered for {new_event.name} on {new_event.date}")
        else:
            print(f"{new_event.name} is already full")

    for event in events:
        print(f"{event.name} on {event.date}: {event.num_vol_registered}/{event.num_vol_required} volunteers required")
        if event.num_vol_registered > 0:
            print(f"Registered volunteers: {', '.join(event.volunteers)}")

main()