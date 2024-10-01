from flask import Flask, request, jsonify
from flask_cors import CORS
import folium
from geopy.geocoders import Nominatim
import requests

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
geolocator = Nominatim(user_agent="geoapi", timeout=10)

@app.route('/geo', methods=['POST'])
def geocode_addresses():
    data = request.json
    
    # 주소 URL
    process_url = 'http://process-api:5001/get_address'
    process_response = requests.get(process_url)
    
    if process_response.ok:
        process_data = process_response.json()
        addresses = [process_data['주소']] if '주소' in process_data else []
    else:
        return jsonify({"주소 호출 실패": process_response.text}), 500


    # 쿼리 파라미터에서 주소 요청
    addresses = data.get('addresses', [])
    store_names = data.get('storeNames', [])
    selected_index = data.get('selectedIndex', -1)

    # 더미 주소
    dummy_addresses = [
        "서울특별시 강서구 공항대로 247",
        "서울특별시 중구 다산로 36길 65"
    ]
    addresses += dummy_addresses  # 더미 주소 추가

    locations = []

    for address in addresses:
        location = geolocator.geocode(address)
        if location:
            locations.append((address, location.latitude, location.longitude))

    # 첫 번째 주소 = 시작 화면
    if locations:
        first_lat, first_lon = locations[0][1], locations[0][2]
        map_folium = folium.Map(location=[first_lat, first_lon], zoom_start=10)

        # folium 마커
        for idx, (address, lat, lon) in enumerate(locations):
            popup_text = store_names[idx] if idx < len(store_names) else "Unknown Store"
            popup = folium.Popup(popup_text, max_width=300) 

            if idx == selected_index:
                # 선택된 주소는 빨간 마커로 표시
                folium.Marker(
                    [lat, lon],
                    popup=popup,
                    icon=folium.Icon(color='red')
                ).add_to(map_folium)
            else:
                # 나머지는 기본 마커로 표시
                folium.Marker(
                    [lat, lon],
                    popup=popup
                ).add_to(map_folium)

        map_html = map_folium._repr_html_()
        return jsonify({'map_html': map_html})

    return jsonify({'message': "주소를 찾을 수 없습니다."})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)