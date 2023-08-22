import pandas as pd
import numpy as np

def load_dataset():
    folder = "FitabaseData"
    calories = pd.read_csv("{0}/dailyCalories_merged.csv".format(folder))
    steps = pd.read_csv("{0}/dailySteps_merged.csv".format(folder))
    sleep = pd.read_csv("{0}/sleepDay_merged.csv".format(folder))
    dataset = [
        ['milk', 'bread', 'sugar'],
        ['bread', 'sugar'],
        ['milk', 'bread'],
        ['milk', 'bread', 'sugar', 'eggs'],
        ['eggs', 'sugar']
    ]
    # prepare Dataset as Dataframe
    calories['ActivityDay'] = pd.to_datetime(calories['ActivityDay'])
    calories.sort_values('ActivityDay')

    steps['ActivityDay'] = pd.to_datetime(steps['ActivityDay'])
    steps.sort_values('ActivityDay')

    sleep['SleepDay'] = pd.to_datetime(sleep['SleepDay'])
    sleep.sort_values('SleepDay')
    sleep = sleep.rename(columns={"SleepDay": "ActivityDay"})

    calories_steps = pd.merge(calories, steps, on=['Id', 'ActivityDay'])
    print(calories_steps.head())

    all = pd.merge(calories_steps, sleep, on=['Id', 'ActivityDay'])
    all = all.loc[all['Id'] == 1503960366] # select data only for 1 person
    print(all)
    all.to_csv("caloriesStepsAndSleepInfo_merged.csv")
    return dataset