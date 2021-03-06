import obj_functions.machine_learning_utils as ml_utils
from obj_functions import models, datasets


def evaluating_model(model, hp_dict, train_data, test_data, cuda_id, save_path):
    print(hp_dict)
    loss_min, acc_max = ml_utils.start_train(model, train_data, test_data, cuda_id, save_path)
    return {"error": 1. - acc_max, "cross_entropy": loss_min}


def rf_safedriver(experimental_settings):
    train_dataset = datasets.get_safedriver(experimental_settings)

    def _imp(hp_dict, cuda_id, save_path):
        score = models.sd_randomforest.evaluate_safedriver(hp_dict, train_dataset)
        return score

    return _imp


def lgbm_toxic(experimental_settings):
    train_dataset = datasets.get_toxic(experimental_settings)

    def _imp(hp_dict, cuda_id, save_path):
        scores = models.toxic_lgbm.evaluate_toxic(hp_dict, train_dataset)
        return scores

    return _imp


def old_mlp(experimental_settings):
    train_dataset, test_dataset = datasets.get_dataset(experimental_settings)
    image_size = experimental_settings.image_size

    def _imp(hp_dict, cuda_id, save_path):
        model = models.OldMultiLayerPerceptron(**hp_dict, n_cls=experimental_settings.n_cls, image_size=image_size)
        train_data, test_data = datasets.get_data(train_dataset, test_dataset, batch_size=model.batch_size)
        return evaluating_model(model, hp_dict, train_data, test_data, cuda_id, save_path)

    return _imp


def mlp(experimental_settings):
    train_dataset, test_dataset = datasets.get_dataset(experimental_settings)
    image_size = experimental_settings.image_size

    def _imp(hp_dict, cuda_id, save_path):
        model = models.MultiLayerPerceptron(**hp_dict, n_cls=experimental_settings.n_cls, image_size=image_size)
        train_data, test_data = datasets.get_data(train_dataset, test_dataset, batch_size=model.batch_size)
        return evaluating_model(model, hp_dict, train_data, test_data, cuda_id, save_path)

    return _imp


def cnn(experimental_settings):
    train_dataset, test_dataset = datasets.get_dataset(experimental_settings)

    def _imp(hp_dict, cuda_id, save_path):
        model = models.CNN(**hp_dict, n_cls=experimental_settings.n_cls)
        train_data, test_data = datasets.get_data(train_dataset, test_dataset, batch_size=model.batch_size)
        return evaluating_model(model, hp_dict, train_data, test_data, cuda_id, save_path)

    return _imp


def wrn(experimental_settings):
    train_dataset, test_dataset = datasets.get_dataset(experimental_settings)

    def _imp(hp_dict, cuda_id, save_path):
        model = models.WideResNet(**hp_dict, n_cls=experimental_settings.n_cls)
        train_data, test_data = datasets.get_data(train_dataset, test_dataset, batch_size=model.batch_size)
        return evaluating_model(model, hp_dict, train_data, test_data, cuda_id, save_path)

    return _imp


def dnbc(experimental_settings):
    train_dataset, test_dataset = datasets.get_dataset(experimental_settings)

    def _imp(hp_dict, cuda_id, save_path):
        model = models.DenseNetBC(**hp_dict, n_cls=experimental_settings.n_cls)
        train_data, test_data = datasets.get_data(train_dataset, test_dataset, batch_size=model.batch_size)
        return evaluating_model(model, hp_dict, train_data, test_data, cuda_id, save_path)

    return _imp
