# Instance checker to reply to Gerardo and Ashwin's email.
def check_instance(instance):
    """
    instance: string path to .json file containing the instance to check. E.g.
    ./IrratDCM/synth_instances/irrat/GSP/10_customers/max_irrat_2/10_3000_10_0.json")
    Make sure to include the full path, with "irrat/" (resp. RUM) folder in the parth, so as to select the right if/else
    condition in lines 17/19.
    """
    content = json.load(open(instance))
    behavior_ar =  np.asarray(content['ground_model']['ranked_lists'])
    lambdas_ar = np.asarray(content['ground_model']['lambdas'])
    irrat_levels = np.asarray(content['ground_model']['irrat_levels'])

     # Number of lambdas = Number of behaviors
    assert lambdas_ar.shape[0] == behavior_ar.shape[1]
     # 10/100 behavuoirs for RUM instances and 11/101 behaviors for Irrat instances
    if "RUM" in instance:
        assert behavior_ar.shape[1] in (10, 100)
    elif "irrat" in instance:
         assert behavior_ar.shape[1] in (11, 101)
    # 10 products for all instances
    assert behavior_ar.shape[0] == 10
    # Each behavior has no duplicates, i.e., the number of unique elements is equal to the number of elements, for each column/behvior of the behaviors matrix
    assert np.all(np.unique(behavior_ar[:,i]).shape[0] == behavior_ar.shape[0] for i in range(behavior_ar.shape[1]))
    # There is a fake behavior, the first one, which is used to ensure a non-zero market share for the no-purchase probability when all products are in the assortment.
    assert behavior_ar[0,0] == 0
    # The first (fake) behavior is always to [0,1,2,3,4,5,6,7,8,9]
    assert np.all(behavior_ar[:, 0] == np.array([0,1,2,3,4,5,6,7,8,9]))
    # The first behavior is always a rational one
    assert irrat_levels[0] == 1