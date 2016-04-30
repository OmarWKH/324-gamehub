--enable foreign keys
PRAGMA foreign_keys = ON;

--Insert users (done through app for encryption)
Insert into auth_user values(1, 'password', Null, 'true', 'first_name', 'last_name', 'e@gmil.co', 'true', 'true', '2016-04-29 15:40', 'dummy');

--Insert games
Insert into Game values(1, 'Killzone 2',
                        'The series is about the galactic war between the Interplanetary Strategic Alliance (ISA) and the Helghast',
                        '4', 1, '1-4', '16+', 'Casual competetion');
Insert into Video_Game values('PS3', 1);

Insert into Game values(2, 'Monopoly', 'A way to demonstrate that an economy which rewards wealth creation is better than one in which monopolists work under few constraints',
                        4, 3, '1', 'Everyone', 'Competetive');
Insert into Board_Game values('dice and minitures', 2);

--!continue making games

--Inesrt groups
Insert into Groups values(1, 'KFUPM Gamers', 'A place for gamers in KFUPM', 'KFUPM, KSA', 1, Null);
Insert into Groups values(2, 'KSU Gamers', 'A place for gamers in KSU', 'KSU, KSA', 1, Null);

Insert into Groups values(3, 'First Meeting', 'Introduction', 'KFUPM', 1, Null);
Insert into Instances values('2016-04-29 15:40', 'B24-R400', 1, 1, 3);

--Insert blogpost
Insert into Blogpost values('It was nice meeting you all, stay tuned for future meetings',
                            '2016-04-30 08:00', 1, 1, 1, 1);

--Insert list (user-list-game)
Insert into List values(1, 'Interesting game', 'I have it', 'Medium', 1, 1);

--Insert type
Insert into Type values(1, 'FPS', 1);
Insert into Type values(2, 'Strategy', 2);

--Insert Users_Groups
Insert into Users_Groups values(1, 1, 1);