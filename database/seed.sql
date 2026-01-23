USE job_portal;

INSERT INTO users (username, email, password, role) VALUES
('employer1', 'employer@example.com', '$2b$12$hashedpassword', 'employer'),
('seeker1', 'seeker@example.com', '$2b$12$hashedpassword', 'job_seeker');

INSERT INTO jobs (title, description, company, location, salary, employer_id) VALUES
('Software Engineer', 'Develop web apps.', 'Tech Corp', 'Remote', 50000.00, 1);