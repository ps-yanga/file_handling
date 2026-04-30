from datetime import datetime

class TextLine:
    """Represents a single line of text with metadata."""

    def __init__(self, content, line_number):
        self.content = content
        self.line_number = line_number
        self.timestamp = datetime.now()
        self.length = len(content)
        self.word_count = len(content.split())

    def __repr__(self):
        return f"Line {self.line_number}: {self.content}"


class TextFileWriter:
    """Advanced text file writer with formatting options."""

    def __init__(self, filename, add_line_numbers=True, add_timestamps=False):
        self.filename = filename
        self.add_line_numbers = add_line_numbers
        self.add_timestamps = add_timestamps
        self.lines = []
        self.statistics = {}

    def add_line(self, content):
        """Add a line to the file."""
        if not content.strip():
            print("⚠ Warning: Empty line ignored")
            return False

        line = TextLine(content, len(self.lines) + 1)
        self.lines.append(line)
        return True

    def interactive_input(self):
        """Get lines interactively from user."""
        print("\n" + "=" * 60)
        print("TEXT FILE WRITER - INTERACTIVE MODE")
        print("=" * 60)
        print("(Empty lines will be ignored)\n")

        while True:
            line_content = input(f"Enter line {len(self.lines) + 1}: ")

            if self.add_line(line_content):
                response = input("Are there more lines? (y/n): ").lower()
                if response != 'y':
                    break

        print(f"\n✓ Total lines entered: {len(self.lines)}")

    def format_line_for_file(self, line):
        """Format a line according to settings."""
        formatted = ""

        if self.add_line_numbers:
            formatted += f"[{line.line_number:3d}] "

        formatted += line.content

        if self.add_timestamps:
            formatted += f" [{line.timestamp.strftime('%H:%M:%S')}]"

        return formatted

    def calculate_statistics(self):
        """Calculate file statistics."""
        if not self.lines:
            return

        all_words = []
        for line in self.lines:
            all_words.extend(line.content.split())

        self.statistics = {
            'total_lines': len(self.lines),
            'total_characters': sum(line.length for line in self.lines),
            'avg_line_length': sum(line.length for line in self.lines) / len(self.lines),
            'longest_line': max(self.lines, key=lambda l: l.length).length,
            'shortest_line': min(self.lines, key=lambda l: l.length).length,
            'total_words': sum(line.word_count for line in self.lines),
            'avg_words_per_line': sum(line.word_count for line in self.lines) / len(self.lines),
            'unique_words': len(set(all_words)),
        }

    def save(self):
        """Save all lines to file."""
        try:
            with open(self.filename, 'w') as file:
                for line in self.lines:
                    formatted_line = self.format_line_for_file(line)
                    file.write(formatted_line + '\n')

            self.calculate_statistics()
            print(f"\n✓ File saved: {self.filename}")
            self.display_statistics()
            return True
        except IOError as e:
            print(f"✗ Error saving file: {e}")
            return False

    def display_statistics(self):
        """Display file statistics."""
        if not self.statistics:
            return

        print("\n" + "=" * 60)
        print("FILE STATISTICS")
        print("=" * 60)
        print(f"Total Lines: {self.statistics['total_lines']}")
        print(f"Total Characters: {self.statistics['total_characters']}")
        print(f"Average Line Length: {self.statistics['avg_line_length']:.1f}")
        print(f"Longest Line: {self.statistics['longest_line']} characters")
        print(f"Shortest Line: {self.statistics['shortest_line']} characters")
        print(f"Total Words: {self.statistics['total_words']}")
        print(f"Average Words per Line: {self.statistics['avg_words_per_line']:.1f}")
        print(f"Unique Words: {self.statistics['unique_words']}")
        print("=" * 60 + "\n")

    def display_preview(self):
        """Display preview of file content."""
        print("\n" + "=" * 60)
        print("FILE PREVIEW")
        print("=" * 60)
        for line in self.lines:
            print(self.format_line_for_file(line))
        print("=" * 60 + "\n")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PROJECT 3: ADVANCED TEXT FILE WRITER")
    print("=" * 60)

    writer = TextFileWriter('my_text.txt', add_line_numbers=True, add_timestamps=False)
    writer.interactive_input()
    writer.display_preview()
    writer.save()
