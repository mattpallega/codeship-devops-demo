# Import the Add function, and assert that it works correctly.
from main import Add

def TestAdd():
        assert Add(9,7) == 16
        print("Add Function works correctly")

if __name__ == '__main__':
        TestAdd()