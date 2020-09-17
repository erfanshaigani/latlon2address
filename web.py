from flask import Flask,request
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    geolocator = Nominatim(user_agent="teslam")
    lat = request.args['lat']
    lon = request.args['lon']
    try:
        location = geolocator.reverse([lat,lon])
        #location = geolocator.reverse("35.726748,51.486301")  
        return location.address
    except:
        return "not available erfan jan"
    #return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


