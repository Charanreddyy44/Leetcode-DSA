# Write your MySQL query statement below
DELETE p FROM person p
JOIN person p2
ON p.Email = p2.Email AND p.Id > p2.Id;
