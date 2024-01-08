## 히트맵 그래프
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
	
# 데이터 불러오기
df = pd.read_csv('최종데이터_b.csv')

# 농가명(id)을 기준으로 그룹화
grouped = df.groupby('id')

# 각 농가별 상관 행렬 및 히트맵 그리기
for name, group in grouped:
    correlation_matrix = group.corr()

    plt.figure(figsize=(12, 8))

    # 히트맵 그리기
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

    # 그래프 제목에 id명 추가
    plt.title(f'{name} id_correlation')

    # # id명을 그래프 위에 추가
    # plt.text(0.5, -0.1, f'id: {name}', horizontalalignment='center', verticalalignment='center',
    #          transform=plt.gca().transAxes)

    plt.show()