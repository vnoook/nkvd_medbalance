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
# print(df)
print()
# print(df[headers])

df_new1 = df.pivot_table(['sgtin'],['status'], aggfunc='min', fill_value = 0)
print(df_new1.to_string())
df_new2 = df.pivot_table(['sgtin'],['status'], aggfunc='max', fill_value = 0)
print(df_new2.to_string())
df_new3 = df.pivot_table(['status'],['sgtin'], aggfunc='count', fill_value = 0)
print(df_new3.to_string())
df_new4 = df.pivot_table(['sgtin'],['status'], aggfunc='count', fill_value = 0)
print(df_new4.to_string())

# df_new2 = df.pivot_table(['sgtin'],['status'], aggfunc='sum', fill_value = 0)
# sumtbl = SampleAccounts.pivot_table(['inf_confirm_date'],  ['tcs_customer_id','open_date','final_pmt_date','credit_limit','currency'], aggfunc='max')
# data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)
# data.pivot_table('PassengerId', ['SibSp'], 'Survived', 'count').plot(ax=axes[0], title='SibSp')
# data.pivot_table('PassengerId', ['Parch'], 'Survived', 'count').plot(ax=axes[1], title='Parch')
