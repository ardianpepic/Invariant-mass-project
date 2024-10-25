# Invariant-mass-project
This Python program is my first particle physics data analysis project, in collaboration with Professor Whiteson of UC Irvine. This repository hosts the initial version of the "warmup" project that I am working on, as a prerequisite for a particle physics research project that I may complete in the future. For this project, I was provided with a text file ("muons.txt") with data from simulated particle collisions. The collisions contained two muons. The objective was to find out whether the muons came from the decay of a heavy particle or not. To answer this question, I had to calculate the "invariant mass" of the hypothetical particle that the muons may have decayed from (i.e., find the invariant mass for each muon collision in the file). In the case that the calculation yielded many events with the same invariant mass, then it would be probable to think that a particle at that mass might exist. My task was to convert this physical problem into a computational one; I did this by writing a Python program that carried out the necessary calculations, and saved them to a new text file, "invariant_masses.txt."

Here is the mathematical foundation for this problem:

For a muon, we measure
"pt", Transverse momentum = sqrt (px^2 + py^2)
"phi",   angle in the x-y plane
"eta", pseudorapidity, which is another form of the angle from the z-axis
	see:  	http://en.wikipedia.org/wiki/Pseudorapidity
"mass", the mass of the muon.

If you know these 4 quantities, you can use trigonometry to calculate the x,y,z components of the momentum, as well as the total energy:

E = sqrt ( mass^2 + momentum^2)

Together, the momentum+energy are a 4-vector or "Lorentz vector"
	see:  http://en.wikipedia.org/wiki/Four-momentum

To calculate the invariant mass of the hypothetical particle from the components, use this formula:

M^2 = (E1 + E2)^2 - ||P1 + P2||^2 = (m1)^2 + (m2)^2 + 2(E1 * E2 - P1 * P2)

see: http://en.wikipedia.org/wiki/Invariant_mass

So, I wrote a Python program that reads in the attached file "muons.txt", and for each event:

i) calculates the 4-vector for each muon

ii) calculates the invariant mass of the hypothetical particle

iii) writes that mass to another file, "invariant_masses.txt"

I used the ROOT data analysis framework to process the data for the muon collisions, and included a function that saved the calculated invariant masses in a histogram file, entitled "invariant_masses_histogram.pdf."
