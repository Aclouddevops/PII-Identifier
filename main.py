# Importing necessary libraries
import streamlit as st  # Streamlit library for creating web apps
import pandas as pd  # Pandas library for data manipulation
import boto3  # AWS SDK for Python

# Function to identify PII in a given text
def identify_pii(text):
    # Creating a client for AWS Comprehend service
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-1')
    # Using the client to detect PII entities in the text
    response = comprehend.detect_pii_entities(Text=text, LanguageCode='en')
    # Returning a list of identified PII entities
    return [{'Type': entity['Type'], 'Text': text[entity['BeginOffset']:entity['EndOffset']]} for entity in response['Entities']]

# Function to create the Streamlit web app
def app():
    # Setting the title of the app
    st.title('PII Identifier')
    # Displaying a warning message
    st.warning('Please do not enter any Personally Identifiable Information (PII).')
    # Creating a text input field
    user_input = st.text_input("Enter some text")
    # Creating a button
    if st.button('Identify PII'):
        # If there is text in the input field
        if user_input:
            # Identifying PII in the text
            pii_entities = identify_pii(user_input)
            # If PII is identified
            if pii_entities:
                # Creating a DataFrame from the list of identified PII entities
                df = pd.DataFrame(pii_entities)
                # Displaying the user's comment and the DataFrame
                st.write("User's comment: ", user_input)
                st.dataframe(df)
            # If no PII is identified
            else:
                # Displaying a message saying so
                st.write("No PII identified in the comment: ", user_input)
        # If there is no text in the input field
        else:
            # Displaying a message asking the user to enter some text
            st.write("Please enter some text.")

# If the script is being run as a standalone script
if __name__ == "__main__":
    # Starting the app
    app()
