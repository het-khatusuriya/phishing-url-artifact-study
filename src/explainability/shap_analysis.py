import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import joblib
import warnings
warnings.filterwarnings('ignore')

class SHAPAnalyzer:
    """SHAP explainability analysis for the ensemble model."""
    
    def __init__(self, model_path, validation_data_path, results_path):
        """
        Initialize SHAP analyzer.
        
        Args:
            model_path: Path to trained ensemble model (.joblib)
            validation_data_path: Path to validation data folder
            results_path: Path to save SHAP results
        """
        self.model = joblib.load(model_path)
        self.validation_data_path = Path(validation_data_path)
        self.results_path = Path(results_path)
        self.results_path.mkdir(parents=True, exist_ok=True)
        
        # Load validation data
        self.X_val = pd.read_csv(self.validation_data_path / "X_validation.csv")
        self.y_val = pd.read_csv(self.validation_data_path / "y_validation.csv")
        self.y_val = self.y_val.iloc[:, 0]  # Convert to series
        
        self.feature_names = self.X_val.columns.tolist()
        
    def generate_shap_values(self, sample_size=None):
        """
        Generate SHAP values for validation set using KernelExplainer.
        
        Args:
            sample_size: Number of samples to explain (default 1000)
        """
        print("Generating SHAP values using KernelExplainer...")
        
        if sample_size is None:
            sample_size = 1000
        
        # Take background and explain samples
        background_sample = self.X_val.iloc[:100].copy()  # Background for explainer
        explain_sample = self.X_val.iloc[:sample_size].copy()  # Samples to explain
        
        # Create KernelExplainer (works with any model)
        explainer = shap.KernelExplainer(
            model=self.model.predict_proba,
            data=background_sample,
            feature_names=self.feature_names
        )
        
        self.shap_values = explainer.shap_values(explain_sample)
        self.X_explain = explain_sample
        self.explainer = explainer
        
        print(f"SHAP values generated for {len(explain_sample)} samples")
        return self.shap_values
    
    def plot_shap_summary(self):
        """
        Create SHAP summary plot showing global feature importance.
        """
        print("Creating SHAP summary plot...")
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # For probability output from VotingClassifier, use malicious class (index 1)
        shap_values_malicious = self.shap_values[1] if isinstance(self.shap_values, list) else self.shap_values
        shap_importance = np.abs(shap_values_malicious).mean(axis=0)
        
        indices = np.argsort(shap_importance)[::-1][:20]  # Top 20
        
        plt.barh(range(len(indices)), shap_importance[indices])
        plt.yticks(range(len(indices)), [self.feature_names[i] for i in indices])
        plt.xlabel("Mean |SHAP value|")
        plt.title("SHAP Global Feature Importance (Top 20)")
        
        plt.tight_layout()
        plt.savefig(self.results_path / "shap_summary_plot.png", dpi=300, bbox_inches='tight')
        print(f" Saved: shap_summary_plot.png")
        plt.close()
    
    def feature_importance_summary(self):
        """
        Generate summary statistics of feature importance.
        """
        print("Generating feature importance summary...")
        
        shap_values_malicious = self.shap_values[1] if isinstance(self.shap_values, list) else self.shap_values
        shap_importance = np.abs(shap_values_malicious).mean(axis=0)
        
        importance_df = pd.DataFrame({
            'Feature': self.feature_names,
            'Mean_Absolute_SHAP': shap_importance,
            'Std_SHAP': np.abs(shap_values_malicious).std(axis=0)
        }).sort_values('Mean_Absolute_SHAP', ascending=False)
        
        importance_df.to_csv(self.results_path / "feature_importance_shap.csv", index=False)
        print(f"✅ Saved: feature_importance_shap.csv\n")
        
        return importance_df
    
    def generate_all_analysis(self):
        """Run complete SHAP analysis."""
        print("\n" + "="*60)
        print("SHAP EXPLAINABILITY ANALYSIS")
        print("="*60 + "\n")
        
        # Generate SHAP values
        self.generate_shap_values(sample_size=1000)
        
        # Summary plot
        self.plot_shap_summary()
        
        # Feature importance summary
        importance_df = self.feature_importance_summary()
        print(importance_df.head(15))
        
        print("\n" + "="*60)
        print("SHAP ANALYSIS COMPLETE")
        print("Results saved to: results/shap/")
        print("="*60)