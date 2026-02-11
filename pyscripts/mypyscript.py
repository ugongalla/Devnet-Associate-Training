# Simple Hello World program
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

def main():
    """Main function."""
    print(greet("World"))
    print(f"2 + 3 = {add(2, 3)}")

if __name__ == "__main__":
    main()