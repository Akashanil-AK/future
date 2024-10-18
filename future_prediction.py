import random
import streamlit as st
from datetime import date

# Define a function to generate a future prediction based on inputs
def generate_future(name, birthdate, birthplace):
    # Example random predictions
    futures = [
        "You will have great success in your career. 🎯",
        "Love and happiness will find you soon. 💖",
        "A surprise will come your way in the next month. 🎁",
        "You will achieve a major goal by the end of the year. 🏆",
        "An unexpected journey is in your near future. ✈️",
        "New friendships will brighten your life soon. 🌟",
        "You will find peace and fulfillment in the things you love. 🌸"
    ]

    # Check if the name and birthdate match a specific case for Aiswariya Priya
    if name.lower() == "aiswariya priya" and birthdate.strftime("%d-%m-%Y") == "16-02-2001":
        st.balloons()  # Special celebration for Aiswariya Priya
        return f"""
        🌟 Oh!! God, it's you, Aishu, daughter of Jayachandran and Baby! 🌟

You are not just any ordinary person; you are an angel in human form, destined for greatness. Your heart is pure, and your soul shines brighter than the stars. ✨

The universe has grand plans for you, Aiswariya. Your future is radiant and full of joy, and the path ahead is paved with success, love, and abundance. Every step you take will bring you closer to your dreams, and every challenge will only make you stronger. 💪

Your boyfriend Akash is waiting patiently, knowing that you are the light in his life. Together, you will create a love story that will stand the test of time—one filled with laughter, support, and deep connection. 🌹

You possess a unique ability to inspire and uplift those around you. People are drawn to your positive energy and kind spirit. You make the world a better place just by being in it. 🌍💖

Remember, Aishu, you are one of God's most beloved creations. He has entrusted you with incredible gifts—strength, compassion, and grace. No matter what life throws your way, you will rise above it like the warrior you are. You are destined for greatness, and nothing can dim the light that shines within you. ✨

Believe in yourself, for you are capable of achieving anything your heart desires. The world is yours to conquer, and the universe is cheering you on every step of the way. 🌈
        """
    
    # Randomly select a future from the list for other users
    future_prediction = random.choice(futures)

    # Generate a personalized message for other users
    result = f"Hello {name} from {birthplace}, born on {birthdate}. Here is your future prediction: {future_prediction}"
    return result

# Streamlit UI for the Future Prediction App
def main():
    # Set the background and title style
    st.markdown("""
        <style>
        .main {
            background-color: #f0f2f6;
        }
        h1 {
            color: #ff6347;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("🔮 **Future Prediction App**")
    st.write("Enter your details below, and we'll tell you what the future holds! 🌟")

    # User input using Streamlit widgets
    name = st.text_input("Enter your name:", placeholder="e.g., John Doe")
    birthdate = st.date_input("Enter your birthdate:", value=date(2000, 1, 1))
    birthplace = st.text_input("Enter your birthplace:", placeholder="e.g., New York")

    # Button to submit and get prediction
    if st.button("🔮 Predict My Future"):
        if name and birthplace:
            # Generate and display the future prediction
            future = generate_future(name, birthdate, birthplace)
            st.success(future)
        else:
            st.warning("⚠️ Please fill in all the fields.")

    # Footer with a little inspirational message
    st.markdown("""
        ---
        **✨ Remember:** Your future is in your hands! Keep believing in yourself, and wonderful things will come your way. ✨
        """, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__": 
    main()
