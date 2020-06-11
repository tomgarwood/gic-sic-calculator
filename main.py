import pandas as pd


def tax_calculator(kind, start, end, base, penalty):
    if kind == 'gic':
        df = pd.read_csv('data/gic_rates.csv')
    elif kind == 'sic':
        df = pd.read_csv('data/sic_rates.csv')
    # set date column as index
    df.set_index('date', inplace=True)
    df.index = pd.to_datetime(df.index)
    # grab relevant subset dataframe based on start/end dates and turn into list
    df_subset = df.loc[start:end]
    rates = df_subset['rate'].tolist()
    # iterate tax amount against rate list and return calculated amount
    amount = base + penalty
    for i in rates:
        amount = amount * i
    return amount - base - penalty

