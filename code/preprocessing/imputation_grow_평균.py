import pandas as pd

# CSV 파일로부터 데이터를 읽어옴
df = pd.read_csv('23번농가_imp.csv', encoding='ansi')

# 'temp_int', 'hum_int', 'CO2', 'st' 컬럼의 데이터 빈 값에 대해 각 컬럼의 평균값으로 채우기
columns_to_fill = ['temp_int', 'hum_int', 'CO2', 'st']

for col in columns_to_fill:
    # 각 컬럼의 평균값 계산
    mean_value = df[col].mean()

    # 빈 값을 평균값으로 채우기
    df[col].fillna(mean_value, inplace=True)

# 결과를 CSV 파일로 내보냄
df.to_csv('23번농가_imp2.csv', index=False, encoding='ansi')