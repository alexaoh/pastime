"""Turned out as one big chaos. 

Anyhow, the simulations verify my theoretical probabilities in Problem set 1 in 
Stochastic Modelling.
"""

import random

N = 100000 # Some large number. 

class Coin_toss:
    """A lot of unnecessary code, which makes no sense currently."""
    def __init__(self, assumption, N):
        self.assumption = assumption
        self.picked_coin = self.pick_coin()
        self.N = N

        self.counts = {
            "heads": 0,
            "tails": 0
        }

        self.p_given_assumption = 0

    def pick_coin(self):
        """Pick either a normal or a biased (two heads) coin from pocket."""
        coin = round(random.uniform(0,1))
        if coin == 0:
            picked_coin = "normal"
        else: 
            picked_coin = "biased"
        return picked_coin

    def toss_once(self):
        """Toss the coin once."""
        for i in range(N):
            if self.picked_coin == "normal":
                random_num = round(random.uniform(0,1))
                if random_num == 1:
                    self.counts[self.assumption] += 1
            elif self.picked_coin == "biased":
                self.p_given_assumption += 1
        return self.p_given_assumption/self.counts[self.assumption]


    def toss_twice(self):
        """Toss the coin twice."""
        for i in range(N):
            pass
        return prob

    def simulate_one_toss(self):
        """Simulate tossing one coin and finding the frequency of biased coins given heads:"""
        self.p_biased_given_heads = 0
        self.heads = 0
        self.tails = 0
        for i in range(N):
            self.flip()
        return self.p_biased_given_heads/self.heads

    def simulate_two_tosses(self):
        """A coin is flipped two times. 
        
        Returns the probability that the biased coin was flipped.
        Heads is resultant in each flip. 
        """
        self.p_biased = 0
        self.heads_heads = 0

        for i in range(N):
            self.flip_2()
        return self.p_biased/self.heads_heads

    def flip(self):
        r = round(random.uniform(0,1))
        if r == 1:
            # Biased coin
            prob_heads = 1
            prob_tails = 0
            self.p_biased_given_heads += 1
            self.heads += 1
        else: 
            # Unbiased coin
            r = round(random.uniform(0,1))
            if r == 1:
                # heads
                self.heads += 1
            else: 
                # tails
                self.tails += 1

    def flip_2(self):
        """Only count when the biased coin is flipped twice. And when heads is twice."""
        r = round(random.uniform(0,1))
        if r == 1:
            # Biased coin
            self.p_biased += 1
            self.heads_heads += 1
        else: 
            # Unbiased coin
            r = round(random.uniform(0,1))
            if r == 1:
                # heads
                r = round(random.uniform(0,1))
                if r == 1:
                    #heads heads
                    self.heads_heads += 1
            else: 
                # tails
                self.tails += 1


coin_toss = Coin_toss("heads", N)
one_toss = coin_toss.simulate_one_toss()
two_toss = coin_toss.simulate_two_tosses()
print(one_toss)
print(two_toss)
