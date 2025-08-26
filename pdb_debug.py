import pdb

def add(a, b):
    return a + b

def main():
    x = 2
    y = 3
    pdb.set_trace()  # Start debugging
    result = add(x, y)
    print(f"Sum: {result}")

if __name__ == "__main__":
    main()
