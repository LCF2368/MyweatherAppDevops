from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = {}
    if request.method == 'POST':
        city = request.form['city']
        api_key = '838bf7d296ff583b7feb835c07808cf0'  # Replace with your actual API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            weather_data['error'] = 'City not found!'
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
