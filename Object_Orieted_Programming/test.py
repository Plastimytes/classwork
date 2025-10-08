import datetime

class VisitorTracker:
    """Stores only the latest visitor entry in a dictionary."""

    def __init__(self):
        # Stores the latest visitor entry: {'StudentID': {details...}}
        self.latest_entry = {}

# ---------------------------------
## Private Validation Method
# ---------------------------------
    def __validate_name(self, name):
        """
        Validates that names contain only letters and spaces using a loop 
        and string methods (no 're' module).
        """
        stripped_name = name.strip()
        
        # 1. Check for empty string
        if not stripped_name:
            raise ValueError("Invalid Name: Name cannot be empty.")
            
        # 2. Check each character
        for char in stripped_name:
            # The isalpha() method checks for letters (a-z, A-Z)
            if not char.isalpha() and char != ' ':
                raise ValueError(f"Invalid Name: '{stripped_name}'. Names must contain only letters and spaces.")
                
        return stripped_name

# ---------------------------------
## Required Methods
# ---------------------------------
    def record(self, student_id, name, hostel_name):
        """Records a new visitor entry, overwriting any previous entry."""
        try:
            validated_name = self.__validate_name(name)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Store the entry
            self.latest_entry[student_id] = {
                'name': validated_name,
                'hostel': hostel_name,
                'timestamp': timestamp
            }

            # Print the required audit line
            print(f"AUDIT | ID: {student_id} | HOSTEL: {hostel_name} | TIME: {timestamp} | ACTION: RECORDED")

        except ValueError as e:
            # Handle the exception for invalid name
            print(f"--- EXCEPTION HANDLED ---")
            print(f"ERROR: Cannot record entry. {e}")
            
    def update(self, student_id, new_hostel_name):
        """Updates the hostel name and timestamp for an existing entry."""
        if student_id not in self.latest_entry:
            print(f"ERROR: Student ID {student_id} not found. Cannot update.")
            return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Update the specific details
        self.latest_entry[student_id]['hostel'] = new_hostel_name
        self.latest_entry[student_id]['timestamp'] = timestamp

        # Print the required audit line
        print(f"AUDIT | ID: {student_id} | HOSTEL: {new_hostel_name} | TIME: {timestamp} | ACTION: UPDATED")

    def show_line(self, student_id):
        """Retrieves and prints the latest entry for a given StudentID."""
        entry = self.latest_entry.get(student_id)
        if entry:
            print("\n--- LATEST ENTRY ---")
            print(f"ID: {student_id} | Name: {entry['name']} | Hostel: {entry['hostel']} | Time: {entry['timestamp']}")
            print("--------------------\n")
        else:
            print(f"No entry found for Student ID: {student_id}")

# ---------------------------------
## Demonstration
# ---------------------------------
if __name__ == "__main__":
    tracker = VisitorTracker()

    # 1. Valid Record
    tracker.record("S101", "  Peter Jones  ", "Block Alpha")
    
    # 2. Invalid Record (Triggers Exception due to number)
    tracker.record("S102", "Jane123 Doe", "Block Beta")

    # 3. Valid Record
    tracker.record("S103", "Mary Anne", "Block Gamma")

    # 4. Update
    tracker.update("S101", "Block Delta")

    # 5. Show
    tracker.show_line("S101")
    tracker.show_line("S102")