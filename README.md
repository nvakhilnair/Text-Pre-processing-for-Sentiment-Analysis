# Text-Pre-processing-for-Sentiment-Analysis

Of all data, the text is the most unstructured form and so means we have a lot of cleaning to do. This API helps converts noise from high dimensional features to low dimensional space to obtain as much accurate information as possible from the text.

## Installation

Installation of required python libraries

```bash
  pip install -r requirement.txt
```

## Run Locally

1. To run this project run the following command in downloaded directory
```bash
  python manage.py runserver 127.0.0.1:9000
```


## Usage(Locally)

- Using curl
    ```bash
    curl -X POST https://text-pre-processing.herokuapp.com -H "Content-Type: application/json" -d "{\"text\":\"I need to watch the Entertaiment but power is not there\",\"corrector\":\"True\"}"
    ```
- Using Python
    ```bash
    import requests
    URL = "http://127.0.0.1:9000"
    data = {"text":"I am happy","corrector":"True"}
    r = requests.post(url = URL, data = data,headers={'Content-Type': 'application/json'})
    ```

## Deployment(Cloud)
The application is deployed on the cloud using heroku.  
link : https://text-pre-processing.herokuapp.com

```bash
    import requests
    URL = "https://text-pre-processing.herokuapp.com/"
    data = {"text":"I am happy","corrector":"True"}
    r = requests.post(url = URL, data = data,headers={'Content-Type': 'application/json'})
```
## Features

- No credentials required
- Responsive and Fast
- Can be easily integrated with any model or application

## Demo
https://text-pre-processing.herokuapp.com


## Tech Stack

**Client:** HTML, CSS

**Server:** Python, Django, Django Rest Framework




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
