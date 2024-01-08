# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)


import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('최종데이터_b.csv')

# 선택한 변수: 농가(id), 일사량_외부, 엽수
selected_data = df[['id', 's_am_day', 'num_leaf']]

# 데이터를 농가(id)로 그룹화
grouped = selected_data.groupby('id')

# 이미지 파일 저장 폴더
image_folder = 'C:/Users/syk19/OneDrive/문서/캡스톤_사진/'

# 각 농가별로 일사량에 따른 엽수 시각화 및 이미지 파일 저장
for name, group in grouped:
    plt.figure(figsize=(12, 6))
    plt.plot(group['s_am_day'], group['num_leaf'], marker='o', linestyle='-', markersize=5)
    plt.title(f'{name} s_am_day vs num_leaf')
    plt.xlabel('s_am_day')
    plt.ylabel('num_leaf')
    plt.grid(True)

    # 이미지 파일로 저장
    image_filename = f'{image_folder}{name}_일사량_엽수2.png'
    plt.savefig(image_filename)

    # 그래프를 닫아 메모리를 확보
    plt.close()

# 모든 그래프를 생성한 후 마지막으로 이미지 폴더 경로를 출력
print(f'농가별 그래프 이미지가 저장된 폴더: {image_folder}')
