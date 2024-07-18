# Chuck Norris jokes with Flask framework

from flask import Flask, jsonify
import requests

app = Flask(__name__)

jokes = []


def fetch_jokes():
    # url = 'http://api.icndb.com/jokes/random/'
    url = 'https://official-joke-api.appspot.com/jokes/random?category=chucknorris'
    for _ in range(10):
        # error handling
        try:
            response = requests.get(url)
            response.raise_for_status()
            joke_data = response.json()
            jokes.append(joke_data)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the joke: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


# Fetch jokes when the server starts
fetch_jokes()


@app.route('/getJokes', methods=['GET'])
def get_jokes():
    return jsonify(jokes)


if __name__ == '__main__':
    # set the endpoint to http://localhost:5000/getJokes
    app.run(host='localhost', port=5000, debug=True)
