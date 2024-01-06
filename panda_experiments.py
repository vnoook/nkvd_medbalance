import pandas as pd

# headers = ['sgtin', 'status', 'withdrawal_type', 'batch', 'expiration_date',
#            'gtin', 'prod_name', 'last_tracing_op_date']
headers = ['sgtin', 'status']

df = pd.read_csv(
                 r'c:\soft\python3\__programki__\nkvd_medbalance\fd_pd.csv',
                 # r'c:\soft\python3\__programki__\nkvd_medbalance\fd_pd_full.csv',
                 # names=headers,
                 # delimiter=',',
                 # sep=',',
                 dtype=object,
                 # dtype=str,
                 # quotechar='"',
                 # doublequote=False,
                 )

print(df.to_string())

# print()
# print(df.astype(str))
# print()

# print(df[headers].to_string())
