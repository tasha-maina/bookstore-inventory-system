from models.customer import Customer

def test_customer_creation():
    cust = Customer(name="Alice", email="alice@example.com")
    assert cust.name == "Alice"
    assert cust.email == "alice@example.com"
