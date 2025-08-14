import pandas as pd

def calculate_demographic_data(print_data=True):
    
    df = pd.read_csv("adult.data", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education_num",
        "marital_status", "occupation", "relationship", "race", "sex",
        "capital_gain", "capital_loss", "hours_per_week", "native_country", "income"
    ], na_values=" ?", skipinitialspace=True)

    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    higher_education_rich = round((df[higher_education]['income'] == '>50K').mean() * 100, 1)

    lower_education_rich = round((df[lower_education]['income'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours_per_week'].min()

    num_min_workers = df[df['hours_per_week'] == min_work_hours]
    rich_percentage = round((num_min_workers['income'] == '>50K').mean() * 100, 1)

    country_earning = df[df['income'] == '>50K']['native_country'].value_counts()
    country_total = df['native_country'].value_counts()
    country_percentage = (country_earning / country_total * 100).round(1)
    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = country_percentage.max()

    india_occupation = df[(df['native_country'] == 'India') & (df['income'] == '>50K')]['occupation'].value_counts()
    top_IN_occupation = india_occupation.idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
