import xgboost as xgb
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("최최종데이터_a_지난주추가.csv", encoding = "cp949")
df = df.drop(columns=['week_start_date'])

def xgboost(df):
    # 스케일링할 열 선택
    columns_to_scale = df.columns[4:]

    # RobustScaler 객체 생성
    scaler = RobustScaler()

    # 선택한 열 스케일링
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    # 주(week) 정보를 기준으로 데이터를 그룹화
    week_groups = df.groupby('week')

    # 5주차부터 25주차까지를 훈련 데이터로 선택
    train_weeks = list(range(5, 26))
    train_data = pd.concat([group for week, group in week_groups if week in train_weeks])

    # 26주차부터 30주차까지를 테스트 데이터로 선택
    test_weeks = list(range(26, 31))
    test_data = pd.concat([group for week, group in week_groups if week in test_weeks])

    # 독립 변수와 종속 변수 분리
    X_train = train_data.drop(columns=['flw_get'])  # 'flw_get' 및 'week_start_date' 열 제거
    y_train = train_data['flw_get']
    X_test = test_data.drop(columns=['flw_get'])  # 'flw_get' 및 'week_start_date' 열 제거
    y_test = test_data['flw_get']

    X_train = X_train[columns_to_scale]
    X_test = X_test[columns_to_scale]

    return X_train, y_train, X_test, y_test

X_train, y_train, X_valid, y_valid = xgboost(df)

# XGBoost 모델 생성
model = xgb.XGBRegressor(
    n_estimators=1000,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.8,
    random_state=100,
    n_jobs=-1  # 병렬처리 활성화
)

# 모델 훈련
model.fit(X_train, y_train)

# 검증 세트로 예측
y_pred = model.predict(X_valid)

# 평가 지표 계산 (평균 제곱 오차)
mse = mean_squared_error(y_valid, y_pred)
print(f"MSE: {mse}")

# 하이퍼파라미터 그리드 설정
param_grid = {
    'n_estimators': [500, 1000],
    'max_depth': [4, 5, 6],
    'learning_rate': [0.05],
    'subsample': [0.8, 0.9]
}

# GridSearchCV 생성
grid_search = GridSearchCV(
    estimator=xgb.XGBRegressor(random_state=100, n_jobs=-1),
    param_grid=param_grid,
    scoring='neg_mean_squared_error',
    cv=3
)

# 그리드 서치를 사용하여 최적의 모델 훈련
grid_search.fit(X_train, y_train)

# 최적의 하이퍼파라미터 출력
print("Best Parameters:", grid_search.best_params_)

# 최적의 모델 얻기
best_model = grid_search.best_estimator_

# 최적의 모델로 예측
y_pred = best_model.predict(X_valid)

# 최적의 모델로 평가 지표 계산
mse = mean_squared_error(y_valid, y_pred)
print(f"MSE (Best Model): {mse}")

# 예측 결과 시각화
plt.figure(figsize=(15, 10))
plt.plot(range(len(y_valid)), y_valid, color='blue', label='Actual')
plt.plot(range(len(y_pred)), y_pred, color='red', label='Predicted')
for i in range(1, 11):
    plt.axvline(x=20*i, linestyle='dotted', color='gray')
plt.title("Actual vs. Predicted")
plt.legend()
plt.show()