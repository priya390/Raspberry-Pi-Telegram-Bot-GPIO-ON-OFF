## How to turn ON/OFF Raspberry Pi GPIO pins using Telegram Bot:
  1. Create your own bot in Telegram using BotFather.  
  2. Install Python Telegram Bot Module using: `https://github.com/python-telegram-bot/python-telegram-bot#installing`  
  3. Open terminal or CMD and type:  
     * `git clone https://github.com/priya390/Raspberry-Pi-Telegram-Bot-GPIO-ON-OFF`  
     * `cd Raspberry-Pi-Telegram-Bot-GPIO-ON-OFF`  
     * Enter your Telegram Bot token inside the main function on line number 56.     
     * `sudo python main.py`  
  4. In this code, we have used GPIO pin number 5(GPIO3).You can change your GPIO pin number on line number 9.
  5. In this code, we have used GPIO27.You can change yout GPIO pin number on line number 10.
  6. Open Telegram, open your bot and type: 
     * `/on` to turn ON the GPIO pin.
     * `/off` to turn OFF the GPIO pin.
     * `/temp` to get current Temperature in Celcius. 
     * `/hum` to get current Humidity in percentage.