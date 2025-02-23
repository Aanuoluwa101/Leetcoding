from collections import deque



# level order BFS queue even filling
# depth DFS stack; control filling direction (go deep in one direction first)
# recursion depth

# debugging is always easier with iterative approaches
# iterative approach is more memory efficient

# stack space consumption
# recursion depth limit in python may be exceeded (stack overflow error) 
def flood_fill_iterative(image, sr, sc, color):
    q = deque()


def print_image(image_arr):
    for row in image_arr:
        for pixel in row:
            print(pixel, end="  ")
        print() 


# one thing to note about recursive functions is that 
# there must always be a kind of stop condition that 
# prevents infinite recursion. It is called Base case

def flood_fill(image, sr, sc, color):
    row_count = len(image) 
    column_count = len(image[0])
    starting_pixel_color = image[sr][sc]

    if image[sr][sc] == color: 
        return image

    image[sr][sc] = color

    # go right 
    if sc + 1 < column_count and image[sr][sc + 1] == starting_pixel_color:
        flood_fill(image, sr, sc + 1, color)
    
    # go left 
    if sc - 1 >= 0 and image[sr][sc - 1] == starting_pixel_color:
        flood_fill(image, sr, sc - 1, color)
    
    # go up 
    if sr - 1 >= 0 and image[sr - 1][sc] == starting_pixel_color:
        flood_fill(image, sr - 1, sc, color)    
    
    # go down
    if sr + 1 < row_count and image[sr + 1][sc] == starting_pixel_color:
        flood_fill(image, sr + 1, sc, color) 
    
    return image
    

image = [[1,1,1], [1,1,0], [1,0,1]]
print_image(image)
image = flood_fill(image, 1, 1, 2)
print()
print_image(image)