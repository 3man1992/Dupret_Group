import pandas as pd
import numpy as np

# Extend dataframe printing lenght
# pd.set_option("display.max_rows", None, "display.max_columns", None)

#Ingest data - Question 1
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

#Question 2
def compute_firing_rate():
    df = create_df()

    #Convert spike times to milliseconds
    df["Spike Times(.res)"] = df["Spike Times(.res)"] / 20
    bins = np.array([0,100,200,300,400,500])

    #Create Seperate DFs for cell types
    p1 = df.loc[(df["Phenotype (.des)"] == "p1")]
    b1 = df.loc[(df["Phenotype (.des)"] == "b1")]

    #How many cells are there
    cell_counts = df["Phenotype (.des)"].value_counts()
    num_p1 = 66042
    num_b1 = 2663

    #Counts
    p1_counts, bin_edges = np.histogram(p1["Spike Times(.res)"], bins=bins)
    b1_counts, bin_edges = np.histogram(b1["Spike Times(.res)"], bins=bins)

    #Firing rate calculations
    p1_average_firing_rate_seconds = (np.mean(p1_counts)/num_p1)*10
    b1_average_firing_rate_seconds = (np.mean(b1_counts)/num_b1)*10
    print("Firing rate for P1 cells (spike/s):",p1_average_firing_rate_seconds)
    print("Firing rate for B1 cells (spike/s):",b1_average_firing_rate_seconds)
    # print(df.describe())

#Tests
compute_firing_rate()

#to do - divide each time stamp by 20 to get millisecond
#add theta column and see what those values look like when divided by 1.25
