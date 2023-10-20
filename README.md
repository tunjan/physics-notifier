# Physics Facts Notifier

## Overview

This script sends you a notification containing an interesting physics fact every 15 minutes. The facts cover various areas in physics and range from fundamental principles to mind-boggling concepts.

## Prerequisites

- Python 3.x
- `plyer` package for notifications
- `schedule` package for scheduling tasks

Install the required Python packages using pip:

```bash
pip install plyer schedule
```

## Files Included

1. `main_script.py`: The main Python script that handles notifications.
2. `physics_facts.txt`: Text file containing the physics facts.
3. `icon_path.ico`: Icon file used for the notification. (Replace with your own icon file)

## How to Use

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies**: Navigate to the cloned repository's folder and install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

3. **Add Physics Facts**: Make sure `physics_facts.txt` is present in the same directory as `main_script.py`.

4. **Add Icon**: Place your desired `.ico` file in the directory and update its path in `main_script.py`.

    ```python
    app_icon='icon_path.ico'
    ```

5. **Run the Script**: Run `main_script.py` to start receiving notifications.

    ```bash
    python main_script.py
    ```

6. **Stop the Script**: To stop receiving notifications, terminate the script by pressing `Ctrl+C` in the terminal.

## Customization

- **Update Physics Facts**: You can add or remove facts in `physics_facts.txt`. Each fact should be on a new line.
- **Change Notification Time**: The notification interval is set to 15 minutes by default. You can change it in `main_script.py`.

    ```python
    schedule.every(15).minutes.do(job)
    ```

## License

This project is licensed under the MIT License. See `LICENSE.md` for details.

## Author

Tunjan/Persaeus

## Contributing

Feel free to fork the project and submit a pull request with your changes!
