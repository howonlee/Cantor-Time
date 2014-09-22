Cantor Time
=====

Introduction
---

>"You will be home before the leaves fall from the trees."
>
>_Kaiser Wilheim II of Germany, August 1914. The war went on for four years._

There are areas of life where systematic and huge, but unpredicted failures in time forecasting occur. They seem to mostly be event-based progressions which do not occur in predictable fashions. The length of revolutions and wars, the length of software and other design projects, the time it takes to make a thing by hand, and so on. The thing which is of most interest to me is software project estimation, which is properly a subset of design projects (a programmer designs software: it is the computer that builds it, unless you're writing assembler). I think some ideas from B. Mandelbrot's work can shed some light on why and how these huge failures in time forecasting occur.

(table indicating huge failures in software project estimation)

One possible way to model these projects is as a temporal stochastic process. Temporal, because we are thinking about the time aspects of these phenomena, and stochastic because although the outcomes of these projects may be deterministic (or not, depending), they are so complicated that we are tempted to ignore the structure and say that progress in the project is stochastic. So we think of temporal stochatic processes, which meander from having nothing done (0) to having the project done as it will be (1). The actual lengths of the intervals both don't and do matter, as we will see, but it is most important to think of the shape and structure of the progression from being not done to being done.

The naive model in some people's heads is that of uniform progression towards the goal. Let's agree that this is idiocy and not talk about it anymore.

(graph of naive model)

Another model we can think about is a normally distributed random walk in 1-dimensional space, which is prevented from going back down because reasons.

(picture of normal random walk)

Back out to a higher level of abstraction. Two significant patterns in the temporal structure of data were noted by Mandelbrot: the Noah Effect, which says that sudden discontinuous changes (grand floods) can occur in a lot of temporal processes, and the Joseph Effect, where temporal processes are stable for a while, but then are not. That sounds totally obvious, a bunch of baloney, but it is important to note that noticing these processes in action make it impossible to say that the temporal process you're talking about can be modelled with a normally distributed random walk (why?).

These two effects seem omnipresent in software project work.

(examples here)

Cantor Sets and Power Laws
====

Another pattern in time noted by Mandelbrot is the patterning of noise in information. To Mandelbrot, noise was patterned like a Cantor set: errors are inevitable and do not go away with enough data, because the process by which the errors occur scale with the size of the temporal interval that you're looking at.

There is, implicitly held in many cases, an assumption of normality in the scheduling of production processes. That is, it is assumed that with some dilligent effort and enough (lots! lots more!) estimation, estimates will veer closer to the truth. But it is also admitted at the same time that errors abound which scale to the size of the temporal interval you're estimating at.

We might think of another model for the timing of design work, wars, and other processes in which these events which have lots of the properties of electrical noise happen in time and invariant to the scale of things. We would take it from Mandelbrot's cantor set construction. You couldn't find out which scale you were on specifically, and you would give up: instead, you would figure out how many doublings of time, or triplings, or what have you, you were going to go through, and try to make your predictions in a power law space instead.

(picture of devil's staircase)

Note that the devil's staircase encompasses the idea that delays accumulate in jumps.

(graph of power law of project sizes)

(put the github analysis here)

Other Explanations
====

This essay only really thinks about one explanation for the power law phenomenon, but if you're not someone like Per Bak, you may admit of many possible sources of power law phenomena. Many of these sources have analogues to this problem, stated this way, and they might also have give some insight into the problem.

Diffusion-limited aggregation, where the Matthew Effect ("For unto every one that hath shall be given, and he shall have abundance: but from him that hath not shall be taken even that which he hath") dominates. It's much harder to shoe-horn these processes into a temporal framework, but the phenomena and especially the Matthew effect has to be mentioned, since it seems to happen a lot in software projects.

It seems to me that this is closely related to R. Gabriel's "New Jersey Style", or "Worse is Better", the phenomena that less functionality is a preferable option to more fiddling. There is also the obvious parallel to much marketing thinking.

(example)

One phenomenon which is fundamentally non-geometric and non-temporal which should also be mentioned (diffusion-limited aggregation was originally invented to explain the geometry of cracking things, lightning and other such figures) which nevertheless comes with an associated power law is the monkeys-typing-randomly model. This is associated quite a bit with linguistic models. If you have a language with _N_ letters and a space bar, where a space separates words and the space is hit with probability _p_, and all the other letters are hit with probability _(1 - p)/N_, the rank-frequency distribution of words follows a power law. That is, a one-letter word is way more frequent than a two-letter word, which is way more frequent than a three-letter one. Many people talk about design languages, and design patterns.

There's a lot of other models which engender power laws out there. Sandpile models, forest fire models, fractional Brownian motion. I will not mention more about them here, but I suspect that some of them may have value also for thinking about the important temporal process of software design.

Consequences
====

The models which I have mentioned are all models, and therefore all convenient lies. They should not really be said to have a reality, but merely a usefulness. However, they seem useful to me in this domain. The only previous connection this strange class of models which involve power laws has had with software projects is in the Pareto principle, which states that 80% of the effect is caused by 20% of the cause.

Although it is probably the case that this essay will seem more useful than it is, if you choose to adopt a fractal time model for your scheduling, there are things to keep in mind. Different points of view towards estimation are engendered by taking on any of these models (that is their point). Keep track of the speed of the doublings of things, says a Cantor dust model of progression in software projects, because the structure of the progress made is invariant with respect to scale. You might be able to play find-the-productivity-gap-size. You might take power law statistics instead of normal people ones.
