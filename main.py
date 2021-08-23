# This is a sample Python script.
import csv

cars_list = [{"id":1, "Brand":"Hyundai", "Model":"Santa_Fe", "hp":189, "price":30000},
             {"id":2, "Brand":"Kia", "Model":"Sorento", "hp":140, "price":20000}]

keys = cars_list[0].keys()

car_file = open("/home/hastatus/git_environment/car_file.csv", "w")
car_writer = csv.DictWriter(car_file, keys)
car_writer.writeheader()
car_writer.writerows(cars_list)
car_file.close()