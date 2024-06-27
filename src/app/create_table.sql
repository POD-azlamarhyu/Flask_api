create table if not exists user_info(
    user_id INT PRIMARY KEY NOT NULL,
    email VARCHAR(225) not null UNIQUE,
    is_superuser BOOLEAN DEFAULT false,
    create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
);

create table if not exists user_profile_info(
    profile_id SERIAL PRIMARY KEY not NULL,
    user_id INTEGER not null,
    nickname VARCHAR(100),
    bio VARCHAR(500),
    link VARCHAR(1000),
    icon bytea,
    bg_image bytea,
    age INTEGER(100000),
    created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
