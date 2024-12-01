import streamlit as st

from openai import OpenAI

def initialize_openai_client(api_key):
    if api_key.startswith("sk-"):
        return OpenAI(api_key=api_key)
    else:
        st.error("Please provide a valid OpenAI API key starting with 'sk-'.")
        return None

# What best describes your role? 
# What’s your industry?
# What value do you aim to provide your network?
# What's your primary goal on LinkedIn?
# What's your content personality?:
# Write a few sentences about anything you're passionate about (work, hobby, interest) - this helps us learn your natural voice.

def generate_post(role, industry, style, purpose, content, sample, topic, model):
    prompt = (
    "Create a professional LinkedIn post about {topic} with the following guidelines:\n\n"
    "Post Structure:\n"
    "- Use a numbered list format (8-9 points)\n"
    "- Each point should have a main insight and a 1-2 line explanation\n"
    "- Include a technical breakdown with professional insights\n"
    "- Demonstrate deep understanding of the technical concept\n\n"
    
    "Tone and Style:\n"
    "- Professional and authoritative\n"
    "- Use technical language with clear explanations\n"
    "- Balance technical depth with readability\n"
    "- Include practical, real-world applications\n\n"
    
    "Content Requirements:\n"
    "- Start with a compelling opening statement about the topic\n"
    "- Break down the topic into 8-9 distinct, meaningful points\n"
    "- Use ↳ for sub-points to enhance readability\n"
    "- Highlight practical implications and industry relevance\n"
    "- Conclude with a thought-provoking question or call-to-action\n\n"
    
    f"Specific Topic Details:\n"
    f"Topic: {topic}\n"
    f"Role: {role}\n"
    f"Industry: {industry}\n"
    f"Style: {style}\n"
    f"Purpose: {purpose}\n"
    f"Content Personality: {content}\n"
    f"Sample: {sample}\n\n"
    
    "Key Objectives:\n"
    "- Demonstrate expertise\n"
    "- Provide actionable insights\n"
    "- Engage professional network\n"
    "- Show thought leadership\n\n"
    
    "Length and Format:\n"
    "- Total post length must not be more than 180 words\n"
    "- Use clear, concise language\n"
    "- Avoid unnecessary jargon\n"
    "- No emojis"
)

    if model == "gpt-4o":

        response = client.chat.completions.create(
        
            model="gpt-4o",
        
            messages=[
        
                {"role": "system", "content": "You are an expert technical communicator who creates LinkedIn posts that break down complex topics into clear, engaging, and professionally structured content. Your posts demonstrate deep expertise, provide actionable insights, and are tailored to a professional audience."},
                {"role": "user", "content": prompt},
        
            ],
        
            max_tokens=500,
        
            temperature=0.8,
        
        )
        
        generated_post = response.choices[0].message.content.strip()
    
    elif model == "gpt-4o-mini":
    
        response = client.chat.completions.create(
    
            model="gpt-4o-mini",
    
            messages=[
    
                {"role": "system", "content": "You are an expert technical communicator who creates LinkedIn posts that break down complex topics into clear, engaging, and professionally structured content. Your posts demonstrate deep expertise, provide actionable insights, and are tailored to a professional audience."},
                {"role": "user", "content": prompt},
    
            ],
    
            max_tokens=500,
    
            temperature=0.8,
    
        )
    
        generated_post = response.choices[0].message.content.strip()

    return generated_post

# Streamlit interface
st.title("LinkedIn Post Generator")

api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Initialize OpenAI client
client = initialize_openai_client(api_key)

# Model selection
model_options = ["gpt-4o", "gpt-4o-mini"]

selected_model = st.selectbox("Select Model:", model_options)

# Input fields
role_options = ["Leader (Executive, Director, Manager)", "Builder (Engineer, Developer, Architect)", "Creator (Designer, Writer, Artist)", "Advisor (Consultant, Strategist, Expert)", "Specialist (Analyst, Researcher, Technician)", "Connector (Sales, BD, Partnerships)", "Guide (Teacher, Trainer, Coach)", "Champion (Marketing, PR, Brand)", "Guardian (Legal, Finance, Operations)", "Helper (Support, Service, Success)"]
role = st.selectbox("What best describes your role?", role_options)

industry_options = ["Technology & Innovation", "Professional Services", "Creative Industries", "Commerce & Trade", "Education & Training", "Healthcare & Wellness", "Financial Services", "Digital Economy", "Social Impact"]
industry = st.selectbox("What's your industry?", industry_options)

style_options = ["Expert Insights", "Innovation Stories Market Analysis", "Success Narratives", "Professional Growth Tips", "Real-World Examples", "Community Building", "Resource Sharing", "Technical Knowledge", "Other Value Add"]
style = st.selectbox("What value do you aim to provide your network?", style_options)

purpose_option = ["Expanding Professional Circle", "Establishing Industry Voice", "Career Advancement", "Business Development", "Team Building", "Knowledge Exchange", "Community Leadership", "Impact Measurement", "Market Research"]
purpose = st.selectbox("What's your primary goal on LinkedIn?", purpose_option)

content_option = ["Bold - Direct, punchy, straight to the point", "Warm - Friendly, supportive, makes everyone feel welcome", "Analytical - Data-driven, logical, research-backed insights", "Witty - Clever, humorous, unexpected fresh takes", "Authentic - Real, honest, sharing genuine experiences", "Persuasive - Compelling, influential, drives people to action", "Helpful - Educational, practical, sharing useful knowledge", "Strategic - Big picture, future-focused, industry insights", "Inspiring - Motivational, uplifting, celebrates growth moments", "Custom - Tell us your unique approach"]
content = st.selectbox("What's your content personality?", content_option)

sample = st.text_input("Write a few sentences about anything you're passionate about (work, hobby, interest) - this helps us learn your natural voice.")

topic = st.text_input("Enter topic:")

# Button to generate cover letter
if st.button("Generate Post"):

    generated_post = generate_post(role, industry, style, purpose, content, sample, topic, selected_model)

    st.subheader("Generated Post:")

    st.markdown(f"*Generated:* {generated_post}")