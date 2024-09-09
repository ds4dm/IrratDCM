In what follows we provide a description of the synthetic instances from

Jena, S. D., Lodi, A., & Sole, C. (2021). *"On the estimation of discrete choice models to capture irrational customer behaviors."* arXiv preprint arXiv:2109.03882. 

Instances are in the `json` format.

The universe of products consists of 10 alternatives. Specifically, 9 products and a no-purchase option, denoted by index 0, which is assumed to be always present in the assortment.

## Instances Classification
The instances have been partitioned based on 
* whether the ground model belongs to RUM (RUM folder) or not (irrat folder)
* ground model (Halo-MNL or GSP)
* number of customer segments

irrational Halo-MNL instances have been further partitioned based on the type of interaction, i.e., Symmetric (Symm folder) or Asymmetric (Asymm folder)

irrational GSP instances have been further partitioned based on the maximum irrationality level of the generalized stochastic preferences in the ground model (i.e., 2, 6 or 10)

## Name Format
the instance name contains the following informations:
	<number of unique training assortments>_<number of training transactions>_<percentage of irrationality>_<id>.json

for example, instance 30_50000_10_1.json stands for
	- 30 unique assortments
	- 50000 training transactions
	- 10% of irrational behaviors (resp. pairwise interactions) for GSP (resp. Halo-MNL) instances 
	- the instance id is 1

## Instance format
We tried to keep the instance format as close as possible to that from [1]. Each instance contains contains the following informations:

### --- Part 1: ground model
This part contains the details of the data-generating model, which one may use to compute the ground-truth chocie probabilities for a given assortment. 
* For Halo-MNL instances, this part contains the following:
	* `lambdas`: vector of probabilities for each customer type
	* `utilities`: this is the $n \times n$ pairwise interaction matrix $U$, such that $u_{i,j}$ denotes the impact of the absence of  product $i$ on the perceived utility of product $i$
* For GSP instances, this part contains te following:
	* `lambdas`: vector of probabilities for each customer type
	* `ranked_lists`: preference sequences of each customer type
	* `irrat_levels`: vector of *irrationality levels* for each customer type. Ranks are defined between 1 and N, where an irrationality level of 1 correponds to a rational customer type, always choosing is favourite option.


To facilitate the **reading of GSP instances** we added a `check_instance.py` file to the repo that shows how to load `ranked_lists`, `lambdas` and `irrat_levels` and runs some basic check to make sure the considered these fields are read correctly.


	
### --- Part 2: Training Transactions
This part lists the transactions that have been used for training the various approaches. Each transaction correponds of a list `[assortment, chosen item]`. For example, the transaction `[[0,2,4,5], 4]` stands for *"Product 3 has been bought, when products 2,4,5 and 0 ( the no-purchase option) where available"*

[1] Berbeglia, G., Garassino, A., & Vulcano, G. (2018). *"A comparative empirical study of discrete choice models in retail operations.*" Available at SSRN 3136816.
