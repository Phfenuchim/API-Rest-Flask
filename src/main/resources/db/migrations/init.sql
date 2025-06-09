CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS user_roles (
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role_id UUID NOT NULL REFERENCES roles(id) ON DELETE CASCADE,
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE IF NOT EXISTS policies (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resource VARCHAR(100) NOT NULL,
    action VARCHAR(50) NOT NULL,
    role_id UUID NOT NULL REFERENCES roles(id) ON DELETE CASCADE
);

INSERT INTO roles (name) VALUES
    ('admin'),
    ('editor'),
    ('viewer')
ON CONFLICT (name) DO NOTHING;

INSERT INTO policies (resource, action, role_id)
SELECT '/users', 'read', id FROM roles WHERE name = 'admin'
UNION ALL
SELECT '/users', 'write', id FROM roles WHERE name = 'admin'
UNION ALL
SELECT '/articles', 'write', id FROM roles WHERE name = 'editor'
UNION ALL
SELECT '/articles', 'read', id FROM roles WHERE name = 'viewer';
