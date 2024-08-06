# ДЗ урок 6 "Словари и множества" module_1_6.py
my_dict = {"Petr": 1985, "Elena": 2001, "Oleg": 2012}
print(my_dict)
print(my_dict.get("Elena"))
print(my_dict.get("Nina"))
my_dict.update({"Cvetlana": 1990, "FiL": 2005})
print(my_dict)
del my_dict["Petr"]
print(my_dict)
my_set = {23.5, "avto", 5, 23.5, "avto", 5, 4}
print(my_set)
my_set.update(["moto", (67, 2, 6)])
print(my_set)
my_set.remove(5)
print(my_set)