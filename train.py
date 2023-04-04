# import libraries
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# # read data to be encoded
# data = pd.read_excel('data_cs.xlsx')

# # read column to be encoded
# column = data[['Q15.5']]

# # set ordinal encoder
# ordinal_encoder = OrdinalEncoder()

# # replace the original data with the encoded data: select-encode-replace
# data['Q15.5'] = ordinal_encoder.fit_transform(data[['Q15.5']])
# print(data['Q15.5'])

# # export to csv
# data.to_excel('encoded_data.xlsx')

# through a function


def encode_columns(file, column_names):

    data = pd.read_excel(file)
    column = data[[column_names]]

    ordinal_encoder = OrdinalEncoder()
    data[column_names] =ordinal_encoder.fit_transform(data[[column_names]])

    return data









