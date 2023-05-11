CREATE TABLE reactions (
    id uuid DEFAULT uuid_generate_v4(),

    type VARCHAR NOT NULL,

    target_id uuid NOT NULL,
    author_id uuid NOT NULL,
    
    PRIMARY KEY (id),
    FOREIGN KEY(target_id) REFERENCES posts(id),
    FOREIGN KEY(author_id) REFERENCES users(id)
);