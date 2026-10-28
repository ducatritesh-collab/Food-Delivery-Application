## Customer Analysis
from cleaning_data import load_clean_data

def customer_analysis(customer_df,orders):
     total_customers=customer_df['customer_id'].nunique()
     gender_count=customer_df['gender'].value_counts() 
     city=[]
     for address in customer_df['Address']:
          city.append(address.split(',')[-1].strip())
     customer_df['city']=city
     city_count=customer_df['city'].value_counts()

     repeted_customers=orders['customer_id'].value_counts()>1
     total_repeted_customers=repeted_customers.sum()
     new_customers=total_customers-total_repeted_customers

     return {'Total_customers':total_customers,
             'Gender count':gender_count,
             'city count':city_count,
             'repeted_custumers':int(total_repeted_customers),
             'new customers':int(new_customers)}

# customer_df=load_clean_data()['Customers']
# orders_df=load_clean_data()['Orders']
# # Res_df=load_clean_data()['Rest']
# # print(orders_df.columns)
# # print(Res_df.columns)
# print(customer_analysis(customer_df,orders_df))
