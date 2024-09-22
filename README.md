# ChatBot using LangChain, HuggingFace & Falcon in Python

## Features
- To run the server, use gunicorn with the command: `gunicorn -b 0.0.0.0:8000 app:app`
- Loads environment variables from a .env file, allowing for secure handling of sensitive information (like API tokens).
- Utilizes the HuggingFaceEndpoint from LangChain to interact with the Falcon model (tiiuae/falcon-7b-instruct) for generating responses.
- Sets up a web server using the Falcon framework to handle incoming HTTP requests.
- The chatbot simulates real-time writing effects, enhancing user engagement by displaying responses as if they are being typed out.
- Returns plain text responses from the model, which can be easily displayed in the user interface.
- While not directly implemented in app.py, the static HTML served can be designed to be mobile-responsive, making the chatbot accessible on various devices.

## Acknowledgments

**Python3**: [http://bit.ly/python3-certifications](http://bit.ly/python3-certifications)  
**LangChain**: [https://www.datacamp.com/completed/statement-of-accomplishment/course/813915691e025008dddb4df55113ed906b57d93a](https://www.datacamp.com/completed/statement-of-accomplishment/course/813915691e025008dddb4df55113ed906b57d93a)
<br>


## Demo Video

Here is a GIF demonstrating the key features of the application:

![Demo Video](https://github.com/marius2347/Automatic-Speech-Recognition-using-Deep-Learning-in-Python/blob/main/video.gif)

> Note: The GIF may take some time to load due to its size.

## Contact

**Email**: mariusc0023@gmail.com
