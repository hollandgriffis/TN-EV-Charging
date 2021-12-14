import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('../data/tn_gas_stations.csv')
df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
df.columns = df.columns.str.replace(' ', '_')
df.columns = df.columns.str.replace(':', '_')
engine = create_engine('postgresql://postgres:password@localhost:5432/postgres')
df.to_sql("tn_gas_stations", engine)
