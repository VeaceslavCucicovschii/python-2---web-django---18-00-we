CREATE TABLE messages (
    id uuid DEFAULT uuid_generate_v4(),

    body TEXT NOT NULL,

    target_id uuid NOT NULL,
    author_id uuid NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY(target_id) REFERENCES users(id),
    FOREIGN KEY(author_id) REFERENCES users(id)
);