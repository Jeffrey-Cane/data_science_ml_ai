def calculate_triangle_area(base, height):
    """
    Parameters:
    base (float): The base of the triangle
    height (float): The height of the triangle
    
    Returns:
    float: Area of the triangle
    """
    return 0.5 * base * height


# Function to get user input and calculate the area
def main():
    print("Calculate the area of a triangle.")
    try:
        # Taking user input for the base and height
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        
        # Calculate and display the area
        area = calculate_triangle_area(base, height)
        print(f"The area of the triangle is: {area}")
    except ValueError:
        print("Error: Please enter valid numeric values for base and height.")


# Run the program
if __name__ == "__main__":
    main()
