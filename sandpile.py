#Program Name: sandpile.ipynb
#Date Created: September 5th, 2022
#Author: Deepesh Verma (dbv293)
#Function: Implementation of the Abelian Sandpile

import numpy as np

class ASP:
    """
     Simulation of the Abelian sandpile. Each lattice site is intiailized with some random value of grains less 
    than max_height. Then a single grain is deposited onto a random lattice site and the system is allowed to 
    evolve following the rules dictating the Bak–Tang–Wiesenfeld model until it becomes stable. The process 
    occurs for n_steps.

    Parameters:
        n: size of the square n by n lattice
        grid: stores the values of the sandpile heights 
        past: stores last step of values of the sandpile heights
    """

    def __init__(self,n,random_state=None):
        """
        Initializes the sandpile and populates it by random int values between 0-3. Also, writes last step 
        values of sandpile heights to past.
        """
        self.n = n
        np.random.seed(random_state)

        #Populates grid with random int values between 0-3.
        self.grid = np.random.choice(4,size=(n,n))

        #Writes last step values of sandpile heights to past.
        self.past = [self.grid.copy()]

    def BTW(self,x,y):
        """
        Implements the update rules of the Bak–Tang–Wiesenfeld model for when we add a single grain to a random
        lattice site. Evolves the heights of the sandpile due to toppling.
        """
        #Adds grain to lattice site.
        self.grid[x,y]+=1      

        #Topple calculation.

        #Pile is below topple height.
        if self.grid[x,y]<4: 
            return None

        #Pile is above topple height.
        else:   
            #Pile topples, so height goes to 0. 
            self.grid[x,y]-=4

            #Update rules for BTW model.
            if x > 0:
                self.BTW(x-1,y)
            if x < self.n-1:
                self.BTW(x+1,y)
            if y > 0:
                self.BTW(x,y-1)
            if y < self.n-1:
                self.BTW(x,y+1)
            return None

    def step(self):
        """
        Evolves the sandpile simulation by a single step. Involves adding a grain to a random lattice site 
        and the corresponding toppling that it causes.
        """
        #Determines a random lattice site for which we add a grain. 
        x, y = np.random.choice(self.n,2)

        #Adds the grain and performs the BTW update for the lattice site. 
        self.BTW(x,y)

    @staticmethod
    def diff(agrid,bgrid):
        """
        Counts the number of different lattice sites between two grids.
        """
        return np.sum(agrid!=bgrid)

    def runsim(self,n_steps):
        """
        Runs the Abelian sandpile simulation for n_steps.
        """
        for i in range(n_steps):
            self.step()
            if self.diff(self.grid,self.past[-1])>0:
                self.past.append(self.grid.copy())
        return self.grid

