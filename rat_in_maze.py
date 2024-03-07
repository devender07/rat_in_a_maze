import random

# ANSI escape codes for text formatting
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"

def create_maze(n, density):
    # Create a maze with walls and open spaces
    maze = [[RED + ' █ ' + RESET if random.random() < density else BLUE + ' ◌ ' + RESET for _ in range(n)] for _ in range(n)]
    maze[0][0] = BOLD + GREEN + ' S ' + RESET   # Start
    maze[n-1][n-1] = BOLD + GREEN + ' E ' + RESET  # End
    return maze

def print_maze(maze):
    # Print the maze, separating each cell with a space
    for row in maze:
        print(" ".join(row))
        print()

def dfs_pathfinding(maze, x, y, path):
    # Depth-First Search algorithm to find a path from the start to the end
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and (maze[x][y] == BLUE + ' ◌ ' + RESET or maze[x][y] == BOLD + GREEN + ' S ' + RESET or maze[x][y] == BOLD + GREEN + ' E ' + RESET):
        path.append((x, y))
        maze[x][y] = BOLD + BLUE + ' ◌ ' + RESET  # Mark as visited

        if x == len(maze) - 1 and y == len(maze[0]) - 1:  # Reached the end
            return True

        # Explore all possible moves: right, down, left, up
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for move in moves:
            new_x, new_y = x + move[0], y + move[1]
            if dfs_pathfinding(maze, new_x, new_y, path):
                return True

        path.pop()  # Backtrack if no valid moves

    return False

def print_maze_with_path(maze, path):
    # Print the maze with the solution path represented by '●'
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) == (0, 0):
                print(BOLD + GREEN + ' S ' + RESET, end=' ')
            elif (i, j) == (len(maze) - 1, len(maze) - 1):
                print(BOLD + GREEN + ' E ' + RESET, end=' ')
            elif (i, j) in path:
                print(BOLD + GREEN + ' ● ' + RESET, end=' ')
            else:
                print(cell, end=' ')
        print()
        print()

def main():
    # Get user input for maze size
    maze_size = int(input("Enter the size of the maze (n x n): "))
    wall_density = 0.25
    
    # Generate the initial maze
    maze = create_maze(maze_size, wall_density)
    
    print("\nGenerated Maze:")
    print_maze(maze)

    while True:
        # Display user menu
        print("1. Print The Path (Not Available After Path Generation)")
        print("2. Generate Another Puzzle")
        print("3. Exit The Game")       
        option = int(input("Enter Your Choice (1/2/3): "))
        
        if option == 1:
            # Find and print the solution path
            path = []
            if dfs_pathfinding(maze, 0, 0, path):
                print("\nPath Found:")
                print_maze_with_path(maze, path)
            else:
                print("\nNo path found.")

        elif option == 2:
            # Generate a new maze and print it
            maze = create_maze(maze_size, wall_density)
            print("\nGenerated Maze:")
            print_maze(maze)
            
        else:
            # Exit the game
            break

if __name__ == '__main__':
    main()
