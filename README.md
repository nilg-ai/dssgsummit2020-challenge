# Keyboard Layout Optimization for ALS Patients

** NOTE ** This README is a work in progress. 

This competition is organized together with the [DSSG Summit 2020](www.summit.dssg.pt). Its goal is to optimize a keyboard layout to minimize the workload for usage by an ALS patient. This was motivated by [Anthony Carbajal](www.anthonycarbajal.com), a full-time daily life hacker that aims to find innovative ways to improve his and other ALS-patient lives, with whom we worked together for developing a first version of this solution. You will work in creating innovative solutions to the problem we tried to solve!

![Hexagonal Keyboard Layout](images/image1.png "Hexagonal Keyboard Layout")

## Building a solution and evaluation


![Optimization Function"](images/image2.png?raw=true "Optimization Function") ![Key Positions](images/image3.png?raw=true "Key Positions")

In this challenge, you will be working with an hexagonal keyboard. 

Keyboard indexes are done by serialization of the positions by clockwise traversing of the concentric rings. Each position contains the proposed letter (right image). The problem translates to finding the best permutation, which is a well-known established optimization problem.

The problem will be evaluated using two different criteria: objective and subjective criteria.

**Objective criteria**

We assume the writing effort is proportional to the expected distance traveled in the transition between each pair of letters (left image). The expected value is computed using a large text corpus.

Participants will be ranked according to a loss function based on the Expected Cost of writing a large corpus of text using the proposed keyboard layout.

You should submit a solution for both portuguese and english language.

**Subjective criteria**

You should submit a Youtube video containing a maximum 3 minute pitch (with slides presentation, or just a video of you talking) describing what you would do to solve this issue of keyboard optimization. Do not talk about what you did in technical terms, but focus on topics like:

- Alternative keyboard layouts, and why they are better than the hexagonal one
- Changes in eye tracking technology and other interaction mechanisms
- Different transition matrix, instead of being at a character level (how and why?) 
- How well would your idea scale to other languages
- How you would make this compatible with multiple wheelchairs and interfaces

Your video will be evaluated according to criteria such as:

- Benchmarking of similar solutions
- Creativity
- Future improvement of idea and opportunities
- Scalability of presented idea
- Replicability of presented idea
- Practicability of presented idea
- Presentation skills - organization and logical flow of pitch


## Prizes

The winning team of this competition will be given a 300€ Amazon gift card, split by the number of members of the team. 

Any further questions, you may direct them to us on the Slack channel or by creating a Github Issue.









