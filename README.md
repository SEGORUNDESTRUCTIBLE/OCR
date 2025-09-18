# Instant OCR

A simple OCR application for Linux that allows you to capture a selected area of the screen and instantly recognize the text within it.

## Features

- Press `Win+Z` to start the screen capture.
- Drag the mouse to select an area of the screen.
- The text in the selected area is automatically recognized and copied to the clipboard.

## Installation

1.  **Install system dependencies:**

    ```bash
    sudo apt-get update && sudo apt-get install -y tesseract-ocr scrot
    ```

2.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main script:

```bash
python main.py
```

The application will run in the background, listening for the `Win+Z` shortcut.

### Running as a service (recommended)

To run the application as a systemd service that starts on boot, follow these steps:

1.  **Move the service file:**

    ```bash
    sudo mv instant-ocr.service /etc/systemd/system/
    ```

2.  **Reload the systemd daemon:**

    ```bash
    sudo systemctl daemon-reload
    ```

3.  **Enable and start the service:**

    ```bash
    sudo systemctl enable --now instant-ocr.service
    ```
