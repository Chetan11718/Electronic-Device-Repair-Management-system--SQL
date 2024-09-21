DELIMITER $$
CREATE FUNCTION count_cost(total_price int)
RETURNS VARCHAR(50)
DETERMINISTIC
BEGIN
DECLARE VALUE varchar(50);
IF total_price<0 then
    set VALUE="Invalid Cost should be greater than 0 ";
ELSE
    set VALUE ="Valid Cost";
end if;
return value;
END $$
DELIMITER ;


with t as (Select user_no,payment_no,total_price as count from payment group by user_no)
select user_no,payment_no,count_cost(count) as Validate,count as Cost from t;

