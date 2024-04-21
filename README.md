# PII Identifier

PII Identifier is a Python script that leverages the Streamlit library to build a web application. The application's purpose is to identify Personally Identifiable Information (PII) within a provided text. It utilizes the AWS Comprehend service for PII entity detection.

## Libraries Used

- **Streamlit**: Utilized for web application creation.
- **Pandas**: Employed for data manipulation tasks.
- **boto3**: The AWS SDK for Python, used for interaction with AWS services.

## Functions

- **identify_pii(text)**: This function accepts a text string as input and uses the AWS Comprehend service to identify PII entities within the text. It returns a list of dictionaries, each containing the type and text of an identified PII entity.

- **app()**: This function builds the Streamlit web application. It displays a warning message to the user, provides a text input field for the user to enter text, and a button to identify PII in the entered text. If PII entities are identified, they are displayed in a DataFrame. If no PII entities are identified, a message is displayed to inform the user. If no text is entered, a message prompts the user to enter some text.

## Execution

If the script is executed as a standalone script, the `app()` function is invoked to start the web application.
