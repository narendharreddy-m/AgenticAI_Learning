ROLE: You are an AI engineer with 5 years of production experience,
writing a cold email to a recruiter — confident, specific, not desperate.

CONTEXT:

Audience — a senior recruiter at OpenAI who reads 200+ emails per day
My background — built async multi-agent systems in production and sclaed up to millions of users on  daily basis.
Goal — get a 15-minute screening call, not a generic "thanks we'll review"
Stakes — this email is one of hundreds in their inbox today.

REFERENCES (the job post I'm applying for):
"""
Senior AI Engineer — OpenAI
We're looking for engineers who have shipped agentic AI systems
to production. You'll work on long-horizon agents, tool use, and
reliability at scale. Strong Python + experience with LLM APIs
required. Bonus: experience with async, retrieval, or evals.
"""

TASK: Write a cold email to the HR recruiter for this role.

FORMAT:
- Subject line (under 15 words, specific, no clichés)
- Greeting (use "Hi Archana " — not "Dear Hiring Manager")
- Body: Keep it crisp and Short and shwo case my project in Star Approach
- One clear ask (15-minute screening call)
- Sign-off

Major Peroject to Shocase:
"""
Built a production-grade RAG-based Content Intelligence Platform for WBD, indexing 25M+ chunks from scripts, subtitles, PDFs, and metadata across 40K+ media assets, enabling semantic search and source-grounded Q&A at scale.
Improved retrieval accuracy to 92% using hybrid search, metadata filters, reranking, and evaluation pipelines; reduced average response latency by 45% through async APIs, caching, and optimized vector search.
Enabled content, marketing, and analytics teams to reduce manual research effort by 60–70%, supporting 1M+ monthly semantic searches across franchise and catalog intelligence use cases.
"""

LENGTH: Maybe under 300. 

CONSTRAINTS:
- No "I hope this email finds you well"
- No "I am writing to express my interest"
- No "esteemed team", "valuable addition", "proven track record"
- No listing of generic qualifications — pick ONE specific match
- No "please find my resume attached" — link is in signature
- Confident tone, not begging tone

EXAMPLES of the style I want:


Subject: Async agents → OpenAI Senior AI role
"Hi Maya — I saw the Senior AI Engineer post. The 'long-horizon
agents' line is exactly what I've been shipping for two years at
[company] — including an async refactor that cut latency by 3x.
15 minutes this week to walk you through it? Resume + agent demo
in signature."

QUALITY CHECK:
Before finalizing, verify: under 300 words, no banned phrases,
one specific match to the JD, one clear ask. If anything fails,
rewrite it.