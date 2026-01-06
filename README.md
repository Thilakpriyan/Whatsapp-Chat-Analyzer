📊 WhatsApp Chat Analyzer

A Streamlit-based data analysis application that analyzes WhatsApp one-to-one and group chats to extract meaningful insights using Python, NLP preprocessing, and data visualization techniques.

Users can upload an exported WhatsApp chat file (.txt) and instantly view interactive statistics, timelines, word clouds, and emoji usage patterns.

🚀 Live Demo

👉 Deployed on Streamlit Community Cloud
🔗 https://whatsapp-chat-analyzer-cp5famyl3afzxa4ccj7dss.streamlit.app/

🎯 Project Objectives

Analyze WhatsApp chat data automatically

Support individual and group chats

Extract time-based and user-based insights

Apply NLP preprocessing and exploratory data analysis

Build an end-to-end deployable analytics application

🧠 Key Features

📩 Total messages & word count

👥 Most active users (group chats)

📅 Monthly & daily chat timelines

🗓️ Weekly activity analysis

⏰ Hour-wise activity heatmap

☁️ WordCloud of most used words

🔤 Most common words analysis

😊 Emoji usage analysis

🔗 Link sharing statistics

📊 Interactive visualizations

🛠️ Tech Stack
Category	Tools
Language	Python
Data Processing	Pandas
Visualization	Matplotlib, Seaborn
UI Framework	Streamlit
NLP Concepts	Regex, Stopwords, Tokenization
Emoji Processing	emoji
URL Extraction	urlextract
Deployment	Streamlit Community Cloud
IDE	PyCharm

📂 Project Structure
whatsapp-chat-analyzer/
│
├── app.py                # Streamlit UI and app logic
├── helper.py             # Analysis and visualization functions
├── prepocessor.py        # Chat preprocessing & feature engineering
├── stopwords.txt         # Stopwords for NLP cleaning
├── requirements.txt      # Project dependencies
└── README.md

⚙️ How the System Works
1️⃣ Chat Preprocessing

Parses raw WhatsApp chat text

Extracts:

Date & time

User names

Message content

Performs feature engineering:

Year, month, day

Day name

Hour & time period slots

2️⃣ Data Analysis

Message statistics

User activity counts

Time-based grouping

Text cleaning & stopword removal

3️⃣ Visualization

Line charts (daily & monthly trends)

Bar charts (user & word frequency)

Heatmaps (weekly & hourly activity)

WordClouds

Emoji pie charts

4️⃣ Deployment

Hosted on Streamlit Community Cloud

Accessible via browser

No local setup required

📥 Input Format

Export WhatsApp chat as .txt file

Supported:

One-to-one chats

Group chats

🧪 Local Setup (Optional)
git clone https://github.com/your-username/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer
pip install -r requirements.txt
streamlit run app.py

🧠 Is This a Machine Learning Project?

This project focuses on NLP preprocessing and exploratory data analysis, which are foundational components of machine learning pipelines.

