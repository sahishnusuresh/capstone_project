import os,glob
import pandas as pd
dir_path="/home/sahi/Desktop/capstone/dataset/input_node_files/sce1a"

# required_path=os.path.join(path,"*.csv")
filenames=glob.glob("/home/sahi/Desktop/capstone/dataset/input_node_files/sce1a/*.csv")
path="/home/sahi/Desktop/capstone/dataset/sce1a_output_merged"
filenames.sort()



filenames_rssi=glob.glob("/home/sahi/Desktop/capstone/dataset/sce1a_output/rssi_*.csv")
df=pd.DataFrame()
# for i in range(100):
#   input_path="/home/sahi/Desktop/capstone/dataset/sce1a_input_merged"
#   exists=os.path.exists(input_path)
#   if not exists:
#     os.makedirs("/home/sahi/Desktop/capstone/dataset/sce1a_input_merged")
#   df1=pd.read_csv(filenames_rssi[i])
#   df1=pd.DataFrame(df1)
#   df2=pd.read_csv(filenames[i])
#   df2=pd.DataFrame(df2)
#   df2['rssi']=df1
#   df2.to_csv(os.path.join(input_path,"input_*[i].csv"))



for file in filenames:
  path1=file
  df1=pd.read_csv(path1)
  df2=pd.DataFrame(df1)
  df=pd.concat([df,df2])
# print(list_input)
os.makedirs("/home/sahi/Desktop/capstone/dataset/sce1a_input")
input_path="/home/sahi/Desktop/capstone/dataset/sce1a_input/input.csv"
exists=os.path.exists(input_path)
if not exists :
  df.to_csv("/home/sahi/Desktop/capstone/dataset/sce1a_input/input.csv")
