
def mandelbrot_iterations(real, imaginary, max_iterations=100, threshold=100):
    c = complex(real, imaginary)
    z = complex(0, 0)
    count = 0

    while count < max_iterations and abs(z) < threshold:
        z = z * z + c
        count += 1

    return count if count < max_iterations else -1

def generate_mandelbrot_text(width, height, xl, xr, yu, yd):
    result = ""

    for y in range(height):
        for x in range(width):
            real = x * (xr - xl) / width + xl
            imaginary = y * (yu - yd) / height + yd

            iterations = mandelbrot_iterations(real, imaginary)

            result += ' ' if iterations == -1 else str(iterations % 10)

        result += '\n'

    return result

def main():
    width, height = 80, 40
    xl, xr = -2.5, 1.5
    yu, yd = 2, -2

    mandelbrot_text = generate_mandelbrot_text(width, height, xl, xr, yu, yd)

    print(mandelbrot_text)

if __name__ == "__main__":
    main()
