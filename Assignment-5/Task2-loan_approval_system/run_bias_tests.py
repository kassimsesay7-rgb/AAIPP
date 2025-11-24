"""
Main script to run bias tests and generate comprehensive report
"""

import json
from bias_testing import BiasTester
from bias_analysis import BiasMitigationAnalyzer


def main():
    """Run complete bias testing pipeline"""
    print("=" * 80)
    print("LOAN APPROVAL SYSTEM - BIAS TESTING")
    print("=" * 80)
    print()
    
    # Initialize components
    tester = BiasTester()
    analyzer = BiasMitigationAnalyzer()
    
    # Define base financial criteria (same for all tests)
    base_financials = {
        "age": 32,
        "credit_score": 680,
        "annual_income": 62000,
        "loan_amount": 15000,
        "dti_ratio": 0.28,
        "employment_years": 3,
        "delinquencies": 0,
        "credit_history_years": 5
    }
    
    print("Step 1: Generating test prompts with different names/genders...")
    test_prompts = tester.generate_test_prompts(base_financials)
    print(f"   Generated {len(test_prompts)} test cases")
    print()
    
    print("Step 2: Running bias tests...")
    results = tester.run_bias_test(test_prompts)
    print(f"   Completed {len(results)} tests")
    print()
    
    print("Step 3: Analyzing results for bias...")
    analysis = tester.analyze_bias(results, base_financials)
    print("   Analysis complete")
    print()
    
    print("Step 4: Generating bias test report...")
    bias_report = tester.generate_report(analysis)
    print(bias_report)
    print()
    
    print("Step 5: Saving test results...")
    tester.save_results(analysis, "bias_test_results.json")
    print()
    
    print("Step 6: Generating mitigation strategies report...")
    mitigation_report = analyzer.generate_mitigation_report(
        analysis.bias_detected,
        analysis.bias_details
    )
    print(mitigation_report)
    print()
    
    print("Step 7: Saving mitigation report...")
    analyzer.save_mitigation_report(mitigation_report, "bias_mitigation_report.txt")
    print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Bias Detected: {'YES [!]' if analysis.bias_detected else 'NO [OK]'}")
    print(f"Decisions Consistent: {'Yes' if analysis.decisions_consistent else 'No'}")
    print(f"Risk Scores Vary: {'Yes' if analysis.risk_scores_vary else 'No'}")
    if analysis.risk_scores_vary:
        print(f"Max Score Difference: {analysis.max_score_diff:.2f} points")
    print()
    print("Files Generated:")
    print("  - bias_test_results.json (Detailed test results)")
    print("  - bias_mitigation_report.txt (Mitigation strategies)")
    print()
    print("=" * 80)
    
    return analysis


if __name__ == "__main__":
    main()

