import pandas as pd
import polyline
import requests
import osmnx as ox



# Reading the data
df= pd.read_csv('E/Metro1/atrifact/access.csv')


def get_route_polyline(start, end):
    url = f'https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}& key=ENTERAPIKEY'
    response = requests.get(url)
    data = response.json()
    polyline_points = data['routes'][0]['overview_polyline']['points']
    return polyline.decode(polyline_points)

# Example
start = '12.92595573,77.58347683'
end = '12.929312265009031,77.5802958957799'
route = get_route_polyline(start, end)
print(route)


# plot the route
start = (12.91654651,77.59089937)
end = (12.929312265009031, 77.5802958957799)

# Create a graph from the street network
G = ox.graph_from_point(start, dist=1000, network_type='all')

# Get the nearest network nodes to the two points
orig = ox.distance.nearest_nodes(G, start[0], start[1])
dest = ox.distance.nearest_nodes(G, end[0], end[1])

# Find the shortest path between the two nodes
route = nx.shortest_path(G, orig, dest, weight='length')

# Plot the street network
fig, ax = ox.plot_graph(G)

# Plot the shortest path
ox.plot_graph_route(G, route, route_linewidth=6, node_size=0, ax=ax, route_color='r')

# Plot the origin and destination points
ax.scatter(start[1], start[0], c='g', s=100, label='Start')
ax.scatter(end[1], end[0], c='b', s=100, label='End')
ax.legend()

