import pandas as pd
from typing import List
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    condition="animals.weight>100"
    df=animals[animals.weight>100].sort_values(by=["weight"], ascending=False)
    return pd.DataFrame(df['name'])


import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:

    return animals[animals['weight']>100].sort_values(['weight'],ascending=False)[['name']]






# get # rows and # columns

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0],len(players.column)]
    


#display 3 rows of data
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

#select columns
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students.student_id==101][['name','age']]


import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[ students["student_id"] == 101, ["name", "age"] ]
    




#join and rename columns

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    combine = customers.merge(orders, how='left', right_on = 'customerId', left_on = 'id')
    combine = combine[combine['customerId'].isna()]
    combine = combine.rename(columns={'name':'Customers'})
    return combine[['Customers']]



##group by

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    sf = actor_director.groupby(['actor_id','director_id']).count().reset_index()
    r = sf[sf['timestamp']>=3][['actor_id','director_id']]
    return r    



import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.groupby("managerId").agg(count = ("managerId", "count")).reset_index()
    df = df.loc[df["count"]>=5, ["managerId"]]
    output = df.merge(employee, how="inner", left_on="managerId", right_on="id")

    return output[["name"]]


import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.managerId.value_counts().reset_index()
    df = df[df['count'] >= 5]

    dg = pd.merge(df, employee, left_on='managerId', right_on='id', how='inner')
    return dg[['name']]

    # return df.loc[employee.id.isin(df.managerId)==True][['name']]
