# Moonlight App

**Moonlight** is a headless (GUI-less) Python application that automates the monitoring of Telegram channels. Its goal is to help you detect and forward relevant messages (such as prices, alerts, or specific keywords) to your own channel using a Telegram bot.

## 💡What does Moonlight do?

- Scans public Telegram channels or groups for user-defined keywords.
- Sends an alert to the user’s Telegram channel when a match is found.
- Automatically forwards messages that meet the configured criteria.
- Runs unattended, ideal for cloud environments (AWS, Azure, VPS).

---

## 🚀 Technologies Used

- **Main Language:** Python  
- **Key Libraries:**  
  - `telethon` for Telegram interaction  
  - `dotenv` for environment variable management  
- **Recommended Platforms:** AWS EC2

---

## ⚙️ Prerequisites

- A [Telegram](https://telegram.org/) account  
- A Telegram bot created via [@BotFather](https://t.me/BotFather)  
- API ID and API Hash from [my.telegram.org](https://my.telegram.org)  
- Python 3.8 or higher  
- Your own Telegram channel (public or private)

---

## 🛠️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/trismald/moonlight.git
   cd moonlight
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the `.env` file:**
   ```
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   ...
   ```

4. **Run the application:**
   ```bash
   python moonlight.py
   ```

---

## 🧪 Example Use Case

Let’s say you want to monitor cryptocurrency channels for the keyword "BTC", and whenever it appears, you want the message to be forwarded to your personal channel:

- Add `BTC` to the regex search pattern.
- Make sure your bot has permission to read from those channels (if they are public).
- The message will be automatically forwarded to `TARGET_CHANNEL` when detected.

---

## ☁️ Recommended Deployment

You can run **Moonlight** in the background or as a service on platforms like:

- AWS EC2  
- Azure VM  
- Google Cloud Compute Engine  
- Raspberry Pi  
- Linux VPS

---

## 🤝 Contributing

Got an idea to improve Moonlight? You're welcome to open a pull request or issue!

---

## 📄 License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

---