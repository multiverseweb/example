# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state
from person p left outer join address a
on p.personId = a.personId;