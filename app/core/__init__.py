"""
SalaryPlan Core Package
Exports constants, quantum constants, and core utilities for the MindTech platform.
"""

from .constants import (
    APP_NAME,
    APP_VERSION,
    APP_DESCRIPTION,
    COMPANY_NAME,
    COMPANY_EMAIL,
    SUPPORT_PHONE,
    WEBSITE_URL,
    PRIVACY_POLICY_URL,
    TERMS_OF_SERVICE_URL,
    QUANTUM_BADGE_TEXT,
    PATENT_NUMBER,
    DEFAULT_CURRENCY,
    SUPPORTED_CURRENCIES,
    AFRICAN_LANGUAGES,
    DATE_FORMAT,
    TIME_FORMAT,
    DATETIME_FORMAT
)

from .quantum_constants import (
    CHSH_S_VALUE,
    QUANTUM_BELL_STATE,
    QUANTUM_MEASUREMENT_BASIS,
    QUANTUM_CIRCUIT_DEPTH,
    CHSH_EXPERIMENT_RESULT,
    QUANTUM_ENTANGLEMENT_MEASURE,
    QUANTUM_CORRELATION_COEFFICIENT
)

from .utils import (
    calculate_quantum_badge_score,
    generate_quantum_signature,
    validate_quantum_state,
    encrypt_user_data,
    decrypt_user_data,
    hash_user_id,
    validate_south_african_id,
    validate_phone_number,
    format_currency,
    parse_currency,
    calculate_loan_payment,
    calculate_savings_projection,
    generate_debt_snowball_plan,
    generate_debt_avalanche_plan,
    calculate_chsh_value,
    verify_patent_status
)

from .security import (
    sanitize_input,
    validate_session,
    rate_limit_check,
    audit_log,
    encryption_key_rotation,
    data_sovereignty_check
)

from .config import (
    get_settings,
    Settings,
    Environment,
    DatabaseSettings,
    AISettings,
    QuantumSettings,
    SecuritySettings
)

__all__ = [
    # Constants
    "APP_NAME",
    "APP_VERSION",
    "APP_DESCRIPTION",
    "COMPANY_NAME",
    "COMPANY_EMAIL",
    "SUPPORT_PHONE",
    "WEBSITE_URL",
    "PRIVACY_POLICY_URL",
    "TERMS_OF_SERVICE_URL",
    "QUANTUM_BADGE_TEXT",
    "PATENT_NUMBER",
    "DEFAULT_CURRENCY",
    "SUPPORTED_CURRENCIES",
    "AFRICAN_LANGUAGES",
    "DATE_FORMAT",
    "TIME_FORMAT",
    "DATETIME_FORMAT",
    
    # Quantum constants
    "CHSH_S_VALUE",
    "QUANTUM_BELL_STATE",
    "QUANTUM_MEASUREMENT_BASIS",
    "QUANTUM_CIRCUIT_DEPTH",
    "CHSH_EXPERIMENT_RESULT",
    "QUANTUM_ENTANGLEMENT_MEASURE",
    "QUANTUM_CORRELATION_COEFFICIENT",
    
    # Utilities
    "calculate_quantum_badge_score",
    "generate_quantum_signature",
    "validate_quantum_state",
    "encrypt_user_data",
    "decrypt_user_data",
    "hash_user_id",
    "validate_south_african_id",
    "validate_phone_number",
    "format_currency",
    "parse_currency",
    "calculate_loan_payment",
    "calculate_savings_projection",
    "generate_debt_snowball_plan",
    "generate_debt_avalanche_plan",
    "calculate_chsh_value",
    "verify_patent_status",
    
    # Security
    "sanitize_input",
    "validate_session",
    "rate_limit_check",
    "audit_log",
    "encryption_key_rotation",
    "data_sovereignty_check",
    
    # Config
    "get_settings",
    "Settings",
    "Environment",
    "DatabaseSettings",
    "AISettings",
    "QuantumSettings",
    "SecuritySettings"
]
