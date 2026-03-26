import projectilemotion

angle = 20.0
speed = 11.0

results = projectilemotion.projectilemotion_solver(angle, speed)

print("=" * 50)
print("PROJECTILE MOTION CALCULATOR")
print("=" * 50)
print(f"Launch Angle: {angle}°")
print(f"Initial Velocity: {speed} m/s")
print("-" * 50)
print(f"(a) Horizontal Distance: {results['range']:.2f} meters")
print(f"(b) Maximum Height: {results['max_height']:.2f} meters")
print("=" * 50)