import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    # group by customer number
    order_count = orders.groupby(['customer_number'])['order_number'].count()
    max_order = order_count.max()
    largest_customers =  order_count[order_count == max_order].index
    return pd.DataFrame(largest_customers, columns=['customer_number'])
