import pandas as pd

# Ler o arquivo XLSX
xlsx_file_path = 'Caminho do arquivo a ser convertido'
df = pd.read_excel(xlsx_file_path)

# Converter o DataFrame para JSON
json_file_path = 'caminho onde o arquivo sera salvo'
df.to_json(json_file_path, orient='records', force_ascii=False, indent=4)
