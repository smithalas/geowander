from flask import Flask, render_template
import folium 

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (51.5, -0.12)
    folium_map = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    folium_map.save('templates/map.html')
    return render_template('index.html')

@app.route('/')
def render_the_map():
    return render_template('the_map.html')

if __name__ == '__main__':
    app.run(debug=True)