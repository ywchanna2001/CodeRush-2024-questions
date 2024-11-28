import ast
from typing import List
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Solution:
    def canReachCorner(
        self, xCorner: int, yCorner: int, circles: List[List[int]]
    ) -> bool:
        def in_circle(x: int, y: int, cx: int, cy: int, r: int) -> int:
            return (x - cx) ** 2 + (y - cy) ** 2 <= r**2

        def cross_left_top(cx: int, cy: int, r: int) -> bool:
            a = abs(cx) <= r and 0 <= cy <= yCorner
            b = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return a or b

        def cross_right_bottom(cx: int, cy: int, r: int) -> bool:
            a = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            b = abs(cy) <= r and 0 <= cx <= xCorner
            return a or b

        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            if cross_right_bottom(x1, y1, r1):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                if vis[j] or not ((x1 - x2) ** 2 + (y1 - y2) ** 2 <= (r1 + r2) ** 2):
                    continue
                if (
                    (x1 * r2 + x2 * r1 < (r1 + r2) * xCorner)
                    and (y1 * r2 + y2 * r1 < (r1 + r2) * yCorner)
                    and dfs(j)
                ):
                    return True
            return False

        vis = [False] * len(circles)
        for i, (x, y, r) in enumerate(circles):
            if in_circle(0, 0, x, y, r) or in_circle(xCorner, yCorner, x, y, r):
                return False
            if (not vis[i]) and cross_left_top(x, y, r) and dfs(i):
                return False
        return True


def draw_rectangle_and_circles(X, Y, guard_towers):
    """
    Function to draw the rectangle and guard towers (circles) on a Cartesian plane.

    Parameters:
        X (int): X-coordinate of the top-right corner of the rectangle.
        Y (int): Y-coordinate of the top-right corner of the rectangle.
        guard_towers (list of lists): Each list contains [Xi, Yi, Ri], where
                                      Xi, Yi are the coordinates of the circle's center,
                                      and Ri is the radius.
    """
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Draw the rectangular land
    rectangle = patches.Rectangle((0, 0), X, Y, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(rectangle)
    
    # Plot each guard tower
    for tower in guard_towers:
        x, y, r = tower
        # Draw the guard area as a circle
        circle = patches.Circle((x, y), r, linewidth=1.5, edgecolor='red', facecolor='none', alpha=0.7)
        ax.add_patch(circle)
        # Mark the tower's center
        plt.plot(x, y, 'ro', label=f"Tower at ({x}, {y})" if guard_towers.index(tower) == 0 else "")
    
    # Plot start and end points
    plt.plot(0, 0, 'go', label="Start (0, 0)")  # Start point
    plt.plot(X, Y, 'bo', label=f"End ({X}, {Y})")  # End point
    
    # Set axis limits and labels
    ax.set_xlim(-1, X + 1)  # Add a small buffer around the rectangle for better visualization
    ax.set_ylim(-1, Y + 1)
    ax.set_xlabel("X-axis (meters)")
    ax.set_ylabel("Y-axis (meters)")
    ax.set_title("Rectangular Land and Guard Towers")
    
    # Set custom ticks for the Cartesian plane
    ax.set_xticks(range(0, X + 2))  # Numbers from 0 to X+1
    ax.set_yticks(range(0, Y + 2))  # Numbers from 0 to Y+1
    
    # Add grid lines for better readability
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    
    # Add legend
    plt.legend(loc="upper left")
    
    # Display the plot
    plt.show()


# Input the X and Y values
X, Y = map(int, input().split())

# Input the 2D array as a string
input_string = input()

# Convert the input string to an actual 2D array
guard_towers = ast.literal_eval(input_string)

# Create an instance of the Solution class
solution = Solution()

# Call the function and get the output
result = solution.canReachCorner(X, Y, guard_towers)

if result:
    print("YES")
else:
    print("NO")

# Draw the rectangle and guard towers
draw_rectangle_and_circles(X, Y, guard_towers)
