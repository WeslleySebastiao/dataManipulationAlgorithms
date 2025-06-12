import pandas as pd

# Ler o arquivo XLSX
xlsx_file_path = 'C:/Users/eaws00155707/Desktop/Agente/Pasta1.xlsx'
df = pd.read_excel(xlsx_file_path)

# Converter o DataFrame para JSON
json_file_path = 'C:/Users/eaws00155707/Desktop/Agente/JSON/ods+iniciativas.JSON'
df.to_json(json_file_path, orient='records', force_ascii=False, indent=4)
