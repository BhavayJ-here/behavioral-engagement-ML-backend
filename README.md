Behavioral Engagement Backend

Predicts how engaged a user is with a piece of content, and recommends what they'd want next based purely on behavioral signals like watch time, skips, rewatches, and session timing.

No likes, no ratings, no explicit feedback. Just behavior in, engagement score and recommendations out.

How it works

Raw session data (watch time, skips, rewatches, time of day, session length) gets converted into derived signals watch ratio, skip rate, rewatch rate, prime time flag, and a composite engagement score. A RandomForest classifier trained on this feature set predicts whether a session counts as "engaged." Recommendations are ranked per-user from historical engagement signal across content.

Endpoints


POST /track — log a session
POST /predict — get an engagement score for a session
GET /recommend?user_id= — get ranked content recommendations for a user
