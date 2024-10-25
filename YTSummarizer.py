import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Configure Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing an important summary in points  within 500 characters.
Please provide the summary of the text given here ..incase the transcript is in hindi translate it to english : """

# Function to generate content using Generative AI
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Function to extract transcript details from YouTube video URL
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        print("videoID: ",video_id)
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
       
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    except Exception as e:
        raise e

# Streamlit app
def main():
    st.title("YouTube Transcript Point-wise Summarizer")

    # Input field for YouTube Video Link
    youtube_link = st.text_input("Enter YouTube Video Link:")

    # Display video thumbnail
    if youtube_link:
        video_id = youtube_link.split("=")[-1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    # Button to fetch transcript details and generate summary
    if st.button("Get Detailed Notes"):
        
                transcript_text = extract_transcript_details(youtube_link)
               
                if transcript_text:
                    summary = generate_gemini_content(transcript_text, prompt)
                    st.markdown("## Detailed Notes:")
                    st.write(summary)
           

if __name__ == "__main__":
    main()
