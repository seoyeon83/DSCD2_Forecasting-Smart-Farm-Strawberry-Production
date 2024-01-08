import pandas as pd
from scipy import interpolate

# CSV 파일로부터 데이터를 읽어옴
df = pd.read_csv('23번농가.csv', encoding='ansi')

# 'temp_int', 'CO2', 'st' 컬럼에 대해 선형 보간 수행
columns_to_interpolate = ['temp_int', 'hum_int','CO2', 'st']
for col in columns_to_interpolate:
    df[col] = df[col].interpolate(method='linear')

# 결과를 CSV 파일로 내보냄
df.to_csv('23번농가_imp.csv', index=False, encoding='ansi')