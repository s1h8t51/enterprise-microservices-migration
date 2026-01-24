from datetime import datetime, timedelta
from typing import Dict, Optional
import hashlib

class LicenseValidator:
    """
    Logic for checking the validity of a license.
    In a real-world scenario, this would include checking a 
    cryptographic signature to prevent tampering.
    """

    def validate_license(self, license_record: Dict) -> Dict:
        """
        Validates the status and expiration date of a license.
        """
        now = datetime.utcnow()
        expires_at = datetime.fromisoformat(license_record['expires_at'])
        
        is_active = license_record.get('status') == 'ACTIVE'
        is_not_expired = expires_at > now
        
        # Simple integrity check (Simulation of digital signature check)
        expected_checksum = self._generate_checksum(license_record['id'], license_record['customer_id'])
        is_authentic = license_record.get('checksum') == expected_checksum

        return {
            "valid": is_active and is_not_expired and is_authentic,
            "status": "VALID" if (is_active and is_not_expired) else "INVALID_OR_EXPIRED",
            "tamper_detected": not is_authentic,
            "days_remaining": (expires_at - now).days if is_not_expired else 0
        }

    def _generate_checksum(self, license_id: str, customer_id: str) -> str:
        # Simplified placeholder for RSA signature verification
        data = f"{license_id}:{customer_id}:SECRET_SALT"
        return hashlib.sha256(data.encode()).hexdigest()

# Example usage
if __name__ == "__main__":
    validator = LicenseValidator()
    mock_license = {
        "id": "LIC-12345",
        "customer_id": "CUST-99",
        "status": "ACTIVE",
        "expires_at": (datetime.utcnow() + timedelta(days=30)).isoformat(),
        "checksum": "17826359...placeholder" # This would be a real signature
    }
    print(validator.validate_license(mock_license))
