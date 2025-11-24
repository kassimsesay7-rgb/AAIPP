"""
Example usage of the Loan Approval System
Demonstrates basic functionality and bias testing
"""

from loan_approval_system import LoanApprovalSystem, LoanApplication, LoanDecision


def example_basic_approval():
    """Example of basic loan approval"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Loan Approval")
    print("=" * 60)
    
    system = LoanApprovalSystem()
    
    # Create an application
    application = LoanApplication(
        credit_score=720,
        annual_income=75000,
        loan_amount=20000,
        debt_to_income_ratio=0.25,
        employment_length_years=5,
        delinquencies_24m=0,
        credit_history_years=8
    )
    
    # Evaluate
    decision, rationale, details = system.evaluate_application(application)
    
    print(f"\nApplication Details:")
    print(f"  Credit Score: {application.credit_score}")
    print(f"  Annual Income: ${application.annual_income:,.0f}")
    print(f"  Loan Amount: ${application.loan_amount:,.0f}")
    print(f"  DTI Ratio: {application.debt_to_income_ratio:.0%}")
    print(f"  Employment: {application.employment_length_years} years")
    print(f"  Delinquencies: {application.delinquencies_24m}")
    print(f"  Credit History: {application.credit_history_years} years")
    
    print(f"\nDecision: {decision.value}")
    print(f"Risk Score: {details['risk_score']:.2f}/100")
    print(f"Rationale: {rationale}")
    print()


def example_rejected_application():
    """Example of a rejected application"""
    print("=" * 60)
    print("EXAMPLE 2: Rejected Application")
    print("=" * 60)
    
    system = LoanApprovalSystem()
    
    # Create an application that will be rejected
    application = LoanApplication(
        credit_score=600,  # Below minimum
        annual_income=40000,
        loan_amount=15000,
        debt_to_income_ratio=0.45,  # Above maximum
        employment_length_years=0.5,  # Below minimum
        delinquencies_24m=4,  # Above maximum
        credit_history_years=1  # Below minimum
    )
    
    # Evaluate
    decision, rationale, details = system.evaluate_application(application)
    
    print(f"\nApplication Details:")
    print(f"  Credit Score: {application.credit_score} (Minimum: 650)")
    print(f"  DTI Ratio: {application.debt_to_income_ratio:.0%} (Maximum: 36%)")
    print(f"  Employment: {application.employment_length_years} years (Minimum: 1)")
    print(f"  Delinquencies: {application.delinquencies_24m} (Maximum: 2)")
    print(f"  Credit History: {application.credit_history_years} years (Minimum: 2)")
    
    print(f"\nDecision: {decision.value}")
    print(f"Rationale: {rationale}")
    print(f"\nFailed Checks:")
    for check, passed in details.items():
        if check != 'risk_score' and not passed:
            print(f"  - {check}: FAILED")
    print()


def example_protected_attributes():
    """Example showing that protected attributes are ignored"""
    print("=" * 60)
    print("EXAMPLE 3: Protected Attributes Ignored")
    print("=" * 60)
    
    system = LoanApprovalSystem()
    
    # Two applications with identical financials but different protected attributes
    app1 = LoanApplication(
        credit_score=680,
        annual_income=62000,
        loan_amount=15000,
        debt_to_income_ratio=0.28,
        employment_length_years=3,
        delinquencies_24m=0,
        credit_history_years=5,
        applicant_name="John",
        gender="male",
        age=32
    )
    
    app2 = LoanApplication(
        credit_score=680,
        annual_income=62000,
        loan_amount=15000,
        debt_to_income_ratio=0.28,
        employment_length_years=3,
        delinquencies_24m=0,
        credit_history_years=5,
        applicant_name="Emily",
        gender="female",
        age=32
    )
    
    # Evaluate both
    decision1, rationale1, details1 = system.evaluate_application(app1)
    decision2, rationale2, details2 = system.evaluate_application(app2)
    
    print(f"\nApplication 1: {app1.applicant_name} ({app1.gender})")
    print(f"  Decision: {decision1.value}")
    print(f"  Risk Score: {details1['risk_score']:.2f}/100")
    
    print(f"\nApplication 2: {app2.applicant_name} ({app2.gender})")
    print(f"  Decision: {decision2.value}")
    print(f"  Risk Score: {details2['risk_score']:.2f}/100")
    
    print(f"\nResults are identical: {decision1 == decision2 and details1['risk_score'] == details2['risk_score']}")
    print("Protected attributes (name, gender) are ignored in decision making.")
    print()


def example_prompt_processing():
    """Example of processing natural language prompts"""
    print("=" * 60)
    print("EXAMPLE 4: Processing Natural Language Prompts")
    print("=" * 60)
    
    system = LoanApprovalSystem()
    
    prompts = [
        "Should we approve a $15,000 loan for John? He has credit score 680, income $62k, DTI 28%",
        "Approve loan for Emily: credit score 680, annual income $62,000, DTI ratio 0.28",
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\nPrompt {i}: {prompt}")
        decision, rationale, details = system.process_prompt(prompt)
        print(f"  Decision: {decision.value}")
        print(f"  Risk Score: {details['risk_score']:.2f}/100")
    print()


if __name__ == "__main__":
    print("\n")
    example_basic_approval()
    example_rejected_application()
    example_protected_attributes()
    example_prompt_processing()
    print("=" * 60)
    print("For bias testing, run: python run_bias_tests.py")
    print("=" * 60)

