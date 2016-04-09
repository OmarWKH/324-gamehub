--enable foreign keys
PRAGMA foreign_keys = ON;

-- Table GAME

CREATE TABLE GAME
(
  GAME_ID INTEGER NOT NULL,
  Name TEXT NOT NULL,
  Description TEXT,
  Poster NONE,
  No_of_players INTEGER,
  Duration INTEGER,
  No_of_sessions INTEGER,
  Age_group TEXT,
  Competitve_level TEXT,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID)
);

-- Table VIDEO_GAME

CREATE TABLE VIDEO_GAME
(
  System_requirements TEXT,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID),
  CONSTRAINT GAME_VIDEO_GAME FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table BOARD_GAME

CREATE TABLE BOARD_GAME
(
  Pieces TEXT,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID),
  CONSTRAINT GAME_BOARD_GAME FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table PHYSICAL_GAME

CREATE TABLE PHYSICAL_GAME
(
  Physical_requirements TEXT,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID),
  CONSTRAINT GAME_PHYSICAL_GAME FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table CARD_GAME

CREATE TABLE CARD_GAME
(
  Cards_type TEXT,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID),
  CONSTRAINT GAME_CARD_GAME FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table TABLETOP_RPG

CREATE TABLE TABLETOP_RPG
(
  Narrative_authority TEXT,
  Settings TEXT,
  Play_Style TEXT,
  Components TEXT,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID),
  CONSTRAINT GAME_TABLETOP_RPG FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table USERS

CREATE TABLE USERS
(
  USER_ID INTEGER NOT NULL,
  first_name TEXT,
  last_name TEXT,
  Location TEXT,
  Email TEXT NOT NULL,
  Is_public NONE NOT NULL,
  Nickname TEXT NOT NULL UNIQUE,
  Password TEXT NOT NULL,
  Is_blocked NONE NOT NULL,
  Is_Admin NONE NOT NULL,
  Is_Moderator NONE NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (USER_ID)
);

-- Table GROUPS

CREATE TABLE GROUPS
(
  GROUP_ID INTEGER NOT NULL,
  Name TEXT NOT NULL,
  Description TEXT,
  Area TEXT NOT NULL,
  Is_public NONE NOT NULL,
  CREATOR_ID INTEGER,
  CONSTRAINT Identifier1 PRIMARY KEY (GROUP_ID),
  CONSTRAINT CREATES FOREIGN KEY (CREATOR_ID) REFERENCES USERS (USER_ID)
);

-- Table INSTANCES

CREATE TABLE INSTANCES
(
  Time NONE NOT NULL,
  Date NONE NOT NULL,
  INSTANCE_Location TEXT NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  GAME_ID INTEGER,
  INSTANCE_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (INSTANCE_ID),
  CONSTRAINT GROUPS_INSTANCES FOREIGN KEY (INSTANCE_ID) REFERENCES GROUPS (GROUP_ID),
  CONSTRAINT BELONGS FOREIGN KEY (GROUP_ID) REFERENCES GROUPS (GROUP_ID),
  CONSTRAINT PLAYAING FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table REPORTS

CREATE TABLE REPORTS
(
  REPORT_ID INTEGER NOT NULL,
  Type TEXT,
  Comment TEXT NOT NULL,
  REPORTER_ID INTEGER NOT NULL,
  REPORTED_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (REPORT_ID,REPORTER_ID,REPORTED_ID),
  CONSTRAINT FILES FOREIGN KEY (REPORTER_ID) REFERENCES USERS (USER_ID),
  CONSTRAINT SUBJECT_OF FOREIGN KEY (REPORTED_ID) REFERENCES USERS (USER_ID)
);

-- Table BLOGPOST

CREATE TABLE BLOGPOST
(
  Text TEXT NOT NULL,
  BP_Time NONE NOT NULL,
  Is_public NONE NOT NULL,
  POST_ID INTEGER NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  USER_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (POST_ID,GROUP_ID,USER_ID),
  CONSTRAINT BELONGS_G FOREIGN KEY (GROUP_ID) REFERENCES GROUPS (GROUP_ID),
  CONSTRAINT WRITES_B FOREIGN KEY (USER_ID) REFERENCES USERS (USER_ID)
);

-- Table COMMENTS

CREATE TABLE COMMENTS
(
  Text TEXT NOT NULL,
  C_Time NONE NOT NULL,
  C_ID INTEGER NOT NULL,
  COMMENTOR_ID INTEGER NOT NULL,
  POST_ID INTEGER NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  POST_WRITER_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (C_ID,COMMENTOR_ID,POST_ID,GROUP_ID,POST_WRITER_ID),
  CONSTRAINT WRITES FOREIGN KEY (COMMENTOR_ID) REFERENCES USERS (USER_ID),
  CONSTRAINT BELONGS_B FOREIGN KEY (POST_ID, GROUP_ID, POST_WRITER_ID) REFERENCES BLOGPOST (POST_ID, GROUP_ID, USER_ID)
);

-- Table CHAT_MESSAGE

CREATE TABLE CHAT_MESSAGE
(
  Text TEXT NOT NULL,
  CM_Time NONE NOT NULL,
  CM_ID INTEGER NOT NULL,
  USER_ID INTEGER NOT NULL,
  CC_Name TEXT NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (CM_ID,USER_ID,CC_Name,GROUP_ID),
  CONSTRAINT WRITES_CM FOREIGN KEY (USER_ID) REFERENCES USERS (USER_ID),
  CONSTRAINT BELONGS_CC FOREIGN KEY (CC_Name, GROUP_ID) REFERENCES CHAT_CHANNEL (CC_Name, GROUP_ID)
);

-- Table CHAT_CHANNEL

CREATE TABLE CHAT_CHANNEL
(
  CC_Name TEXT NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (CC_Name,GROUP_ID),
  CONSTRAINT BELONGS_G2 FOREIGN KEY (GROUP_ID) REFERENCES GROUPS (GROUP_ID)
);

-- Table LIST

CREATE TABLE LIST
(
  ID INTEGER NOT NULL UNIQUE, --surrogate for django primary key
  Note TEXT,
  Ownership TEXT,
  Skill TEXT,
  GAME_ID INTEGER NOT NULL,
  USER_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID,USER_ID),
  CONSTRAINT GL FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID),
  CONSTRAINT UL FOREIGN KEY (USER_ID) REFERENCES USERS (USER_ID)
);

-- Table TYPE

CREATE TABLE TYPE
(
  ID INTEGER NOT NULL UNIQUE, --surrogate for django primary key
  Genre TEXT,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID, Genre),
  CONSTRAINT TYPE_OF FOREIGN KEY (GAME_ID) REFERENCES GAME (GAME_ID)
);

-- Table PLATFORM

CREATE TABLE PLATFORM
(
  ID INTEGER NOT NULL UNIQUE, --surrogate for django primary key
  OS TEXT NOT NULL,
  GAME_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (GAME_ID, OS),
  CONSTRAINT WORKS_ON FOREIGN KEY (GAME_ID) REFERENCES VIDEO_GAME (GAME_ID)
);

-- Table TAG

CREATE TABLE TAG
(
  ID INTEGER NOT NULL UNIQUE, --surrogate for django primary key
  TAG TEXT,
  POST_ID INTEGER NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  USER_ID INTEGER NOT NULL,
  CONSTRAINT Identifier1 PRIMARY KEY (POST_ID,GROUP_ID,USER_ID, TAG),
  CONSTRAINT CONTAINS FOREIGN KEY (POST_ID, GROUP_ID, USER_ID) REFERENCES BLOGPOST (POST_ID, GROUP_ID, USER_ID)
);

-- Table USERS_GROUPS

CREATE TABLE USERS_GROUPS
(
  ID INTEGER NOT NULL UNIQUE, --surrogate for django primary key
  USER_ID INTEGER NOT NULL,
  GROUP_ID INTEGER NOT NULL,
  CONSTRAINT Key1 PRIMARY KEY (USER_ID,GROUP_ID),
  CONSTRAINT MEMBER_OF FOREIGN KEY (USER_ID) REFERENCES USERS (USER_ID),
  CONSTRAINT MEMBER_OF_G FOREIGN KEY (GROUP_ID) REFERENCES GROUPS (GROUP_ID)
);
