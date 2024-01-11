import pandas as pd

headers = ['prod_name', 'full_prod_name','sgtin']

df_all = pd.read_csv(
                 r'fd_pd.csv',
                 # r'fd_pd_full.csv',
                 # r'fd_pd_new.csv',
                 # r'8eb6f4c7-5407-4f5f-9ace-7da6cf4a6ea7-0.csv',
                 dtype=object)

print(df_all.to_string())
print()

df1 = df_all[headers]
print(df1.to_string())
print()

df_new1 = df1.pivot_table(['sgtin'], ['status'], aggfunc='min', fill_value = 0)
print(df_new1.to_string())
print()

# df_new2 = df1.pivot_table(['sgtin'], ['status'], aggfunc='max', fill_value = 0)
# print(df_new2.to_string())
# print()
#
# df_new3 = df1.pivot_table(['status'], ['sgtin'], aggfunc='count', fill_value = 0)
# print(df_new3.to_string())
# print()
#
# df_new4 = df1.pivot_table(['sgtin'], ['status'], aggfunc='count', fill_value = 0)
# print(df_new4.to_string())
# print()




# df_new2 = df.pivot_table(['sgtin'],['status'], aggfunc='sum', fill_value = 0)
# sumtbl = SampleAccounts.pivot_table(['inf_confirm_date'],  ['tcs_customer_id','open_date','final_pmt_date',
#                                      'credit_limit','currency'], aggfunc='max')
# data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)
# data.pivot_table('PassengerId', ['SibSp'], 'Survived', 'count').plot(ax=axes[0], title='SibSp')
# data.pivot_table('PassengerId', ['Parch'], 'Survived', 'count').plot(ax=axes[1], title='Parch')
