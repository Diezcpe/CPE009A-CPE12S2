import math

def projectilemotion_solver(angle_degrees, initial_velocity, g=9.8):
    angle_radians = math.radians(angle_degrees)
    projectile_range = (initial_velocity**2 * math.sin(2 * angle_radians)) / g
    max_height = (initial_velocity**2 * math.sin(angle_radians)**2) / (2 * g)
    
    return {
        'range': projectile_range,
        'max_height': max_height
    }