from read_user import read_user
from read_product import read_product
from read_service import read_service
from read_employee import read_employee
from read_payment import read_payment

def read(selected_table):
    if selected_table == 'User Details':
        read_user()
    elif selected_table == 'Product':
        read_product()
    elif selected_table == 'Service':
        read_service()
    elif selected_table == 'Payment':
        read_payment()
    elif selected_table == 'Employee':
        read_employee()