# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head() 

unique_values = data['whoAmI'].unique()
encoder = {value: i for i, value in enumerate(unique_values)}
encoded_data = [[encoder[value]] for value in data['whoAmI']]
one_hot = pd.DataFrame.from_records(encoded_data, columns=unique_values)
print(one_hot.head())

