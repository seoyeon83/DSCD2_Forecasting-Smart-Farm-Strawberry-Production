import pandas as pd

# 데이터를 불러옵니다. 파일 경로를 적절히 설정해야 합니다.
data = pd.read_csv('환경데이터_최종.csv', encoding='ansi')

# 데이터를 날짜 및 시간 열로 변환합니다.
data['realTime'] = pd.to_datetime(data['realTime'])


# 편차를 계산하는 함수
def calculate_deviation(data, column):
    return data.groupby(['realTime', 'name'])[column].transform(func='mean')


# 결측치를 보간합니다.
columns_to_interpolate = ['temp_ex', 'temp_int', 'hum_int', 'CO2', 'st']

for column in columns_to_interpolate:
    # 결측치의 인덱스를 찾습니다.
    missing_data_mask = data[column].isnull()

    for index in missing_data_mask.index[missing_data_mask]:
        # 해당 시간대와 컬럼에 대한 편차 평균값을 가져옵니다.
        deviation_mean = calculate_deviation(data, column).loc[index]

        # 편차 평균값을 사용하여 결측치를 채웁니다.
        data.loc[index, column] = deviation_mean

# 결과를 저장하거나 필요한 작업을 수행합니다.
data.to_csv('보간된_데이터.csv', index=False, encoding='ansi')