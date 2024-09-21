--union
SELECT user_no FROM user_details 
UNION  
SELECT user_no FROM services;  

--union all
SELECT user_no FROM user_details   
UNION ALL  
SELECT user_no FROM payment; 

--intersect
SELECT prod_id FROM product
INTERSECT  
SELECT prod_id FROM services;  