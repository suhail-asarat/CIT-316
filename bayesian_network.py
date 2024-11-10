class BayesianNetwork:
    def __init__(self):
        self.network = {}

    def add_variable(self, name, probabilities):
        self.network[name] = probabilities

    def get_probability(self, variable, evidence):
        prob = self.network[variable]
        if isinstance(prob, dict):
            for e in evidence:
                prob = prob[evidence[e]]
        return prob

# Define a sample Bayesian Network for testing
# Example usage
# bn = BayesianNetwork()
# bn.add_variable('Rain', {True: 0.2, False: 0.8})
# bn.add_variable('Sprinkler', {True: 0.1, False: 0.9})
# print("P(Rain=True):", bn.get_probability('Rain', {}))
