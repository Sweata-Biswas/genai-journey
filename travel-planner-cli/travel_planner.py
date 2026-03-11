#CLI- command line interface
#user enter 
#budget
#number of days
#type of trip ( mountain/beach)
#output - short iternary idea

def suggest_destination(budget,trip_type):
    if trip_type=="mountains":
        if budget< 15000:
            return "Kasol or Triund"
        elif budget <30000:
            return "Dharamshala or Manali"
        else:
            return "Spiti"
    elif trip_type=="beach":
        if budget<15000:
            return "Gokarna"
        elif budget<30000:
            return "Goa"
        else:
            return "Kerala"
        

    else:
        return "explore local desitnation"
    

def itinerary(days):
    if days<=2:
        return "Weekend trip with light sightseeing"
    elif days <=5:
        return "Explore local attractions and nature"
    else:
        return "Full exploration trip with adventure activities"

budget = int(input("Enter your Budget:"))
days = int(input("Enter number of days you are planning:"))
trip_type = input("Enter your trip type (mountains/beach):") 

destination = suggest_destination(budget,trip_type)
itinerary_days = itinerary(days)
 
print("Based on your budget and trip type, you should visit: ",destination)
print("Suggested itinerary: ",itinerary_days)