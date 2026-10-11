from sklearn.ensemble import VotingClassifier


def create_weighted_soft_voting_ensemble(
    logistic_model,
    random_forest_model,
    xgboost_model,
    weights=(1, 2, 2)
):
    return VotingClassifier(
        estimators=[
            ("logistic_regression", logistic_model),
            ("random_forest", random_forest_model),
            ("xgboost", xgboost_model)
        ],
        voting="soft",
        weights=list(weights),
        n_jobs=-1
    )