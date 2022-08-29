import os,glob
import pandas as pd
filenames_airtime=glob.glob("/home/sahi/Desktop/capstone/dataset/sce1a_output/airtime_*.csv")
df=pd.DataFrame()
for file in filenames_airtime:
  path1=file
  df1=pd.read_csv(path1)
  df2=pd.DataFrame(df1)
  df=pd.concat([df,df2])
# print(list_input)
os.makedirs("/home/sahi/Desktop/capstone/dataset/sce1a_output_airtime")
input_path="/home/sahi/Desktop/capstone/dataset/sce1a_output_airtime/airtime.csv"
exists=os.path.exists(input_path)
if not exists :
  df.to_csv("/home/sahi/Desktop/capstone/dataset/sce1a_output_airtime/airtime.csv")