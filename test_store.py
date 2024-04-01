import pytest
import schemas
import api_helpers


# 2) Consider using @pytest.fixture to create unique test data for each run
@pytest.fixture(scope='function')
def order_data():
    # Example order data, you can customize this as needed for your test
    return {
        "id": "54321",
        "petId": 0,
        "quantity": 1,
        "status": "placed"
    }


def test_patch_order_by_id(order_data):
    # 1) Creating a function to test the PATCH request /store/order/{order_id}
    test_endpoint = f"/store/order/{order_data['id']}"
    new_status = "shipped"  # Example new status to update the order

    # 2)Making the PATCH request
    response = api_helpers.patch_api_data(
        test_endpoint, {"status": new_status})

    # 3) Validate the response codes
    assert response.status_code == 200  # Assuming a successful update returns 200 OK

    # 4) Validate the response values
    updated_order = response.json()
    # Ensure status is updated as expected
    assert updated_order['status'] == new_status

    # 5) Validate the response message "Order and pet status updated successfully"
    assert response.text == "Order and pet status updated successfully"
