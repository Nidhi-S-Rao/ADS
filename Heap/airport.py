""" An airport is developing a computer simulation of air-traffic control that handles events such as 
landings and takeoffs. Each event has a time stamp that denotes the time when the event will 
occur with additional information like, plane number, takeoff or landing. The simulation program 
needs to efficiently perform the following two fundamental operations: 1. Insert an event with a 
given time stamp, aircraft number, takeoff / landing (add a future event). 2. Extract the event 
with smallest time stamp (that is, determine the next event to process). Design and implement 
suitable data structures that work efficiently in terms of time."""



import heapq

class Event:
    def __init__(self, timestamp, plane_number, takeoff):
        self.timestamp = timestamp
        self.plane_number = plane_number
        self.takeoff = takeoff

class AirTrafficControl:
    def __init__(self):
        self.event_heap = []  # Minimum heap to store events

    def insert_event(self, event):
        heapq.heappush(self.event_heap, (event.timestamp, event))

    def extract_next_event(self):
        if not self.event_heap:
            return None

        _, next_event = heapq.heappop(self.event_heap)
        return next_event

# Example usage:
atc = AirTrafficControl()

event1 = Event(10, "ABC123", True)  # Plane ABC123 taking off at timestamp 10
event2 = Event(15, "XYZ789", False)  # Plane XYZ789 landing at timestamp 15
event3 = Event(5, "DEF456", True)   # Plane DEF456 taking off at timestamp 5

atc.insert_event(event1)
atc.insert_event(event2)
atc.insert_event(event3)

next_event = atc.extract_next_event()
while next_event:
    takeoff_or_landing = "takeoff" if next_event.takeoff else "landing"
    print(f"At timestamp {next_event.timestamp}, plane {next_event.plane_number} is scheduled for {takeoff_or_landing}")
    next_event = atc.extract_next_event()
