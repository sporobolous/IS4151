import time
import sqlite3
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from joblib import dump

def main():
    print('🌱 Starting environment clustering training process')

    np.random.seed(int(round(time.time())))

    while True:
        try:
            conn = sqlite3.connect('/Users/eve_lappy/Developer/IS4151/MockPracticalExam/Mock_BME280/TaskD_CloudServer/environment.db')
            c = conn.cursor()
            c.execute('SELECT id, temp, humidity, timestamp FROM environment ORDER BY id ASC')
            results = c.fetchall()
            conn.close()

            # Convert results to DataFrame
            df = pd.DataFrame(results, columns=['id', 'temp', 'humidity', 'timestamp'])

            # Show any rows with missing values
            nan_rows = df[df[['temp', 'humidity']].isnull().any(axis=1)]
            if not nan_rows.empty:
                print("⚠️ Found rows with missing temp or humidity:")
                print(nan_rows)

            # Drop rows with missing values
            df = df.dropna(subset=['temp', 'humidity'])

            if df.empty:
                print("🚫 No valid data to train. Skipping this round.")
                time.sleep(10)
                continue

            # Prepare data for clustering
            X = df[['temp', 'humidity']].values

            # Train KMeans model
            kmeans = KMeans(n_clusters=2, random_state=0)
            kmeans = kmeans.fit(X)

            # Attach cluster labels
            df['cluster'] = kmeans.labels_

            # Print summary
            for cluster in df.cluster.unique():
                sub = df[df.cluster == cluster]
                print(f"Cluster {cluster} → Temp Mean: {sub.temp.mean():.2f}, Humidity Mean: {sub.humidity.mean():.2f}")

            # Save model
            dump(kmeans, 'envcluster.joblib')
            print("✅ Model saved to envcluster.joblib")

            time.sleep(10)

        except KeyboardInterrupt:
            print("🛑 Program terminated by user")
            break

        except Exception as error:
            print(f'❌ Error: {error}')
            time.sleep(10)
            continue

if __name__ == '__main__':
    main()
