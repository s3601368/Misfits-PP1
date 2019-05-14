import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.DataFrame(pd.read_csv('studentInfo.csv',header=1))
pd.pivot_table(df,index=["id_student","age_band"])



