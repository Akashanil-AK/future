import random
import streamlit as st

# Define a function to generate a future prediction based on inputs
def generate_future(name, birthdate, birthplace):
    # Example random predictions
    futures = [
        "You will have great success in your career.",
        "Love and happiness will find you soon.",
        "A surprise will come your way in the next month.",
        "You will achieve a major goal by the end of the year.",
        "An unexpected journey is in your near future.",
        "New friendships will brighten your life soon.",
        "You will find peace and fulfillment in the things you love."
    ]

    # Check if the name and birthdate match a specific case
    if name.lower() == "aiswariya priya" and birthdate.strftime("%d-%m-%Y") == "16-07-2001":
        return f"oh!! God its you  aishu daughter of jayachandran and baby. you are an angel born as human Your future is as bright as your eyes. You will achieve immense success and happiness in all areas of your life.keep the faith in yourself and work for your dreams there is a lot of happines waiting for you, your boyfriend akash is waiting for you to shine his life with your light of your grace. your are one of the Blessed human beings on earth, who can enchance their surondigs with their presence,  your boyfriend is so lucky! God give their toughest soldiers their toughfest battle you are Gods favorite angel"

    # Randomly select a future from the list
    future_prediction = random.choice(futures)

    # Generate a personalized message
    result = f"Hello {name} from {birthplace}, born on {birthdate}. Here is your future prediction: {future_prediction}"
    return result

# Streamlit UI for the Future Prediction App
def main():
    st.title("🔮 Future Prediction App")
    st.write("Enter your details below, and we'll tell you what the future holds!")

    # User input using Streamlit widgets
    name = st.text_input("Enter your name:")
    birthdate = st.date_input("Enter your birthdate:")
    birthplace = st.text_input("Enter your birthplace:")

    # Button to submit and get prediction
    if st.button("Predict My Future"):
        if name and birthplace:
            # Generate and display the future prediction
            future = generate_future(name, birthdate, birthplace)
            st.success(future)
        else:
            st.warning("Please fill in all the fields.")

# Run the Streamlit app
if __name__ == "__main__": 
    main()

