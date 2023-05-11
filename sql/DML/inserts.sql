INSERT INTO users(username, email, password) 
VALUES
    ('Mason Kidd',   'mk@mail.com', '123mk'), -- 1aea5af2-c09b-45dc-bbf9-b4ee679c0388
    ('Elias Hurst',  'eh@mail.com', '123eh'), -- 49e8618b-c7ee-4ecd-aa89-2ddde6bacee9
    ('Mabel Mccann', 'mm@mail.com', '123mm'); -- f05538bf-9274-42ba-980a-020da0f34c50

INSERT INTO posts(title, body, author_id) 
VALUES
    ('New house!', '...', '1aea5af2-c09b-45dc-bbf9-b4ee679c0388'), -- 44d2b3b6-e4d7-40d4-9674-1a9c1431d9d2
    ('Vacation!',  '...', '49e8618b-c7ee-4ecd-aa89-2ddde6bacee9'); -- 214a0984-2c68-4ec7-8bd3-d4d69ddc45ff

INSERT INTO comments(body, target_id, author_id) 
VALUES
    ('So cool!',    '44d2b3b6-e4d7-40d4-9674-1a9c1431d9d2', 'f05538bf-9274-42ba-980a-020da0f34c50'),
    ('I envy you!', '214a0984-2c68-4ec7-8bd3-d4d69ddc45ff', 'f05538bf-9274-42ba-980a-020da0f34c50');

INSERT INTO messages(body, target_id, author_id) 
VALUES
    ('How was your day?', '1aea5af2-c09b-45dc-bbf9-b4ee679c0388', 'f05538bf-9274-42ba-980a-020da0f34c50'),
    ('Where are you?',    '1aea5af2-c09b-45dc-bbf9-b4ee679c0388', '49e8618b-c7ee-4ecd-aa89-2ddde6bacee9');

INSERT INTO reactions(type, target_id, author_id) 
VALUES
    ('angry', '44d2b3b6-e4d7-40d4-9674-1a9c1431d9d2', '49e8618b-c7ee-4ecd-aa89-2ddde6bacee9'),
    ('smile', '214a0984-2c68-4ec7-8bd3-d4d69ddc45ff', 'f05538bf-9274-42ba-980a-020da0f34c50');
