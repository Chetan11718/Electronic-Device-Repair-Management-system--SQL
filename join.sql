--Displying the valid products who qty is between greater than 0 and less than 3.
select user_no,prod_id,services.ser_no,services.qty FROM product 
NATURAL JOIN services where (services.qty>0 and services.qty<3);

--
select user_no,fname ,lname , sex , phone_no , dob, age ,email,product.prod_id,product.name
FROM user_details NATURAL JOIN product where product.name="Laptop";
