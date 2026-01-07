import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('titanic.csv')

# Bagi data menjadi fitur (X) dan target (y)
X = df[['pclass', 'sex', 'age']] # eksplisit & benar
y = df['survived']

le = LabelEncoder()
X['sex'] = le.fit_transform(X['sex'])  

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skala fitur menggunakan StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Bangun model K-Nearest Neighbors
k = 5 # Jumlah tetangga terdekat
model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train_scaled, y_train)

# Prediksi pada data uji
y_pred = model.predict(X_test_scaled)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
print("Akurasi:", accuracy)
print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred))
print("\nMatriks Konfusi:")
print(confusion_matrix(y_test, y_pred))

# Input data dari user
print()
print("Masukkan Data Pasien Baru")
pclass = int(input("Input pclass: "))
sex_input = input("Input sex (male/female): ").lower()
sex = 1 if sex_input == 'female' else 0
age = int(input("Input age: "))

my_patient = pd.DataFrame({
    "pclass": [pclass],
    "sex": [sex],
    "age": [age]
})

print()
print("---")
print()

# Pastikan data baru menggunakan kolom yang sama dengan X_train
my_patient = my_patient[X_train.columns]

# Skala data baru menggunakan scaler yang sudah dilatih
my_patient_scaled = scaler.transform(my_patient)

# Prediksi
prediction = model.predict(my_patient_scaled)

print()
print(prediction)
print()

if prediction[0] == 1:
    print("Penumpang selamat.")
else:
    print("Penumpang meninggal.")