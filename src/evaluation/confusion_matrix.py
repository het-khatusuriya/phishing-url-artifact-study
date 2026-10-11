from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix


def save_confusion_matrix(
    y_true,
    y_pred,
    model_name,
    output_folder
):
    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    matrix = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        matrix,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Legitimate", "Phishing"],
        yticklabels=["Legitimate", "Phishing"]
    )

    plt.xlabel("Predicted label")
    plt.ylabel("True label")
    plt.title(f"Confusion Matrix — {model_name}")
    plt.tight_layout()

    safe_name = model_name.lower().replace(" ", "_")
    output_path = output_folder / f"{safe_name}_confusion_matrix.png"

    plt.savefig(output_path, dpi=300)
    plt.close()

    return output_path