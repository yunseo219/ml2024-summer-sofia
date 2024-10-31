from module5_mod import NumberTracker

def main():
    tracker = NumberTracker()
    n = tracker.get_N()
    tracker.get_numbers(n)
    x = tracker.get_X()
    result = tracker.find_X(x)
    if result == -1:
        print("-1")
    else:
        print(f"Index of {x} is found at the position: #{result}")

if __name__ == "__main__":
    main()
