import pre_proccessing as pp
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation


df1=pp.max_150_cities


feature_cols =  ['genderCode','cityCode']

X = df1[feature_cols] # Features
y =  df1.avgPurRange.astype('float') # Target variable



# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

clf = DecisionTreeClassifier()


# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn import tree
tree.plot_tree(clf)


import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)

graph.render("customers_9f")


from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()


export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=False,node_ids=True,proportion=True,
                special_characters=True ,feature_names=feature_cols)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('customers_9f.png')
Image(graph.create_png())

graph = graphviz.Source(dot_data)
print(graph)
