from sklearn.metrics import classification_report

y_true_demo = [0, 0, 0, 0, 1, 1, 1, 2, 2, 2]

y_pred_demo = [0, 0, 0, 0, 1, 1, 0, 2, 1, 1]

print(
    classification_report(
        y_true_demo,
        y_pred_demo,
        target_names=["A类", "B类", "C类"]
    )
)


