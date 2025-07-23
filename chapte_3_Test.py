devices = []  # Global list to store smart_phone objects

class smart_phone:
    def __init__(self, type, size, color):
        self.type = type      # Phone type (e.g., Android, iPhone)
        self.size = size      # Phone size (e.g., 60, 70, etc.)
        self.color = color    # Phone color

    def string(self):
        # String representation for printing the object
        return f"type: {self.type} size: {self.size} color: {self.color}"

def get_divice():
    global devices
    # Create a list of smart_phone objects and assign to devices
    devices = [
        smart_phone("Android", 60, "red"),
        smart_phone("iPhone", 50, "blue"),
        smart_phone("Android", 70, "white"),
        smart_phone("Android", 50, "black"),
        smart_phone("Android", 60, "purple"),
        smart_phone("iPhone", 60, "black"),
        smart_phone("Android", 50, "green"),
        smart_phone("iPhone", 70, "yellow"),
        smart_phone("iPhone", 80, "purple"),
        smart_phone("Android", 60, "yellow")
    ]

def outcome():
    global devices
    get_divice()  # Populate the devices list
    for i in devices:
        print(i.string())  # Print each smart_phone object

outcome()  # Run the outcome function to