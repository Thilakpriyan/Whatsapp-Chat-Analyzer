from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import re


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

def create_wordcloud(selected_user,df):
    if selected_user != 'Overall':
        df=df[df['user']==selected_user]
    wc= WordCloud(width=800, height=600,min_font_size=10,background_color='white')
    df_wc=wc.generate(df['message'].str.cat(sep=''))
    return df_wc
import os
print('STOPWORDS FILE PATH:',os.path.abspath('stopwords.txt'))
def most_common_words(selected_user, df):
    import re
    from collections import Counter
    import pandas as pd

    with open('stopwords.txt', 'r', encoding='utf-8') as f:
        stop_words = set(f.read().split())
    print("STOPWORDS SAMPLE:", list(stop_words)[:20])
    print("TOTAL STOPWORDS:", len(stop_words))
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
