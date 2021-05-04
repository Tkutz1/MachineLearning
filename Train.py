import pandas as pd


Train = pd.read_json(r"Train.json")
print(Train)
print(Train.shape)
for col in Train:
    print(col)
print(Train.thread[3])
