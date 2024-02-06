import streamlit as stream
from streamlit_chat import message
from dotenv import load_dotenv
import os
import requests


from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)


def init():

        # Load the OpenAI API key from the environment variable
    load_dotenv()
    
    # test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")




    stream.set_page_config(
        page_title="DataBase ChatGPT",
        page_icon="🤖"
        )





def main():
    
    init()

    chat = ChatOpenAI(model_name="gpt-4",temperature=0)

    def fetch_data_from_backend(user_input):
    # Replace this with your actual API endpoint
        api_url = "http://127.0.0.1:8000/api/v1/code-explain/"
        payload = {"_input": user_input}

        try:
            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 201:
                # return {"info": f"Success: {response.status_code} - {response.text}"}
                return response.json()
            else:
                return {"error": f"Error: {response.status_code} - {response.text}"}
        except Exception as e:
            return {"error": f"Error: {str(e)}"}


    # initialize message history
    if "messages" not in stream.session_state:
        stream.session_state.messages = [
            SystemMessage(content="You are a helpful assistant.")
        ]



    stream.header("DataBase GPT 🤖")

    # with stream.sidebar:
    user_input = stream.chat_input("Your Query: ", key ="user_input")

# handle user input
    if user_input:
        stream.session_state.messages.append(HumanMessage(content=user_input))
        with stream.spinner("Thinking..."):
            response = chat(stream.session_state.messages)
            print("OpenAI GPT Response:", response.content)
            # Fetch data from the custom API endpoint based on user input
            endpoint_response = fetch_data_from_backend(user_input)
            print("API Endpoint Response:", endpoint_response)
            # if "info" in endpoint_response:
            #     combined_info = f"ChatBOT:\nOutput: {endpoint_response['info']}"
            #     stream.session_state.messages.append(AIMessage(content=combined_info))
            if "error" not in endpoint_response:
            # Assuming the API response contains relevant data
                # stream.session_state.messages.append(AIMessage(content=endpoint_response.content))
                output_content = endpoint_response.get("_output", "")
                stream.session_state.messages.append(AIMessage(content=str(output_content)))
            else:
                stream.warning(endpoint_response["error"])

    # display message history
    messages = stream.session_state.get('messages', [])
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')


if __name__ == "__main__":
    main()