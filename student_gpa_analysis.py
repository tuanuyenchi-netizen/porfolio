
import pandas as pd

# Sample student data
data = {
    "Name": ["A", "B", "C"],
    "Major": ["IT", "IT", "BA"],
    "GPA": [3.6, 3.8, 3.2]
}

df = pd.DataFrame(data)

# Average GPA by Major
print(df.groupby("Major")["GPA"].mean())
