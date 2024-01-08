# 누적 일사량 계산

import pandas as pd

df = pd.read_csv('38번농가_h2.csv', encoding='ansi')

df['측정시간'] = pd.to_datetime(df['측정시간'])

df['일사량_외부'] = df['일사량_외부'] * 100

# 날짜를 기준으로 그룹화하여 누적값 계산
df['누적일사량_외부'] = df.groupby(df['측정시간'].dt.date)['일사량_외부'].cumsum()

df.to_csv('38번농가_최종.csv', index=False, encoding='ansi')