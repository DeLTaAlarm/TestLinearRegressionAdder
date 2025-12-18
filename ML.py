from sklearn import datasets, linear_model, metrics, model_selection
import pandas as pd

def train(dataset):
    df = pd.read_csv(dataset, skipinitialspace=True)
    X = df[['a', 'b']]
    y = df['c']

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=42)

    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("MAE:", metrics.mean_absolute_error(y_test, y_pred))
    print("R2:", metrics.r2_score(y_test, y_pred))

    return model

model = train("datasetBig.csv")

while True:
    a = float(input("Введите a: "))
    b = float(input("Введите b: "))

    input_data = pd.DataFrame([[a, b]], columns=['a', 'b'])

    prediction = model.predict(input_data)

    print(f"{a} + {b} = {prediction[0]:.2f}")
