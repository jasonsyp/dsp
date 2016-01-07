# Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats"/>](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)  

## Instructions

The ThinkStats book is approximately 200 pages in length.  It is recommended you read the entire book, particularly if you are less familiar with introductory statistical concepts.

The stats exercises have been chosen to introduce/solidify some relevant statistical concepts related to data science.  The solutions for these exercises are available in the ThinkStats repository on GitHub.  You should focus on understanding the statistical concepts, python programming and interpreting the results.  If you are stuck, review the solutions and recode the python in a way that is more understandable to you. 

For example, in the first exercise, the author has already written a function to compute Cohen's D.  You could import it, or you could write your own to practice python and develop a deeper understanding of the concept. 

Complete the following exercises along with the questions in this file. They come from Think Stats, and some can be solved using code provided with the book. The preface of Think Stats [explains](http://greenteapress.com/thinkstats2/html/thinkstats2001.html#toc2) how to use the code.  

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

---

### Instructions for cloning the repo 
Using the code referenced in the book, follow the step-by-step instructions below.  

**Step 1. Create a directory on your computer where you will do the prework.  Below is an example:**

```
(Mac):      /Users/yourname/ds/metis/prework  
(Windows):  C:/ds/metis/prework
```

**Step 2. cd into the prework directory.  Use GitHub to pull this repo to your computer.**

```
$ git clone https://github.com/AllenDowney/ThinkStats2.git
```

**Step 3.  Put your ipython notebook or python code files in this directory (that way, it can pull the needed dependencies):**

```
(Mac):     /Users/yourname/ds/metis/prework/ThinkStats2/code  
(Windows):  C:/ds/metis/prework/ThinkStats2/code
```

---

###Required Exercises

###Q1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (effect size of Cohen's d)  
Cohen's D is an example of effect size.  Other examples of effect size are:  correlation between two variables, mean difference, regression coefficients and standardized test statistics such as: t, Z, F, etc. In this example, you will compute Cohen's D to quantify (or measure) the difference between two groups of data.   

You will see effect size again and again in results of algorithms that are run in data science.  For instance, in the bootcamp, when you run a regression analysis, you will recognize the t-statistic as an example of effect size.

```python
import nsfg
import thinkstats2

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

mean_live = live.totalwgt_lb.mean()
mean_first = firsts.totalwgt_lb.mean()
mean_others = others.totalwgt_lb.mean()

print('Mean Live:', mean_live)
print('Mean First:', mean_first)
print('Mean Others', mean_others)

print('Difference in lbs:', mean_first - mean_others)
print('Difference in oz:', (mean_first - mean_others) * 16)

d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print("Cohen's d:", d)
```

###Q2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
This problem presents a robust example of actual vs biased data.  As a data scientist, it will be important to examine not only the data that is available, but also the data that may be missing but highly relevant.  You will see how the absence of this relevant data will bias a dataset, its distribution, and ultimately, its statistical interpretation.

```python
import nsfg
import thinkstats2
import thinkplot
import chap01soln

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

if __name__ == '__main__':
    resp = chap01soln.ReadFemResp()
    pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')
    biased = BiasPmf(pmf, label='biased')

    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased])
    thinkplot.Show()
```

###Q3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (random distribution)  
This questions asks you to examine the function that produces random numbers.  Is it really random?  A good way to test that is to examine the pmf and cdf of the list of random numbers and visualize the distribution.  If you're not sure what pmf is, read more about it in Chapter 3.  

```python
import random
import thinkstats2
import thinkplot

nums = [random.random() for _ in range(1000)]

my_pmf = thinkstats2.Pmf(nums)
thinkplot.Pmf(my_pmf, linewidth=0.1)
thinkplot.Show()

my_cdf = thinkstats2.Cdf(nums)
thinkplot.Cdf(my_cdf)
thinkplot.Show()
```

###Q4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (normal distribution of blue men)
This is a classic example of hypothesis testing using the normal distribution.  The effect size used here is the Z-statistic. 

As a bonus (optional) step, write out the null hypothesis, alternative hypothesis, critical value for testing, and the associated p-value.  You will see p-values in virtually every algorithm output during the bootcamp.  And from this exercise, you will know how the p-value has been computed and its relationship to a distribution.

```python
import thinkstats2
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)

# subtract the cdf of the bottom of the range from the cdf of the top to get the % in the acceptable range
bottom = dist.cdf(177.8)    # 5'10"
top = dist.cdf(185.4)   # 6'1"
print(int()(top - bottom)*100), '% of US males are in the Blue Man Group eligible range')
```

###Q5. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (correlation of weight vs. age)
In this exercise, you will compute the effect size of correlation.  Correlation measures the relationship of two variables, and data science is about exploring relationships in data.    

>>  The correlation between these two variables is weak.  It is difficult to ascertain a relationship from the scatterplot, and there are many outliers.   The percentiles suggest a relationship between ages 15 to 25, but after that it weakens and varies.  The low (near zero) correlation coefficients suggest a weak relationship as well.  Pearson's is lower than Spearman's which can be effected by the numerous amount of outliers.

```python
import numpy as np
import nsfg
import first
import thinkplot
import thinkstats2
import scatter

preg = nsfg.ReadFemPreg()
live = preg.dropna(subset=['agepreg', 'totalwgt_lb'])
ages = live.agepreg
weights = live.totalwgt_lb

print("Pearson's correlation:", thinkstats2.Corr(ages, weights))
print("Spearman's correlation:", thinkstats2.SpearmanCorr(ages, weights))

thinkplot.Scatter(ages, weights, alpha=2.0)
thinkplot.Show(xlabel='age (years)', ylabel='weight (lbs)',
                 xlim=[10, 50],
                 ylim=[0, 15],
                 legend=False)

bins = np.arange(16, 42, 4)
indices = np.digitize(preg.agepreg, bins)
groups = preg.groupby(indices)

ages = [group.agepreg.mean() for i, group in groups]
cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

thinkplot.PrePlot(3)
for percent in [75, 50, 25]:
    weights = [cdf.Percentile(percent) for cdf in cdfs]
    label = '%dth' % percent
    thinkplot.Plot(ages, weights, label=label)
thinkplot.Config(xlabel="mother's age (years)",
                ylabel='birth weight (lbs)')
thinkplot.Show()
```

###Q6. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
In the theoretical world, all data related to an experiment or a scientific problem would be available.  In the real world, some subset of that data is available.  This exercise asks you to take samples from an exponential distribution and examine how the standard error and confidence intervals vary with the sample size.

>> As the sample size increases, the RMSE approachs O, and the confidence interval decreases, meaning L is an unbiased estimator of lambda.

```python
import thinkstats2
import thinkplot
import math
import random
import numpy as np
from scipy import stats
from estimation import RMSE, MeanError

thinkstats2.RandomSeed(10)

lam=2
n=10
m=1000

while n <= 1000:
    means = []
    for i in range(m):
            xs = np.random.exponential(1.0/lam, n)
            L = 1.0 / np.mean(xs)
            means.append(L)
    cdf = thinkstats2.Cdf(means)
    ci5 = cdf.Percentile(5)
    ci95 = cdf.Percentile(95)
    print(n,  'RMSE:', RMSE(means, lam), 'confidence interval:', ci5, 'to', ci95)

    thinkplot.Plot([ci5, ci5], [0, 1], color='0.8', linewidth=3)
    thinkplot.Plot([ci95, ci95], [0, 1], color='0.8', linewidth=3)
    thinkplot.Cdf(cdf)
    thinkplot.Config(xlabel='estimate',
                    ylabel='CDF',
                    title='Sampling distribution')
    thinkplot.Show()
    n = n * 10
```

###Q7. Bayesian (Elvis Presley twin) 

Bayes' Theorem is an important tool in understanding what we really know, given evidence of other information we have, in a quantitative way.  It helps incorporate conditional probabilities into our conclusions.

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin? Assume we observe the following probabilities in the population: fraternal twin is 1/125 and identical twin is 1/300.  

>> 
P(I) = 1/300  
P(F) = 1/125  
P(I|TB) = P(I)P(TB|I)/P(TB)
P(TB|I) = 1/2 (probability of twin boys given they are identical)  
P(TB|F) = 1/4 (probability of twin boys given they are fraternal; BB | BG | GB | GG)  
P(TB) = P(TB|I)P(I) + P(TB|F)P(F)  
P(I|TB) = (1/300 * 1/2)/(1/2 * 1/300 + 1/4 * 1/125) = 5/11  

---

###Q8. Bayesian &amp; Frequentist Comparison  
How do frequentist and Bayesian statistics compare?

>> Frequentist statistics focuses on the probability of the data, given the hypothesis, i.e. P(D|H).  Whereas, Bayesian statistics focuses on the probability of the hypothesis, given the data, i.e. P(H|D).

---

###Optional Exercises

The following exercises are optional, but we highly encourage you to complete them if you have the time.

###Q9. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (skewness of household income)
###Q10. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
###Q11. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)

## More Resources

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.







