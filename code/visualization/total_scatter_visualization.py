## 산점도 그래프
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('최종데이터_b.csv')

# 선택한 변수: 개체번호(obj_num)와 화방별 착과수(flw_get)
obj_num = df['obj_num']
flower_yield = df['flw_get']

# 산점도 그리기
plt.figure(figsize=(10, 6))
plt.scatter(obj_num, flower_yield, alpha=0.5, color='green')
plt.title('obj_num vs. flw_get')
plt.xlabel('obj_num')
plt.ylabel('flw_get')
plt.grid(True)
plt.show()