import json

# المسار إلى ملف الجيوجيسون
file_path = 'alx.geojson'
# فتح الملف وقراءة البيانات
with open(file_path, 'r', encoding='utf-8') as file:
    geojson_data = json.load(file)

# طباعة محتويات ملف الجيوجيسون
print(json.dumps(geojson_data, indent=2, ensure_ascii=False))
