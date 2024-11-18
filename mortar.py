import math

def mortar_support(v0, h, theta):
    # Convert angle to radians
    theta_rad = math.radians(theta)
    
    # Gravity constant
    g = 9.81
    
    # Calculate flight time
    flight_time = (v0 * math.sin(theta_rad) + math.sqrt((v0 * math.sin(theta_rad))**2 + 2 * g * h)) / g
    
    # Calculate horizontal range
    horizontal_range = v0 * math.cos(theta_rad) * flight_time
    
    # Calculate maximum height
    max_height = h + (v0 * math.sin(theta_rad))**2 / (2 * g)
    
    # Round results to 2 decimal places
    flight_time = round(flight_time, 2)
    horizontal_range = round(horizontal_range, 2)
    max_height = round(max_height, 2)
    
    return flight_time, horizontal_range, max_height

# Example test case
v0 = 100
h = 100
theta = 45

# Calculate and print the results
flight_time, horizontal_range, max_height = mortar_support(v0, h, theta)
print(f"Flight time: {flight_time} seconds")
print(f"Horizontal range: {horizontal_range} meters")
print(f"Maximum height: {max_height} meters")
