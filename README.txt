In what follows we provide a description of the synthetic instances from

Leitner, M., Lodi, A., Roberti, R., & Sole, C. (2021). An Exact Method for (Constrained) Assortment Optimization Problems with Product Costs. arXiv preprint arXiv:2109.03357. 

Instances are in json format.

The universe of products consists of 10 alternatives. Specifically, 9 products and a no-purchase option, denoted by index 0, which is assumed to be always present.

# Instance Classification
The instances have been partitioned based on 
	- whether the ground model belongs to RUM (RUM folder) or not (irrat folder)
	- ground model (Halo-MNL or GSP)
	- number of customer segments

irrational Halo-MNL instances have been further partitioned into 
	- Asymm/Symm (Halo-MNL instnaces)

irrational GSP instances have been further partitioned based on the maximum irrationality level of the generalized stochastic preferences in the ground model (i.e., 2, 6 or 10)

# Name Format
the instance name contains the following informations:
	<number of unique training assortments>_<number of training transactions>_<percentage of irrationality>_<seed>.json

for example, instance 30_50000_10_1.json stands for
	- 30 unique assortments
	- 50000 training transactions
	- 10% of irrational behaviors (resp. pairwise interactions) for GSP (resp. Halo-MNL) instances 
	- seed 1

# Instance format
Each instance contains contains the following informations:

# --- Part 1: ground model
Here we save the model generating the data, which one may use to compute the ground-truth chocie probabilities for a given assortment. 
	For Halo-MNL model, this part contains the following:
		- 



