import pandas as pd
import random
from datetime import datetime, timedelta

equipamentos = ["TR-01", "TR-02", "CR-01", "CV-01"]
setores = ["porto", "ferrovia", "pelotizacao"]

data = []

for i in range(1000):
    temperatura = random.randint(60, 120)
    vibracao = round(random.uniform(0.1, 5.0), 2)

    status = "normal"

    if temperatura > 100 or vibracao > 4:
        status = "critico"

    data.append({
        "timestamp": datetime.now() - timedelta(minutes=i),
        "equipment_id": random.choice(equipamentos),
        "setor": random.choice(setores),
        "temperatura": temperatura,
        "vibracao": vibracao,
        "pressao": random.randint(20, 100),
        "status": status
    })

df = pd.DataFrame(data)

df.to_csv("data/telemetry.csv", index=False)

print("Dados gerados com sucesso!")