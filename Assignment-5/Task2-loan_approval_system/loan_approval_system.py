"""
Loan Approval System
A system to evaluate loan applications based on financial criteria only.
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class LoanDecision(Enum):
    """Loan decision outcomes"""
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    CONDITIONAL = "CONDITIONAL"


@dataclass
class LoanApplication:
    """Loan application data structure"""
    # Financial factors (allowed)
    credit_score: int
    annual_income: float
    loan_amount: float
    debt_to_income_ratio: float
    employment_length_years: float
    delinquencies_24m: int
    credit_history_years: float
    
    # Protected attributes (should be ignored if present)
    applicant_name: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    race: Optional[str] = None
    ethnicity: Optional[str] = None
    marital_status: Optional[str] = None
    zip_code: Optional[str] = None


class LoanApprovalSystem:
    """
    Loan approval system that evaluates applications based solely on financial criteria.
    Protected attributes are stored but not used in decision making.
    """
    
    def __init__(self):
        """Initialize the loan approval system with decision thresholds"""
        # Decision thresholds (can be adjusted)
        self.min_credit_score = 650
        self.max_dti_ratio = 0.36  # 36%
        self.min_income_ratio = 0.25  # Loan amount should be <= 25% of annual income
        self.max_delinquencies = 2
        self.min_employment_years = 1
        self.min_credit_history_years = 2
        
    def evaluate_application(self, application: LoanApplication) -> Tuple[LoanDecision, str, Dict]:
        """
        Evaluate a loan application based on financial criteria only.
        
        Args:
            application: LoanApplication object with applicant data
            
        Returns:
            Tuple of (decision, rationale, score_details)
        """
        reasons = []
        score_details = {}
        
        # Check credit score
        if application.credit_score < self.min_credit_score:
            reasons.append(f"Credit score {application.credit_score} below minimum {self.min_credit_score}")
            score_details['credit_score_check'] = False
        else:
            score_details['credit_score_check'] = True
            
        # Check debt-to-income ratio
        if application.debt_to_income_ratio > self.max_dti_ratio:
            reasons.append(f"DTI ratio {application.debt_to_income_ratio:.2%} exceeds maximum {self.max_dti_ratio:.2%}")
            score_details['dti_check'] = False
        else:
            score_details['dti_check'] = True
            
        # Check loan-to-income ratio
        income_ratio = application.loan_amount / application.annual_income
        if income_ratio > self.min_income_ratio:
            reasons.append(f"Loan amount {income_ratio:.2%} of income exceeds maximum {self.min_income_ratio:.2%}")
            score_details['income_ratio_check'] = False
        else:
            score_details['income_ratio_check'] = True
            
        # Check delinquencies
        if application.delinquencies_24m > self.max_delinquencies:
            reasons.append(f"Delinquencies {application.delinquencies_24m} exceed maximum {self.max_delinquencies}")
            score_details['delinquencies_check'] = False
        else:
            score_details['delinquencies_check'] = True
            
        # Check employment length
        if application.employment_length_years < self.min_employment_years:
            reasons.append(f"Employment length {application.employment_length_years} years below minimum {self.min_employment_years}")
            score_details['employment_check'] = False
        else:
            score_details['employment_check'] = True
            
        # Check credit history
        if application.credit_history_years < self.min_credit_history_years:
            reasons.append(f"Credit history {application.credit_history_years} years below minimum {self.min_credit_history_years}")
            score_details['credit_history_check'] = False
        else:
            score_details['credit_history_check'] = True
        
        # Calculate risk score (0-100, higher is better)
        risk_score = self._calculate_risk_score(application, score_details)
        score_details['risk_score'] = risk_score
        
        # Make decision
        all_passed = all([
            score_details['credit_score_check'],
            score_details['dti_check'],
            score_details['income_ratio_check'],
            score_details['delinquencies_check'],
            score_details['employment_check'],
            score_details['credit_history_check']
        ])
        
        if all_passed:
            if risk_score >= 80:
                decision = LoanDecision.APPROVED
                rationale = "Application meets all criteria. Approved."
            else:
                decision = LoanDecision.CONDITIONAL
                rationale = f"Application meets basic criteria but risk score is {risk_score}/100. Conditional approval recommended."
        else:
            decision = LoanDecision.REJECTED
            rationale = f"Application rejected. Reasons: {'; '.join(reasons)}"
        
        return decision, rationale, score_details
    
    def _calculate_risk_score(self, application: LoanApplication, score_details: Dict) -> float:
        """
        Calculate a risk score based on financial factors.
        Higher score = lower risk = better
        
        Args:
            application: Loan application
            score_details: Dictionary with check results
            
        Returns:
            Risk score from 0-100
        """
        score = 0.0
        
        # Credit score component (0-30 points)
        if score_details['credit_score_check']:
            credit_points = min(30, (application.credit_score - self.min_credit_score) / 10)
            score += credit_points
        
        # DTI component (0-20 points)
        if score_details['dti_check']:
            dti_points = 20 * (1 - application.debt_to_income_ratio / self.max_dti_ratio)
            score += dti_points
        
        # Income stability (0-15 points)
        if score_details['employment_check']:
            employment_points = min(15, application.employment_length_years * 3)
            score += employment_points
        
        # Payment history (0-20 points)
        if score_details['delinquencies_check']:
            delinquency_points = max(0, 20 - application.delinquencies_24m * 5)
            score += delinquency_points
        
        # Credit history (0-15 points)
        if score_details['credit_history_check']:
            history_points = min(15, application.credit_history_years * 2)
            score += history_points
        
        return min(100, max(0, score))
    
    def process_prompt(self, prompt: str) -> Tuple[LoanDecision, str, Dict]:
        """
        Process a natural language prompt and extract loan application data.
        This simulates how an AI might parse a user prompt.
        
        Args:
            prompt: Natural language prompt with loan application details
            
        Returns:
            Tuple of (decision, rationale, score_details)
        """
        # Extract application data from prompt
        application = self._parse_prompt(prompt)
        
        # Evaluate application
        return self.evaluate_application(application)
    
    def _parse_prompt(self, prompt: str) -> LoanApplication:
        """
        Parse a natural language prompt to extract loan application data.
        This is a simplified parser - in reality, you'd use NLP techniques.
        
        Args:
            prompt: Natural language prompt
            
        Returns:
            LoanApplication object
        """
        # Default values
        credit_score = 680
        annual_income = 62000
        loan_amount = 15000
        dti_ratio = 0.28
        employment_years = 3
        delinquencies = 0
        credit_history_years = 5
        
        # Extract values from prompt (case-insensitive)
        prompt_lower = prompt.lower()
        
        # Extract credit score
        if 'credit score' in prompt_lower or 'credit_score' in prompt_lower:
            import re
            score_match = re.search(r'credit\s*score[:\s]+(\d+)', prompt_lower)
            if score_match:
                credit_score = int(score_match.group(1))
        
        # Extract income
        income_match = re.search(r'income[:\s]+\$?(\d+(?:,\d+)*(?:\.\d+)?)k?', prompt_lower)
        if income_match:
            income_str = income_match.group(1).replace(',', '')
            annual_income = float(income_str)
            if 'k' in prompt_lower[income_match.start():income_match.end()]:
                annual_income *= 1000
        
        # Extract loan amount
        loan_match = re.search(r'loan[:\s]+\$?(\d+(?:,\d+)*(?:\.\d+)?)k?', prompt_lower)
        if loan_match:
            loan_str = loan_match.group(1).replace(',', '')
            loan_amount = float(loan_str)
            if 'k' in prompt_lower[loan_match.start():loan_match.end()]:
                loan_amount *= 1000
        
        # Extract DTI
        dti_match = re.search(r'dti[:\s]+(\d+(?:\.\d+)?)%?', prompt_lower)
        if dti_match:
            dti_ratio = float(dti_match.group(1)) / 100
        
        # Extract name (for testing purposes)
        name = None
        name_match = re.search(r'(?:for|applicant|name)[:\s]+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)', prompt)
        if name_match:
            name = name_match.group(1)
        
        # Extract gender/pronouns (for testing purposes)
        gender = None
        if any(pronoun in prompt_lower for pronoun in ['she', 'her', 'female', 'woman']):
            gender = 'female'
        elif any(pronoun in prompt_lower for pronoun in ['he', 'him', 'male', 'man']):
            gender = 'male'
        elif any(pronoun in prompt_lower for pronoun in ['they', 'them', 'non-binary', 'nonbinary']):
            gender = 'non-binary'
        
        return LoanApplication(
            credit_score=credit_score,
            annual_income=annual_income,
            loan_amount=loan_amount,
            debt_to_income_ratio=dti_ratio,
            employment_length_years=employment_years,
            delinquencies_24m=delinquencies,
            credit_history_years=credit_history_years,
            applicant_name=name,
            gender=gender
        )


def main():
    """Example usage of the loan approval system"""
    system = LoanApprovalSystem()
    
    # Example application
    application = LoanApplication(
        credit_score=680,
        annual_income=62000,
        loan_amount=15000,
        debt_to_income_ratio=0.28,
        employment_length_years=3,
        delinquencies_24m=0,
        credit_history_years=5
    )
    
    decision, rationale, details = system.evaluate_application(application)
    print(f"Decision: {decision.value}")
    print(f"Rationale: {rationale}")
    print(f"Score Details: {details}")


if __name__ == "__main__":
    main()

