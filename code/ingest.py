import pandas as pd

# Extend dataframe printing lenght
# pd.set_option("display.max_rows", None, "display.max_columns", None)

#Ingest data
def create_df():
    spiketimes_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109_2.res"
    clusterID_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109_2.clu"
    #I believe the des file is from the wrong session but it shouldn't matter the code will work but data might be wrong
    des_celltype_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109.des"

    #Create spiketimes df
    df = pd.read_fwf(spiketimes_file,header=None)
    df.columns = ["Spike Times(.res)"]

    #Create clusterID df then add to spike times
    clu = pd.read_fwf(clusterID_file,header=None)
    df["Cluster ID's(.clu)"] = clu.iloc[1:].values
    df = df[df["Cluster ID's(.clu)"] != 1]

    #Neurons = 68 as per doc info
    num_neurons = 68

    #Add cell types to dataframe - .des is 68 rows of data meaning 68 neurons
    #Assume the index of .des = cluster ID. So index 0 = cluster ID 1, and index 1 = Cluster ID 2
    des = pd.read_fwf(des_celltype_file,header=None)
    #Get rid of cluster id 1 so .dex index 0
    des = des.iloc[1:]
    #Align index to Cluster ID
    des.index = des.index + 1
    #Merge des df into main df
    df = df.merge(des, how="left", left_on="Cluster ID's(.clu)", right_index=True)
    df = df.rename(columns={ df.columns[2]: "Phenotype (.des)" })
    return(df)

#Filter def / Remove cluster 0 and cluster 1 as per document ask
df = create_df()
print(df)


#Tests
# print(df)

#to do - divide each time stamp by 20 to get millisecond
#add theta column and see what those values look like when divided by 1.25
