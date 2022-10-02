# -------------------------------------------------------------------------
# AUTHOR: your name
# FILENAME: title of the source file
# SPECIFICATION: description of the program
# FOR: CS 5990 (Advanced Data Mining) - Assignment #2
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/
import numpy
# importing some Python libraries
from sklearn import tree, preprocessing
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataSets = ['cheat_training_1.csv', 'cheat_training_2.csv']

for ds in dataSets:

    X = []
    Y = []

    df = pd.read_csv(ds, sep=',', header=0)  # reading a dataset eliminating the header (Pandas library)
    data_training = np.array(df.values)[:, 1:]  # creating a training matrix without the id (NumPy library)

    # transform the original training features to numbers and add them to the 5D array X.
    # For instance, Refund = 1, Single = 1, Divorced = 0, Married = 0,
    # Taxable Income = 125, so X = [[1, 1, 0, 0, 125], [2, 0, 1, 0, 100], ...]].
    # The feature Marital Status must be one-hot-encoded and Taxable Income must be converted to a float.

    marital_codes = ['Divorced', 'Married', 'Single']
    max_income = 0
    min_income = 10000

    for i in range(len(df)):
        attributes = list(df.values[i])
        instance = []

        refund_status = attributes[1]
        if 'Yes' in attributes[1]:
            instance.append(1)
        else:
            instance.append(0)

        marital_status = attributes[2]
        marital_code = [0, 0, 0]

        for n in range(len(marital_codes)):
            if attributes[2] in marital_codes[n]:
                instance.append(1)
            else:
                instance.append(0)

        income = int(attributes[3].strip('k'))
        instance.append(income)
        min_income = min(income, min_income)
        max_income = max(income, max_income)

        X.append(instance)

        # transform the original training classes to numbers and add them to the vector Y.
        # For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
        if 'Yes' in attributes[4]:
            Y.append(1)
        else:
            Y.append(0)

    for n in range(len(df)):
        income = X[n][4]
        normalized_income = (income - min_income) / (max_income - min_income)
        X[n][4] = normalized_income


    accuracies = []
    # loop your training and test tasks 10 times here
    for i in range(10):
        correct = 0
        # fitting the decision tree to the data by using Gini index and no max_depth
        clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=None)
        clf = clf.fit(X, Y)

        # plotting the decision tree
        tree.plot_tree(clf, feature_names=['Refund', 'Single', 'Divorced', 'Married', 'Taxable Income'], class_names=['Yes', 'No'], filled=True, rounded=True)
        plt.show()
        # read the test data and add this data to data_test NumPy
        # --> add your Python code here
        dTest = pd.read_csv('cheat_test.csv', sep=',', header=0)
        data_test = dTest.values

        Xtest = []
        Ytest = []

        maxTest_income = 0
        minTest_income = 10000

        for data in data_test:
        # transform the features of the test instances to numbers following the same strategy done during training,
        #  and then use the decision tree to make the class prediction. For instance:
        # class_predicted = clf.predict([[1, 0, 1, 0, 115]])[0], where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        # --> add your Python code here
            attributes = list(data)
            instance = []

            refund_status = attributes[1]
            if 'Yes' in attributes[1]:
                instance.append(1)
            else:
                instance.append(0)

            marital_status = attributes[2]
            marital_code = [0, 0, 0]

            for n in range(len(marital_codes)):
                if attributes[2] in marital_codes[n]:
                    instance.append(1)
                else:
                    instance.append(0)

            income = int(attributes[3].strip('k'))
            instance.append(income)
            minTest_income = min(income, minTest_income)
            maxTest_income = max(income, maxTest_income)

            Xtest.append(instance)

            # transform the original training classes to numbers and add them to the vector Y.
            # For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
            if 'Yes' in attributes[4]:
                Ytest.append(1)
            else:
                Ytest.append(0)

        for n in range(len(data_test)):
            income = Xtest[n][4]
            normalized_income = (income - minTest_income) / (maxTest_income - minTest_income)
            Xtest[n][4] = normalized_income

        # compare the prediction with the true label of the test instance to start calculating the model accuracy.
        class_predicted = clf.predict(Xtest)

        index = 0
        for data in data_test:
            if data[4] in 'Yes' and class_predicted[index] == 1:
                correct += 1
            elif data[4] in 'No' and class_predicted[index] == 0:
                correct += 1
            index += 1

        accuracies.append(correct/len(data_test))

    # find the average accuracy of this model during the 10 runs (training and test set)
    sum = 0
    for value in accuracies:
        sum += value
    average = sum/len(accuracies)

    # print the accuracy of this model during the 10 runs (training and test set).
    # your output should be something like that: final accuracy when training on cheat_training_1.csv: 0.2
    print(f'final accuracy when training on {ds}: {average}')

