import tkinter as tk

# Global variables for the Mandelbrot set parameters
width, height = 400, 200
initial_xl, initial_xr = -2.5, 1.5
initial_yu, initial_yd = 2, -2

# Copy initial values for reset
xl, xr, yu, yd = initial_xl, initial_xr, initial_yu, initial_yd

# Function to calculate Mandelbrot iterations for a given complex number
def mandelbrot_iterations(real, imaginary, max_iterations=100, threshold=100):
    c = complex(real, imaginary)
    z = complex(0, 0)
    count = 0

    # Loop until max iterations or threshold reached
    while count < max_iterations and abs(z) < threshold:
        z = z * z + c
        count += 1

    # Return the number of iterations or -1 if max iterations reached
    return count if count < max_iterations else -1

# Function to generate and display the Mandelbrot set using Tkinter
def generate_and_display_mandelbrot(canvas):
    # Clear previous drawings
    canvas.delete("all")

    # Loop through each pixel in the canvas
    for y in range(height):
        for x in range(width):
            # Calculate the real and imaginary parts based on the pixel position
            real = x * (xr - xl) / width + xl
            imaginary = y * (yu - yd) / height + yd

            # Get the number of Mandelbrot iterations for the complex number
            iterations = mandelbrot_iterations(real, imaginary)

            # Color the pixel based on the number of iterations
            if iterations == -1:
                color = "#000000"  # Set color to black for points in the Mandelbrot set
            else:
                # Use a shade of sky blue based on the number of iterations
                blue_shade = min(255, iterations * 10)  # Adjust the multiplication factor for intensity
                color = "#{:02x}{:02x}ff".format(50, blue_shade)  # Adjust the red component (here set to 200)

            # Draw a rectangle (pixel) on the canvas with the calculated color
            canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)

# Function to zoom in at the mouse click position
def zoom(event):
    global xl, xr, yu, yd
    factor = 0.5
    click_real = event.x * (xr - xl) / width + xl
    click_imaginary = event.y * (yu - yd) / height + yd
    xl = click_real + (xl - click_real) * factor
    xr = click_real + (xr - click_real) * factor
    yu = click_imaginary - (click_imaginary - yu) * factor
    yd = click_imaginary + (yd - click_imaginary) * factor
    generate_and_display_mandelbrot(canvas)

# Function to reset the canvas to its original form
def reset_canvas():
    global xl, xr, yu, yd
    xl, xr, yu, yd = initial_xl, initial_xr, initial_yu, initial_yd
    generate_and_display_mandelbrot(canvas)

# Create a window
window = tk.Tk()
window.title("Mandelbrot Set")

# Create a canvas to draw on
canvas = tk.Canvas(window, width=width, height=height)
canvas.pack()

# Create a reset button
reset_button = tk.Button(window, text="Reset", command=reset_canvas)
reset_button.pack(side=tk.LEFT, padx=5)

# Bind mouse click event to the zoom function
canvas.bind("<Button-1>", zoom)  # Left mouse click for zooming

# Generate and display the Mandelbrot set initially
generate_and_display_mandelbrot(canvas)

# Start the Tkinter event loop
window.mainloop()

