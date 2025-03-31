import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import time



try:
    
    np.random.seed(int(round(time.time())))    
    
    df = pd.DataFrame(columns=['Temperature'])
    print(df)
    
    while True:
        
        randomTemp = round(np.random.uniform(25.0, 35.0), 1)
        df = pd.concat([df, pd.DataFrame([{'Temperature': randomTemp}])], ignore_index=True)
        df.plot(kind='bar')                
        plt.savefig('./static/temp.png')
        plt.close()
        time.sleep(5)
    

except KeyboardInterrupt:
    
    print("Program terminated!")
