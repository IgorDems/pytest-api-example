import pytest
import schemas
import api_helpers



@pytest.fixture(scope='function')
def order_data():
   
    return {
        "id": "54321",
        "petId": 0,
        "quantity": 1,
        "status": "placed"
    }


def test_patch_order_by_id(order_data):
    # Creating a function to test the PATCH request /store/order/{order_id}
    test_endpoint = f"/store/order/{order_data['id']}"
    new_status = "shipped"  # Example new status to update the order

    # Making the PATCH request
    response = api_helpers.patch_api_data(
        test_endpoint, {"status": new_status})

    # Validate the response codes
    assert response.status_code == 200  # Assuming a successful update returns 200 OK

    # Validate the response values
    updated_order = response.json()
    # Ensure status is updated as expected
    assert updated_order['status'] == new_status

    # Validate the response message "Order and pet status updated successfully"
    assert response.text == "Order and pet status updated successfully"
