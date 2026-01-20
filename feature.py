# Feature F1 Implementation
def calculate_inventory(quantity, price):
    """Calculate total inventory value"""
    return quantity * price

def get_medication_stock(medication_id):
    """Retrieve medication stock information"""
    stock_data = {
        medication_id: {
            "name": "Aspirin",
            "quantity": 500,
            "price": 2.50,
            "expiry_date": "2026-12-31"
        }
    }
    return stock_data.get(medication_id)

def update_pharmacy_records(record_id, new_data):
    """Update pharmacy records in database"""
    print(f"Updating record {record_id} with {new_data}")
    return True

# Random test data
test_medications = [
    {"id": 1, "name": "Ibuprofen", "stock": 150},
    {"id": 2, "name": "Paracetamol", "stock": 200},
    {"id": 3, "name": "Amoxicillin", "stock": 75}
]

if __name__ == "__main__":
    print("Pharmacy Management System - Feature F1")
    print("Stock levels:", [med["stock"] for med in test_medications])
