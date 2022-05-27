import pandas as pd
#import numpy as np
#import random
#from nltk.corpus import names
#import nltk
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

feature_columns_to_use=["userFollowerCount","userFollowingCount","userBiographyLength","userMediaCount","userHasProfilPic","userIsPrivate","usernameDigitCount","usernameLength","isFake"]


real_users = pd.read_json("insta-data/fake-v1.0/realAccountData.json")
fake_users = pd.read_json("insta-data/fake-v1.0/fakeAccountData.json")

test_data = pd.concat([real_users[120:180],fake_users[600:]])
test = pd.DataFrame(test_data)
y_test = test.loc[:,'isFake'].values
test = test.loc[:,feature_columns_to_use].values
x=pd.concat([real_users[0:120],fake_users[0:600]])
X=pd.DataFrame(x)

y=X.loc[:,'isFake'].values
#print(X)

ty=X.loc[:,feature_columns_to_use].values

knn=KNeighborsClassifier()

knn.fit(ty,y)
print("the score of trainning:")
print(knn.score(ty, y))
print("the score of testing:")
y_pred=knn.predict(test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

a = pd.DataFrame(fake_users[120:]).loc[:,feature_columns_to_use].values
#print(pd.DataFrame(real_users[100:]).loc[:,'isFake'].values)

#test
rs=[[345,336, 40, 27, 1, 1, 0, 7,0]]
result = knn.predict(rs)
print(result)