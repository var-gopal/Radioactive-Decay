# Radioactive Decay

## Aim

The aim of this checkpoint is to write an application to simulate the radioactive decay of unstable nuclei.

Radioactive decay is a statistical process; it is impossible to predict when a given nucleus will decay, only a probability that it might. As the decay of individual nuclei are random events, if there are $N$ nuclei present at time $t$, the number of nuclei $ΔN$ which decay in a small time interval between $t$ and $t+Δt$ is proportional to $N$:

$ΔN=−λNΔt$

where the constant of proportionality $λ$ is the decay constant.

### Exponential decay formula Reveal
Integrating the expression above gives the well-known exponential decay formula for radioactive decay:

$N=N_0e^{−λt}$

where $N_0$ is the number of nuclei at time $t=0$.

However, you should NOT use this formula to code this checkpoint. Instead, you will simulate the random nature of radioactive decay directly using a random number generator. This is an example of a ‘Monte Carlo’ simulation.

###
    
We can also rearrange this expression to obtain the probability $p$ that a nucleus decays within a given time interval $Δt$:

$p=ΔN/N=−λΔt$

(the minus sign simply means that the number of undecayed nuclei decreases).

Note that in the expressions above we have assumed that $N$ is constant (to a good approximation) over the time interval $Δt$, i.e. that only a small fraction of the nuclei will decay during this time. This means that the probability of decay in the time interval $Δt$ should be small, i.e. $p$ should be much less than $1$. In turn, this means that the time interval $Δt$ should be short compared to the average lifetime $τ$, where $τ=1/λ$.

### Average lifetime, half-life and decay constant
The average lifetime, $τ$, is given by the time taken for the number of undecayed nuclei to be reduced to $1/e$ of its initial value. It is related to the decay constant by $τ=1/λ$.
The half-life, $T_{1/2}$, is the time taken for the number of undecayed nuclei to be reduced to half of its initial value. It is related to the decay constant by

$T1/2=ln(2)/λ$.

## Task

Iodine-128 is a radionucleide often used as a medical tracer. It has a half-life $T_1/2=24.98$ minutes, giving a decay constant $λ=0.02775 min^{−1}$.

Write an object-oriented Python program to simulate the radioactive decay of a 2D array (or list) of N×N Iodine-128 nuclei. (Note there is nothing significant in a 2D array here. It is just a convenient way to ‘hold’ and visualise the atoms.)

Your code should prompt the user for the value of the decay constant $λ$, the length $N$ of the 2D array and the timestep $Δt$. For Iodine-128, suggested values are $N=50$ and $Δt=0.01 min$.

Your code should then simulate radiative decay by randomly selecting undecayed nuclei to decay as follows: At each timestep it should iterate over all of the elements in the array, check each to see whether it has decayed and if not, determine whether or not to decay it by generating a random number and comparing it to $p$, the probability of decay in the given time interval.

Rather than run until all of the nuclei have decayed (which could take many iterations - remember that decay is a random process!), your code should terminate when the number of undecayed nuclei has fallen to half of the initial value. The time taken to reach this point is the ‘simulated’ value of the half-life $T_1/2$. It should then print out:

- A visual representation of the array of nuclei; this should clearly distinguish between undecayed and decayed nuclei, for example by using 0 and 1 for decayed and undecayed nuclei respectively.
- The initial and final number of undecayed nuclei.
- The simulated value of the half-life.
- The actual value of the half-life, as given by the decay constant.