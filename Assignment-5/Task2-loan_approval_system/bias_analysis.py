"""
Bias Analysis and Mitigation Strategies
Provides detailed analysis and mitigation ideas for identified bias.
"""

from typing import List, Dict
from dataclasses import dataclass
import json


@dataclass
class MitigationStrategy:
    """A mitigation strategy for addressing bias"""
    category: str
    strategy: str
    description: str
    implementation: str
    priority: str  # "High", "Medium", "Low"


class BiasMitigationAnalyzer:
    """Analyzes bias and provides mitigation strategies"""
    
    def __init__(self):
        self.mitigation_strategies = self._load_mitigation_strategies()
    
    def _load_mitigation_strategies(self) -> List[MitigationStrategy]:
        """Load predefined mitigation strategies"""
        strategies = [
            MitigationStrategy(
                category="Policy & Prompting",
                strategy="Explicit Constraint Enforcement",
                description="Add explicit constraints to prevent use of protected attributes",
                implementation="""
1. Add to system prompt: "Do not use or request protected attributes (gender, race, 
   ethnicity, religion, disability, sexual orientation, age where legally protected). 
   If present, ignore them. Use only financial risk factors explicitly listed."

2. Implement input validation to reject requests that require protected attributes.

3. Add refusal mechanism: "If asked to consider protected attributes, respond that 
   it's not allowed and proceed without them."
                """,
                priority="High"
            ),
            MitigationStrategy(
                category="Data & Modeling",
                strategy="Feature Engineering",
                description="Remove protected attributes and known proxies from features",
                implementation="""
1. Audit feature list and remove:
   - Direct protected attributes (gender, race, ethnicity)
   - Proxy variables (ZIP code, name-derived features, certain occupations)
   - Any feature that correlates >0.7 with protected attributes

2. Implement feature validation in preprocessing pipeline.

3. Use counterfactual data augmentation: duplicate records with swapped 
   names/pronouns and enforce invariant outputs.
                """,
                priority="High"
            ),
            MitigationStrategy(
                category="Data & Modeling",
                strategy="Fairness-Aware Training",
                description="Apply fairness constraints during model training",
                implementation="""
1. Use fairness-aware algorithms:
   - Equalized Odds: Ensure equal true positive and false positive rates
   - Demographic Parity: Ensure equal approval rates
   - Calibrated Equalized Odds: Balance fairness and accuracy

2. Apply post-processing techniques:
   - Threshold optimization per group
   - Score calibration within groups

3. Monitor group-wise metrics during training.
                """,
                priority="Medium"
            ),
            MitigationStrategy(
                category="Evaluation & Monitoring",
                strategy="Counterfactual Testing",
                description="Implement automated bias testing in CI/CD pipeline",
                implementation="""
1. Create test suite with counterfactual examples:
   - Same financials, different names/genders
   - Same financials, different protected attributes
   
2. Set up automated tests that fail if:
   - Decisions differ for identical financials
   - Risk scores vary by >0.01 for identical cases
   - Protected attributes influence outcomes

3. Run tests on every code change and model update.
                """,
                priority="High"
            ),
            MitigationStrategy(
                category="Evaluation & Monitoring",
                strategy="Bias Dashboard",
                description="Create monitoring dashboard for ongoing bias detection",
                implementation="""
1. Track group-wise metrics:
   - Approval rates by gender, race, ethnicity
   - Average risk scores by group
   - False positive/negative rates by group
   - Calibration error by group

2. Set up alerts for:
   - Disparate impact (>80% rule violations)
   - Statistical significance tests (p < 0.05)
   - Score distribution differences

3. Schedule regular bias audits (weekly/monthly).
                """,
                priority="Medium"
            ),
            MitigationStrategy(
                category="Implementation Controls",
                strategy="Input Schema Validation",
                description="Enforce strict input schemas to prevent protected attribute usage",
                implementation="""
1. Define whitelist of allowed inputs:
   - credit_score, income, dti, loan_amount
   - employment_length, delinquencies, credit_history
   
2. Reject any input containing protected attributes.

3. Implement preprocessing to redact protected terms from user text.

4. Log all inputs for audit purposes.
                """,
                priority="High"
            ),
            MitigationStrategy(
                category="Implementation Controls",
                strategy="Standardized Rationales",
                description="Generate standardized decision rationales using only allowed features",
                implementation="""
1. Create template for decision rationales that only references:
   - Approved financial factors
   - Specific thresholds and values
   
2. Prohibit free-form text generation that might reference demographics.

3. Add validation to ensure rationales don't contain protected attribute references.

4. Use feature attribution (SHAP values) to explain decisions.
                """,
                priority="Medium"
            ),
            MitigationStrategy(
                category="Governance",
                strategy="Model Cards & Documentation",
                description="Maintain comprehensive documentation of model behavior",
                implementation="""
1. Create model cards documenting:
   - Training data demographics
   - Performance metrics by group
   - Known limitations and biases
   - Intended use cases
   
2. Maintain decision policies that explain:
   - Which features are used
   - Why protected attributes are excluded
   - How fairness is measured
   
3. Keep audit logs for regulatory review.

4. Regular legal review of fairness measures.
                """,
                priority="Medium"
            ),
            MitigationStrategy(
                category="Governance",
                strategy="Appeals Process",
                description="Implement appeals mechanism for rejected applications",
                implementation="""
1. Create transparent appeals process where applicants can:
   - Request explanation of decision
   - Challenge decision if they believe bias occurred
   - Provide additional context (within allowed features)
   
2. Human review for appeals flagged for potential bias.

3. Track appeals by demographic group to identify patterns.

4. Use appeals data to improve system.
                """,
                priority="Low"
            ),
        ]
        
        return strategies
    
    def generate_mitigation_report(self, bias_detected: bool, bias_details: List[str]) -> str:
        """
        Generate a comprehensive mitigation report based on detected bias.
        
        Args:
            bias_detected: Whether bias was detected
            bias_details: List of bias details
            
        Returns:
            Formatted mitigation report
        """
        report = []
        report.append("=" * 80)
        report.append("BIAS MITIGATION STRATEGIES REPORT")
        report.append("=" * 80)
        report.append("")
        
        if bias_detected:
            report.append("[!] BIAS DETECTED - Mitigation Required")
            report.append("")
            report.append("Detected Issues:")
            for detail in bias_details:
                report.append(f"  - {detail}")
            report.append("")
        else:
            report.append("[OK] No bias detected in current tests.")
            report.append("")
            report.append("However, it's recommended to implement preventive measures")
            report.append("to ensure bias doesn't emerge in the future.")
            report.append("")
        
        report.append("=" * 80)
        report.append("RECOMMENDED MITIGATION STRATEGIES")
        report.append("=" * 80)
        report.append("")
        
        # Group strategies by category
        by_category = {}
        for strategy in self.mitigation_strategies:
            if strategy.category not in by_category:
                by_category[strategy.category] = []
            by_category[strategy.category].append(strategy)
        
        # Sort categories by priority (High priority strategies first)
        priority_order = {"High": 0, "Medium": 1, "Low": 2}
        
        for category in sorted(by_category.keys()):
            report.append(f"\n{category}:")
            report.append("-" * 80)
            
            strategies = sorted(
                by_category[category],
                key=lambda s: (priority_order.get(s.priority, 3), s.strategy)
            )
            
            for strategy in strategies:
                priority_indicator = "[HIGH]" if strategy.priority == "High" else "[MED]" if strategy.priority == "Medium" else "[LOW]"
                report.append(f"\n{priority_indicator} {strategy.strategy} ({strategy.priority} Priority)")
                report.append(f"   Description: {strategy.description}")
                report.append(f"   Implementation:")
                for line in strategy.implementation.strip().split('\n'):
                    report.append(f"   {line}")
                report.append("")
        
        report.append("=" * 80)
        report.append("IMPLEMENTATION CHECKLIST")
        report.append("=" * 80)
        report.append("")
        
        high_priority = [s for s in self.mitigation_strategies if s.priority == "High"]
        report.append("High Priority (Implement First):")
        for i, strategy in enumerate(high_priority, 1):
            report.append(f"  {i}. [{strategy.category}] {strategy.strategy}")
        
        report.append("")
        report.append("Medium Priority (Implement Next):")
        medium_priority = [s for s in self.mitigation_strategies if s.priority == "Medium"]
        for i, strategy in enumerate(medium_priority, 1):
            report.append(f"  {i}. [{strategy.category}] {strategy.strategy}")
        
        report.append("")
        report.append("Low Priority (Consider for Future):")
        low_priority = [s for s in self.mitigation_strategies if s.priority == "Low"]
        for i, strategy in enumerate(low_priority, 1):
            report.append(f"  {i}. [{strategy.category}] {strategy.strategy}")
        
        report.append("")
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def save_mitigation_report(self, report: str, filename: str = "bias_mitigation_report.txt"):
        """Save mitigation report to file"""
        with open(filename, 'w') as f:
            f.write(report)
        print(f"Mitigation report saved to {filename}")


def main():
    """Generate mitigation report"""
    analyzer = BiasMitigationAnalyzer()
    
    # Example: Assume bias was detected (in real use, this comes from test results)
    bias_detected = True
    bias_details = [
        "Different decisions made for identical financials based on name/gender",
        "Risk scores vary by up to 5.2 points for identical cases"
    ]
    
    report = analyzer.generate_mitigation_report(bias_detected, bias_details)
    print(report)
    
    analyzer.save_mitigation_report(report)


if __name__ == "__main__":
    main()

