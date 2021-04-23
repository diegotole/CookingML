import os
import zipfile
import json
import io

def getData():
    def getObj(myfile):
        buffer = f.read()
        z = zipfile.ZipFile(io.BytesIO(buffer))
        buffer = z.open("train.json.zip").read()
        z2 = zipfile.ZipFile(io.BytesIO(buffer)).open('train.json').read()
        obj = json.loads(z2)
        return obj


    try:
        with open("whats-cooking.zip", "rb") as f:
            obj =  getObj(f)


    except Exception as e:
        print("Downloading Kaggle zip file:", e)
        os.system("kaggle competitions download -c whats-cooking")
        with open("whats-cooking.zip", "rb") as f:
            obj =  getObj(f)

    # ingredients = set()
    # for recipe in obj:
    #     for ingred in recipe["ingredients"]:
    #         ingredients.add(ingred)
    #
    #
    # return list(ingredients)
    return obj






if __name__ == "__main__":

    obj = getData()
    print(obj)