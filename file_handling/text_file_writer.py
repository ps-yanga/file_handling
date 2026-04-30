from datetime import datetime
import os

class TextLine:
    """Represents a single line in a text file."""

    def __init__(self, content, line_number):
        self.content = content
        self.line_number = line_number
        self.timestamp = datetime.now()
        self.length = len(content)

    def __repr__(self):
        return f'Line{self.line_number}: {self.content}'

    class TextFileWriter:
        """Advanced text file writer."""

        def __init__(self, filename, add_line_numbers=True, add_timestamp=False):
            self.filename = filename
            self.add_line_numbers = add_line_numbers
            self.add_timestamp = add_timestamp
            self.lines = []
            self.statistics={}

        def add_line(self, content):
            """Adds a line to the text file."""
            if not content.strip():
                print("Warning: Empty line")
                return False

            line=TextLine(content, len(self.lines)+1)
            self.lines.append(line)
            return True

        def interactive_input(self):
            """Format a line accoring to an interactive prompt."""
            formatted=""

            if self.add_line_numbers:
                formatted+=f"[{line.line_number:3d}]"

            formatted+=line.content
            if self.add_timestamp:
                formatted+=f"[{line.timestamp.strftime('%H:%M:%S')}]"

            return formatted

        def calculate_statistics(self):
            """Calculate statistics about the lines."""
            if not self.lines:
                return

            self.statistics={'total_lines': len(self.lines),   'total_characters': sum(line.length for line in self.lines),
                             'avg_line_length': sum(line.length for line in self.lines) / len(self.lines),
                             'longest_line': max(self.lines, key=lambda l: l.length).length,
                             'shortest_line': min(self.lines, key=lambda l: l.length).length,
                             'total_words': sum(len(line.content.split()) for line in self.lines),}
        def save(self):
            """Save the statistics to a text file."""
            try:
                with open(self.filename, 'w') as file:
                    for line in self.lines:
                        formatted_line=self.format_line_for_file(line)
                        file.write(formatted_line+'\n')
                self.calculate_statistics()
                print(f"\n File saved to {self.filename}")
                self.display_statistics()
            except FileNotFoundError:
                print("File not found.")
                raise
        def display_statistics(self):
            """Display statistics about the lines."""
            if not self.statistics:
                return

            print("\n" + "=" * 50)
            print("FILE STATISTICS")
            print("=" * 50)
            print(f"Total Lines: {self.statistics['total_lines']}")
            print(f"Total Characters: {self.statistics['total_characters']}")
            print(f"Average Line Length: {self.statistics['avg_line_length']:.1f}")
            print(f"Longest Line: {self.statistics['longest_line']} characters")
            print(f"Shortest Line: {self.statistics['shortest_line']} characters")
            print(f"Total Words: {self.statistics['total_words']}")
            print("=" * 50 + "\n")

        def display_preview(self):
            """Display preview of file content."""
            print("\n" + "=" * 50)
            print("FILE PREVIEW")
            print("=" * 50)
            for line in self.lines:
                print(self.format_line_for_file(line))
            print("=" * 50 + "\n")


class TextFileWriter:
    pass


if __name__ == "__main__":
    writer = TextFileWriter('my_text.txt', add_line_numbers=True, add_timestamps=False)
    writer.interactive_input()
    writer.display_preview()
    writer.save()
