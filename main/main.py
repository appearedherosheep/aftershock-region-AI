from model import PolyLR, LongMinorAxis, returnEllipse
import folium
import numpy as np
import pandas as pd

model = PolyLR()
# # seki


# def FormulaSeki(M):
#     return 10**(1.02*M - 4.01)


# FormulaSeki_vec = np.vectorize(FormulaSeki)
# # smith


# def FormulaSmith(M):
#     return 10**(M-3.34)


# FormulaSmith_vec = np.vectorize(FormulaSmith)

경주_규모 = 5.8
경주_경위도 = (35.75, 129.18)
경주_region = model.predict([[경주_규모]])
# 경주_region2 = FormulaSeki_vec(경주_규모)
# 경주_region3 = FormulaSmith_vec(경주_규모)

경주_장축, 경주_단축 = LongMinorAxis(경주_region)
경주_ellipse = returnEllipse(경주_경위도, theta=230, Long=경주_장축, Minor=경주_단축)
경주_poly = [[x, y] for x, y in 경주_ellipse.exterior.coords]
print(경주_region, 경주_장축, 경주_단축)

# 경주_장축2, 경주_단축2 = LongMinorAxis(경주_region2)
# 경주_ellipse2 = returnEllipse(경주_경위도, theta=230, Long=경주_장축2, Minor=경주_단축2)
# 경주_poly2 = [[x, y] for x, y in 경주_ellipse2.exterior.coords]
# print(경주_region2, 경주_장축2, 경주_단축2)

# 경주_장축3, 경주_단축3 = LongMinorAxis(경주_region3)
# 경주_ellipse3 = returnEllipse(경주_경위도, theta=230, Long=경주_장축3, Minor=경주_단축3)
# 경주_poly3 = [[x, y] for x, y in 경주_ellipse3.exterior.coords]
# print(경주_region3, 경주_장축3, 경주_단축3)

html_경주 = """<h1 style="margin-bottom:0;"><b>경주 지진</b></h1> <br/>
         <p style="margin:0;font-size:15px;"> 진원: KMA 35.77°N 129.18°E<br/> 여진역: 152.1km<sup>2</sup><br/>
           장축: 28.2km<br/>
           단축: 5.3km</p>
"""
popup_경주 = folium.Popup(html_경주, min_width=200, max_width=200)


포항_규모 = 5.4
포항_경위도 = (36.11, 129.37)
포항_region = model.predict([[포항_규모]])
# 포항_region2 = FormulaSeki_vec(포항_규모)
# 포항_region3 = FormulaSmith_vec(포항_규모)

포항_장축, 포항_단축 = LongMinorAxis(포항_region)
print(포항_region, 포항_장축, 포항_단축)
포항_ellipse = returnEllipse(포항_경위도, theta=13, Long=포항_장축, Minor=포항_단축)
포항_poly = [[x, y] for x, y in 포항_ellipse.exterior.coords]

# 포항_장축2, 포항_단축2 = LongMinorAxis(포항_region2)
# 포항_ellipse2 = returnEllipse(포항_경위도, theta=230, Long=포항_장축2, Minor=포항_단축2)
# 포항_poly2 = [[x, y] for x, y in 포항_ellipse2.exterior.coords]
# print(포항_region2, 포항_장축2, 포항_단축2)

# 포항_장축3, 포항_단축3 = LongMinorAxis(포항_region3)
# 포항_ellipse3 = returnEllipse(포항_경위도, theta=230, Long=포항_장축3, Minor=포항_단축3)
# 포항_poly3 = [[x, y] for x, y in 포항_ellipse3.exterior.coords]
# print(포항_region3, 포항_장축3, 포항_단축3)

html_포항 = """<h1 style="margin-bottom:0;"><b>포항 지진</b></h1> <br/>
         <p style="margin:0;font-size:15px;"> 진원: KMA 36.11°N 129.36°E<br/> 여진역: 53.6km<sup>2</sup><br/>
           장축: 16.7km<br/>
           단축: 3.2km</p>
"""
popup_포항 = folium.Popup(html_포항, min_width=200, max_width=200)


m = folium.Map([35.9260, 129.2585], zoom_start=10)

양산단층 = [[35.21, 128.83], [36.27, 129.54]]
울산단층 = [[35.9225, 129.2984], [35.5000, 129.3822]]
folium.PolyLine(locations=양산단층, tooltip='양산단층',
                color='#25292e', weight='7').add_to(m)
folium.PolyLine(locations=울산단층, tooltip='울산단층',
                color='#25292e', weight='7').add_to(m)


folium.Polygon(경주_poly, fill='Cartodb Positron',
            #    color='#1e3e50',
               #    fill_color='#fffggg',
               popup=popup_경주,
               tooltip='경주 지진 여진역 인공지능의 예측 범위').add_to(m)

# folium.Polygon(경주_poly2, fill='Cartodb Positron',
#                color='#2c5b76',
#                #    fill_color='#fffggg',
#                popup=popup_경주,
#                tooltip='경주 지진 여진역 seki 공식의 예측 범위').add_to(m)

# folium.Polygon(경주_poly3, fill='Cartodb Positron',
#                color='#4895c2',
#                #    fill_color='#fffggg',
#                popup=popup_경주,
#                tooltip='경주 지진 여진역 smith 공식의 예측 범위').add_to(m)

folium.Circle(location=경주_경위도, radius=400, color='#000000',
              fill='crimson', weight='10', tooltip='경주 지진 진앙').add_to(m)


folium.Polygon(포항_poly, fill='Cartodb Positron',
               #    color='#ffffgg',
               #    fill_color='#fffggg',
               popup=popup_포항,
               tooltip='포항 지진 여진역 예측 범위').add_to(m)


folium.Circle(location=포항_경위도, radius=400, color='#000000',
              fill=True, weight='10', tooltip='포항 지진 진앙').add_to(m)

# path = 'D:/github/aftershock-region-AI/data/포항_여진.csv'
# data = pd.read_csv(path)
# data = data.dropna()
# 포항여진_위도 = data['latitude']
# 포항여진_경도 = data['longtitude']
# for i in range(len(data)):
#     folium.Circle(location=(포항여진_위도[i], 포항여진_경도[i]), radius=300, color='#e03124',
#                   fill=True, weight='10', tooltip='포항 여진').add_to(m)

# path2 = 'D:/github/aftershock-region-AI/data/경주_여진.csv'
# data2 = pd.read_csv(path2)
# data2 = data2.dropna()
# 경주여진_위도 = data2['latitude']
# 경주여진_경도 = data2['longtitude']
# print(경주여진_경도[3],경주여진_위도[3])
# for j in range(len(data2)):
#     folium.Circle(location=(경주여진_위도[j], 경주여진_경도[j]), radius=300, color='#ff5426',
#                   fill=True, weight='10', tooltip='경주 여진').add_to(m)

m.add_child(folium.LatLngPopup())
m.save('index.html')
