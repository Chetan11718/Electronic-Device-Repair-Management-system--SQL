--count
SELECT COUNT(*) FROM product WHERE qty=1; 

--SUM
SELECT SUM(estimated_price) FROM services WHERE qty>1;  

--AVG
SELECT AVG(total_price) FROM payment; 