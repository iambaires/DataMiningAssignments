# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#importing some Python libraries
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot
import numpy as np
import pandas as pd

# read the dataset cheat_data.csv and prepare the data_training numpy array
df = pd.read_csv('cheat_data.csv', sep=',', header=0)  # reading a dataset eliminating the header (Pandas library)
data_training = np.array(df.values)[:, 1:]  # creating a training matrix without the id (NumPy library)

# transform the original training features to numbers and add them to the 5D array X. For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
# Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [0, 0, 1, 0, 100], ...]]. The feature Marital Status must be one-hot-encoded and Taxable Income must
# be converted to a float.
# --> add your Python code here
X = []

# transform the original training classes to numbers and add them to the vector y. For instance Yes = 1, No = 0, so Y = [1, 1, 0, 0, ...]
# --> add your Python code here
Y = []

marital_codes = ['Divorced', 'Married', 'Single']
max_income = 140
min_income = 60

marital_codes = ['Divorced', 'Married', 'Single']
max_income = 0
min_income = 10000

for i in range(len(df)):
    attributes = list(df.values[i])
    instance = []

    refund_status = attributes[0]
    if 'Yes' in attributes[0]:
        instance.append(0)
    else:
        instance.append(0)

    marital_status = attributes[1]
    marital_code = [0, 0, 0]

    for n in range(len(marital_codes)):
        if attributes[1] in marital_codes[n]:
            instance.append(1)
        else:
            instance.append(0)

    income = int(attributes[2].strip('k'))
    instance.append(income)
    min_income = min(income, min_income)
    max_income = max(income, max_income)

    X.append(instance)

    # transform the original training classes to numbers and add them to the vector Y.
    # For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    if 'Yes' in attributes[3]:
        Y.append(1)
    else:
        Y.append(0)

for n in range(len(df)):
    income = X[n][4]
    normalized_income = (income - min_income) / (max_income - min_income)
    X[n][4] = normalized_income

# split into train/test sets using 30% for test
trainX, testX, trainY, testy = train_test_split(X, Y, test_size=.30)

# generate a no skill prediction (random classifier - scores should be all zero)
ns_probs = [0 for _ in range(len(testy))]

# fit a decision tree model by using entropy with max depth = 2
clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=2)
clf = clf.fit(trainX, trainY)

# predict probabilities for all test samples (scores)
dt_probs = clf.predict_proba(testX)

# keep probabilities for the positive outcome only

dt_probs = dt_probs[:, 1]

# calculate scores by using both classifeirs (no skilled and decision tree)
ns_auc = roc_auc_score(testy, ns_probs)
dt_auc = roc_auc_score(testy, dt_probs)

# summarize scores
print('No Skill: ROC AUC=%.3f' % ns_auc)
print('Decision Tree: ROC AUC=%.3f' % dt_auc)

# calculate roc curves
ns_fpr, ns_tpr, _ = roc_curve(testy, ns_probs)
dt_fpr, dt_tpr, _ = roc_curve(testy, dt_probs)

# plot the roc curve for the model
pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')
pyplot.plot(dt_fpr, dt_tpr, marker='.', label='Decision Tree')

# axis labels
pyplot.xlabel('False Positive Rate')
pyplot.ylabel('True Positive Rate')

# show the legend
pyplot.legend()

# show the plot
pyplot.show()