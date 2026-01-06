from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import re
import emoji


extract=URLExtract()
def fetch_stats(selected_user,df):

    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    num_messages=df.shape[0]
    words=[]
    for message in df['message']:
            words.extend(message.split())
    media_message=df[df['message']=='<Media omitted>\n'].shape[0]

    links=[]
    for message in df['message']:
        links.extend(extract.find_urls(message))


    return num_messages,len(words),media_message,len(links)


def most_busy_users(df):
    user_counts = df['user'].value_counts().head()
    percent_df = round(
        (df['user'].value_counts() / df.shape[0]) * 100,
        2
    ).reset_index()

    percent_df.columns = ['user', 'percent']

    return user_counts, percent_df
def create_wordcloud(selected_user, df):

    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stopwords(message):
        words = []
        message = message.lower()
        message = re.sub(r'[^\w\s]', '', message)

        for word in message.split():
            if word not in stop_words:
                words.append(word)

        return " ".join(words)

    cleaned_text = temp['message'].apply(remove_stopwords).str.cat(sep=' ')

    wc = WordCloud(
        width=800,
        height=600,
        min_font_size=10,
        background_color='white'
    )

    df_wc = wc.generate(cleaned_text)

    return df_wc
import os
print('STOPWORDS FILE PATH:',os.path.abspath('stopwords.txt'))
def most_common_words(selected_user, df):

    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        stop_words = set(f.read().split())

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']

    words = []

    for message in temp['message']:
        message = message.lower()
        message = re.sub(r'http\S+', '', message)
        message = re.sub(r'[^\w\s]', '', message)

        for word in message.split():
            word = word.strip()
            if word and word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(
        Counter(words).most_common(20),
        columns=['word', 'count']
    )

    return most_common_df


def emoji_helper(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []

    for message in df['message']:
        for char in message:
            if emoji.is_emoji(char):
                emojis.append(char)

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(),
        columns=['emoji', 'count']
    )

    return emoji_df
def monthly_timeline(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(
        ['Year', 'month_num', 'Month']
    ).count()['message'].reset_index()

    timeline = timeline.sort_values(['Year', 'month_num'])

    # create proper time label
    timeline['time'] = timeline['Month'] + '-' + timeline['Year'].astype(str)

    return timeline
def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline=df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline
def week_activity(selected_user,df):
     if selected_user !='Overall':
         df=df[df['user'] == selected_user]


     return df['day_name'].value_counts()


def month_activity(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['Month'].value_counts()


def activity_heatmap(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user'] == selected_user]
    user_heatmap=df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap