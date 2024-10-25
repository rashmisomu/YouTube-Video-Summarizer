# YouTube Transcript Point-wise Summarizer

## Overview
This application allows users to enter a YouTube video link and obtain a concise summary of the video’s transcript. Utilizing Google's Generative AI, the app generates a point-wise summary based on the video content. The app also displays the video thumbnail for a better user experience.

## Features
- Enter any YouTube video link to get a summary of its content.
- Automatic extraction of video transcripts.
- Summarization of the transcript into key points.
- Display of the video thumbnail.

## Technologies Used
- **Streamlit**: For creating the web application interface.
- **Python**: The programming language used for backend logic.
- **Google Generative AI**: For generating summaries from the transcript.
- **YouTube Transcript API**: For fetching video transcripts.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/YouTube-Transcript-Summarizer.git
   cd YouTube-Transcript-Summarizer
   ```

2. **Create a Virtual Environment (Optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   - Create a `.env` file in the root directory and add your Google Gemini API key:
     ```
     GOOGLE_GEMINI_API=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the provided link in your browser to access the application.

3. Enter the YouTube video link in the input field and click on "Get Detailed Notes" to see the summary.

## Example
Here is how the input and output would look:

**Input:**
```
Enter YouTube Video Link: https://www.youtube.com/watch?v=ABC123XYZ
```

**Output:**
- Summary of the video in key points.



## Acknowledgements
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/generative-ai)

