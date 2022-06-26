
from fun_api import *
def get_recommendations(element_the_search):

    index_of_element = df[df['Course Name']==element_the_search].index.values[0]
    show_element_the_search = df.iloc[index_of_element]['Reference']
    df_without_element = df.drop(index_of_element).reset_index()

    vectors_array = list(tag_vectors)
    target = vectors_array.pop(index_of_element).reshape(1,-1)


    vectors_array = np.array(vectors_array)

    rec_similar = cosine_similarity(target, vectors_array)[0]

    idx = (-rec_similar).argsort()

    all_values = df_without_element[['Reference']]
    for recommend in idx:
        simular = all_values.values[idx]

    recommendations_df = ({'Reference': show_element_the_search,
                           "1": simular[0][0],
                           "2": simular[1][0],
                           "3": simular[2][0],
                           "4": simular[3][0],
                           "5": simular[4][0]})


    return recommendations_df

from flask import Flask,request

app = Flask(__name__)


@app.route('/rec/<courseName>', methods=['GET'])
def get_books_rec(courseName):
    # show the user profile for that user
    return get_recommendations(courseName)


if __name__ == "__main__":
    app.run(debug=True)

