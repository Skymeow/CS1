import random, sys
random.seed(42)
from person import Person
# from logger import Logger
from cleanUp import virus_list
class Simulation(object):
    '''
    Main class that will run the herd immunity simulation program.  Expects initialization
    parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.

    _____Attributes______

    logger: Logger object.  The helper object that will be responsible for writing
    all logs to the simulation.

    population_size: Int.  The size of the population for this simulation.

    population: [Person].  A list of person objects representing all people in
        the population.

    next_person_id: Int.  The next available id value for all created person objects.
        Each person should have a unique _id value.

    virus_name: String.  The name of the virus for the simulation.  This will be passed
    to the Virus object upon instantiation.

    mortality_rate: Float between 0 and 1.  This will be passed
    to the Virus object upon instantiation.

    basic_repro_num: Float between 0 and 1.   This will be passed
    to the Virus object upon instantiation.

    vacc_percentage: Float between 0 and 1.  Represents the total percentage of population
        vaccinated for the given simulation.

    current_infected: Int.  The number of currently people in the population currently
        infected with the disease in the simulation.

    total_infected: Int.  The running total of people that have been infected since the
    simulation began, including any people currently infected.

    total_dead: Int.  The number of people that have died as a result of the infection
        during this simulation.  Starts at zero.


    _____Methods_____

    __init__(population_size, vacc_percentage, virus_name, mortality_rate,
     basic_repro_num, initial_infected=1):
        -- All arguments will be passed as command-line arguments when the file is run.
        -- After setting values for attributes, calls self._create_population() in order
            to create the population array that will be used for this simulation.

    _create_population(self, initial_infected):
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
    '''

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.initial_infected = initial_infected
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        # TODO: Create a Logger object and bind it to self.logger.  You should use this
        # logger object to log all events of any importance during the simulation.  Don't forget
        # to call these logger methods in the corresponding parts of the simulation!
        # self.logger = None
        self._infect_newly_infected()
        self.newly_infected.append(self.next_person_id)
        # This attribute will be used to keep track of all the people that catch
        # the infection during a given time step. We'll store each newly infected
        # person's .ID attribute in here.

        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        self.population.append(self._create_population(initial_infected))


    def _create_population(self, initial_infected):
        # TODO: Finish this method!  This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        self.population = []
        infected_count = 0
        while len(self.population) != self.population_size:
            if infected_count !=  initial_infected:
                disease_object = [self.mortality_rate, self.basic_repro_num]
                new_person = Person(self.next_person_id, False, True, disease_object)
                infected_count += 1
                self.population.append(new_person)
                # TODO: Create all the infected people first, and then worry about the rest.
                # Don't forget to increment infected_count every time you create a new infected person!
            else:
                # Every time a new person will be created If this random number(0,1) is smaller than vacc_percentage, this person
                # should be created as a vaccinated person.
                rand_num = random.uniform(0, 1)
                disease_object = [self.mortality_rate, self.basic_repro_num]
                if rand_num < self.vacc_percentage:
                    rest_person = Person(self.next_person_id, True, True, None)
                    self.population.append(rest_person)
                else:
                    rest_person = Person(self.next_person_id, False, True, None)
                    self.population.append(rest_person)
            self.next_person_id += 1
        # print(self.population)
        return(self.population, infected_count)

    def _simulation_should_continue(self, initial_infected):
        # TODO: Complete this method!  This method should return True if the simulation
        # should continue, or False if it should not.  The simulation should end under
        # any of the following circumstances:
        #     - The entire population is dead.
        #     - There are no infected people left in the population.
        # In all other instances, the simulation should continue.
        all_created_peep = self._create_population(initial_infected)
        if len(self.population) == 0 or all_created_peep[1] == 0:
            return False
        else:
            return True


    def run(self, initial_infected):
        # TODO: Finish this method.  This method should run the simulation until
        # everyone in the simulation is dead, or the disease no longer exists in the
        # population. To simplify the logic here, we will use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # This method should keep track of the number of time steps that
        # have passed using the time_step_counter variable.  Make sure you remember to
        # the logger's log_time_step() method at the end of each time step, pass in the
        # time_step_counter variable!
        time_step_counter = 0
        should_continue = True
        # TODO: Remember to set this variable to an intial call of
        # if self._simulation_should_continue(initial_infected) == True:
        #     should_continue = True
        # else:
        #     should_continue = False
        while should_continue == True:
            self.time_step()
        should_continue = self._simulation_should_continue(initial_infected)
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.  At the end of each iteration of this loop, remember
        # to rebind should_continue to another call of self._simulation_should_continue()
        print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        # TODO: Finish this method!  This method should contain all the basic logic
        # for computing one time step in the simulation.  This includes:
            # - For each infected person in the population
            for person in self.population:
                if person.infection is not None:
                    interactions = 0
                    while interactions < 100:
                        rand_index = random.randint(0,len(self.population)-1)
                        random_person = self.population[rand_index]
                        if person.is_alive == False or random_person.is_alive == False:
                           continue
                        else:
                            self.interaction(person, random_person)
                            interactions += 1

    def interaction(self, person, random_person):
        # TODO: Finish this method! This method should be called any time two living
        # people are selected for an interaction.  That means that only living people
        # should be passed into this method.  Assert statements are included to make sure
        # that this doesn't happen.
        assert person.is_alive == True
        assert random_person.is_alive == True
        # random_person is healthy, but unvaccinated:
        if random_person.is_vaccinated == False and random_person.infection == None:
            rand_num = random.uniform(0, 1)
            if rand_num < self.basic_repro_num:
                newly_infected.append(random_person._id)
                random_person.infection.append(self.virus_name)
                # self.logger.log_interaction
            else:
                return
        else:
            return

            # generate a random number between 0 and 1.  If that number is smaller
            # than basic_repro_num, random_person's ID should be appended to
            # Simulation object's newly_infected array, so that their .infected
            # attribute can be changed to True at the end of the time step.
        # TODO: Remember to call self.logger.log_interaction() during this method!


    def _infect_newly_infected(self):
        # TODO: Finish this method! This method should be called at the end of
        # every time step.  This method should iterate through the list stored in
        # self.newly_infected, which should be filled with the IDs of every person
        # created.  Iterate though this list.
        for person in self.population:
            # in my case set the infection to none if the id is not in newly_infected
            if not person._id in self.newly_infected:
                person.infection == None
        self.newly_infected = []

        # For every person id in self.newly_infected:
        #   - Find the Person object in self.population that has this corresponding ID.
        #   - Set this Person's .infected attribute to True.
        # NOTE: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list!

if __name__ == "__main__":
    # get rid of the first element of command line argument which is python3
    # params = sys.argv[1:]
    # pop_size = int(params[0])
    # vacc_percentage = float(params[1])
    # virus_name = str(params[2])
    # mortality_rate = float(params[3])
    # basic_repro_num = float(params[4])
    # if len(params) == 6:
    #     initial_infected = int(params[5])
    # else:
    #     initial_infected = 1
    simulation = Simulation(10000, 98, 'Anthrax (untreated)', virus_list['Anthrax (untreated)'][0]*0.01, virus_list['Anthrax (untreated)'][1], 100)
    simulation.run(simulation.initial_infected)
