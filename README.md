# Emotion Detection System 😃🥺😲😠😨🤢

## Overview

The Emotion Detection System is a web application that utilizes advanced face detection technology to identify emotions in real-time. Users can either upload an image or capture a photo using their camera to detect emotions. The application provides a user-friendly interface with modals for image preview and emotion prediction.

## Features

- **Upload Image:** Users can upload an image from their device to detect emotions.
- **Start Camera:** Users can activate their camera to capture a photo and detect emotions.
- **Real-time Emotion Detection:** Detect emotions from uploaded or captured images.
- **Image Preview:** View the uploaded or captured image along with the detected emotion.

## Technologies Used

- **HTML5 & CSS3:** For structuring and styling the web pages.
- **Bootstrap 4.5:** For responsive design and UI components.
- **JavaScript:** For handling user interactions and image processing.
- **Fetch API:** For making network requests to the server.
- **FileReader API:** For reading image files on the client side.
- **WebRTC:** For accessing the camera.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/emotion-detection-system.git
    cd emotion-detection-system
    ```

2. **Install Dependencies:**

    Ensure you have a web server set up to serve the static files and handle POST requests. For example, you can use Flask or another web framework. Install the required dependencies as per your project's requirements.

3. **Run the Server:**

    Set up and start your server. For example, if using Flask:

    ```bash
    python app.py
    ```

4. **Access the Application:**

    Open your web browser and go to `http://localhost:5000` (or the address configured for your server).

## Usage

1. **Uploading an Image:**
    - Click the "Upload Image" button.
    - Select an image file from your device.
    - The selected image will be displayed in a modal along with the predicted emotion.

2. **Capturing an Image:**
    - Click the "Start Camera" button to open the camera modal.
    - Click the "Capture Image" button to take a photo.
    - The captured image will be displayed in a new modal along with the predicted emotion.

## Code Explanation

- **HTML Structure:** The `index.html` file contains the structure of the web application, including modals for image preview and camera capture.
- **JavaScript Functionality:** The script handles user interactions, such as uploading an image, starting the camera, capturing an image, and displaying results.
- **Modals:** Bootstrap modals are used for displaying images and predicted emotions.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests. To contribute:

1. **Fork the repository.**
2. **Create a new branch:**

    ```bash
    git checkout -b feature/your-feature
    ```

3. **Make your changes.**
4. **Commit your changes:**

    ```bash
    git commit -m 'Add new feature'
    ```

5. **Push to the branch:**

    ```bash
    git push origin feature/your-feature
    ```

6. **Open a pull request.**


## Acknowledgments

- [Bootstrap](https://getbootstrap.com/) for the responsive design components.
- [WebRTC](https://webrtc.org/) for camera access functionality.
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) for network requests.
