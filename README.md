📊 WhatsApp Chat Analyzer (ML + Streamlit)
🔍 Project Overview

The WhatsApp Chat Analyzer is a Machine Learning–powered data analysis application that analyzes one-to-one chats and group chats exported from WhatsApp.
Users can upload a WhatsApp chat file (.txt), and the application provides insights, statistics, and visualizations about chat activity.

The project is built using Python, Pandas, Streamlit, and Machine Learning techniques, developed in PyCharm, and deployed on Heroku.

🎯 Objectives

Analyze WhatsApp chat data automatically

Support individual chats and group chats

Extract useful insights such as:

Most active users

Message frequency

Timeline analysis

Word usage patterns

Provide an easy-to-use web interface

Deploy as a live web application

🧠 Features

📁 Upload WhatsApp chat .txt file

👤 Separate users and messages automatically

📅 Time-based analysis (daily, monthly activity)

💬 Message count per user

📈 Visual charts and statistics

🤖 Machine learning–ready preprocessing

🌐 Web app using Streamlit

🛠️ Technologies Used
Programming & Libraries

Python 3

Pandas

NumPy

Regex (re)

Streamlit

Matplotlib / Seaborn (for visualization)

Tools & Platforms

PyCharm (Development)

Git & GitHub (Version Control)

Streamlit (Web Interface)

Heroku (Deployment)

🧩 Project Structure
Whatsapp-chat-analyzer/
│
├── app.py               # Main Streamlit application
├── preprocessor.py      # Chat preprocessing and ML logic
├── requirements.txt     # Required Python libraries
├── .gitignore           # Ignored files for Git
├── README.md            # Project documentation

📥 Input Format

WhatsApp chat exported as .txt file

Supports:

Personal chats

Group chats

Language-independent (works with emojis & Unicode)

📤 Output / Analysis Provided

Total messages count

User-wise message contribution

Chat activity over time

Identification of group notifications

Cleaned and structured DataFrame for ML tasks

🚀 How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Whatsapp-chat-analyzer.git
cd Whatsapp-chat-analyzer

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Streamlit App
streamlit run app.py


Open browser:

http://localhost:8501

🌐 Deployment (Heroku)

The application is deployed using Heroku

Uses Procfile and requirements.txt

GitHub repository is connected to Heroku for deployment

🎓 Learning Outcomes

Real-world data cleaning & preprocessing

Regex-based text parsing

Pandas DataFrame manipulation

Streamlit web application development

GitHub workflow

Cloud deployment using Heroku

🔮 Future Enhancements

Emoji analysis

Sentiment analysis using NLP

Chat comparison between users

Export analysis reports as PDF

Support multiple chat files

👤 Author

Thilakpriyan R
B.Tech / B.E – Computer Science
Interested in Machine Learning & Data Analytics

⭐ Acknowledgements

WhatsApp chat export format

Streamlit community

Open-source Python ecosystem
