import folium


def draw_map(gps):
    begin = True
    fmap = None
    point_lat = 0
    point_lng = 0
    points = []
    for item in gps:
        if item['lat'] is None or item['lng'] is None:
            continue

        if begin:
            fmap = folium.Map(location=[item['lat'], item['lng']], zoom_start=15)
            marker = folium.Marker(location=[item['lat'], item['lng']], popup='begin',
                                   icon=folium.Icon(icon='info-sign', color='red'))
            begin = False
        else:
            marker = folium.Marker(location=[item['lat'], item['lng']], popup=f'<b>{item["created_at"]}</b>')

        points.append([float(item['lat']), float(item['lng'])])
        fmap.add_child(child=marker)
        point_lat = item['lat']
        point_lng = item['lng']

    # folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(fmap)
    if len(points) > 1:
        marker = folium.Marker(location=[point_lat, point_lng], popup='<b>end</b>',
                               icon=folium.Icon(icon='info-sign', color='green'))
        fmap.add_child(child=marker)
    if fmap is not None:
        fmap.save("index.html")
