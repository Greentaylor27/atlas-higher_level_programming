-- Displays all cities within California
SELECT cities.id cities.name FROM cities, states WHERE cities.state_id = state_id AND states.name = 'California' ORDER BY cities.name ASC;
