#Imports
import networkx as nx
import random

#Ward Nodes
class WardNode:
    def __init__(self, ward_id, events):
        self.id = ward_id
        self.events = events
        self.adjacent = []


#Creating Sample Nodes
def create_sample():
    sample_list = []
    adjecency = [
        [2, 5, 7],
        [1, 3, 5],
        [2, 4],
        [3, 5, 9, 10],
        [1, 2, 4, 6, 7, 8, 9],
        [5, 7, 8, 18],
        [1, 5, 6],
        [5, 6, 9, 12, 15],
        [4, 5, 8, 10, 11, 12],
        [4, 9, 11, 13, 14],
        [9, 10, 12, 13, 14, 15],
        [8, 9, 11, 15],
        [10, 11, 14],
        [10, 11, 13, 15, 19],
        [8, 11, 12, 14, 16, 17, 18],
        [15, 17, 19, 21],
        [15, 16, 18, 22],
        [6, 15, 17],
        [14, 16, 20],
        [19, 21, 24],
        [16, 20, 22, 23, 24],
        [17, 21, 23],
        [21, 22, 24, 25],
        [20, 21, 23, 25],
        [23, 24]
    ]
    event_choices = [0, 1, 2, 3, 4, 5, 6]
    event_probabilities = [0.1, 0.2, 0.25, 0.2, 0.15, 0.05, 0.05]
    
    for i in range(25):
        new_node = WardNode(i + 1, random.choices(event_choices, event_probabilities, k=24))
        sample_list.append(new_node)
    for i in range(25):
        for j in adjecency[i]:
            sample_list[i].adjacent.append(sample_list[j - 1])
    
    return sample_list

#Classifying risk levels for a specific hour
def classify_risk(wards, hour, high_threshold, low_threshold):
    max_risk = []
    high_risk = []
    medium_risk = []
    low_risk = []

    for ward in wards:
        events_count = ward.events[hour]
        if events_count == 6:
            max_risk.append(ward)
        elif events_count >= high_threshold:
            high_risk.append(ward)
        elif events_count >= low_threshold:
            medium_risk.append(ward)
        else:
            low_risk.append(ward)

    return max_risk, high_risk, medium_risk, low_risk


#Finding minimum number of patrol routes and number of patrol units
def optimize_patrol_routes(G):
    components = list(nx.connected_components(G))
    num_patrol_units = len(components)

    patrol_routes = [list(component) for component in components]

    return num_patrol_units, patrol_routes


#Adding closest medium risk wards to available units
def assign_patrols_to_medium_risk(G, patrol_routes, medium_risk_wards):
    assigned_routes = []

    for route in patrol_routes:
        last_ward_id = route[-1]
        nearest_ward = None
        min_distance = float('inf')

        for ward in medium_risk_wards:
            distance = nx.shortest_path_length(G, source=last_ward_id, target=ward.id)
            if distance < min_distance:
                min_distance = distance
                nearest_ward = ward

        if nearest_ward:
            route.append(nearest_ward.id)
            medium_risk_wards.remove(nearest_ward)

        assigned_routes.append(route)

    return assigned_routes


#Manually finding minimum agents required based on hours
def find_min_units(wards, max_risk, high_risk):
    min_units = 0
    min_units += 2*len(max_risk[0])
    min_units += len(high_risk[0])
    previous_max_risk = max_risk[0]
    previous_high_risk = high_risk[0]
    for hour in range(1,24):
        current_max_risk = max_risk[hour]
        current_high_risk = high_risk[hour]
        found = False
        for ward in current_max_risk[:]:
            for adjacent_ward in ward.adjacent:
                if adjacent_ward in previous_max_risk:
                    found = True
                    current_max_risk.remove(ward)
                    previous_max_risk.remove(adjacent_ward)
                    break
            if not found:
                got_first = False
                first_ward = None
                for adjacent_ward in ward.adjacent:
                    if adjacent_ward in previous_high_risk:
                        if got_first:
                            previous_high_risk.remove(adjacent_ward)
                            previous_high_risk.remove(first_ward)
                            current_max_risk.remove(ward)
                            break
                        else:
                            got_first = True
                            first_ward = adjacent_ward
        for ward in current_high_risk[:]:
            prev_max_used = []
            found = False
            for adjacent_ward in ward.adjacent:
                if adjacent_ward in previous_max_risk:
                    found = True
                    current_high_risk.remove(ward)
                    if adjacent_ward.id in prev_max_used:
                        previous_max_risk.remove(adjacent_ward)
                    else:
                        prev_max_used.append(adjacent_ward.id)
                    break
            if not found:
                for adjacent_ward in ward.adjacent:
                    if adjacent_ward in previous_high_risk:
                        previous_high_risk.remove(adjacent_ward)
                        current_high_risk.remove(ward)
                        break
        min_units += 2*len(current_max_risk)
        min_units += len(current_high_risk)
    return min_units
                            
                

#ChatGPT Answer
def find_min_agents(wards, max_risk, high_risk):
    total_agents = 0

    for hour in range(24):
        # Combine max and high risk wards for the current hour
        critical_wards = set(max_risk[hour]) | set(high_risk[hour])
        covered_wards = set()
        agents_needed = 0

        while critical_wards:
            # Select the ward with the maximum number of adjacent critical wards
            ward = max(critical_wards, key=lambda w: len(critical_wards & set(wards[w].adjacent)))
            agents_needed += 1
            covered_wards.add(ward)
            critical_wards.remove(ward)
            # Remove adjacent wards from the critical set
            for neighbor in wards[ward].adjacent:
                if neighbor in critical_wards:
                    critical_wards.remove(neighbor)

        # Each max risk ward requires an additional agent
        agents_needed += len(max_risk[hour])
        total_agents += agents_needed

    return total_agents

#Recommendation main function
def main():
    wards = create_sample()
    high_threshold = 4
    low_threshold = 2
    hour = 0
    max_risk = []
    high_risk = []
    medium_risk = []
    low_risk = []
    
    for i in range(24):
        temp_max, temp_high, temp_medium, temp_low = classify_risk(wards, i, high_threshold, low_threshold)
        max_risk.append(temp_max)
        high_risk.append(temp_high)
        medium_risk.append(temp_medium)
        low_risk.append(temp_low)
    
    
    manual_min_units = find_min_units(wards, max_risk, high_risk)
    
    G = nx.Graph()

    for ward in high_risk[hour]:
        G.add_node(ward.id)

    for ward in high_risk[hour]:
        for neighbor in ward.adjacent:
            if neighbor in high_risk[hour]:
                G.add_edge(ward.id, neighbor.id)
    
    num_patrol_units, patrol_routes = optimize_patrol_routes(G)
    final_routes = assign_patrols_to_medium_risk(G, patrol_routes, medium_risk)

    return final_routes
