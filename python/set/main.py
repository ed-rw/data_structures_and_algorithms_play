from impl import Unsigned16BitIntSet

def main():
    s = Unsigned16BitIntSet()

    values_to_add = [4, 100, 0, 65536]
    print(f"Adding values: {values_to_add}")
    for value in values_to_add:
        s.add(value)

    print(f"contains 2: {s.contains(2)}")
    print(f"contains 4: {s.contains(4)}")
    print(f"contains 0: {s.contains(0)}")
    print(f"contains 65536: {s.contains(65536)}")
    print(f"contains 101: {s.contains(101)}")

    s.add(4)
    print(f"contains 4 after adding again: {s.contains(4)}")

    s.remove(4)
    print(f"contains 4, after removal: {s.contains(4)}")

if __name__ == '__main__':
    main()
