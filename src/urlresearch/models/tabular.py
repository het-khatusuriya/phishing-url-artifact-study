"""Tabular model factories with train-only preprocessing.

Each factory returns an sklearn Pipeline whose preprocessing is fitted inside
`fit`, so cross-validation and grouped splits remain leakage-free.
"""
from __future__ import annotations

from typing import List, Optional, Sequence

import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, StackingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from xgboost import XGBClassifier


def make_preprocessor(numeric: Sequence[str], categorical: Sequence[str], scale: bool,
                      min_frequency: int = 20) -> ColumnTransformer:
    transformers = []
    if numeric:
        transformers.append(("num", StandardScaler() if scale else "passthrough", list(numeric)))
    if categorical:
        transformers.append(("cat", OneHotEncoder(handle_unknown="infrequent_if_exist",
                                                  min_frequency=min_frequency, sparse_output=False),
                             list(categorical)))
    return ColumnTransformer(transformers, remainder="drop", verbose_feature_names_out=False)


def logistic_regression(numeric, categorical=(), seed=42, C=1.0) -> Pipeline:
    return Pipeline([
        ("prep", make_preprocessor(numeric, categorical, scale=True)),
        ("model", LogisticRegression(max_iter=2000, C=C, class_weight="balanced", random_state=seed)),
    ])


def random_forest(numeric, categorical=(), seed=42, n_estimators=200, n_jobs=-1) -> Pipeline:
    return Pipeline([
        ("prep", make_preprocessor(numeric, categorical, scale=False)),
        ("model", RandomForestClassifier(n_estimators=n_estimators, class_weight="balanced",
                                         random_state=seed, n_jobs=n_jobs)),
    ])


def xgboost(numeric, categorical=(), seed=42, n_estimators=200, max_depth=6, learning_rate=0.1,
            n_jobs=-1) -> Pipeline:
    return Pipeline([
        ("prep", make_preprocessor(numeric, categorical, scale=False)),
        ("model", XGBClassifier(n_estimators=n_estimators, max_depth=max_depth,
                                learning_rate=learning_rate, subsample=0.8, colsample_bytree=0.8,
                                objective="binary:logistic", eval_metric="logloss",
                                random_state=seed, n_jobs=n_jobs, tree_method="hist")),
    ])


def lightgbm(numeric, categorical=(), seed=42, n_estimators=400, num_leaves=63, learning_rate=0.05,
             n_jobs=-1) -> Pipeline:
    from lightgbm import LGBMClassifier
    return Pipeline([
        ("prep", make_preprocessor(numeric, categorical, scale=False)),
        ("model", LGBMClassifier(n_estimators=n_estimators, num_leaves=num_leaves,
                                 learning_rate=learning_rate, subsample=0.8, subsample_freq=1,
                                 colsample_bytree=0.8, random_state=seed, n_jobs=n_jobs, verbose=-1)),
    ])


def soft_voting(numeric, categorical=(), seed=42, weights=(1, 2, 2)) -> VotingClassifier:
    """The original repository's hybrid: LR:RF:XGB soft vote with weights 1:2:2."""
    return VotingClassifier(
        estimators=[("lr", logistic_regression(numeric, categorical, seed)),
                    ("rf", random_forest(numeric, categorical, seed)),
                    ("xgb", xgboost(numeric, categorical, seed))],
        voting="soft", weights=list(weights), n_jobs=1)


def stacking(numeric, categorical=(), seed=42) -> StackingClassifier:
    return StackingClassifier(
        estimators=[("lr", logistic_regression(numeric, categorical, seed)),
                    ("rf", random_forest(numeric, categorical, seed)),
                    ("xgb", xgboost(numeric, categorical, seed))],
        final_estimator=LogisticRegression(max_iter=1000),
        stack_method="predict_proba", cv=5, n_jobs=1, passthrough=False)


MODEL_FACTORIES = {
    "lr": logistic_regression,
    "rf": random_forest,
    "xgb": xgboost,
    "lgbm": lightgbm,
    "softvote": soft_voting,
    "stack": stacking,
}
