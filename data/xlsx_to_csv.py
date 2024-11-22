import pandas as pd
from pathlib import Path

xlsx_folder = Path('./xlsx_files')
latest_xlsx = max(xlsx_folder.glob('*.xlsx'), key=lambda f: f.stat().st_mtime)
excel_file = latest_xlsx

df = pd.read_excel(excel_file)
df.replace('\n', ' ', regex=True, inplace=True) #过滤自定义输入中的换行符，防止污染csv格式
df.replace(',', '，', regex=True, inplace=True) #过滤自定义输入中的英文逗号……

df = df.map(lambda x: str(int(x)) 
            if isinstance(x, float) and x.is_integer() 
            else x) #将数据中的浮点数转换为字符串

csv_file = 'original_data.csv'
df.to_csv(csv_file, index=False, encoding='utf-8')