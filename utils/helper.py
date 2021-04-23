from numpy import array
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import utils.whatscooking.data as wcdata
from numpy import argmax
from sklearn.preprocessing import MultiLabelBinarizer




def getMultiLabelTransformer(ingredients):
    mlb = MultiLabelBinarizer()
    mlb.fit([ingredients])

    return mlb


def getWhatsCookingIngredients(recipes_train_json):
    # get list of ingredients
    ingredients = set()

    for recipe in recipes_train_json:
        for ingred in recipe["ingredients"]:
            ingredients.add(ingred)

    ingredients = list(ingredients)
    #ingredients.sort()
    return ingredients

if __name__ == "__main__":

    d = wcdata.getData()[:10]
    ingredients = getWhatsCookingIngredients(d)


    mlb = MultiLabelBinarizer()
    print("size:", len(ingredients))
    mlb.fit([ingredients])

    sample = [ [ ingr for ingr in r['ingredients']  ]      for r in d    ]
    z2 = mlb.transform(sample)


    print(len(d))

