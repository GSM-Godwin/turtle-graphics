def turtle_graphics(commands):
    # Initialize the 20x20 floor with zeros
    floor = [[0] * 20 for _ in range(20)]

    # Turtle starting position and state
    x, y = 10, 10  # Starting near the center of the grid
    pen_down = False  # Pen initially up
    direction = "E"  # Turtle starts facing East

    # Directions mapping for turning right or left
    directions = ["N", "E", "S", "W"]  # North, East, South, West

    # Function to display the floor grid
    def display_floor():
        for row in floor:
            print("".join("*" if cell == 1 else " " for cell in row))

    # Process each command in the input list
    for command in commands:
        if command == 1:
            pen_down = False  # Pen up
        elif command == 2:
            pen_down = True  # Pen down
        elif command == 3:
            # Turn right: Move to the next direction in the sequence
            direction = directions[(directions.index(direction) + 1) % 4]
        elif command == 4:
            # Turn left: Move to the previous direction in the sequence
            direction = directions[(directions.index(direction) - 1) % 4]
        elif isinstance(command, tuple) and command[0] == 5:
            # Move forward by the specified number of steps
            steps = command[1]
            for _ in range(steps):
                if direction == "N":
                    x = max(0, x - 1)  # Move up, ensuring we don't go out of bounds
                elif direction == "E":
                    y = min(19, y + 1)  # Move right, ensuring we don't go out of bounds
                elif direction == "S":
                    x = min(19, x + 1)  # Move down, ensuring we don't go out of bounds
                elif direction == "W":
                    y = max(0, y - 1)  # Move left, ensuring we don't go out of bounds

                if pen_down:
                    floor[x][y] = 1  # Mark the floor if the pen is down
        elif command == 6:
            # Display the floor grid
            display_floor()
        elif command == 9:
            # End of commands
            break

# Example command set to draw a 12-by-12 square near the center of the grid
commands = [
    2,          # Pen down
    (5, 12),    # Move forward 12 spaces
    3,          # Turn right
    (5, 12),    # Move forward 12 spaces
    3,          # Turn right
    (5, 12),    # Move forward 12 spaces
    3,          # Turn right
    (5, 12),    # Move forward 12 spaces
    1,          # Pen up
    6,          # Display floor
    9           # End of data
]

# Run the turtle graphics simulation
turtle_graphics(commands)

# Explanation of Code:
# 1. The grid starts with all zeros, representing an empty floor.
# 2. The turtle starts near the center of the grid at (10, 10) for better use of the available space.
# 3. Command `2` puts the pen down, and movements marked by `(5, steps)` mark the path with 1s.
# 4. Turning commands (`3` for right, `4` for left) change the turtle's orientation.
# 5. `display_floor` uses "*" for marked cells (1s) and spaces for unmarked cells (0s).
# 6. The example program draws a 12x12 square and displays it.
# 7. Copy this code into a Python file and modify the commands list to create different shapes.
