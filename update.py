from update_user import update_user
from update_product import update_product
from update_service import update_service
from update_employee import update_employee
from update_payment import update_payment

def update(selected_table):
    if selected_table == 'User Details':
        update_user()
    elif selected_table == 'Product':
        update_product()
    elif selected_table == 'Service':
        update_service()
    elif selected_table == 'Payment':
        update_payment()
    elif selected_table == 'Employee':
        update_employee()