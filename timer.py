import platform
import tkinter as tk
from tkinter import messagebox


class CountdownTimer:
    def __init__(self, master):
        """
        Initializes the Countdown Timer with UI elements and default settings.

        :param master: The root Tkinter window object.
        """
        # Main window setup
        self.master = master
        self.master.overrideredirect(True)  # Remove the title bar for a clean interface
        self.master.title("Countdown Timer")  # Set the window title
        self.master.geometry("-150+100")  # Set window dimensions and position
        self.master.resizable(False, False)  # Disable window resizing

        # Initialize variables for window dragging
        self.x_offset = 100  # Default horizontal offset
        self.y_offset = 100  # Default vertical offset

        # Pin window on top initially
        self.master.wm_attributes("-topmost", 1)  # Keep the window always on top
        self.is_pinned = True  # Track the pinned state of the window

        # Bind mouse events for dragging the window
        self.master.bind("<Button-1>", self.start_drag)  # Start drag on mouse button press
        self.master.bind("<B1-Motion>", self.do_drag)  # Perform drag on mouse movement

        # Initialize timer settings
        self.default_time = 60 * 5  # Default countdown time in seconds (5 minutes)
        self.time_left = self.default_time  # Remaining time for the countdown
        self.running = False  # Flag to track if the timer is running

        # Input frame for timer configuration
        self.input_frame = tk.Frame(self.master)  # Container for input widgets
        self.input_frame.pack(padx=10, pady=10)  # Add padding around the frame

        # Timer input label
        self.time_input_label = tk.Label(self.input_frame, text="Set Timer (HH:MM:SS)", font=("Helvetica", 10))
        self.time_input_label.grid(row=0, column=0, padx=5)  # Place label in grid layout

        # Hour spinbox
        self.hour_spinbox = tk.Spinbox(self.input_frame, from_=0, to=999, width=5, font=("Helvetica", 10))
        self.hour_spinbox.grid(row=0, column=1, padx=1)  # Place hour spinbox

        # Minute spinbox
        self.minute_spinbox = tk.Spinbox(self.input_frame, from_=0, to=59, width=3, font=("Helvetica", 10))
        self.minute_spinbox.grid(row=0, column=2, padx=1)  # Place minute spinbox

        # Second spinbox
        self.second_spinbox = tk.Spinbox(
            self.input_frame, from_=0, to=59, width=3, font=("Helvetica", 10))
        self.second_spinbox.grid(row=0, column=3, padx=1)  # Place second spinbox

        # Add mouse scroll functionality to spinboxes
        self.bind_scroll_to_spinbox(self.hour_spinbox)
        self.bind_scroll_to_spinbox(self.minute_spinbox)
        self.bind_scroll_to_spinbox(self.second_spinbox)

        # Timer display label
        self.timer_label = tk.Label(self.master, text=self.format_time(0, 0, self.default_time), font=("Helvetica", 32))
        self.timer_label.pack(pady=10)  # Add padding below the timer label

        # Button frame for control buttons
        self.button_frame = tk.Frame(self.master)  # Container for control buttons
        self.button_frame.pack(padx=10, pady=10)  # Add padding around the button frame

        # Create and place control buttons
        self.set_button = self.create_button("Set", self.set_custom_time)
        self.set_button.grid(row=0, column=0, padx=1)

        self.start_button = self.create_button("Start", self.start_timer)
        self.start_button.grid(row=0, column=1, padx=1)

        self.pause_button = self.create_button("Pause", self.pause_timer)
        self.pause_button.grid(row=0, column=2, padx=1)

        self.reset_button = self.create_button("Reset", self.reset_timer)
        self.reset_button.grid(row=0, column=3, padx=1)

        self.theme_button = self.create_button("🎨", self.toggle_theme)
        self.theme_button.grid(row=0, column=4, padx=1)

        # Pin button for toggling "always on top" behavior
        self.pin_button = self.create_button("📌", self.toggle_pin)
        self.pin_button.grid(row=0, column=5, padx=1)
        self.pin_button.config(bg="#00cc66")  # Indicate pinned state (active) with a light color

        # Exit button to close the application
        self.exit_button = self.create_button("✖", lambda: self.master.quit())
        self.exit_button.grid(row=0, column=6, padx=1)

        # Initialize theme (default is dark)
        self.current_theme = "dark"
        self.apply_theme()

    @property
    def version(self):
        """
        :return: str - Returns the version of the CountdownTimer class.
        """
        return "v1.1"

    @staticmethod
    def bind_scroll_to_spinbox(spinbox):
        """
        Bind mouse scroll to change the value of a spinbox.

        :param spinbox: The Tkinter Spinbox widget to which the scroll event will be bound.
        """

        def on_mouse_wheel(event):
            """
            Handles the mouse scroll event to increment or decrement the spinbox value.

            :param event: The Tkinter event object containing details about the scroll action.
            """
            if event.delta > 0:  # If scrolled up
                spinbox.invoke('buttonup')  # Increment the spinbox value
            else:  # If scrolled down
                spinbox.invoke('buttondown')  # Decrement the spinbox value

        # Bind the mouse scroll event to the custom handler
        spinbox.bind("<MouseWheel>", on_mouse_wheel)

    @staticmethod
    def format_time(hours, minutes, seconds):
        """
        Converts hours, minutes, and seconds into a formatted string HH:MM:SS.

        :param hours: The number of hours (int).
        :param minutes: The number of minutes (int).
        :param seconds: The number of seconds (int).
        :return: Formatted time as a string in HH:MM:SS format.
        """
        # Convert all time components into total seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds

        # Calculate hours, minutes, and seconds from total seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Format the time string with leading zeros for readability
        return f"{hours:03}:{minutes:02}:{seconds:02}"

    def create_button(self, text, command):
        """
        Creates a button with specific styling, rounded corners, and a hover effect.

        :param text: The text to display on the button (str).
        :param command: The function to execute when the button is clicked (callable).
        :return: The configured Button widget.
        """
        # Create a button with the specified text, font, and command
        button = tk.Button(self.button_frame, text=text, font=("Helvetica", 12), command=command, relief="flat")

        # Configure the button's appearance
        button.config(
            bg="#555555",  # Background color
            fg="#333333",  # Foreground (text) color
            activebackground="#888888",  # Background color when hovered
            activeforeground="black"  # Text color when hovered
        )

        return button  # Return the created and configured button

    def start_drag(self, event):
        """
        Records the initial mouse position when the user starts dragging the window.

        :param event: The event object containing the x and y coordinates of the mouse.
        """
        # Store the x and y offsets relative to the window's position
        self.x_offset = event.x
        self.y_offset = event.y

    def do_drag(self, event):
        """
        Moves the window based on the current mouse position during dragging.

        :param event: The event object containing the current x and y coordinates of the mouse.
        """
        # Calculate the new x-coordinate for the window
        x = self.master.winfo_x() - self.x_offset + event.x
        # Calculate the new y-coordinate for the window
        y = self.master.winfo_y() - self.y_offset + event.y
        # Update the window's position using the calculated coordinates
        self.master.geometry(f"+{x}+{y}")

    def update_timer(self):
        """
        Updates the countdown timer every second.

        - If the timer is running, it decrements the time by 1 second and updates the display.
        - When the timer reaches 0, it stops, plays a sound, and displays a "Time's Up!" alert.

        This method is recursively scheduled using `after` for continuous updates.
        """
        if self.running and self.time_left > 0:
            # Decrease the remaining time by 1 second
            self.time_left -= 1

            # Calculate hours, minutes, and seconds from remaining time
            hours, remainder = divmod(self.time_left, 3600)
            minutes, seconds = divmod(remainder, 60)

            # Update the timer display with the formatted time
            self.timer_label.config(text=self.format_time(hours, minutes, seconds))

            # Schedule the next update in 1 second
            self.master.after(1000, self.update_timer)
        elif self.time_left == 0:
            # Stop the timer when time runs out
            self.running = False

            # Update the label to indicate time is up
            self.timer_label.config(text="Time's Up!")

            # Windows only: winsound and messagebox works on Windows os only
            if platform.system() == "Windows":

                # Show a popup message to alert the user
                messagebox.showinfo("Timer Alert", "Time's Up!")

    def start_timer(self):
        """
        Starts or resumes the countdown timer.

        - If the timer is not running, it checks for custom time input.
        - If a custom time is set, it initializes the timer with that value.
        - Otherwise, it resumes from the default time.

        The `update_timer` method is called to begin the countdown process.
        """
        if not self.running:
            # Set the timer to running state
            self.running = True

            # Call the update_timer method to start the countdown
            self.update_timer()

    def pause_timer(self):
        """
        Pauses the countdown timer.

        - Sets the `running` attribute to `False` to stop the countdown.
        - The timer can be resumed later by calling the `start_timer` method.
        """
        self.running = False  # Stop the countdown by changing the running state to False

    def reset_timer(self):
        """
        Resets the timer to the default time (5 minutes).

        - Stops the countdown by setting `self.running` to `False`.
        - Resets the time to the default value (`self.default_time`).
        - Updates the timer display to show the default time in HH:MM:SS format.
        """
        self.running = False  # Stop the countdown by setting the running state to False
        self.time_left = self.default_time  # Reset the time to the default value (5 minutes)
        hours, remainder = divmod(self.default_time, 3600)  # Convert total seconds to hours, minutes
        minutes, seconds = divmod(remainder, 60)  # Convert remaining seconds to minutes and seconds
        self.timer_label.config(text=self.format_time(hours, minutes, seconds))  # Update the timer display

    def set_custom_time(self):
        """
        Sets a custom countdown time based on user input from spinboxes for HH, MM, and SS.

        - Retrieves the time values from the spinboxes (HH, MM, SS).
        - Converts the input into total seconds and updates the timer's remaining time (`self.time_left`).
        - Updates the timer display with the new time without starting the countdown.
        - If the user input is invalid, it displays an error message.
        """
        try:
            # Retrieve values from the spinboxes and convert them to integers
            hours = int(self.hour_spinbox.get())  # Get hours input
            minutes = int(self.minute_spinbox.get())  # Get minutes input
            seconds = int(self.second_spinbox.get())  # Get seconds input

            # Convert custom time to total seconds
            self.time_left = hours * 3600 + minutes * 60 + seconds
            self.default_time = self.time_left  # Update the default time to the custom time
            self.timer_label.config(text=self.format_time(hours, minutes, seconds))  # Update the display

        except ValueError:
            # Handle invalid input (non-integer or empty values)
            messagebox.showerror("Invalid Input", "Please enter valid time values.")

    def apply_theme(self):
        """
        Applies the current theme (light or dark) to the app.

        - Changes background (`bg`) and foreground (`fg`) colors of various widgets to match the selected theme.
        - If the theme is light, it sets lighter colors; for dark theme, it applies darker colors.
        """
        if self.current_theme == "light":
            # Apply light theme: white background with black text
            self.master.config(bg="white")  # Set main window background to white
            self.timer_label.config(bg="white", fg="black")  # Timer label background to white and text to black
            self.time_input_label.config(bg="white", fg="black")  # Set label colors for input section
            # Set background color for input and button frames
            self.input_frame.config(bg="white")
            self.button_frame.config(bg="white")
            # Update button colors for light theme
            buttons = [self.set_button, self.start_button, self.pause_button, self.reset_button, self.theme_button,
                       self.exit_button]
            for button in buttons:
                button.config(bg="lightgray", fg="black")  # Light gray button with black text

        elif self.current_theme == "dark":
            # Apply dark theme: dark background with white text
            self.master.config(bg="#333333")  # Set main window background to dark gray
            self.timer_label.config(bg="#333333", fg="white")  # Timer label text to white on dark gray
            self.time_input_label.config(bg="#333333", fg="white")  # Label colors for input section
            # Set background color for input and button frames
            self.input_frame.config(bg="#333333")
            self.button_frame.config(bg="#333333")
            # Update button colors for dark theme
            buttons = [self.set_button, self.start_button, self.pause_button, self.reset_button, self.theme_button,
                       self.exit_button]
            for button in buttons:
                button.config(bg="#555555", fg="white")  # Darker gray button with white text

    def toggle_theme(self):
        """
        Switches between light and dark themes.

        This method toggles the theme when the user clicks the "Switch Theme" button.
        It checks the current theme and switches to the opposite one, then applies the changes.
        """
        if self.current_theme == "light":
            # Change to dark theme
            self.current_theme = "dark"
        else:
            # Change to light theme
            self.current_theme = "light"

        # Apply the updated theme
        self.apply_theme()

    def toggle_pin(self):
        """
        Toggles the 'always on top' behavior of the window.

        When pinned, the window remains on top of other windows.
        When unpinned, it can be behind other windows.
        This method updates the window's attribute and the pin button's color accordingly.
        """
        if self.is_pinned:
            # Disable always on top behavior
            self.master.wm_attributes("-topmost", 0)
            self.is_pinned = False
            # Optionally change the button color to indicate unpinned state (deactivate)
            self.pin_button.config(bg="#990000")
        else:
            # Enable always on top behavior
            self.master.wm_attributes("-topmost", 1)
            self.is_pinned = True
            # Change the button color to indicate pinned state (active)
            self.pin_button.config(bg="#00cc66")


def main():
    """Main function to start the application."""
    root = tk.Tk()
    countdown = CountdownTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
