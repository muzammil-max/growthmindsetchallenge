import streamlit as st

st.title("🌱 Growth Mindset Challenge 🚀")
st.write(
    "Welcome! This app explores the power of a growth mindset and how it can transform your personal and academic journey. 🌟"
)
st.write(
    "A growth mindset is all about believing that your abilities and intelligence aren't fixed. With hard work, dedication, and a willingness to learn, you can achieve anything! 💪🧠"
)

st.header("🤔 What Exactly is a Growth Mindset?")
st.write(
    "Imagine your brain as a muscle. The more you use it and challenge it, the stronger it gets! 💪 A growth mindset, popularized by the amazing psychologist Carol Dweck, suggests that our skills aren't set in stone. Instead, they can grow and develop with effort and practice. 🌱"
)
st.write(
    "It's the opposite of a fixed mindset, where people believe their abilities are limited. With a growth mindset, you see challenges as opportunities, not roadblocks! 🚧➡️🌟"
)

st.header("🏆 Why Embrace a Growth Mindset?")
st.write(
    "- **Embrace Challenges**: See obstacles as exciting chances to learn and grow. 🧗‍♀️➡️🌟"
)
st.write(
    "- **Learn from Mistakes**: Mistakes are valuable lessons in disguise. Don't be afraid to stumble; it's part of the journey! 🚶‍♀️➡️💡"
)
st.write(
    "- **Persist Through Difficulties**: Keep going, even when things get tough. Remember, every expert was once a beginner. 🚀"
)
st.write(
    "- **Celebrate Effort**: Appreciate the hard work you put in, regardless of the outcome. Effort is what fuels growth! 🔥"
)
st.write(
    "- **Keep an Open Mind**: Stay curious and be willing to adapt your approach based on new information. 💡"
)


st.header("🛠️ How to Cultivate a Growth Mindset")
st.write(
    "- **Set Learning Goals**: Focus on developing specific skills and gaining a deeper understanding. 🎯"
)
st.write(
    "- **Reflect on Your Learning**: Take time to analyze what you've learned from both successes and setbacks. 📝"
)
st.write(
    "- **Seek Feedback**: Welcome constructive criticism as a tool for improvement. 👂"
)
st.write(
    "- **Stay Positive**: Believe in your potential and encourage others to do the same. Spread the growth mindset love! ❤️"
)

# --- Interactive Elements (Example) ---
st.subheader("✍️ Reflect on Your Growth Today")
reflection = st.text_area("What's one thing you learned or improved on today? Share your thoughts!")
if st.button("Submit Reflection"):
    st.write("Thank you for sharing your reflection! Keep growing! 🌱")

# # --- Additional Features to add later ---
# st.header("🚀 More Exciting Features Coming Soon...")
# st.write(
#     "This is just the beginning! We'll be adding quizzes, progress trackers, and more interactive tools to help you on your growth mindset journey. Stay tuned! 🎉"
# )
quiz_questions = [
    {
        "question": "I believe my intelligence is something very basic that I can't change much.",
        "options": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        "correct_answer": "Strongly Disagree",  # Example: Correct answer for growth mindset
    },
    {
        "question": "I enjoy challenges and see them as opportunities to grow.",
        "options": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        "correct_answer": "Strongly Agree",
    },
    {
        "question": "When things get difficult, I tend to give up quickly.",
        "options": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        "correct_answer": "Strongly Disagree",
    },
    {
        "question": "I learn the most when I make mistakes.",
        "options": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        "correct_answer": "Strongly Agree",
    },
    {
        "question": "I don’t like to be challenged; I prefer doing things I’m already good at.",
        "options": ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"],
        "correct_answer": "Strongly Disagree",
    },
]
st.header("🧠 Test Your Growth Mindset!")
answers = []
for i, question in enumerate(quiz_questions):
    st.subheader(f"Question {i + 1}:")
    answer = st.radio(question["question"], options=question["options"])
    answers.append(answer)


# --- Calculate Score and Store Results ---
def calculate_score(answers, quiz_questions):
    score = 0
    for i, answer in enumerate(answers):
        if answer == quiz_questions[i]["correct_answer"]:
            score += 1
    return score


# --- Display Results ---
if st.button("Submit Quiz"):
    score = calculate_score(answers, quiz_questions)
    st.session_state.quiz_results = {"score": score, "total": len(quiz_questions)} #Store data in session State
    st.write(f"You scored {score} out of {len(quiz_questions)}!")