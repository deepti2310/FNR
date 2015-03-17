import random
import operator

class FNRGeneticAlgorithm(object):
    def __init__(self, failed_sensor_nodes = [], nodes_info = {}, population_size = 100,  ):
        self.failed_sensor_nodes = failed_sensor_nodes
        self.sensor_nodes_info = nodes_info
        self.population_size = population_size
        self.init_population = []
        self.current_population = []
    
    def __initialize(self):
        for i in range(self.population_size):
            chromosome = []
            for j in range(len(self.failed_sensor_nodes)):
                chromosome.append(random.randint(0,1))
            self.self.init_population.append(chromosome)
    
    def __calculate_fitness_function(self, chromosome):
        """
        Implemeting some dummy fitness function
        2*x1 - 2.x2 + 3*x3 + 4*x4 - 5*x5 +2*x6 - 3*x7 + 4*x8 + 9*x9 + 10*x10
        input = [1,1,0,1,0,1,1,1,1,1]
        output = 2*1 -2*1 + 3*0+4*1-5*0+2*1-3*1+4*1+9*1+10*1 = 2-2+0+4-0+2-3+4+9+10=26
        """
        factors_list = [2,-2,3,4,-5,2,-3,4,9,10]
        return tuple(chromosome),sum([i*j for i,j in zip(chromosome, factors_list)])
        
        
        pass
        
    def __evaluation(self):
        pass
    
    def __crossover(self):
        pass
    
    def __mutation(self):
        pass
    
    
    def get_solutions(self, iterations=2):
        self.__initialize()
        population = []
        for chromosome in self.init_population:
            key,value=self.__calculate_fitness_function(chromosome)
            population.append((key,value))
        population=sorted(population, key = lambda item: item[1], reverse = True)
        
def main():
    g = FNRGeneticAlgorithm(failed_sensor_nodes = [9, 7, 10, 81, 23, 57, 34, 46, 66, 70])
    g.get_solutions() # init population
    
    
if __name__ == "__main__":
    main()
