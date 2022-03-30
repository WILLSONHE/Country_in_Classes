# Name: Shenghua He
# Student number: 251016121
# Course: CS1026A 002 SU21
# Instructor: Duff Jones
# Python file "country.py" description: this file works as a basic class of "catalogue.py".

class Country:  # define class name
    # define instance variables
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._population = pop
        self._area = area
        self._continent = continent

    # get method in following
    def get_name(self):
        return self._name

    def get_population(self):
        return self._population

    def get_area(self):
        return self._area

    def get_continent(self):
        return self._continent

    # set method in following
    def set_population(self, new_pop):
        self._population = new_pop

    def set_area(self, new_area):
        self._area = new_area

    def set_continent(self, new_continent):
        self._continent = new_continent

    # string representation class
    def __repr__(self):
        return "{} (pop: {}, size: {}) in {}".format(self._name, self._population, self._area, self._continent)
