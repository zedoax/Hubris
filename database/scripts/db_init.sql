CREATE TABLE tournament (
  -- Tournament Information --
  tournament_id VARCHAR(25) NOT NULL,
  title VARCHAR(100) NOT NULL,
  date VARCHAR(20) NOT NULL,
  game_title VARCHAR(100) NOT NULL,
  tourney_type VARCHAR(20) NOT NULL,
  rule_set VARCHAR(2000),
  PRIMARY KEY(tournament_id),
  FOREIGN KEY(tourney_type) REFERENCES rule_set(tourney_type)
);

CREATE TABLE rule_set (
  -- Default Rule set (Should not change much) --
  tourney_type VARCHAR(20) NOT NULL,
  rules VARCHAR(3000) NOT NULL,
  PRIMARY KEY(tourney_type)
);

CREATE TABLE match (
  -- Tournament Identifying Data --
  tournament_id VARCHAR(25) NOT NULL,
  initial_round BOOLEAN NOT NULL,
  -- Match Specific Data --
  match_id VARCHAR(35) NOT NULL,
  team_a_id VARCHAR(35),
  team_b_id VARCHAR(35),
  next_match_id VARCHAR(35),
  PRIMARY KEY(match_id),
  FOREIGN KEY(tournament_id) REFERENCES tournament(tournament_id),
  FOREIGN KEY(team_a_id) REFERENCES team(team_id),
  FOREIGN KEY(team_b_id) REFERENCES team(team_id)
);

CREATE TABLE team (
  team_id VARCHAR(35) NOT NULL,
  user_id VARCHAR(25) NOT NULL,
  PRIMARY KEY(team_id)
);