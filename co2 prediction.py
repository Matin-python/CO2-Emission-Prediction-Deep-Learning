import pandas as pd
from matplotlib import pyplot as plt

from keras_visualizer import visualizer

from keras.models import Sequential
from keras.layers import Dense

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('co2.csv')
df.head(10)
df.describe()

# Build neural network
model = Sequential()
model.add(Dense(20, input_dim= 5, activation= 'relu'))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer="adam", metrics=["mean_squared_error"])
model.summary()

visualizer(model, file_name="model_DL", file_format="png")

# Preprocess data
X = df.drop('out1',axis=1)
y = df.out1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)


'''
note: If you normalize your data, the output will be slightly better, 
in addition, you will reach the final output with less training.
'''
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)


# Train model
history = model.fit(
                    X_train,
                    y_train, 
                    epochs=200,
                    verbose= 1)
y_pred = model.predict(X_test, verbose= 0)
print("y_pred= ", y_pred)
print()
print("y_test= ", y_test)

# Evaluate
print("metrics.mean_squared_error= ", mean_squared_error(y_test, y_pred))
print("mean_squared_error= ", history.history['loss'][-1])

# Visualize
er=history.history['loss']
er=er[5:]
plt.close()
plt.plot(er)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.grid(True)
plt.show()