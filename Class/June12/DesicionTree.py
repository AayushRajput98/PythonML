from sklearn import tree
clf=tree.DecisionTreeClassifier()
x=[[180, 15, 0],
   [120, 18, 1],
   [150, 34, 0],
   [195, 41, 1],
   [187, 25, 0],
   [148, 35, 1]]
y=['man','woman','man','woman','man','woman']
clf = clf.fit(x,y)
prediction = clf.predict([[148, 35, 1]])
print(prediction)