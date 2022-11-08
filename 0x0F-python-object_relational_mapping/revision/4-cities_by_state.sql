-- Create states table
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("Lagos"), ("Oyo"), ("Osun");

CREATE TABLE IF NOT EXISTS cities(
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

INSERT INTO cities (state_id, name) VALUES (1, "Ikeja"), (1, "Oshodi"), (1, "Lekki");
INSERT INTO cities (state_id, name) VALUES (2, "Ibadan"), (2, "Egbeda"), (2, "Igbeti");
INSERT INTO cities (state_id, name) VALUES (3, "Ife"), (3, "Osogbo"), (3, "Iwo");
