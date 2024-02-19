import pandas as pd

# названия колонок для чтения в csv
headers = ['prod_name', 'full_prod_name', 'status', 'sgtin']

# прочитать весь файл
df_all = pd.read_csv(
                 r'fd_pd.csv',
                 # r'fd_pd_full.csv',
                 dtype=object)

# вывести весь файл
# print(df_all.to_string())
# print()

# выбрать нужные колонки
df = df_all[headers]
# print(df.to_string())
# print()

# посчитать количество prod_name
q_prod_name = df.pivot_table('full_prod_name', 'prod_name', aggfunc='count', fill_value = 0)
# print(q_prod_name.to_string())
# print()
q_prod_name.to_excel('output1.xlsx', sheet_name='Sheet2')

# подсчёт full_prod_name в колонке относительно prod_name
df_group1 = df.pivot_table(['prod_name'],
                           ['prod_name', 'full_prod_name', 'status', 'sgtin'],
                           aggfunc='count',
                           fill_value = 0)
# print(df_group1.to_string())
# print()
df_group1.to_excel('output1.xlsx', sheet_name='Sheet1')
# df_group1.to_excel('output2.xlsx')

df_group1 = df_group1.reset_index()
for index, row in df_group1.iterrows():
    print(index)
    # print(row)

    for val in headers:
        print(f'{row[val] = }')

    # print()
    # for i in row:
    #     print(type(i), i)
    print('*'*155)

df_group1.to_excel('output2.xlsx')
