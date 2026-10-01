SELECT users.name, users.followers, posts.likes
FROM users JOIN posts
ON users.user_id = posts.user_id
WHERE users.followers > 9000;
