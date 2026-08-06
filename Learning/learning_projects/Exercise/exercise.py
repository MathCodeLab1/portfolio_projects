
neighbourhood_prices = (
    df_clean
    .groupby("neighbourhood")["price"].mean()
    .sort_values(ascending=False)
    neighbourhood_prices.head(10)
)



    



    


    






