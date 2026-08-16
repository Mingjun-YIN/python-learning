import numpy as np
heart_rates_list = [60, 70, 80, 90, 100]
print(heart_rates_list)
print(type(heart_rates_list))
heart_rates_array = np.array(heart_rates_list)
print(heart_rates_array)
print(type(heart_rates_array))
print(heart_rates_list * 2)
print(heart_rates_array * 2)
print(heart_rates_array + 5)
print(heart_rates_array / 2)
print(heart_rates_array ** 2)