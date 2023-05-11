CREATE TABLE posts (
    id uuid DEFAULT uuid_generate_v4(),

    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL,

    author_id uuid NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY(author_id) REFERENCES users(id)
);