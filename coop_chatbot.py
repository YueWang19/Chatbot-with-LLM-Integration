import streamlit as st
import ollama

def get_coop_advice(query):
    # Updated prompt with explicit reference to Northeastern University
    contextual_prompt = (f"As a co-op advisor for Northeastern University, please provide specific information "
                         f"about the university's co-op program in response to the student's inquiry: '{query}'")
    
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': contextual_prompt}],
        stream=False  # Set this to True if needed for streaming responses
    )
    
    return response['message']['content']

def main():
    st.title("Northeastern University Co-op Advisor Chatbot")
    st.write("Ask me anything about Northeastern's co-op program!")

    # Initialize or get the chat history from session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
        st.session_state.counter = 0  # Initialize a counter in session state

    user_input = st.text_input("Enter your question about co-op:", key="co_op_input")

    if st.button("Ask", key="ask_button"):
        if user_input:
            # Fetching response with enhanced context understanding
            response = get_coop_advice(user_input)
            st.session_state.chat_history.append(("You", user_input))
            st.session_state.chat_history.append(("Advisor", response))
            st.session_state.counter += 1  # Increment the counter each time the button is pressed

            # Display all past interactions with unique keys
            for index, (role, text) in enumerate(st.session_state.chat_history):
                unique_key = f"{role}_{index}_{st.session_state.counter}"  # Unique key generation
                st.text_area(f"{role}:", value=text, height=300, key=unique_key)
        else:
            st.write("Please enter a question to get started.")

if __name__ == "__main__":
    main()
