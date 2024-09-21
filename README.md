# 🤖 Automatic Message Bot
This project is an automatic message bot that allows you to send messages programmatically using Python. The bot utilizes libraries like Flask for a lightweight web interface and PyWhatKit for sending messages via WhatsApp.

## 📋 Requirements
Make sure you have Python installed on your system. This project uses the following dependencies:
- pywin32: For Windows interactions.
- Flask: To create a lightweight web interface.
- pywhatkit: To send messages via WhatsApp.

## 🔧 How to Run the Program

1. Install Dependencies

```sh
pip install pywin32
pip install flask
pip install pywhatkit
```

2. Configure the Phone Number
To add the phone number to which messages will be sent, create a file named config.py in the root of the project. Add the following function:
```sh
def number():
    number = '+5500000000'  # Replace with the desired number
    return number
```

3. Running the Bot
After configuring the number, you can start the bot by executing the main file of your project
```
python app.py
```

Thank you for checking out the "Automatic Message Bot" project! Feel free to try it out and contribute!
