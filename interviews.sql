SELECT
	ct.contest_id,
	ct.hacker_id,
	ct.name,
	SUM(s.total_submissions) AS contest_submissions,
	SUM(s.total_accepted_submissions) AS contest_accepted_submissions,
	SUM(v.total_views) AS contest_views,
	SUM(v.total_unique_submissions) AS contest_unique_views
FROM
	contests AS ct
	JOIN colleges AS col
	ON ct.contest_id = col.contest_id
	JOIN challenges AS ch
	ON col.college_id = ch.college_id
	JOIN view_stats AS v
	ON ch.challenge_id = v.challenge_id
	JOIN submission_stats AS s
	ON ch.challenge_id = s.challenge_id
GROUP BY ct.contest_id, ct.hacker_id, ct.name
HAVING NOT (contest_submissions = 0 AND contest_accepted_submissions = 0 AND contest_views = 0 AND contest_unique_views = 0)
ORDER BY ct.contest_id
