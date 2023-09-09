import  numpy as np
import pandas as pd
import sktime.datasets as load_data
if __name__ == '__main__':
    df, labels = load_data.load_from_tsfile_to_dataframe('Heartbeat/Heartbeat_TEST.ts', return_separate_X_and_y=True,replace_missing_vals_with='NaN')
    df1, labels1 = load_data.load_from_tsfile_to_dataframe('CTG/CTG_TRAIN.ts', return_separate_X_and_y=True,replace_missing_vals_with='NaN')
    labels = pd.Series(labels, dtype="category")
    labels1 = pd.Series(labels1, dtype="category")
    labels_df = pd.DataFrame(labels.cat.codes,dtype=np.int8)
    labels_df1 = pd.DataFrame(labels1.cat.codes,dtype=np.int8)

    lengths = df.applymap(lambda x: len(x)).values
    horiz_diffs = np.abs(lengths - np.expand_dims(lengths[:, 0], -1))
    lengths = df.applymap(lambda x: len(x)).values
    vert_diffs = np.abs(lengths - np.expand_dims(lengths[0, :], 0))
    max_seq_len = lengths[0, 0]
    df = pd.concat((pd.DataFrame({col: df.loc[row, col] for col in df.columns}).reset_index(drop=True).set_index(
        pd.Series(lengths[row, 0] * [row])) for row in range(df.shape[0])), axis=0)
    # data1 = np.genfromtxt('Heartbeat/Heartbeat_TEST.ts', delimiter='\t', dtype=None, names=('timestamp', 'value'))
    # data2 = np.genfromtxt('CTG/CTG_TRAIN.ts', delimiter='\t', dtype=None, names=('timestamp', 'value'))
    print(df)