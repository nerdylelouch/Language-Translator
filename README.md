# Language Translator GUI

This project is a **language translation application** built using Python's `tkinter` for the graphical user interface (GUI) and Google Translate API for translating text between different languages. The application also includes **speech recognition** capabilities, allowing users to input text via their voice.

## Features

- Translate text between multiple languages using Google Translate.
- Speech-to-text functionality using Google Speech Recognition.
- Graphical interface for easy user interaction.
- Select source and destination languages from a dropdown menu.
- Real-time translation with support for both text and voice input.

## Requirements

Before running the application, make sure you have the following Python libraries installed:

```bash
pip install tkinter googletrans==4.0.0-rc1 speechrecognition
```

## Usage
- Open the application, select the Source Language and Destination Language from the dropdown menus.
- Enter the text you want to translate in the text box, or click the Translate button after selecting the languages.
- You can also speak into your microphone, and the app will convert your speech to text and translate it automatically.

## Future Improvements
- Add more error handling for speech recognition failures.
- Implement offline translation capabilities.
- Enhance UI with custom themes and better font integration.
