import pandas as pd

# headers = ['sgtin', 'status', 'withdrawal_type', 'batch', 'expiration_date',
#            'gtin', 'prod_name', 'last_tracing_op_date']
headers = ['sgtin', 'status']

df_all = pd.read_csv(
                 r'fd_pd.csv',
                 # r'fd_pd_full.csv',
                 # names=headers,
                 # delimiter=',',
                 # sep=',',
                 dtype=object,
                 # dtype=str,
                 # quotechar='"',
                 # doublequote=False,
                 )

print(df_all.to_string())
print()

df1 = df_all[['sgtin', 'status']]
print(df1)
print()

df2 = df_all[['sgtin', 'gtin']]
print(df2)
print()

df3 = df_all[['sgtin', 'status', 'sell_name', 'prod_name']]
print(df3)
print()

df_new1 = df1.pivot_table(['sgtin'], ['status'], aggfunc='min', fill_value = 0)
print(df_new1.to_string())
print()

df_new2 = df1.pivot_table(['sgtin'], ['status'], aggfunc='max', fill_value = 0)
print(df_new2.to_string())
print()

df_new3 = df1.pivot_table(['status'], ['sgtin'], aggfunc='count', fill_value = 0)
print(df_new3.to_string())
print()

df_new4 = df1.pivot_table(['sgtin'], ['status'], aggfunc='count', fill_value = 0)
print(df_new4.to_string())
print()

# df_new2 = df.pivot_table(['sgtin'],['status'], aggfunc='sum', fill_value = 0)
# sumtbl = SampleAccounts.pivot_table(['inf_confirm_date'],  ['tcs_customer_id','open_date','final_pmt_date',
#                                      'credit_limit','currency'], aggfunc='max')
# data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)
# data.pivot_table('PassengerId', ['SibSp'], 'Survived', 'count').plot(ax=axes[0], title='SibSp')
# data.pivot_table('PassengerId', ['Parch'], 'Survived', 'count').plot(ax=axes[1], title='Parch')
