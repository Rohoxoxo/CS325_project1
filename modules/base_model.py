# This is a base class to define the common behavior for any model (e.g., scraping, sentiment analysis, etc.)
# It will act like a "template" class that other modules (like scraper or sentiment analyzer) can inherit from.

class BaseModel:
    def __init__(self, input_file_path, output_file_path):
        """
        Initializes the base model with input and output file paths.

        :param input_file_path: Path to the file that contains input data
        :param output_file_path: Path to the file where output will be saved
        """
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def read_input_file(self):
        """
        Reads lines from the input file and returns them as a list.

        :return: List of lines (strings) from the input file
        """
        with open(self.input_file_path, 'r') as file:
            lines = file.readlines()
            # Strip newline characters and return list of cleaned lines
            return [line.strip() for line in lines]

    def write_output_file(self, lines):
        """
        Writes a list of lines to the output file.

        :param lines: List of strings to write to the file
        """
        with open(self.output_file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')

    def process(self):
        """
        A placeholder method that should be overridden in child classes.
        """
        raise NotImplementedError("Subclasses must implement this method.")
