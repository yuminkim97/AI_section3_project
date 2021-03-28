import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score

from musical_app.services.musical_api import get_musical_info, get_musical_list

musical_list = get_musical_list()

user_info = {'gender':2, 'age':25, 'experience':1, 'accompany':2}
user_info_df = pd.DataFrame(user_info, index=[0])

# num_list = []
pred_proba = []

for musical in musical_list :
    num = musical['res_no']

    df = pd.read_csv(f'musical_app/dataset/df_{num}.csv')
    labels = df['satisfy']
    data = df.iloc[:,:-1]

    classifier = LogisticRegression()
    classifier.fit(data, labels)

    prediction = classifier.predict_proba(user_info_df)
    pred_proba.append({'res_no':num, 'pred':prediction[0][1]})

best_result = max(pred_proba, key=lambda x:x['pred'])
print(pred_proba)
print(best_result['res_no'])