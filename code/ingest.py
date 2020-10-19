import pandas as pd

#Ingest data
def create_df():
    spiketimes_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109_2.res"
    clusterID_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109_2.clu"
    #I believe the des file is from the wrong session but it shouldn't matter the code will work but data will be wrong
    des_celltype_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109.des"
    df = pd.read_fwf(spiketimes_file,header=None)
    df.columns = ["Spike Times(.res)"]
    df1 = pd.read_fwf(clusterID_file,header=None)
    df["Cluster ID's(.clu)"] = df1.iloc[1:].values
    #Is it 68 or 69 data says 69 but pdf says 68
    num_neurons = 69
    df["Cell Types (.des)"] = pd.read_fwf(des_celltype_file,header=None)
    return(df)

#Filter def
df = create_df()
def filter_df(df):
    #Cluster 0 and 1 should not be used
    df = df[df["Cluster ID's(.clu)"] != 0]
    df = df[df["Cluster ID's(.clu)"] != 1]
    return(df)
df = filter_df(df)

#Tests
print(df)

#to do - divide each time stamp by 20 to get millisecond
#add theta column and see what those values look like when divided by 1.25
