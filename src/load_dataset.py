"""Import """
import os
import pandas as pd
# from preprocess import apply_cleaning
# from similarity import vect_tf_idf

# Path of dataset
PATH= os.path.join("data","Songs.csv")

#loading dataset
df= pd.read_csv(PATH)

# Tests
# print("dataset shape: ", df.shape,"\n")
#print("dataset columns:\n",df.columns)
# print("dataset head:\n", df.head(),"\n")
# df= apply_cleaning(df)
# vect= vect_tf_idf(df)
# print(df.head())
# print(vect)
