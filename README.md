# ChatBot using LangChain, HuggingFace and Falcon in Python

## Features
- To run the server, use gunicorn with the command: `gunicorn -b 0.0.0.0:8000 app:app`
- Loads environment variables from a .env file, you can obtain one from here: `https://huggingface.co/settings/tokens`
- Utilizes the HuggingFaceEndpoint from LangChain to interact with the Falcon model (tiiuae/falcon-7b-instruct) for generating responses.
- Sets up a web server using the Falcon framework to handle incoming HTTP requests.
- The chatbot simulates real-time writing effects, enhancing user engagement by displaying responses as if they are being typed out.
- Returns plain text responses from the model, which can be easily displayed in the user interface.
- While not directly implemented in app.py, the static HTML served can be designed to be mobile-responsive, making the chatbot accessible on various devices.

## Acknowledgments

**Python3**: [http://bit.ly/python3-certifications](http://bit.ly/python3-certifications)  
**LangChain**: [https://bit.ly/langchain-certification](https://bit.ly/langchain-certification)
<br>


## Demo Video

Here is a GIF demonstrating the key features of the application:

![Demo Video](https://github.com/marius2347/ChatBot-using-LangChain-and-HuggingFace-in-Python/blob/main/video.gif)

> Note: The GIF may take some time to load due to its size.

## Contact

**Email**: mariusc0023@gmail.com
