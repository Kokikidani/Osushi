from Osushi import app

from flask import Flask, render_template, jsonify, request
import folium
import osmnx as ox
import networkx as nx

start_point = (35.15860218649584, 136.9743955129251)  # 正門サイネージの座標
end_point = (35.15526895594977, 136.97969555815104)    # ボート乗り場の座標

# OpenStreetMapからグラフデータを取得 (歩道のみを含む)
G = ox.graph_from_place('Chikusa Ward, Nagoya, Japan', network_type='walk')


def calculate_route(start, end):
    start_node = ox.distance.nearest_nodes(G, start[1], start[0])
    end_node = ox.distance.nearest_nodes(G, end[1], end[0])
    route = nx.shortest_path(G, start_node, end_node, weight='length')
    route_coordinates = [[G.nodes[node]['y'], G.nodes[node]['x']] for node in route]
    return route_coordinates


# ルート計算の初期化
initial_route = calculate_route(start_point, end_point)




def add_markers_to_map(m, start_point, end_point):
    folium.Marker(
        location=start_point,
        icon=folium.Icon(color='green'),  # スタート地点のマーカーは緑色
        popup='Start Point'  # マーカーにポップアップを追加
    ).add_to(m)


    # ゴール地点のマーカーを追加
    folium.Marker(
        location=end_point,
        icon=folium.Icon(color='red'),  # ゴール地点のマーカーは赤色
        popup='End Point'  # マーカーにポップアップを追加
    ).add_to(m)
# OpenStreetMapからグラフデータを取得 (歩道のみを含む)


m = folium.Map(location=[(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2], zoom_start=17, width=300, height=400)


start_node = ox.distance.nearest_nodes(G, start_point[1], start_point[0])
end_node = ox.distance.nearest_nodes(G, end_point[1], end_point[0])
route = nx.shortest_path(G, start_node, end_node, weight='length')
route_coordinates = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]










@app.route('/')
def index():
    # Foliumを使用して地図を表示
    m = folium.Map(location=[(start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2], zoom_start=16)

    # ルートを地図に追加
    folium.PolyLine(locations=route_coordinates, color='blue').add_to(m)

    # 地図をHTMLに変換してテンプレートに渡す
    map_html = m._repr_html_()
    return render_template('index.html', map_html=map_html)

@app.route('/form')
def form():
    return render_template(
        'form.html'
    )

@app.route('/update_location', methods=['POST'])
def update_location():
    global start_point
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    start_point = (float(lat), float(lon))

    # 新しいルートを計算
    new_route = calculate_route(start_point, end_point)
    return jsonify(new_route)  # ルート座標をJSONで返す