import pickle

import pandas as pd
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score
import warnings

warnings.filterwarnings('ignore')


df=pd.read_csv("flood_risk_ml_dataset.csv")

#Splitinf of data into x & y
x=df.drop(["Flood_Risk","Population_Density"],axis=1)
y=df["Flood_Risk"]

#train test split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=42,stratify=y)

cat_col=x.select_dtypes(include="object").columns
num_col=x.select_dtypes(include="number").columns


#one hot Encoding of categorial columns and scaling of numerical columns
preprocessor=ColumnTransformer(
    transformers=[
        ("categorical",OneHotEncoder(handle_unknown="ignore"),cat_col),
         ("numerical",StandardScaler(),num_col)
    ]
)


from xgboost import XGBClassifier

#Label Encoding
le=LabelEncoder()
ytrain_encoded=le.fit_transform(ytrain)
ytest_encoded=le.transform(ytest)


#XG Boost
xgb=XGBClassifier(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0,
    reg_lambda=1,
    objective="multi:softprob",
    eval_metric="mlogloss",
    random_state=42,
)

#Model
model=Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", xgb)
])

model.fit(xtrain,ytrain_encoded)

#Prediction
xgb_pred=model.predict(xtest)

#Accuracy score
print(accuracy_score(ytest_encoded,xgb_pred))

#Saving Model
with open("model.pkl","wb") as file:
    pickle.dump({"model":model, "label_encoder":le},file)

print("Model trained and saved successfully!")