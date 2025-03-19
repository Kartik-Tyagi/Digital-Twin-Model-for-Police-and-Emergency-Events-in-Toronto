#Imports
import networkx as nx

#Ward Nodes
class WardNode:
    def __init__(self, ward_id, events):
        self.id = ward_id
        self.events = events  # List of predicted events for each hour
        self.adjacent = []    # List of adjacent WardNode references


#Classifying risk levels for a specific hour
def classify_risk(wards, hour, high_threshold, low_threshold):
    high_risk = []
    medium_risk = []
    low_risk = []

    for ward in wards:
        events_count = ward.events[hour]
        if events_count >= high_threshold:
            high_risk.append(ward)
        elif events_count >= low_threshold:
            medium_risk.append(ward)
        else:
            low_risk.append(ward)

    return high_risk, medium_risk, low_risk


#Finding minimum number of patrol routes and number of patrol units
def optimize_patrol_routes(high_risk_wards):
    G = nx.Graph()

    for ward in high_risk_wards:
        G.add_node(ward.id)

    for ward in high_risk_wards:
        for neighbor in ward.adjacent:
            if neighbor in high_risk_wards:
                G.add_edge(ward.id, neighbor.id)

    components = list(nx.connected_components(G))
    num_patrol_units = len(components)

    patrol_routes = [list(component) for component in components]

    return num_patrol_units, patrol_routes


#Adding closest medium risk wards to available units
def assign_patrols_to_medium_risk(patrol_routes, medium_risk_wards):
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


#Recommendation
def main(wards, hour, high_threshold, low_threshold):
    high_risk, medium_risk, low_risk = classify_risk(wards, hour, high_threshold, low_threshold)

    num_patrol_units, patrol_routes = optimize_patrol_routes(high_risk)

    final_routes = assign_patrols_to_medium_risk(patrol_routes, medium_risk)

    return final_routes
