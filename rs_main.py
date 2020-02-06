import utils
import optimizer


if __name__ == '__main__':
    opt_requirements, experimental_settings = utils.parse_requirements()
    hp_utils = utils.HyperparameterUtilities(experimental_settings)
    opt = optimizer.RandomSearch(hp_utils, opt_requirements, experimental_settings, given_default=a)
    best_conf, best_performance = opt.optimize()
