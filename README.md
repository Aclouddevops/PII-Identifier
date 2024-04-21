# PII-Identifier
PII Identifier
This Python script uses the Streamlit library to create a web application that identifies Personally Identifiable Information (PII) in a given text. It uses the AWS Comprehend service to detect PII entities.

## Libraries Used

Streamlit: This library is used to create the web application.
Pandas: This library is used for data manipulation.
boto3: This is the AWS SDK for Python, used to interact with AWS services.

### Functions
identify_pii(text)
This function takes a string of text as input and uses the AWS Comprehend service to identify PII entities in the text. It returns a list of dictionaries, where each dictionary contains the type and text of an identified PII entity.

### app()

This function creates the Streamlit web application. It displays a warning message to the user, provides a text input field for the user to enter some text, and a button to identify PII in the entered text. If PII entities are identified in the text, they are displayed in a DataFrame. If no PII entities are identified, a message is displayed saying so. If no text is entered, a message is displayed asking the user to enter some text.

### Execution

If the script is run as a standalone script, the app() function is called to start the web application.


