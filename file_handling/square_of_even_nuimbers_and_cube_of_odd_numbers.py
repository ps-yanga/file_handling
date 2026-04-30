from datetime import datetime
from abc import ABC, abstractmethod


class MathOperation(ABC):
    """Abstract base class for mathematical operations."""

    @abstractmethod
    def apply(self, number):
        pass

    @abstractmethod
    def get_name(self):
        pass


class SquareOperation(MathOperation):
    """Square operation for even numbers."""

    def apply(self, number):
        return number ** 2

    def get_name(self):
        return "Square"


class CubeOperation(MathOperation):
    """Cube operation for odd numbers."""

    def apply(self, number):
        return number ** 3

    def get_name(self):
        return "Cube"


class ProcessedNumber:
    """Represents a number and its processed result."""

    def __init__(self, original, result, operation_name):
        self.original = original
        self.result = result
        self.operation = operation_name

    def __repr__(self):
        return f"{self.original} → {self.result} ({self.operation})"


class IntegerProcessor:
    """Process integers with mathematical operations."""

    def __init__(self, input_file, even_output_file, odd_output_file):
        self.input_file = input_file
        self.even_output_file = even_output_file
        self.odd_output_file = odd_output_file
        self.numbers = []
        self.processed_even = []
        self.processed_odd = []
        self.statistics = {}
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def read_integers(self):
        """Read integers from file."""
        try:
            with open(self.input_file, 'r') as file:
                self.numbers = [int(line.strip()) for line in file if line.strip()]
            print(f"✓ Read {len(self.numbers)} integers from {self.input_file}")
            return True
        except FileNotFoundError:
            print(f"✗ File {self.input_file} not found!")
            return False
        except ValueError:
            print("✗ Invalid integer format in file!")
            return False

    def process_numbers(self):
        """Process even and odd numbers with their operations."""
        square_op = SquareOperation()
        cube_op = CubeOperation()

        for num in self.numbers:
            if num % 2 == 0:
                result = square_op.apply(num)
                self.processed_even.append(ProcessedNumber(num, result, square_op.get_name()))
            else:
                result = cube_op.apply(num)
                self.processed_odd.append(ProcessedNumber(num, result, cube_op.get_name()))

        print(f"✓ Processed {len(self.processed_even)} even numbers")
        print(f"✓ Processed {len(self.processed_odd)} odd numbers")

    def calculate_statistics(self):
        """Calculate statistics for processed numbers."""
        even_results = [p.result for p in self.processed_even]
        odd_results = [p.result for p in self.processed_odd]

        self.statistics = {
            'total_even': len(self.processed_even),
            'total_odd': len(self.processed_odd),
            'sum_even_squares': sum(even_results) if even_results else 0,
            'sum_odd_cubes': sum(odd_results) if odd_results else 0,
            'avg_even_square': sum(even_results) / len(even_results) if even_results else 0,
            'avg_odd_cube': sum(odd_results) / len(odd_results) if odd_results else 0,
            'max_even_square': max(even_results) if even_results else 0,
            'max_odd_cube': max(odd_results) if odd_results else 0,
        }

    def save_results(self):
        """Save processed numbers to output files."""
        try:
            with open(self.even_output_file, 'w') as file:
                file.write(f"# Squares of Even Numbers (Generated: {self.timestamp})\n")
                file.write(f"# Total: {len(self.processed_even)}\n\n")
                for processed in self.processed_even:
                    file.write(f"{processed.original}² = {processed.result}\n")
            print(f"✓ Saved even squares to {self.even_output_file}")

            with open(self.odd_output_file, 'w') as file:
                file.write(f"# Cubes of Odd Numbers (Generated: {self.timestamp})\n")
                file.write(f"# Total: {len(self.processed_odd)}\n\n")
                for processed in self.processed_odd:
                    file.write(f"{processed.original}³ = {processed.result}\n")
            print(f"✓ Saved odd cubes to {self.odd_output_file}")
        except IOError as e:
            print(f"✗ Error saving files: {e}")
            return False
        return True

    def display_summary(self):
        """Display processing summary."""
        print("\n" + "=" * 70)
        print("INTEGER PROCESSING SUMMARY")
        print("=" * 70)
        print(f"\nINPUT: {self.input_file}")
        print(f"Total Numbers Processed: {len(self.numbers)}")

        print(f"\nEVEN NUMBERS (Squared):")
        print(f"  Count: {self.statistics['total_even']}")
        print(f"  Sum of Squares: {self.statistics['sum_even_squares']}")
        print(f"  Average Square: {self.statistics['avg_even_square']:.2f}")
        print(f"  Maximum Square: {self.statistics['max_even_square']}")
        print(f"  Output File: {self.even_output_file}")

        print(f"\nODD NUMBERS (Cubed):")
        print(f"  Count: {self.statistics['total_odd']}")
        print(f"  Sum of Cubes: {self.statistics['sum_odd_cubes']}")
        print(f"  Average Cube: {self.statistics['avg_odd_cube']:.2f}")
        print(f"  Maximum Cube: {self.statistics['max_odd_cube']}")
        print(f"  Output File: {self.odd_output_file}")

        print(f"\nTIMESTAMP: {self.timestamp}")
        print("=" * 70 + "\n")

    def run(self):
        """Execute the complete processing pipeline."""
        if not self.read_integers():
            return False

        self.process_numbers()
        self.calculate_statistics()

        if not self.save_results():
            return False

        self.display_summary()
        return True


if __name__ == "__main__":
    processor = IntegerProcessor(
        input_file="numbers.txt",
        even_output_file="even_squares.txt",
        odd_output_file="odd_cubes.txt"
    )
    processor.run()