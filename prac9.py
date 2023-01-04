import pandas as pd
raw_data={"City":["Mumbai","Bangalore","Chennai","Kolkata"],
          "Rank":["1","2","3","4"],
          "Score1":[100,80,70,60],
          "Score2":[100,80,70,60]}
df=pd.DataFrame(raw_data,
                index=pd.Index(["A","B","C","D"],name="Letter"),
                columns=pd.Index(["City","Rank","Score1","Score2"],name="Attributes"))
# print(df)
print(df.reindex(["C","B","D","A"]))#doesn't change the original dataframe
# print(df)
column_name=["Rank","Score1","Score2","City"]
print(df.reindex(columns=column_name))
# print(df)
# import numpy and pandas module
# import pandas as pd
# import numpy as np
#
# column=['a','b','c','d','e']
# index=['A','B','C','D','E']
#
# # create a dataframe of random values of array
# df1 = pd.DataFrame(np.random.rand(5,5),
#             columns=column, index=index)
#
# print(df1)
#
# print('\n\nDataframe after reindexing rows: \n',
# df1.reindex(['B', 'D', 'A', 'C', 'E']))
