import winsound
import time
from melodies import *


class Player:
    """
    A class to represent a music player that plays melodies using frequency and duration data.

    This class allows for the creation of custom melodies or the use of a default alert melody.
    The melody is played by iterating over its notes, where each note is represented by a frequency and duration.
    """

    def __init__(self, melody=None):
        """
        Initialize the Player with a melody.

        :param melody: A dictionary containing:
            - 'name': (str) The name of the melody.
            - 'notes': (list of tuples) Each tuple contains:
                - freq: (int) Frequency in Hz (0 for pauses).
                - duration: (int) Duration in milliseconds.

        :raises ValueError: If the melody is not properly formatted or is missing required keys ('name' or 'notes').

        The constructor sets the melody to a default alert melody if no valid melody is provided.
        It also calculates the total duration of the melody based on the sum of individual note durations.
        """
        # If no melody is provided or if the provided melody is not properly formatted,
        # set the melody to the default alert melody.
        if melody is None or 'name' not in melody or 'notes' not in melody:
            melody = self.alert

        # Assign the melody name and notes to the instance attributes
        self.name = melody['name']
        self.notes = melody['notes']

        # Calculate the total duration of the melody by summing up the durations of all notes
        self.duration = sum([d for f, d in self.notes])

    @property
    def version(self):
        """
        :return: str - Returns the version of the Player class.
        """
        return "v1.0"

    @property
    def alert(self):
        """
        Returns the default alert melody when no custom melody is provided.

        The alert melody consists of three short beep sounds (A5, 880 Hz), with pauses between each beep.
        The default melody is used for alerting the user when no custom melody is set.
        """
        return {
            "name": "High-Pitched Alert",
            "notes": [
                (880, 200),  # A5, 200ms
                (0, 100),  # Rest, 100ms
                (880, 200),  # A5, 200ms
                (0, 100),  # Rest, 100ms
                (880, 200),  # A5, 200ms
            ]
        }

    def play(self):
        """
        Play the melody stored in the Player instance.

        This method iterates through each note in the melody:
            - If the frequency is 0, it pauses for the specified duration.
            - Otherwise, it plays the sound at the given frequency for the specified duration.

        The method prints the name of the melody and its total duration in seconds.
        If there are no notes, it prints "No melody to play!" and exits.
        """
        # If there are no notes, print a message and stop
        if not self.notes:
            print("No melody to play!")
            return

        # Display the name of the melody and its total duration in seconds
        print(f"Playing: \"{self.name}\" in {self.duration / 1000}sec\n")

        # Loop through each note and play it
        for freq, duration in self.notes:
            if freq == 0:  # If the frequency is 0, it's a pause
                time.sleep(duration / 1000.0)  # Convert ms to seconds for the pause
            else:
                winsound.Beep(freq, duration)  # Play the note at the specified frequency and duration
