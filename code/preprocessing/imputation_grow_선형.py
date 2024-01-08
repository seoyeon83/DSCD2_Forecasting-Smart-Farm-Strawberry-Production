import pandas as pd

# CSV 파일로부터 데이터를 읽어옴
df = pd.read_csv('23번농가_생육.csv', encoding='ansi')

# 개체번호(1, 2, 3, 4) 별로 선형 보간 수행
df['액아 개수'] = df.groupby('개체번호')['액아 개수'].transform(lambda x: x.interpolate(method='linear'))
df['초장'] = df.groupby('개체번호')['초장'].transform(lambda x: x.interpolate(method='linear'))
df['엽수'] = df.groupby('개체번호')['엽수'].transform(lambda x: x.interpolate(method='linear'))
df['엽장'] = df.groupby('개체번호')['엽장'].transform(lambda x: x.interpolate(method='linear'))
df['엽폭'] = df.groupby('개체번호')['엽폭'].transform(lambda x: x.interpolate(method='linear'))
df['엽병장'] = df.groupby('개체번호')['엽병장'].transform(lambda x: x.interpolate(method='linear'))
df['관부직경'] = df.groupby('개체번호')['관부직경'].transform(lambda x: x.interpolate(method='linear'))

# '엽수' 컬럼을 정수로 변환
df['엽수'] = df['엽수'].astype(int)

# 결과를 CSV 파일로 내보냄
df.to_csv('23번농가_생육.csv', index=False, encoding='ansi')