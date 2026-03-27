# Calculate the net worth of Ram and Lakshman
ram_bank_balance=100000
#ram's bank balance, note this is a positive value
ram_loan=500000
#ram's loan, this is to be returned, so it is a negative value

lakshman_bank_balance=2000000
lakshman_loan=10000000

net_income=ram_bank_balance+lakshman_bank_balance
#this is the total income of the family
net_liability=ram_loan+lakshman_loan
#this is the total loan of the family

final_value=net_income-net_liability
#final_value is the net worth of the family (could be positive or negative)
print("so, the family has", final_value)
