# Loan Approval System with Bias Testing

A comprehensive loan approval system that evaluates loan applications based solely on financial criteria, with built-in bias testing capabilities to identify and mitigate potential discrimination.

## Features

- **Financial-Only Decision Making**: Evaluates loans based on credit score, income, DTI ratio, employment history, and payment history
- **Protected Attribute Handling**: Stores but ignores protected attributes (gender, race, ethnicity, etc.)
- **Bias Testing Framework**: Automated testing with prompt variations using different names/genders
- **Bias Analysis**: Comprehensive analysis of test results to detect bias
- **Mitigation Strategies**: Detailed recommendations for addressing identified bias
- **REST API Option**: Expose the evaluation and bias testing workflow over HTTP via Flask

## Project Structure

```
loan_approval_system/
├── loan_approval_system.py    # Main loan approval logic
├── bias_testing.py            # Bias testing framework
├── bias_analysis.py           # Bias analysis and mitigation strategies
├── app.py                  # Flask API entry point
├── run_bias_tests.py        # Main script to run all tests
├── example_usage.py         # Interactive examples
├── test_cases.json          # Test cases with different names/genders
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── BIAS_TEST_SUMMARY.md     # Summary of bias testing results
```

## Installation

1. **Clone or navigate to the project directory**:
```bash
cd loan_approval_system
```

2. **Install dependencies** (optional, mainly for testing):
```bash
pip install -r requirements.txt
```

## Usage

### Basic Loan Approval

```python
from loan_approval_system import LoanApprovalSystem, LoanApplication

# Create system instance
system = LoanApprovalSystem()

# Create application
application = LoanApplication(
    credit_score=680,
    annual_income=62000,
    loan_amount=15000,
    debt_to_income_ratio=0.28,
    employment_length_years=3,
    delinquencies_24m=0,
    credit_history_years=5
)

# Evaluate application
decision, rationale, details = system.evaluate_application(application)
print(f"Decision: {decision.value}")
print(f"Rationale: {rationale}")
```

### REST API (Flask)

Start the Flask development server:

```bash
python app.py
```

The server listens on `http://localhost:5000` by default and exposes:

- `GET /` — Health check and endpoint overview
- `POST /evaluate` — Evaluate a loan application (JSON body)
- `POST /bias-test` — Run the default bias test suite (optional JSON body to override base financials)

#### Example request body for `/evaluate`

```json
{
  "credit_score": 680,
  "annual_income": 62000,
  "loan_amount": 15000,
  "debt_to_income_ratio": 0.28,
  "employment_length_years": 3,
  "delinquencies_24m": 0,
  "credit_history_years": 5,
  "applicant_name": "John",
  "gender": "male"
}
```

Only the financial fields are required; protected attributes are optional and ignored by the decision logic.

### Running Bias Tests

Run the complete bias testing pipeline:

```bash
python run_bias_tests.py
```

This will:
1. Generate test prompts with different names/genders but identical financials
2. Run tests through the loan approval system
3. Analyze results for bias
4. Generate comprehensive reports

### Individual Components

**Run bias testing only**:
```bash
python bias_testing.py
```

**Generate mitigation strategies**:
```bash
python bias_analysis.py
```

## Bias Testing Methodology

The system tests for bias by:

1. **Creating Counterfactual Tests**: Same financial criteria, different names/genders
   - Names tested: John, Emily, Aisha, Raj, José, Mei, Alex, Taylor
   - Genders tested: male, female, non-binary

2. **Checking Consistency**:
   - All applicants with identical financials should receive identical decisions
   - Risk scores should not vary based on name or gender
   - Rationales should not reference protected attributes

3. **Detecting Bias**:
   - Different decisions for identical financials
   - Varying risk scores for identical cases
   - Gender-based patterns in outcomes

## Expected Output

### Bias Test Report

The system generates a report showing:
- Test results for each applicant
- Decision consistency check
- Risk score variance analysis
- Bias detection status
- Detailed bias findings (if any)

### Mitigation Strategies Report

If bias is detected, the system provides:
- **High Priority** strategies:
  - Explicit constraint enforcement
  - Feature engineering (remove protected attributes)
  - Counterfactual testing in CI/CD

- **Medium Priority** strategies:
  - Fairness-aware training
  - Bias monitoring dashboard
  - Standardized rationales

- **Low Priority** strategies:
  - Appeals process
  - Governance documentation

## System Design

### Decision Criteria

The system evaluates applications based on:
- **Credit Score**: Minimum 650
- **Debt-to-Income Ratio**: Maximum 36%
- **Loan-to-Income Ratio**: Maximum 25%
- **Delinquencies**: Maximum 2 in last 24 months
- **Employment Length**: Minimum 1 year
- **Credit History**: Minimum 2 years

### Protected Attributes (Ignored)

The system explicitly ignores:
- Gender
- Race
- Ethnicity
- Religion
- Age (where legally protected)
- Marital status
- ZIP code (as demographic proxy)

## Example Output

```
================================================================================
BIAS TEST REPORT - Loan Approval System
================================================================================

Test Group: Gender/Name Variation Test

Financial Criteria (Same for All Tests):
  age: 32
  credit_score: 680
  annual_income: 62000
  loan_amount: 15000
  dti_ratio: 0.28
  employment_years: 3
  delinquencies: 0
  credit_history_years: 5

--------------------------------------------------------------------------------
Test Results:
--------------------------------------------------------------------------------

Applicant: John (male)
Decision: APPROVED
Risk Score: 85.00/100
Rationale: Application meets all criteria. Approved.

[... more results ...]

--------------------------------------------------------------------------------
Bias Analysis:
--------------------------------------------------------------------------------
Decisions Consistent: Yes
Risk Scores Vary: No

BIAS DETECTED: NO

No bias detected. System treats all applicants equally when financial
criteria are identical, regardless of name or gender.
```

## Customization

### Adjusting Decision Thresholds

Edit `loan_approval_system.py`:

```python
system = LoanApprovalSystem()
system.min_credit_score = 700  # Change minimum credit score
system.max_dti_ratio = 0.40    # Change maximum DTI ratio
```

### Adding Test Cases

Edit `test_cases.json` or modify `bias_testing.py` to add more test variations.

### Custom Financial Criteria

Modify the `base_financials` dictionary in `run_bias_tests.py`:

```python
base_financials = {
    "credit_score": 720,
    "annual_income": 80000,
    # ... other criteria
}
```

## Limitations

1. **Simplified Parser**: The prompt parser is basic and may not handle all natural language variations
2. **Static Thresholds**: Decision thresholds are fixed (could be made configurable)
3. **Limited Testing**: Tests focus on gender/name bias; other forms of bias may require additional tests

## Future Improvements

- [ ] More sophisticated NLP for prompt parsing
- [ ] Machine learning model integration
- [ ] Real-time bias monitoring
- [ ] Integration with external fairness libraries
- [ ] Support for additional protected attributes
- [ ] Automated threshold optimization

## Legal and Ethical Considerations

- This system is for educational and testing purposes
- In production, consult legal experts on fair lending regulations
- Ensure compliance with local laws (e.g., Equal Credit Opportunity Act in US)
- Regular audits and monitoring are essential

## License

This project is provided as-is for educational purposes.

## Contact

For questions or issues, please refer to the assignment guidelines or instructor.

