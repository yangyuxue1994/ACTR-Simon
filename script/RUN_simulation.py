from simon_device import *
import glob
import itertools

def check_parameters(param):
	log = pd.read_csv("../data/log.csv", usecols=['motivation', 'init_cost', 'update_cost', 'valid_cue_percentage']).convert_dtypes()
	logs = log.values
	for l in logs:
		if all(param == l):
			return True
	return False

def simulate(): 
	
	motivation = np.linspace(0.1, 10, 10).round(2)
	init_cost = np.linspace(0.01, 0.1, 10).round(2)
	update_cost = [True, False]
	valid_cue_percentage = [0, 0.25, 0.5, 0.75, 1]

	param_sets = list(itertools.product(*[motivation, init_cost, update_cost, valid_cue_percentage]))
	for param in param_sets:
		if check_parameters(param):
			print("SKIP", param)
		else:
			run_simulation(n_simulation=1, n_session=7, param_set={"motivation":param[0], "init_cost":param[1],
                                           "update_cost":param[2], "valid_cue_percentage":param[3]})
            
#run_simulation(n_simulation=1, n_session=7, param_set={"init_cost":0.03, "update_cost":True, "valid_cue_percentage":.5, "motivation":1.5}, log=True)
