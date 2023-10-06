# How much can you earn on bank cashback?

Different banks have different loyalty programs for their customers. Otkritie Bank is one of the worthy, in my opinion, Russian banks that have good service and infrastructure processes for private clients. One of these loyalty programs is 3% on all purchases in the form of "bonuses", which can be used to reimburse existing expenses (1 bonus = 1 ruble).

Let's try to minimize our losses from the selection of the amount, using mathematics and programming so as to maximize cashback. As a result, to see how the compiled algorithm will work and how much we will be able to save, I use unbiased mathematics.

## Bonus Redemption Formula

Mathematically speaking, we have some amount of "bonuses" S, which we can cash out by choosing expenses x, which are more than 1500 rubles and in total do not exceed S:

formula 1

Then, if we want to get the maximum benefit from our cashbacks, we must collect such a maximum amount from the proposed number of expenses, so that it is maximum:

formula 2

## Implementation

Despite the seemingly complex mathematical formula, let's simplify the algorithmic approach by using the algorithm of a complete search of combinations.

Although we have quite a lot of combinations of sorting options, we will not run into a very large time limit. Therefore, this algorithm is even better suited to a Greedy strategy.

Without going into details, we will create an algorithm in the Python programming language that accepts all the necessary constants as input, starts a full search of options and compares each new option with a minimum deviation from the amount already found. The code is in the file "main.py "

This dynamic approach to minimizing the difference allows the algorithm to find the optimal value we need up to 10 seconds of work (with the number of expenses < 80)

## Testing

To compare the results, I took a real example of my costs and the possibility of reimbursing the amount with cashback. I have the following costs and cashback amount:

bills ang goal 1

For the experiment, I modeled a situation where a buyer selects a suitable amount for him within 10 minutes, based only on my feelings. In order to conduct fairer tests, I reduced the amount of expenses and removed the restrictions of 1500 rubles.

To conduct experiments, I asked my student, having a smart calculator on hand, to find the optimal cashback in the allotted time.

## Results

After conducting the experiment, I entered the results in a table and compared them with what the program gave out in less than a second runtime:

|                     | Student                     | Algoritm                                    |
| --------------------| --------------------------- | ------------------------------------------- |
| Choosing  expenses  | [4735, 540, 234]            | [203.24, 234, 540, 849.8, 1698, 2299]       |
| Choosing  sum       | 5509                        | 5824.04                                     |
| Unused cashback     | 335.04 (~5,73%)             | 20 (~0.34%)                                 |

As part of the experiment, the algorithm showed its effectiveness 16.7 times more than a person! Let's estimate the total possible profit from this algorithm, provided that it will be used for about 10 years.

The average amount of cashback I receive: is ~6920 bonuses per month. Then, within 10 years (10 years * 12 months = 120 months), our difference in cashback usage approaches will be: 44758.66 rubles

## Exploitation

Only the use of the program and rough calculations managed to achieve a difference of 44758.56 rubles over 10 years, while spending up to 2 seconds a year. Evaluating the efforts made (this report was written much longer than the algorithm itself), we can conclude that the program is effective.

I also use a similar optimization strategy in other loyalty programs, in particular, digital equipment stores.


