import time
import os
import sqlite3
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from joblib import dump


def main():
    print('Starting temperature clustering process...\n')
    np.random.seed(int(round(time.time())))

    while True:
        try:
            # Clear the console for cleaner logs
            os.system('clear')  # use 'cls' on Windows
            print('🔁 Retraining KMeans Model...')

            # Connect to DB
            conn = sqlite3.connect('/Users/eve_lappy/Developer/IS4151/MockPracticalExam/Mock-Microbit/TaskD_CloudServer/temp.db')
            c = conn.cursor()
            c.execute('SELECT id, devicename, temp, timestamp FROM temp ORDER BY id ASC')
            results = c.fetchall()
            conn.close()

            # Load into DataFrame
            df = pd.DataFrame(results, columns=['id', 'devicename', 'temp', 'timestamp'])

            # Skip if there's not enough data
            if len(df) < 2:
                print("⚠️ Not enough data to train clustering model.\n")
                time.sleep(10)
                continue

            # Train model
            X = df['temp'].values.reshape(-1, 1)
            kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

            # Clustered results
            result = pd.DataFrame({
                'temp': df['temp'],
                'cluster': kmeans.labels_
            })

            # Show cluster centers
            print("\n📍 Cluster Centers (°C):")
            for idx, center in enumerate(kmeans.cluster_centers_):
                print(f"Cluster {idx}: {center[0]:.2f}°C")

            # Show how many in each cluster
            print("\n📊 Cluster Sizes:")
            print(result['cluster'].value_counts())

            # Sample of clustered temps
            print("\n📋 Clustered Temperature Samples:")
            print(result.groupby('cluster').head(3).sort_values(by='cluster'))

            # Save model
            dump(kmeans, 'tempcluster.joblib')
            print("\n✅ Model saved as tempcluster.joblib")

            # Wait before next cycle
            time.sleep(10)

        except Exception as error:
            print(f"❌ Error: {error}")
            time.sleep(10)

        except KeyboardInterrupt:
            print('\n⛔ Program terminated by user.')
            break


if __name__ == '__main__':
    main()
