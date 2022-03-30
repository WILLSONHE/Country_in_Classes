# Name: Shenghua He
# Student number: 251016121
# Course: CS1026A 002 SU21
# Instructor: Duff Jones
# Python file "catalogue.py" description: this file works as a basic class for "process_updates.py"

# import class Country
from country import *


class CountryCatalogue:
    # instance variables
    def __init__(self, country_file):
        self.country_cat = dict()
        file = open(country_file, "r")
        for line in file.readlines()[1:]:  # skip first line to avoid display bug
            line = line.strip()  # strip to avoid display bug
            each_country_element_list = line.split("|")  # define list for each element
            name = each_country_element_list[0]
            continent = each_country_element_list[1]
            population = each_country_element_list[2]
            area = each_country_element_list[3]
            country_object = Country(name, population, area, continent)  # define object for each country
            self.country_cat[name] = country_object  # define country_cat

    # setter methods
    def set_country_population(self, name, new_pop):
        if name in self.country_cat:
            self.country_cat[name].set_population(new_pop)

    def set_country_area(self, name, new_area):
        if name in self.country_cat:
            self.country_cat[name].set_area(new_area)

    def set_country_continent(self, name, new_continent):
        if name in self.country_cat:
            self.country_cat[name].set_continent(new_continent)

    # find country
    def find_country(self, name):
        if name in self.country_cat:
            return self.country_cat
        else:
            return None

    def add_country(self, name, pop, area, cont):
        if name in self.country_cat.keys():  # found and return false
            return False
        country_element = Country(name, pop, area, cont)
        self.country_cat[name] = country_element
        return True  # not found, need to add in and return true

    def print_country_catalogue(self):
        self.country_cat.__repr__()

    def save_country_catalogue(self, fname):
        lines = "Country|Continent|Population|Area\n"  # print initial of display
        counting = 0  # set up counting value to be returned
        for name, country_object in sorted(self.country_cat.items()):
            lines += "{}|{}|{}|{}\n".format(name, country_object.get_continent(), country_object.get_population(), country_object.get_area())
            counting += 1
        try:  # print the whole catalogue into "output.txt"
            output_file = open(fname, "w")
            output_file.writelines(lines)
            return counting
        except IOError:
            return -1
