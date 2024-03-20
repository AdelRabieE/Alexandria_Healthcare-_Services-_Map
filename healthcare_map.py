import sqlite3
import folium

database_path = "C:\\Users\\0\\Desktop\\p2\\locations.db"

# الاتصال بالداتا بيز
conn = sqlite3.connect(database_path)
cur = conn.cursor()

# كويري للحصول علي الداتات
cur.execute('SELECT name, type, latitude, longitude FROM locations')
locations = cur.fetchall()

#  اغلاق الاتصال بالداتا بيز
conn.close()

# إنشاء خريطة باستخدام Folium
map = folium.Map(location=[30.033333, 31.233334], zoom_start=12) # استخدم موقع مركزي للخريطة

# إضافة نقاط إلى الخريطة
for loc in locations:
    folium.Marker(
        location=[loc[2], loc[3]],
        popup=f'{loc[1]}: {loc[0]}',
    ).add_to(map)

# حفظ الخريطة في ملف HTML
map.save('map.html')
