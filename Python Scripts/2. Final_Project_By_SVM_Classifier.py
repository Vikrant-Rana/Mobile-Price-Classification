# The First Step is To Import Libraries Required

import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np

# The Second Step is To Locate , Read And View The Overflow Of Data (.csv File)

train_data=pd.read_csv('D:\Project\mobile_price_range_data.csv')
train_data.head()
train_data.info()

# The Third Step Is To Remove The data Points With Missing Data

train_data_f = train_data[train_data['sc_w'] != 0]
train_data_f.shape

# The Fourth Step Is To  Predict The price range For Test Data And visualize the number of elements in each class of mobile phones

sns.set()
price_plot= train_data_f['price_range'].value_counts().plot(kind='bar')
plt.xlabel('price_range')
plt.ylabel('Count')
plt.show()

# In Fifth Step, To See The Distribution Of Data We Will Analyse Some Data Features

# Let's See How the battery mAh power is spread

sns.set(rc={'figure.figsize':(5,5)})
ax=sns.displot(data=train_data["battery_power"])
plt.show()

# Let's Check How Many Devices Have 3G Or Not

sns.set(rc={'figure.figsize':(5,5)})
ax=sns.displot(data=train_data["three_g"])
plt.show()

# Let's check How Many Devices Have Wifi Or Not

sns.set(rc={'figure.figsize':(5,5)})
ax=sns.displot(data=train_data["wifi"])
plt.show()

# Let's check How Many Devices Have Bluetooth Or Not

sns.set(rc={'figure.figsize':(5,5)})
ax=sns.displot(data=train_data["blue"])
plt.show()


# Let Check if there are any missing values or missing data

X= train_data_f.drop(['price_range'], axis=1)
y= train_data_f['price_range']
#missing values
X.isna().any()

# In Sixth Step We Will Split The Dataset And define a function for creating a confusion matrix

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid= train_test_split(X, y, test_size=0.2, random_state=7)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
def my_confusion_matrix(y_test, y_pred, plt_title):
    cm=confusion_matrix(y_test, y_pred)
    print(classification_report(y_test, y_pred))
    sns.heatmap(cm, annot=True, fmt='g', cbar=False, cmap='BuPu')
    plt.xlabel('Predicted Values')
    plt.ylabel('Actual Values')
    plt.title(plt_title)
    plt.show()
    return cm

# For Seventh And Last Step We Will Train The Models And Predict Value For Dataset

# At Second We Will Use SVM Classifier

from sklearn import svm
svm_clf = svm.SVC(decision_function_shape='ovo')
svm_clf.fit(X_train, y_train)
y_pred_svm=svm_clf.predict(X_valid)
print('SVM Classifier Accuracy Score: ',accuracy_score(y_valid,y_pred_svm))
cm_rfc=my_confusion_matrix(y_valid, y_pred_svm, 'SVM Confusion Matrix')


