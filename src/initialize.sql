CREATE TABLE users (
	user_id INT PRIMARY KEY,
	name VARCHAR(100),
	email VARCHAR(100),
	followers INT
);
CREATE TABLE posts (
	post_id INT PRIMARY KEY,
	user_id INT,
	post_content TEXT,
	likes INT,
	post_date DATE,
	FOREIGN KEY (user_id) REFERENCES users(user_id)
);
INSERT INTO users VALUES (001, 'Jaxon Smith-Njigba', 'jsn@gmail.com', 10354);
INSERT INTO users VALUES (002, 'Sam Darnold', 'sdarnold@gmail.com', 12340);
INSERT INTO users VALUES (003, 'Julian Love', 'love20@gmail.com', 9874);
INSERT INTO users VALUES (004, 'Devon Witherspoon', 'spoon@gmail.com', 8342);
INSERT INTO users VALUES (005, 'Leonard Williams', 'bigcat@gmail.com', 7824);
INSERT INTO users VALUES (006, 'Ernest Jones IV', 'ejiv@gmail.com', 4893);
INSERT INTO users VALUES (007, 'Nick Emmanwori', 'nick3@gmail.com', 8943);
INSERT INTO users VALUES (008, 'Byron Murphy II', 'bmurph2@gmail.com', 9745);
INSERT INTO users VALUES (009, 'Jake Bobo', 'bobo@gmail.com', 16854);
INSERT INTO users VALUES (010, 'Mike Macdonald', 'goat@gmail.com', 9282);
INSERT INTO posts VALUES (001, 001, 'Go Seahawks!', 9000, '2026-08-30');
INSERT INTO posts VALUES (002, 002, 'Injured :(', 8743, '2026-09-09');
INSERT INTO posts VALUES (003, 010, 'Great start to the season!', 6533, '2026-09-09');
INSERT INTO posts VALUES (004, 005, 'Thank you 12s!', 9703, '2026-09-10');
INSERT INTO posts VALUES (005, 003, 'Back soon', 4367, '2026-09-11');
INSERT INTO posts VALUES (006, 004, 'New contract is great', 5879, '2026-09-12');
INSERT INTO posts VALUES (007, 009, 'Back home in Mass', 10823, '2026-09-14');
INSERT INTO posts VALUES (008, 008, 'Almost gameday', 8333, '2026-09-19');
INSERT INTO posts VALUES (009, 006, 'Big win! Let''s go!', 9007, '2026-09-20');
INSERT INTO posts VALUES (010, 007, 'Felt good to be back', 7845, '2026-09-21');
