SELECT * FROM meetups WHERE Start > '2015/12/01 10:00:00';
SELECT Id,Start,Location,Description FROM meetups WHERE Topic LIKE 'Ivo';
SELECT * FROM users WHERE Avatar='bk';
SELECT * FROM statuses WHERE Val='Going';
SELECT StatusId,MeetupsId,UsersId FROM meetupregistrations WHERE Id IS NOT NULL;
