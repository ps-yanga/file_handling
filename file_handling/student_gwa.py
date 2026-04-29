from datetime import datetime


class Student:
    """Represents a student with name and GWA."""

    def __init__(self, name, gwa):
        self.name = name
        self.gwa = float(gwa)
        self.rank = None

    def __repr__(self):
        return f"Student({self.name}, GWA: {self.gwa})"

    def __eq__(self, other):
        return self.gwa == other.gwa

    def __lt__(self, other):
        return self.gwa > other.gwa

    def is_honor_student(self, threshold=1.5):
        """Check if student is an honor student."""
        return self.gwa <= threshold


class GWAAnalyzer:
    """Analyze student GWA data."""

    def __init__(self, input_file):
        self.input_file = input_file
        self.students = []
        self.report_file = f"gwa_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    def read_students(self):
        """Read student data from file."""
        try:
            with open(self.input_file, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        name = parts[0].strip()
                        gwa = parts[1].strip()
                        self.students.append(Student(name, gwa))
            print(f"✓ Loaded {len(self.students)} students")
        except FileNotFoundError:
            print(f"✗ File {self.input_file} not found!")
            raise
        except ValueError as e:
            print(f"✗ Invalid GWA format - {e}")
            raise

    def calculate_rankings(self):
        """Calculate rankings based on GWA."""
        sorted_students = sorted(self.students)
        for rank, student in enumerate(sorted_students, 1):
            student.rank = rank

    def get_highest_gwa_student(self):
        """Get student with highest GWA (lowest number)."""
        return min(self.students, key=lambda s: s.gwa)

    def get_lowest_gwa_student(self):
        """Get student with lowest GWA (highest number)."""
        return max(self.students, key=lambda s: s.gwa)

    def get_honor_students(self, threshold=1.5):
        """Get all honor students."""
        return [s for s in self.students if s.is_honor_student(threshold)]

    def get_average_gwa(self):
        """Calculate average GWA."""
        if not self.students:
            return 0
        return sum(s.gwa for s in self.students) / len(self.students)

    def display_top_students(self, top_n=5):
        """Display top N students."""
        sorted_students = sorted(self.students)
        print(f"\n{'=' * 60}")
        print(f"TOP {top_n} STUDENTS BY GWA")
        print(f"{'=' * 60}")
        print(f"{'Rank':<6} {'Name':<25} {'GWA':<10} {'Status':<15}")
        print(f"{'-' * 60}")
        for student in sorted_students[:top_n]:
            status = "Honor Student" if student.is_honor_student() else "Regular"
            print(f"{student.rank:<6} {student.name:<25} {student.gwa:<10.2f} {status:<15}")
        print(f"{'=' * 60}\n")

    def generate_full_report(self):
        """Generate a comprehensive report."""
        self.calculate_rankings()
        report_lines = ["=" * 70, "STUDENT GWA ANALYSIS REPORT",
                        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", "=" * 70, "",
                        "SUMMARY STATISTICS", f"Total Students: {len(self.students)}",
                        f"Average GWA: {self.get_average_gwa():.2f}",
                        f"Highest GWA: {self.get_highest_gwa_student().gwa:.2f} ({self.get_highest_gwa_student().name})",
                        f"Lowest GWA: {self.get_lowest_gwa_student().gwa:.2f} ({self.get_lowest_gwa_student().name})",
                        f"Honor Students: {len(self.get_honor_students())}", "", "TOP 10 STUDENTS",
                        f"{'Rank':<6} {'Name':<30} {'GWA':<10}", "-" * 70]

        for student in sorted(self.students)[:10]:
            report_lines.append(f"{student.rank:<6} {student.name:<30} {student.gwa:<10.2f}")
        report_lines.append("")

        report_lines.append("HONOR STUDENTS (GWA <= 1.5)")
        report_lines.append(f"{'Name':<30} {'GWA':<10}")
        report_lines.append("-" * 70)
        for student in sorted(self.get_honor_students()):
            report_lines.append(f"{student.name:<30} {student.gwa:<10.2f}")

        report_lines.append("=" * 70)

        with open(self.report_file, 'w') as file:
            file.write('\n'.join(report_lines))

        print('\n'.join(report_lines))
        print(f"\n✓ Report saved to {self.report_file}")


if __name__ == "__main__":
    analyzer = GWAAnalyzer('students.txt')
    analyzer.read_students()
    analyzer.display_top_students(5)
    analyzer.generate_full_report()
