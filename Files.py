import streamlit as st
import pandas as pd

st.subheader("Loading the CSV File")
file_csv = st.file_uploader("Upload the CSV File : ", type = ['csv' , 'xlsx'])

st.subheader('Loading the CSV File')
if file_csv is not None:
    df = pd.read_csv(file_csv).describe()
    st.table(df)

st.subheader("Dealing with images while uploading")
img_file = st.file_uploader("Upload the image file : ", type = ["png" , 'jpg' , 'jpeg'])
if img_file is not None:
    st.image(img_file)

st.subheader("Dealing with Videos")
video_file = st.file_uploader("Upload the Video file : ", type = ['mkv' , 'mp4'])
if video_file is not None:
    st.video(video_file , start_time = 0)

st.subheader("Dealing with Audio")
audio_file = st.file_uploader("Upload the audio file : ", type = ['mp3' , 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())
    
