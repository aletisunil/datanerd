stats(), iv_woe(), pushdb()

This function provides some statistical summary of a given dataframe.

The **stats()** function takes in a dataframe and returns the following statistics:

- count
- mean
- std
- min
- 10th percentile
- 20th percentile
- 25th percentile
- 30th percentile
- 40th percentile
- 50th percentile (median)
- 60th percentile
- 70th percentile
- 75th percentile
- 80th percentile
- 90th percentile
- 95th percentile
- 99th percentile
- max
- % of missing values
- % of non-zero values
- #numberofunique_values

```python
import pandas as pd
import datanerd as dn

df = pd.read_csv('titanic.csv')
dn.stats(df)
```

The **iv_woe()** function is used to calculate the Weight of Evidence (WoE) and Information Value (IV) for a given dataframe. 

The WoE is a measure of how much the presence or absence of a predictor (feature) contributes to the probability of target. 

The IV is a measure of the strength of the relationship between the predictor and the target.

The **iv_woe()** function takes in the following arguments:

**data:** a dataframe containing the predictor variables and the target variable

**target:** the name of the target variable

**bins:** the number of bins to use for discretizing continuous variables

**optimize:** a boolean indicating whether to optimize the binning of the continuous variables

**thresold:** the minimum percentage of non-events (negative outcome) in each bin for optimization. If optimize is set to True, the function will iterate over the number of bins from 20 to 1 and calculate the WoE and IV for each bin. If the percentage of non-events in each bin is greater than or equal to the specified thresold, it will return the WoE and IV for that bin. If it cannot find a binning that meets the thresold, it will return the WoE and IV for the best bin it could find.

If optimize is set to False, the function will calculate the WoE and IV for the specified number of bins.

The function returns a dataframe containing the WoE and IV for each predictor variable.

```python
import pandas as pd
import datanerd as dn

df = pd.read_csv('cancer.csv')
iv,woe = dn.iv_woe(data=df,target='Diagnosis',bins=20,optimize=True,thresold=True)
```

This **pushdb()** function takes Pandas dataframe (**`data`**), a table name (**`tablename`**), a server name (**`server`**), a database name (**`database`**), and a schema name (**`schema`**)

It then creates a connection to a Microsoft SQL Server database using these input parameters, and pushes the **`data`** i.e dataframe to the specified table in the database. The function is written to handle a fast execution of many records using the **`fast_executemany`** argument in the **`create_engine`** function.

```python
import pandas as pd
import datanerd as dn

df = pd.read_csv('day.csv')
dn.pushdb(df, tablename='day', server='SQL-DW', database='schedule', schema='ana')
```

This will push the data i.e dataframe to the **day** table in the **schedule** database on the **SQL-DW** server, using the **ana** schema.








