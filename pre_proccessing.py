from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import AffinityPropagation
from matplotlib import pyplot
import ConnectToDB as db
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch

connection=db.connectToDB()
df=db.tableName('johnson_clean.jc_customers',connection)

df.head()

df1 = pd.DataFrame(df, columns = ['city', 'gender','avgPur'])
# , 'quanitem','valuePur','avgPur'
# df1 = df1.apply(pd.to_numeric, errors='ignore')
df1.sort_values(by=['city','gender','avgPur'], inplace=True)

from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder()






X1 = df1.gender
X1 = np.array(X1).reshape(len(X1),1)
X1[X1==None]='None'


enc.fit(X1)
print(enc.categories_)
genderCode = enc.transform(X1)


X2 = df1.city
X2 = np.array(X2).reshape(len(X2),1)
X2[X2==None]='None'


enc.fit(X2)
print(enc.categories_)
cityCode = enc.transform(X2)

df1['genderCode'] = genderCode
df1['cityCode'] = cityCode



X3 = df1.avgPur
X3 = np.array(X3).reshape(len(X3),1)

X3[pd.isna(X3)]=-99


enc.fit(X3)

avgPurRange = enc.transform(X3)

df1['avgPurRange'] = avgPurRange




##Find the 150 cities that contain the most records
citiesList=df1['cityCode'].value_counts().nlargest(10).index
max_150_cities = df1[df1['cityCode'].isin(citiesList)]


max_150_cities.loc[(max_150_cities.avgPur<50) ,'avgPurRange']=50
max_150_cities.loc[(max_150_cities.avgPur>=50)&(max_150_cities.avgPur<150) ,'avgPurRange']=150
max_150_cities.loc[(max_150_cities.avgPur>=150)&(max_150_cities.avgPur<300) ,'avgPurRange']=300
max_150_cities.loc[(max_150_cities.avgPur>=300)&(max_150_cities.avgPur<450) ,'avgPurRange']=450
max_150_cities.loc[(max_150_cities.avgPur>=450)&(max_150_cities.avgPur<1000) ,'avgPurRange']=1000
max_150_cities.loc[(max_150_cities.avgPur>1000) ,'avgPurRange']=1500
max_150_cities.loc[(max_150_cities.avgPur==None) ]='None'
# max_150_cities=max_150_cities.loc[(max_150_cities.avgPurRange==1000)]
# max_150_cities.loc[pd.isna(max_150_cities.avgPurRange),'avgPurRange']=-99
max_150_cities
