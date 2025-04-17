# base_model.py
# This is a reusable base class for any module that deals with reading from or writing to files.
# Both the Scraper and SentimentAnalyzer will inherit from this class to avoid repeating common code.

class BaseModel:
    def __init__(self, input_file_path, output_file_path):
        """
        Constructor method that sets up input and output file paths.

        Parameters:
        - input_file_path (str): File path where the class should read input data (e.g., scraped headlines).
        - output_file_path (str): File path where the class should save output data (e.g., sentiments).
        """
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def read_input_file(self):
        """
        Reads content from the input file line by line.

        Returns:
        - A list of strings, where each string is a line from the file (i.e., a headline).
        - It also removes any newline characters at the end of each line using strip().
        """
        with open(self.input_file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]

    def write_output_file(self, lines):
        """
        Writes a list of strings (lines) to the output file, one per line.

        Parameters:
        - lines (list of str): Each item in the list is written as a separate line in the file.
        """
        with open(self.output_file_path, 'w') as file:
            for line in lines:
                file.write(line + '\n')  # Adds a newline character at the end of each line

    def process(self):
        """
        A placeholder method that is meant to be implemented by child classes.

        This method will be overridden by:
        - The Scraper class (to handle scraping and saving headlines)
        - The SentimentAnalyzer class (to read headlines and generate sentiments)

        If a subclass does not override this method, running it will raise an error.
        """
        raise NotImplementedError("Subclasses must implement this method.")
