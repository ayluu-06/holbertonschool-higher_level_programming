-- script that creates the table id_not_null
-- script that creates the table force_name
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256) NOT NULL
)