# FastAPI Text Processing API

This FastAPI project provides an endpoint to process and clean uncleaned text data for NLP applications. Also option for auto spelling corrector is present which is optional query parameter

## Endpoint

- `/process_text`: This endpoint accepts uncleaned text data and returns the cleaned text in JSON format.

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Docker

To containerize the application using Docker, follow these steps:

1. Build the Docker image: 
    ```
    docker build -t fastapi-text-processing .
    ```
2. Run the Docker container: 
    ```
    docker run -d -p 8000:8000 fastapi-text-processing
    ```


## Starting the Application

To start the application, you can use the provided batch (.bat) or shell (.sh) files:

- For Windows (.bat): 
    ```
    start_app.bat
    ```
- For Unix-based systems (.sh):
    ```
    ./start_app.sh
    ```

Ensure that you have installed the required dependencies mentioned in `requirements.txt` before starting the application.

## Usage

To utilize the text processing API provided by this project, you can send a `GET` request to the `/process_text` endpoint. Below is an example `curl` command demonstrating how to use the endpoint:

### using curl
```
curl 'http://127.0.0.1:8000/process_text/?input_text=Hello%20my%20name%20is%20akhil&autocorrector=false
```

### using python

```
import requests

url = 'http://127.0.0.1:8000/process_text/'
params = {
    'input_text': 'Hello my name is akhil',
    'autocorrector': 'false'
}
response = requests.get(url, params=params)
```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Feedback

If you have any feedback, please reach out to us at madewithpy009@gmail.com

For support, email madewithpy009@gmail.com.## 🚀 About Me
- 👋 Hi, I’m @nvakhilnair
- 👀 I’m interested in Data Science,Machine learning, Data Mining, Data Visualization and Programing
- 🌱 I’m currently open to work
- 📫 How to reach me https://www.linkedin.com/in/akhilnvnair
## Authors

- [@nvakhilnair](https://github.com/nvakhilnair)
