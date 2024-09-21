from create_user import create_user
from create_product import create_product
from create_service import create_service
from create_employee import create_employee
from create_payment import create_payment

def create(selected_table):
    if selected_table == 'User Details':
        create_user()
    elif selected_table == 'Product':
        create_product()
    elif selected_table == 'Service':
        create_service()
    elif selected_table == 'Payment':
        create_payment()
    elif selected_table == 'Employee':
        create_employee()