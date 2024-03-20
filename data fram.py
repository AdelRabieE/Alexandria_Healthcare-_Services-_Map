import json
import pandas as pd


file_path = 'alx.geojson'

#عايز اتاكد ان المسار صح وان كمان الملف موجود؟
try:
    # فتح الملف وتحميل البيانات
    with open(file_path, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    # تحويل البيانات لـ DataFrame
    df = pd.json_normalize(geojson_data['features'])

    # عرض أول 5 صفوف للتأكد من البيانات
    print(df.head())

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
