USE fantasy;

DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS player_stats;
DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS teams;

CREATE TABLE players(
name_ VARCHAR(50) PRIMARY KEY,
position VARCHAR(50),
team VARCHAR(50)
);

CREATE TABLE games(
game_id INT AUTO_INCREMENT PRIMARY KEY,
week_number INT,
home_team VARCHAR(50),
away_team VARCHAR(50),
home_points INT,
away_poitns INT
);

CREATE TABLE player_stats(
player_name VARCHAR(50),
game_id INT,
week_number INT,
stat_type VARCHAR(50),
stat_value DOUBLE(12,2),
PRIMARY KEY(player_name, game_id, stat_type)
);

CREATE TABLE teams(
team_code VARCHAR(50) PRIMARY KEY,
team_name VARCHAR(50)
);