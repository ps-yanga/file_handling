import os
from datetime import datetime

class NumberProcessor:
    """Process numbers from a file and separate them into even and odd files"""

    def _init_(self, input_file, even_file, odd_file, log_file=None):
        self.input_file = input_file
        self.even_file = even_file
        self.odd_file = odd_file
        self.log_file = log_file
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = []
        self.statistics={}

    def read_numbers(self):
        """Read the numbers from input file"""
        try:
            with open(self.input_file,'r') as file:
                self.numbers=[int(line.strip()) for line in file.readlines() if line.strip()]
                self.log(f"Successfully read {len(self.numbers)} numbers from {self.input_file}")
        except FileNotFoundError:
            self.log(f"Error: File {self.input_file} not found")
            raise
        except ValueError as e:
            self.log(f"Error: Invalid number format - {e}")
            raise

    def separate_numbers(self):
        """Split numbers into even and odd numbers"""
        self.even_numbers=[num for num in self.numbers if num%2==0]
        self.odd_numbers=[num for num in self.numbers if num%2!=0]
        self.log(f"Separated: {len(self.even_numbers)} even,{len(self.odd_numbers)} odd")


    def calculate_statistics(self):
        """Calculate statistics about the numbers."""
        if not self.numbers:
            return

        self.statistics = {
            'total_count': len(self.numbers),
            'even_count': len(self.even_numbers),
            'odd_count': len(self.odd_numbers),
            'sum_even': sum(self.even_numbers),
            'sum_odd': sum(self.odd_numbers),
            'avg_even': sum(self.even_numbers) / len(self.even_numbers) if self.even_numbers else 0,
            'avg_odd': sum(self.odd_numbers) / len(self.odd_numbers) if self.odd_numbers else 0,
            'min_even': min(self.even_numbers) if self.even_numbers else None,
            'max_even': max(self.even_numbers) if self.even_numbers else None,
            'min_odd': min(self.odd_numbers) if self.odd_numbers else None,
            'max_odd': max(self.odd_numbers) if self.odd_numbers else None,}

    def write_numbers(self):
        """Write separated numbers to output files."""
        try:
            with open(self.even_file, 'w') as file:
                for num in sorted(self.even_numbers):
                    file.write(str(num) + '\n')
            self.log(f"Wrote {len(self.even_numbers)} even numbers to {self.even_file}")

            with open(self.odd_file, 'w') as file:
                for num in sorted(self.odd_numbers):
                    file.write(str(num) + '\n')
            self.log(f"Wrote {len(self.odd_numbers)} odd numbers to {self.odd_file}")
        except IOError as e:
            self.log(f"ERROR: Failed to write files - {e}")
            raise

    def display_statistics(self):
        """Display statistics in a formatted way."""
        print("\n" + "=" * 50)
        print("NUMBER PROCESSING STATISTICS")
        print("=" * 50)
        print(f"Total Numbers: {self.statistics['total_count']}")
        print(f"Even Numbers: {self.statistics['even_count']}")
        print(f"Odd Numbers: {self.statistics['odd_count']}")
        print("\n--- EVEN NUMBERS ---")
        print(f"Sum: {self.statistics['sum_even']}")
        print(f"Average: {self.statistics['avg_even']:.2f}")
        print(f"Min: {self.statistics['min_even']}, Max: {self.statistics['max_even']}")
        print("\n--- ODD NUMBERS ---")
        print(f"Sum: {self.statistics['sum_odd']}")
        print(f"Average: {self.statistics['avg_odd']:.2f}")
        print(f"Min: {self.statistics['min_odd']}, Max: {self.statistics['max_odd']}")
        print("=" * 50 + "\n")

    def log(self, message):
        """Log messages to file and console."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(self.log_file, 'a') as file:
            file.write(log_message + '\n')

    def process(self):
        """Execute the complete processing workflow."""
        self.log("=== Processing started ===")
        self.read_numbers()
        self.separate_numbers()
        self.calculate_statistics()
        self.write_numbers()
        self.display_statistics()
        self.log("=== Processing completed ===\n")

if __name__ == "_main_":
    processor = NumberProcessor('numbers.txt', 'even.txt', 'odd.txt')
    processor.process()
