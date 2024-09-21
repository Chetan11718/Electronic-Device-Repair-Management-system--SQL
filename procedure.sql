--used to update the age of the users.

DELIMITER $$
CREATE procedure age_updation_f(
IN u_no varchar(30),IN DB date, OUT msg varchar(30))
BEGIN
DECLARE age int;
IF DB>sysdate() THEN
    set msg= 'Invalid DOB';
ELSE
update user_details
set Age=(datediff(sysdate(),DB))/365
where user_no= u_no;
update user_details
set dob=DB
where user_no=u_no;
set msg='Age updated Successfully';
END IF;
END;$$
DELIMITER ;
CALL age_updation_f('1001','2002-02-18',@A);
SELECT @A;

select * from user_details where user_no='1001';