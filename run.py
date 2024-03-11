import csv
import math

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((int(city1['X']) - int(city2['X']))**2 + (int(city1['Y']) - int(city2['Y']))**2)

# Function to find the nearest city to a given city
def nearest_city(cities, current_city, visited):
    nearest_distance = float('inf')
    nearest_city_index = -1
    for i, city in enumerate(cities):
        if not visited[i]:
            distance = euclidean_distance(current_city, city)
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_city_index = i
    return nearest_city_index

# Function to insert the nearest city to the current route
def insert_nearest_city(cities, route, visited):
    current_city_index = route[-1]
    nearest_city_index = nearest_city(cities, cities[current_city_index], visited)
    route.append(nearest_city_index)
    visited[nearest_city_index] = True

# Main function
def main():
    # Read data from CSV file
    with open('cities.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        cities = [row for row in reader]

    # Initialize the route and visited list
    route = [0]
    visited = [False] * len(cities)
    visited[0] = True

    # Perform Nearest Insertion algorithm
    for _ in range(len(cities) - 1):
        insert_nearest_city(cities, route, visited)

    # Add the first city to complete the route
    route.append(0)

    # Calculate the total distance of the optimized route
    total_distance = sum(euclidean_distance(cities[route[i]], cities[route[i-1]]) for i in range(1, len(route)))
    print(f'Optimized route: {[cities[i]["City"] for i in route]}')
    print(f'Total distance: {total_distance:.2f}')

if __name__ == '__main__':
    main()

