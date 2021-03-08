customer_time = int(input("введите время в секундах >>>"))

customer_h = customer_time // 3600
remeins_for_m = customer_time - customer_h * 60 * 60
customer_m = remeins_for_m // 60
customer_s = customer_time - customer_h * 60 * 60 - customer_m * 60
print(f'{customer_h}:{customer_m}:{customer_s}')
