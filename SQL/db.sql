CREATE DATABASE Events;
USE Events;
CREATE Table Events (
	id INT NOT NULL AUTO_INCREMENT,
	title VARCHAR(255) NOT NULL,
	description VARCHAR(255) NOT NULL,
	date DATE NOT NULL,
	fees INT NOT NULL,
	PRIMARY KEY (id)
);

INSERT INTO Events (title, description, date, fees) VALUES
("Summer Music Festival","Annual Summer Music Festival!","2023-08-20", 50),
("Soccer Championship", "World Famous Soccer Championship.", "2023-09-10", 30),
("Cirque du Mystique", "Cirque du Mystique's mesmerizing performance.", "2023-08-28", 70);

SELECT * FROM Events;