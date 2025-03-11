# Markov Chain Monte Carlo (MCMC) Sampling <br> with the Metropolis-Hastings Algorithm
Gianmarc Grazioli, Ph.D.

This short demonstration applies MCMC sampling to a 1D potential energy surface, $V(x) = (x-1)^2(x+1)^2$, where the system obeys Boltzmann statistics, meaning the probability of observing the system in position $x$ as a function of temperature is expressed in the following way:

$P(x) = \frac{e^{- V(x) / k_BT}}{Z}$ <br><br>
where $T$ is temperature, $k_B$ is Boltzmann's constant, and $Z$ is the partition function:<br>

$Z = \int_{-\infty}^{\infty} e^{- V(x) / k_BT} dx$. <br><br>
Note that $Z$, the partition function, is the normalization constant for the probability density function (PDF). In this application, we carry out a simple numerical integration by approximating the integral as a sum over the area of many thin rectangles of width $dx$ and height $e^{- V(x) / k_BT}$. <br><br>

$Z \approx \sum_{x=x_{min}}^{x_{max}} e^{- V(x) / k_BT} dx$

This code can be run either by executing the Jupyter notebook or the main.py file.

Enjoy! :-)