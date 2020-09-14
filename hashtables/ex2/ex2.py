#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    # Ticket Dictionary
    ticket_dict = {}

    # Loop through number of flights and add to dictionary
    for i in range(0, length):
        ticket_dict[tickets[i].source] = tickets[i].destination

    # Empty route list
    route = []

    # Find source starting point
    source = "NONE"
    destination = ticket_dict[source]

    # Loop through and find matching destination and add to list
    while destination != "NONE":
        route.append(destination)
        source = destination
        destination = ticket_dict[source]

    # Add "NONE" to end of list when no more flights
    route.append("NONE")

    # Return flight ordered list
    return route


# Visual Test
ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

result = reconstruct_trip(tickets, 10)
print(result)
