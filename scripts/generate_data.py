import pandas as pd
import random
from datetime import datetime, timedelta

data = []

for i in range(1000):
    data.append({
        "timestamp": datetime.now() - timedelta(minutes=i),
        "temperatura": random.randint(60, 120),
        "vibracao": round(random.uniform(0.1, 5.0), 2),
        "pressao": random.randint(20, 100)
    })

df = pd.DataFrame(data)

df.to_csv("data/telemetry.csv", index=False)

print("Dados gerados com sucesso!")