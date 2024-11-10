import random

def genetic_algorithm(population, fitness, mutate, crossover, generation_limit=100):
    for generation in range(generation_limit):
        population = sorted(population, key=fitness, reverse=True)
        if fitness(population[0]) == 1.0:  # Assume 1.0 is perfect fitness
            break
        next_generation = population[:2]
        while len(next_generation) < len(population):
            parent1, parent2 = random.sample(population[:10], 2)
            child = mutate(crossover(parent1, parent2))
            next_generation.append(child)
        population = next_generation
    return population[0]

# Example problem setup
def fitness(individual):
    return sum(individual) / len(individual)

def mutate(individual):
    idx = random.randint(0, len(individual) - 1)
    individual[idx] = 1 - individual[idx]
    return individual

def crossover(parent1, parent2):
    idx = random.randint(1, len(parent1) - 1)
    return parent1[:idx] + parent2[idx:]

# Example usage
# population = [[random.randint(0, 1) for _ in range(10)] for _ in range(20)]
# best = genetic_algorithm(population, fitness, mutate, crossover)
# print("Best individual:", best)
