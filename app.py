# ChatBot using LangChain and HuggingFace in Python

# libraries
import os
from dotenv import load_dotenv
from pathlib import Path
import json
import falcon
from langchain_huggingface import HuggingFaceEndpoint
import time
from time import sleep

# load environment variables from .env
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(os.path.join(BASE_DIR, '.env'))
hugging_face_token = os.getenv('TOKEN')

# set up the LangChain and HuggingFaceEndpoint
llm = HuggingFaceEndpoint(repo_id='tiiuae/falcon-7b-instruct',
                          huggingfacehub_api_token=hugging_face_token)

# define the Falcon Resource for Chatbot
class ChatbotResource:
    def on_post(self, req, resp):
        """Handles POST requests with user queries in a streaming fashion."""
        try:
            # parse the user query from the request body
            data = json.load(req.bounded_stream)
            user_query = data.get("query")

            # generate and stream the response
            resp.status = falcon.HTTP_200
            resp.content_type = 'text/plain; charset=utf-8'
            resp.stream = self.stream_response(user_query)

        except Exception as e:
            # handle any errors
            resp.media = {"error": str(e)}
            resp.status = falcon.HTTP_500

    def stream_response(self, query):
        """Yields the response one chunk at a time."""
        response = llm.invoke(query)
        for chunk in response:
            yield chunk.encode('utf-8')  
            time.sleep(0.05)  

# create Falcon API and add the Chatbot Resource
app = falcon.App()
chatbot = ChatbotResource()
app.add_route('/chatbot', chatbot)

# serve the static file
class StaticResource:
    def on_get(self, req, resp):
        """Serve the static index.html file."""
        resp.content_type = 'text/html; charset=utf-8'
        with open('index.html', 'r', encoding='utf-8') as f:
            resp.text = f.read()

static = StaticResource()
app.add_route('/', static)
