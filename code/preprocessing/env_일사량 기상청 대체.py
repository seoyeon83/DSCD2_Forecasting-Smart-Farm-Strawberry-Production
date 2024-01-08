import pandas as pd

# CSV 파일을 'euc-kr' 인코딩으로 읽기
df1 = pd.read_csv('26번농가_imp.csv', encoding='euc-kr')
df2 = pd.read_csv('26_전북남원_순창.csv', encoding='euc-kr')

merged_df = pd.merge(df1, df2, left_on='측정시간', right_on='일시', how='left')

# 새로운 컬럼을 만들어 값을 할당
df1['일사량'] = merged_df['일사(MJ/m2)'].fillna(0)

df1.to_csv('26번.csv', index=False, encoding='utf-8-sig')