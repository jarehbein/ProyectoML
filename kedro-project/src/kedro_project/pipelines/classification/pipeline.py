from kedro.pipeline import Pipeline, node
from .nodes import (
    prepare_data,
    train_random_forest,
    train_logistic_regression,
    train_svc,
    evaluate_model,
    combine_evaluations,
    select_best_model
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=prepare_data,
                inputs="cleaned_data",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="prepare_data_node",
            ),
            node(
                func=train_random_forest,
                inputs=["X_train", "y_train"],
                outputs="rf_model",
                name="train_random_forest_node",
            ),
            node(
                func=train_logistic_regression,
                inputs=["X_train", "y_train"],
                outputs="lr_model",
                name="train_logistic_regression_node",
            ),
            node(
                func=train_svc,
                inputs=["X_train", "y_train"],
                outputs="svc_model",
                name="train_svc_node",
            ),
            node(
                func=evaluate_model,
                inputs=dict(
                    model="rf_model", 
                    X_test="X_test", 
                    y_test="y_test", 
                    model_name="'Random Forest'"
                ),
                outputs="rf_evaluation",
                name="evaluate_rf_node",
            ),
            node(
                func=evaluate_model,
                inputs=dict(
                    model="lr_model", 
                    X_test="X_test", 
                    y_test="y_test", 
                    model_name="'Logistic Regression'"
                ),
                outputs="lr_evaluation",
                name="evaluate_lr_node",
            ),
            node(
                func=evaluate_model,
                inputs=dict(
                    model="svc_model", 
                    X_test="X_test", 
                    y_test="y_test", 
                    model_name="'SVC'"
                ),
                outputs="svc_evaluation",
                name="evaluate_svc_node",
            ),
            node(
            func=combine_evaluations,
            inputs=["rf_evaluation", "lr_evaluation", "svc_evaluation"],
            outputs="evaluation_results",
            name="combine_evaluations_node",
            ),
            node(
                func=select_best_model,
            inputs="evaluation_results",  # Cambiamos las entradas
            outputs="best_model",
            name="select_best_model_node",
            ),
        ]
    )
