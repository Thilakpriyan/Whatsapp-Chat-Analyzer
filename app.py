import streamlit as st
import matplotlib.pyplot as plt
import helper
import prepocessor
from helper import most_common_words

st.sidebar.title('WHATSAPP CHAT ANALYZER')


uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data= bytes_data.decode("utf-8")
    df=prepocessor.prepocesses(data)


    #fetch unique users
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'Overall')

    selected_user=st.sidebar.selectbox('SHOW ANALYZIS ',user_list)
    if st.sidebar.button('Show Analysis'):
        num_messages,words,media_message,links= helper.fetch_stats(selected_user,df)
        st.title('Top Statistics')
        col1,col2,col3,col4 =st.columns(4)

        with col1:
            st.header('Totalmessages')
            st.title(num_messages)
        with col2:
            st.header('Total Words')
            st.title(words)
        with col3:
            st.header('Media Shared')
            st.title(media_message)
        with col4:
            st.header('Links Shared')
            st.title(links)
        #Monthlytimeline
        st.title('Monthly Timeline')
        timeline=helper.monthly_timeline(selected_user,df)

        fig,ax=plt.subplots()

        ax.plot(timeline['time'],timeline['message'],color='Red')

        plt.xticks(rotation='vertical')

        st.pyplot(fig)

        #dailytimeline

        st.title('Daily Timeline')
        daily_timeline = helper.daily_timeline(selected_user, df)

        fig, ax = plt.subplots()

        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='green')

        plt.xticks(rotation='vertical')

        st.pyplot(fig)




        #finding the busiest user in the group
        if selected_user =='Overall':
            st.title('MOST BUSY USER')
            x,new_df=helper.most_busy_users(df)

            fig,ax=plt.subplots()

            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index, x.values )

                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
    #wordcloud
    st.title('WordCloud')
    df_wc=helper.create_wordcloud(selected_user,df)
    fig,ax=plt.subplots()
    plt.imshow(df_wc)
    st.pyplot(fig)

    #mostcommon word
    most_common_df = helper.most_common_words(selected_user, df)

    fig, ax = plt.subplots()

    ax.bar(most_common_df['word'], most_common_df['count'])

    plt.xticks(rotation=90)

    st.pyplot(fig)

    #Emoji Analysis

    emoji_df=helper.emoji_helper(selected_user,df)
    st.title('Emoji Analysis')
    col1,col2=st.columns(2)
    with col1:

      st.dataframe(emoji_df)
    with col2:
        fig,ax=plt.subplots()
        ax.pie(emoji_df['count'].head(),labels=emoji_df['emoji'].head(),autopct='%1.1f')

        st.pyplot(fig)

