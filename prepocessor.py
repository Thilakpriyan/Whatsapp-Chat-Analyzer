import re
import pandas as pd

def prepocesses(data):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s?(?:AM|PM)'
    messages = re.split(pattern, data)

    data = data.replace('\u202f', ' ')

    dates = re.findall(pattern, data)
    min_len = min(len(messages), len(dates))
    messages = messages[:min_len]
    dates = dates[:min_len]

    df = pd.DataFrame({
        'user_message': messages,
        'message_date': dates
    })

    df['message_date'] = df['message_date'].str.replace('\u202f', ' ')

    df['message_date'] = pd.to_datetime(
        df['message_date'],
        format='%m/%d/%y, %I:%M %p'
    )

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users = []
    msgs = []

    for text in df['user_message']:
        if ': ' in text:
            user, msg = text.split(': ', 1)
            users.append(user)
            msgs.append(msg)
        else:
            users.append('group_notification')
            msgs.append(text)

    df['user'] = users
    df['message'] = msgs

    df.drop(columns=['user_message'], inplace=True)
    df['only_date']=df['date'].dt.date
    df['Year'] = df['date'].dt.year
    df['month_num']=df['date'].dt.month
    df['Month'] = df['date'].dt.month_name()
    df['Day'] = df['date'].dt.day
    df['Hour'] = df['date'].dt.hour
    df['Minute'] = df['date'].dt.minute

    return df