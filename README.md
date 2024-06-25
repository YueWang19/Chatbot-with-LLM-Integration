# Northeastern University Co-op Advisor Chatbot

This chatbot is designed to provide information about the co-op program at Northeastern University. It uses the `ollama` package to power the interactions with an AI model, offering users responses based on their inquiries about the co-op programs.

## Prerequisites

Before you begin, ensure you have the following installed on your computer:

- Python 3.6 or higher
- pip (Python package installer)

## Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

To clone the repository and navigate into the project directory, run:

`git clone https://github.com/YueWang19/Chatbot-with-LLM-Integration.git`

`cd Chatbot-with-LLM-Integration`

### 2. Set Up a Virtual Environment (Optional)

It's a good practice to use a virtual environment to isolate package dependencies. To set up and activate a virtual environment, run:

- Install virtualenv if it is not installed

`pip install virtualenv`

- Create a virtual environment

`virtualenv venv`

- Activate the virtual environment
- On Windows

`venv\Scripts\activate`

- On MacOS/Linux

`source venv/bin/activate`

### 3. Install Dependencies

Install the required Python packages using pip:

`pip install streamlit`

`pip install ollama`

### 4. Choose the model Llama3 as a local LLM model

`ollama run llama3`

### 5. Run the Application

To start the application, run:

`streamlit run coop_chatbot.py`
