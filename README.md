# Physics Facts Notifier

## Overview

This script sends a desktop notification with an interesting physics fact at regular intervals. It can use either a local file or an online source for the facts.

## Prerequisites

- Python 3.x
- `plyer` package for notifications
- `schedule` package for task scheduling
- `requests` package for fetching facts online

You can install all the required packages by running:

```bash
pip install plyer schedule requests
```

## Configuration

The script is configured using a JSON file called `config.json`. The available settings are:

- `interval`: Time interval (in minutes) between notifications (default: 15).
- `use_online_source`: Whether to fetch facts from an online source (default: true).
- `online_source_url`: The URL to fetch the facts from if `use_online_source` is true.
- `enable_logging`: Whether to enable logging (default: true).
- `log_file`: The file to store logs.

## Usage

1. **Clone the Repository**: Clone this GitHub repository to your local machine.

    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies**: Navigate to the directory containing the cloned repository and install the required packages.

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure the Script**: Edit `config.json` to customize your settings, like notification interval, data source, etc.

4. **Run the Script**: Execute the Python script to start receiving notifications.

    ```bash
    python physics-notifier.py
    ```

5. **Stop the Script**: To stop receiving notifications, press `Ctrl+C` in the terminal where the script is running.

## Customization

- **Update Physics Facts**: You can add or remove facts in `physics_facts.txt`. Each fact should be on a new line.
- **Change Configuration**: Edit `config.json` to adjust your settings.

## Author

Persaeus/Tunjan

## License

This project is under the MIT License. See `LICENSE` for more details.

## Contributing

Feel free to fork this repository and create a pull request if you have some improvements or features to add.
