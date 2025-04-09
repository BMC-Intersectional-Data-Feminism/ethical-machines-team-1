import urban_planning 
import random

# Example algorithm: Always picks the non-vehicle option
def always_pick_non_vehicle(option1, option2):
    """This algorithm always picks the non-vehicle if possible.
    It will return first the picked option and second the non-chosen option. """
    
    if option1[0] in urban_planning.all_non_vehicles: ## Check if option 1 is a non-vehicle, if so, pick that. 
        return option1, option2
    elif option2[0] in urban_planning.all_non_vehicles:  ## If option 1 is not a non-vehicle, check if option 2 is. If so, pick that. 
        return option2, option1
    else:
        return option1, option2  # Default to first option if both are vehicles

# Student function placeholder
def pick_animal(option1, option2):
    """Always picks animal."""
    ## option = [type of vehicle or non vehicle, modifier]
    possible_animal = urban_planning.non_vehicles['Animal']
    possible_pedestrian = urban_planning.non_vehicles['Pedestrian']

    if option1[0] in possible_animal:
        if option2[0] in possible_animal:
            selected = random.choice([option1, option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
        else:
            return option1, option2
    elif option2[0] in possible_animal:
        return option2, option1
    elif option1[0] in possible_pedestrian:
        if option2[0] in possible_pedestrian:
            selected = random.choice([option1,option2])
            if option1 == selected:
                return selected, option2
            else:
                return selected, option1
    elif option2[0] in possible_pedestrian:
        return option2, option1
    else: 
        selected = random.choice([option1,option2])
        if option1 == selected:
            return selected, option2
        else:
            return selected, option1


# Function to run the simulation using a given algorithm
# Run the activity
#urban_planning.run_activity()

# Run the activity using the example algorithm
#print("\n🔹 Running Example Algorithm: Always Pick Non-Vehicle 🔹")
urban_planning.run_activity(num_scenarios=25, decision_function = pick_animal)

#print("\n🔹 Now it's your turn! Modify 'student_algorithm' and run again. 🔹")
