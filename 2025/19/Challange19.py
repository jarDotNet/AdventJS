'''
Challenge #19: 🎄 Santa's Secret Journey

The sleigh’s GPS has gone crazy! 😱 Santa Claus has the segments of his trip, but they’re all out of order.

Your mission is to reconstruct the complete route from the origin to the final destination.

Keep in mind: The first element of the array is always the first segment of the trip. From there, you must keep connecting destinations to the next origins.

revealSantaRoute([
  ['MEX', 'CAN'],
  ['UK', 'GER'],
  ['CAN', 'UK']
])
// → ['MEX', 'CAN', 'UK', 'GER']

revealSantaRoute([
  ['USA', 'BRA'],
  ['JPN', 'PHL'],
  ['BRA', 'UAE'],
  ['UAE', 'JPN'],
  ['CMX', 'HKN']
])
// → ['USA', 'BRA', 'UAE', 'JPN', 'PHL']

revealSantaRoute([
  ['STA', 'HYD'],
  ['ESP', 'CHN']
])
// → ['STA', 'HYD']

🔎 Keep in mind:

- There are no duplicate routes or cycles in Santa’s path.
- There may be segments that don’t belong to the route; these must be ignored.
'''

def reveal_santa_route_original(routes: list[list[str]]) -> list[str]:
  route = routes[0]
  location = route[0]
  destination = route[1]
  santa_route = [location]

  while destination:
    destination_found = False
    santa_route.append(destination)
    for route in routes:
      if route[0] == destination:
        destination_found = True
        location = destination
        destination = route[1]
        break
      
    if not destination_found:
      destination = None

  return santa_route

def reveal_santa_route(routes: list[list[str]]) -> list[str]:
    route_map = {route[0]: route[1] for route in routes}
    
    santa_route = []
    location = routes[0][0]

    while location:
        santa_route.append(location)
        location = route_map.get(location)

    return santa_route

# Main program
print(
  reveal_santa_route([
    ['MEX', 'CAN'],
    ['UK', 'GER'],
    ['CAN', 'UK']
  ]))

print(
  reveal_santa_route([
    ['USA', 'BRA'],
    ['JPN', 'PHL'],
    ['BRA', 'UAE'],
    ['UAE', 'JPN'],
    ['CMX', 'HKN']
  ]))

print(
  reveal_santa_route([
    ['STA', 'HYD'],
    ['ESP', 'CHN']
  ]))