from flask import Flask, jsonify
import requests

app = Flask(__name__)

jokes = []


def fetch_jokes():
    url = 'https://official-joke-api.appspot.com/jokes/random?category=chucknorris'
    for _ in range(10):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for HTTP errors
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
    app.run(host='localhost', port=5000, debug=True)
