from sklearn.model_selection import train_test_split


def create_data_splits(
    dataframe,
    feature_columns,
    target_column="label",
    test_size=0.20,
    validation_size=0.20,
    random_state=42
):
    X = dataframe[feature_columns].copy()
    y = dataframe[target_column].map({
        "legitimate": 0,
        "phishing": 1
    })

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )

    validation_relative_size = validation_size / (1 - test_size)

    X_train, X_validation, y_train, y_validation = train_test_split(
        X_train_val,
        y_train_val,
        test_size=validation_relative_size,
        stratify=y_train_val,
        random_state=random_state
    )

    return (
        X_train,
        X_validation,
        X_test,
        y_train,
        y_validation,
        y_test
    )