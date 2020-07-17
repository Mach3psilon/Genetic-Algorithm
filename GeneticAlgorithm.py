

import random
#You can enter the String that you want to test below
OPTIMAL = ""
DNA_SIZE = len(OPTIMAL)
POP_SIZE = 100
GENERATIONS = 1500


def random_char():
    """
    Return a random character between ASCII 32 and 126 (i.e. spaces, symbols,
    letters, and digits). All characters returned will be nicely printable.
    """
    return chr(random.randrange(32, 126, 1))


def random_population():
    """
    Return a list of POP_SIZE individuals, each randomly generated via iterating
    DNA_SIZE times to generate a string of random characters with random_char().
    """
    pop = []
    for i in range(POP_SIZE):
        dna = ""
        for c in range(DNA_SIZE):
            dna += random_char()
        pop.append(dna)
    return pop


def weighted_choice(items):
    """
    Chooses a random element from items, where items is a list of tuples in
    the form (item, weight). weight determines the probability of choosing its
    respective item. Note: this function is borrowed from ActiveState Recipes.
    """
    weight_total = sum((item[1] for item in items))
    n = random.uniform(0, weight_total)
    for item, weight in items:
        if n < weight:
            return item
        n = n - weight
    return item


def fitness(dna):
    """
    For each gene in the DNA, this function calculates the difference between
    it and the character in the same position in the OPTIMAL string. These values
    are summed and then returned.
    """
    fitness = 0
    for c in range(DNA_SIZE):
        if dna[c] == OPTIMAL[c]:
            fitness += 1
    return fitness


def mutate(dna):
    """
    For each gene in the DNA, there is a mutation_chance chance that it will be
    switched out with a random character. This ensures diversity in the
    population, and ensures that is difficult to get stuck in local minima.
    """
    dna_out = ""
    mutation_chance = 0.01
    for c in range(DNA_SIZE):
        if random.uniform(0, 1) < mutation_chance:
            dna_out += random_char()
        else:
            dna_out += dna[c]
    return dna_out


def crossover(dna1, dna2):
    """
    Slices both dna1 and dna2 into two parts at a random index within their
    length and merges them. Both keep their initial sublist up to the crossover
    index, but their ends are swapped.
    """
    pos = int(random.random() * DNA_SIZE)
    new_dna1 = dna1[:pos] + dna2[pos:]
    return new_dna1


population = random_population()

for generation in range(GENERATIONS):
    print("Generation %s... Random sample: '%s'" % (generation, population[0]))

    weighted_population = []

    for individual in population:
        fitness_val = fitness(individual)

        pair = (individual, fitness_val)

        weighted_population.append(pair)

    population = []
    for _ in range(int(POP_SIZE)):
        # Selection
        ind1 = weighted_choice(weighted_population)
        ind2 = weighted_choice(weighted_population)

        # Crossover
        ind = crossover(ind1, ind2)

        # Mutate and add back into the population.
        population.append(mutate(ind))

    fittest_string = population[0]
    maximum_fitness = fitness(population[0])


for individual in population:
    ind_fitness = fitness(individual)
    if ind_fitness > maximum_fitness:
        fittest_string = individual
        maximum_fitness = ind_fitness

print("Fittest String: %s" % fittest_string)

a= input("Restart the algorithm in case of a different try")