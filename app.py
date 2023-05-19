import streamlit as st
import diffusers
from diffusers import DiffusionPipeline

# Load the diffusion pipeline
pipeline = diffusers.DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b")

# Create a text input field
text_input = st.text_input("Enter your text here")

# Generate the video
video = pipeline(text_input)

# Save the video
video.save("output.mp4")

# Download the video
st.download_button("Download Video", "output.mp4")
