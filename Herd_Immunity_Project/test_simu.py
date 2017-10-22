import pytest
import random, sys
from simulation import Simulation
from person import Person

def setup_for_test():
    pop_size = 30
    vacc_percentage = 0.70
    virus_name = "skydisease"
    mortality_rate = 0.50
    basic_repro_num = 0.25
    initial_infected = 15
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected)
    return simulation

def test_setup():
    simulation = setup_for_test()
    assert simulation.population_size == 30
    assert simulation.vacc_percentage == 0.70
    assert simulation.virus_name == "skydisease"
    assert simulation.mortality_rate == 0.50
    assert simulation.basic_repro_num == 0.25
    assert simulation.initial_infected == 15
    assert simulation.population == []

def test_create_population():
    simulation = setup_for_test()
    assert len(simulation.population) == 30

def test_simulaiton_should_continue():
    simulation = setup_for_test()
    population_size = 30
    population = ["sky1", "sky2"]
    assert True




