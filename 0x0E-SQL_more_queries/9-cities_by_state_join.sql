-- lists all cities contained in the database hbtn_0d_usa.

SELECT cities.id, cities.name AS states.name
FROM hbtn_0d_usa.cities
JOIN states ON cities.state_id =  states.id
ORDER BY cities.id ASC;