def func(gain):
    max_altitude = 0
    current_altitude = 0
    
    for change in gain:
        current_altitude += change
        max_altitude = max(current_altitude,max_altitude)
        
    return max_altitude

gain = [-5,1,5,0,-7]
print(func(gain))