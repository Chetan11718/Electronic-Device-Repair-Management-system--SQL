from delete_user import delete_user
from delete_product import delete_product
from delete_service import delete_service
from delete_employee import delete_employee
from delete_payment import delete_payment

def delete(selected_table):
    if selected_table == 'User Details':
        delete_user()
    elif selected_table == 'Product':
        delete_product()
    elif selected_table == 'Service':
        delete_service()
    elif selected_table == 'Payment':
        delete_payment()
    elif selected_table == 'Employee':
        delete_employee()