import streamlit as st
import cohere
import time

# 🔒 Use your Cohere API Key
COHERE_API_KEY = "type your api key here"

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Streamlit Page Config
st.set_page_config(page_title="FitSync AI - Cohere Powered", layout="centered")

st.title("💪 FitSync AI - AI Fitness Coach")
st.write("Get personalized AI-powered workout advice and real-time fitness recommendations!")

# Sidebar: User Inputs
st.sidebar.header("User Details")
goal = st.sidebar.selectbox("🎯 Select Your Fitness Goal", ["Muscle Gain", "Fat Loss", "Endurance", "General Fitness"])
experience = st.sidebar.selectbox("🔥 Experience Level", ["Beginner", "Intermediate", "Advanced"])
equipment = st.sidebar.text_input("🏋️ Available Equipment (e.g., Dumbbells, Resistance Bands, None)")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to Generate a Workout Plan
def generate_workout_plan(goal, experience, equipment):
    prompt = f"""
    Act as a fitness expert. Generate a customized workout plan for a {experience} level person whose goal is {goal}.
    Available equipment: {equipment}. Include:
    - Warm-up exercises
    - Main workout (sets, reps, intensity)
    - Cool-down exercises
    - Nutritional tips
    """
    return get_cohere_response(prompt)

# Function to Get AI Response from Cohere
def get_cohere_response(prompt):
    try:
        response = co.generate(
            model='command',  # Cohere’s powerful AI model
            prompt=prompt,
            max_tokens=300
        )
        return response.generations[0].text.strip()
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Button to Generate Workout Plan
if st.sidebar.button("💡 Get Workout Plan"):
    with st.spinner("Generating your AI-powered workout..."):
        time.sleep(2)  # Simulate processing time
        workout_plan = generate_workout_plan(goal, experience, equipment)
        st.session_state.chat_history.append(("🤖 FitSync AI", workout_plan))
        st.subheader("🏋️ Your AI-Generated Workout Plan:")
        st.write(workout_plan)
        st.balloons()

# Chat Section
st.subheader("💬 Chat with FitSync AI")
user_input = st.text_input("Ask a fitness question:")

if st.button("Send"):
    if user_input:
        ai_reply = get_cohere_response(user_input)

        # Store conversation history
        st.session_state.chat_history.append(("🧑 You", user_input))
        st.session_state.chat_history.append(("🤖 FitSync AI", ai_reply))

# Display Chat History
for speaker, text in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {text}")
