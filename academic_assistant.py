from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# IBM Watson setup
def setup_watson_assistant():
    authenticator = IAMAuthenticator('xuYxwXTjo0u-EofayBxP0Cub-Rmcn66fIlz-iqesKtpw')  # Replace with your API key
    assistant = AssistantV3(
        version='2021-06-14',
        authenticator=authenticator
    )
    assistant.set_service_url('https://api.au-syd.assistant.watson.cloud.ibm.com/instances/1f29ac1e-49fe-4ddc-b486-8f18fbda95d6')  # Replace with your URL
    return assistant

# Define the ask_bot function to handle user queries
def ask_bot(user_input):
    # Initialize Watson Assistant client
    assistant = setup_watson_assistant()
  
    # Create a session with Watson Assistant
    session_response = assistant.create_session(
        assistant_id='9a6aa849-05d4-41ef-aaa7-4654c0ed3336'
    ).get_result()
    session_id = session_response['session_id']
  
    try:
        # Send user input to Watson Assistant
        response = assistant.message(
            assistant_id='9a6aa849-05d4-41ef-aaa7-4654c0ed3336',
            session_id=session_id,
            input={
                'message_type': 'text',
                'text': user_input
            }
        ).get_result()

        # Check if Watson has a valid response
        watson_response = response['output'].get('generic')
        if watson_response:
            return watson_response[0]['text']
        else:
            return "I'm sorry, I couldn’t find any information on that topic."
    finally:
        # Clean up by deleting the session
        assistant.delete_session(
            assistant_id='9a6aa849-05d4-41ef-aaa7-4654c0ed3336',
            session_id=session_id
        )
