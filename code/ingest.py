import pandas as pd

#Ingest data
def create_df():
    spiketimes_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109_2.res"
    clusterID_file = "/Users/laurence/Desktop/Neuroscience/Dupret_Group/dataset_student_training/mvl10-200109_2.clu"
    # df = pd.read_fwf(spiketimes_file)
    df = pd.read_fwf(spiketimes_file,header=None)
    df.columns = ["Spike Times(.res)"]
    df1 = pd.read_fwf(clusterID_file,header=None)
    df["Cluster ID's(.clu)"] = df1.iloc[1:].values
    num_neurons = 69
    return(df)

#Next task
df = create_df()
print("hello world")
