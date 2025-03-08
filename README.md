📌 FitSync AI - Cohere Powered
AI-powered fitness assistant that provides personalized workout plans and real-time fitness recommendations using Cohere AI.

🚀 Features
Generate AI-powered workout plans based on goal, experience level, and available equipment.
Interactive chat for real-time fitness Q&A.
Powered by Cohere AI for dynamic, personalized responses.
Easy-to-use interface with Streamlit.
🛠️ Installation & Setup
1️⃣ Clone the Repository (Optional if using Git)
bash
Copy
Edit
git clone https://github.com/your-repo/FitSync-AI.git
cd FitSync-AI
2️⃣ Set Up Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # For Windows (Git Bash)
source venv/bin/activate      # For Mac/Linux
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt is missing, install manually: pip install streamlit cohere python-dotenv)

4️⃣ Set Up Cohere API Key
Create a .env file in the project directory and add:

ini
Copy
Edit
COHERE_API_KEY=your-cohere-api-key
Or, export it temporarily:

bash
Copy
Edit
export COHERE_API_KEY="your-cohere-api-key"
5️⃣ Run the Application
bash
Copy
Edit
streamlit run app.py
This will open FitSync AI in your browser. 🎉

📌 How to Use
1️⃣ Select Your Goal, Experience Level, and Available Equipment (from the sidebar).
2️⃣ Click “💡 Get Workout Plan” to generate a custom AI-powered fitness plan.
3️⃣ Chat with FitSync AI in the text box for additional fitness guidance.

🛠️ Troubleshooting
Cohere API key error?

Ensure .env file is correctly set up.
Verify API key validity at Cohere API.
Streamlit not found?

bash
Copy
Edit
pip install streamlit
Git not found?

bash
Copy
Edit
git --version
If missing, install from Git-SCM.

🤝 Contributing
Fork the repo & create a new branch.
Make changes and test locally.
Create a pull request with a clear description.
📜 License
MIT License © 2025 FitSync AI.

Let me know if you need any modifications! 🚀🔥
