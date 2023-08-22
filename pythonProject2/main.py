# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import uvicorn
from fastapi import FastAPI
from dataset import load_dataset
from apriori import apriori_alg

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/apriori")
async def apriori():
    dataset = load_dataset()
    min_support = 0.01

    frequent_itemsets = apriori_alg(dataset, min_support)

    print("Frequent Itemsets:")
    for itemset in frequent_itemsets:
        print(itemset)

    return {"recommendation: {0}".format(frequent_itemsets)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)