from langchain.prompts import ChatPromptTemplate

# Training examples for few-shot learning - showing input/output patterns
examples = [
    {
        "Raw_Text": """
            Zeus Artificial Intelligence logo
            Zeus Artificial Intelligence
            Full Stack Developer Intern (React + Node.js)
            Ahmedabad, Gujarat, India · 5 hours ago · Over 100 people clicked apply

            Promoted by hirer · Responses managed off LinkedIn

                On-site Full-time
                Curious where you stand? See how you compare to over 100 others who clicked apply. Try Premium for ₹0

            About the job

            We're looking for Full Stack Developer Interns to join our team for a 3-month paid internship working on live company projects. This is a great opportunity to gain real-world experience and potentially transition into a full-time role based on performance.

            Requirements:

                Strong knowledge of React, Node.js, and Express.js
                Experience with SQL and MongoDB databases
                Understanding of web development tools such as Git & GitHub (version control), Postman (API testing), and a Basic understanding of RESTful APIs, debugging, and deployment.
                Ability to work independently on real-time projects (this internship is for practical experience, not training)

            What you'll get:

                Work on actual company products, not dummy tasks
                Opportunity to learn in a professional environment
                Stipend provided
                Possibility of a full-time job offer at the end of the internship

            Duration: 3 Months

            Internship Type: Paid

            Location: On Site (Ahmedabad)

            Apply now and gain real project experience that counts.

            Fill this form to apply: https://forms.gle/LGsh8XGRA8CvcfoM7
            Unlock hiring insights on Zeus Artificial Intelligence

            8%-8 Employee growth
            Chart
            Chart with 13 data points.
            The chart has 1 X axis displaying values. Range: 1711411200000 to 1749254400000.
            The chart has 1 Y axis displaying values. Range: 0 to 20.
            End of interactive chart.
            Applicant education level

            79%

            have a Bachelor's Degree
            Applicant seniority level

            73%

            Entry level applicants
            Try Premium for ₹0

            1-month free with 24/7 support. Cancel anytime. We'll remind you 7 days before your trial ends.
            About the company
            Zeus Artificial Intelligence company logo
            Zeus Artificial Intelligence
            365 followers
            Computer Hardware Manufacturing 11-50 employees 12 on LinkedIn

            Advanced cloud services for analysis monitoring and tracking in real time
        """,
        "Output": """
            Full Stack Developer Intern (React + Node.js)
            Zeus Artificial Intelligence
            Location: Ahmedabad
            Type: Paid Internship
            Duration: 3 Months

            About the Role:
            We're looking for Full Stack Developer Interns to join our team for a 3-month paid internship working on live company projects. This is a great opportunity to gain real-world experience and potentially transition into a full-time role based on performance.

            Requirements:
            • Strong knowledge of React, Node.js, and Express.js
            • Experience with SQL and MongoDB databases
            • Understanding of web development tools such as Git & GitHub (version control), Postman (API testing), and a Basic understanding of RESTful APIs, debugging, and deployment
            • Ability to work independently on real-time projects (this internship is for practical experience, not training)

            What You'll Get:
            • Work on actual company products, not dummy tasks
            • Opportunity to learn in a professional environment
            • Stipend provided
            • Possibility of a full-time job offer at the end of the internship

            How to Apply:
            Fill this form to apply: https://forms.gle/LGsh8XGRA8CvcfoM7
        """
    },
    {
        "Raw_Text": """       
        Creative Nuts logo
        Creative Nuts
        Full Stack Developer
        Bengaluru, Karnataka, India · 6 days ago · Over 100 applicants

        Promoted by hirer · No response insights available yet
Full Stack Developer (Leadership Role)
            Creative Nuts
            Location: Bengaluru 
            JobFull Stack Developer (Leadership Role)
            Creative Nuts
            Location: Bengaluru 
            Job Type: Full-Time

            About the Company:
            We are a fast-growing digital agency based in Bengaluru, seeking a skilled and driven Full Stack Developer to join us in a leadership capacity. This is a full-time, on-site role where you'll work closely with cross-functional teams to build and maintain scalable, performance-driven web applications.

            The ideal candidate is not only technically proficient but also strategic, with the ability to lead projects end-to-end, guide junior developers, and contribute to technology choices that align with both client goals and internal strengths.

            Key Responsibilities:
            • Lead the planning, design, and development of complex web applications from the ground up
            • Select and recommend appropriate tech stacks based on client requirements and project goals
            • Mentor and build a high-performing development team by identifying and nurturing key talent
            • Guide and oversee project execution, ensuring delivery timelines, code quality, and performance standards are met
            • Collaborate with UI/UX designers, project managers, and clients to translate business needs into technical solutions
            • Build, integrate, and maintain RESTful APIs and ensure seamless interaction with third-party systems
            • Conduct regular code reviews, maintain documentation, and follow best practices in software development
            • Stay current with emerging technologies and frameworks to continuously improve the tech stack and delivery process

            Job Requirements:
            • Proven ability to manage and execute web development projects independently and in teams
            • Strong leadership skills with a proactive mindset and a collaborative attitude
            • Ability to assess business requirements and translate them into scalable technical architectures
            • Strong decision-making skills for choosing tech stacks and resolving technical bottlenecks

            Qualifications:
            • 2–4 years of hands-on experience as a Full Stack Developer
            • Proficiency in front-end technologies like HTML, CSS, JavaScript, and frameworks such as React.js, Angular, or Vue.js
            • Solid back-end development experience with Node.js, Express, Python, or similar technologies
            • Experience working with relational and NoSQL databases such as MySQL, PostgreSQL, or MongoDB
            • Familiarity with RESTful API architecture, microservices, and system integrations
            • Good understanding of software design patterns, performance optimization, and application security
            • Proficient in Git and version control workflows
            • Excellent problem-solving and debugging skills
            • Strong verbal and written communication skills
            On-site Full-time
            See how you compare to over 100 other applicants. Try Premium for ₹0

        Full Stack Developer
        Creative Nuts · Bengaluru, Karnataka, India (On-site)
        About the job

        Job Title: Full Stack Developer (Leadership Role)

        Location: Bengaluru (On-site)

        Job Type: Full-Time

        Introduction:

        We are a fast-growing digital agency based in Bengaluru, seeking a skilled and driven Full Stack Developer to join us in a leadership capacity. This is a full-time, on-site role where you'll work closely with cross-functional teams to build and maintain scalable, performance-driven web applications.

        The ideal candidate is not only technically proficient but also strategic, with the ability to lead projects end-to-end, guide junior developers, and contribute to technology choices that align with both client goals and internal strengths. If you're someone who thrives in a collaborative, innovation-fo

        Key Responsibilities:

            Lead the planning, design, and development of complex web applications from the ground up.
            Select and recommend appropriate tech stacks based on client requirements and project goals.
            Mentor and build a high-performing development team by identifying and nurturing key talent.
            Guide and oversee project execution, ensuring delivery timelines, code quality, and performance standards are met.
            Collaborate with UI/UX designers, project managers, and clients to translate business needs into technical solutions.
            Build, integrate, and maintain RESTful APIs and ensure seamless interaction with third-party systems.
            Conduct regular code reviews, maintain documentation, and follow best practices in software development.
            Stay current with emerging technologies and frameworks to continuously improve the tech stack and delivery process.

        Job Requirements:

            Proven ability to manage and execute web development projects independently and in teams.
            Strong leadership skills with a proactive mindset and a collaborative attitude.
            Ability to assess business requirements and translate them into scalable technical architectures.
            Strong decision-making skills for choosing tech stacks and resolving technical bottlenecks. 

        Qualifications:

            2–4 years of hands-on experience as a Full Stack Developer.
            Proficiency in front-end technologies like HTML, CSS, JavaScript, and frameworks such as React.js, Angular, or Vue.js.
            Solid back-end development experience with Node.js, Express, Python, or similar technologies.
            Experience working with relational and NoSQL databases such as MySQL, PostgreSQL, or MongoDB.
            Familiarity with RESTful API architecture, microservices, and system integrations.
            Good understanding of software design patterns, performance optimization, and application security.
            Proficient in Git and version control workflows.
            Excellent problem-solving and debugging skills.
            Strong verbal and written communication skills.

        Unlock hiring insights on Creative Nuts

        23%23 Employee growth
        Chart
        Chart with 13 data points.
        The chart has 1 X axis displaying values. Range: 1711411200000 to 1749254400000.
        The chart has 1 Y axis displaying values. Range: 0 to 20.
        End of interactive chart.
        Applicant education level

        38%

        have a Bachelor's Degree
        Applicant seniority level

        79%

        Entry level applicants
        Try Premium for ₹0

        1-month free with 24/7 support. Cancel anytime. We'll remind you 7 days before your trial ends.
        About the company
        Creative Nuts company logo
        Creative Nuts
        5,396 followers
        Advertising Services 11-50 employees 16 on LinkedIn

        We are artisans and craftsmen of beautiful brands and bespoke digital solutions. We apply the term 'design' to nearly everything we do, because quite simply, everyone is creative. Design is what happens when great information coalesces into big ideas, gorgeous brands, and powerful communications.

        We integrate strategic planning, creative innovation, cutting-edge technology, in-house operational proficiency, and intelligent data-driven approaches to present highly engaging communications through relationship- and result-focused initiatives tailored for a brand's target audience.

        We've collaborated with leading brands in Technology & IT, FMCG, Automobiles, Commodity, and Consumer durables. Our track record includes consistently providing solutions that go beyond mere sales outcomes, contributing to the transformation of these brands.
        …

        Show more
        """,
        "Output": """
            Full Stack Developer (Leadership Role)
            Creative Nuts
            Location: Bengaluru 
            JobFull Stack Developer (Leadership Role)
            Creative Nuts
            Location: Bengaluru 
            Job Type: Full-Time

            About the Company:
            We are a fast-growing digital agency based in Bengaluru, seeking a skilled and driven Full Stack Developer to join us in a leadership capacity. This is a full-time, on-site role where you'll work closely with cross-functional teams to build and maintain scalable, performance-driven web applications.

            The ideal candidate is not only technically proficient but also strategic, with the ability to lead projects end-to-end, guide junior developers, and contribute to technology choices that align with both client goals and internal strengths.

            Key Responsibilities:
            • Lead the planning, design, and development of complex web applications from the ground up
            • Select and recommend appropriate tech stacks based on client requirements and project goals
            • Mentor and build a high-performing development team by identifying and nurturing key talent
            • Guide and oversee project execution, ensuring delivery timelines, code quality, and performance standards are met
            • Collaborate with UI/UX designers, project managers, and clients to translate business needs into technical solutions
            • Build, integrate, and maintain RESTful APIs and ensure seamless interaction with third-party systems
            • Conduct regular code reviews, maintain documentation, and follow best practices in software development
            • Stay current with emerging technologies and frameworks to continuously improve the tech stack and delivery process

            Job Requirements:
            • Proven ability to manage and execute web development projects independently and in teams
            • Strong leadership skills with a proactive mindset and a collaborative attitude
            • Ability to assess business requirements and translate them into scalable technical architectures
            • Strong decision-making skills for choosing tech stacks and resolving technical bottlenecks

            Qualifications:
            • 2–4 years of hands-on experience as a Full Stack Developer
            • Proficiency in front-end technologies like HTML, CSS, JavaScript, and frameworks such as React.js, Angular, or Vue.js
            • Solid back-end development experience with Node.js, Express, Python, or similar technologies
            • Experience working with relational and NoSQL databases such as MySQL, PostgreSQL, or MongoDB
            • Familiarity with RESTful API architecture, microservices, and system integrations
            • Good understanding of software design patterns, performance optimization, and application security
            • Proficient in Git and version control workflows
            • Excellent problem-solving and debugging skills
            • Strong verbal and written communication skills
        """
    }
]


prompt = ChatPromptTemplate.from_messages([
    ("system", """
        You are a specialized AI assistant that extracts clean, structured job descriptions from raw LinkedIn job postings and similar sources.

        TASK: Extract only the essential job posting content while removing all noise, metadata, and promotional elements.

        WHAT TO EXTRACT:
        - Job title and basic job information (location, type, duration)
        - Company introduction/about section (if relevant to the role)
        - Main job description and responsibilities
        - Requirements, qualifications, and skills needed
        - What the company offers (benefits, compensation, growth opportunities)
        - Application process or next steps (if mentioned)

        WHAT TO REMOVE:
        - LinkedIn interface elements (logos, follower counts, application statistics)
        - Promotional text ("Try Premium for ₹0", "See how you compare", etc.)
        - Charts, graphs, and statistical data
        - Company growth metrics and hiring insights
        - Generic LinkedIn features and advertisements
        - Hashtags and social media elements
        - Redundant company information not directly related to the job
        - Navigation elements and UI text

        OUTPUT FORMAT:
        Provide a clean, well-structured text that preserves:
        - Original formatting and bullet points for readability
        - Logical flow from job overview to requirements to benefits
        - Professional tone and essential information only
        - Proper spacing and hierarchy of information

        QUALITY GUIDELINES:
        - Maintain the professional tone of the original posting
        - Keep all technical requirements and skill specifications
        - Preserve important details like experience levels, location, and job type
        - Ensure the output reads naturally and professionally
        - Remove any fragmented or incomplete sentences from parsing errors

        EXAMPLES:

        Example 1:
        Input: Zeus Artificial Intelligence logo Zeus Artificial Intelligence Full Stack Developer Intern (React + Node.js) Ahmedabad, Gujarat, India · 5 hours ago · Over 100 people clicked apply Promoted by hirer · Responses managed off LinkedIn On-site Full-time Curious where you stand? See how you compare to over 100 others who clicked apply. Try Premium for ₹0 About the job We're looking for Full Stack Developer Interns to join our team for a 3-month paid internship working on live company projects...

        Output: Full Stack Developer Intern (React + Node.js) Zeus Artificial Intelligence Location: On Site (Ahmedabad) Type: Paid Internship Duration: 3 Months About the Role: We're looking for Full Stack Developer Interns to join our team for a 3-month paid internship working on live company projects...

        Example 2:
        Input: Creative Nuts logo Creative Nuts Full Stack Developer Bengaluru, Karnataka, India · 6 days ago · Over 100 applicants Promoted by hirer · No response insights available yet On-site Full-time See how you compare to over 100 other applicants. Try Premium for ₹0...

        Output: Full Stack Developer (Leadership Role) Creative Nuts Location: Bengaluru (On-site) Job Type: Full-Time About the Company: We are a fast-growing digital agency based in Bengaluru, seeking a skilled and driven Full Stack Developer...

        Now extract the clean job description from the following raw text:
    """),
    ("human", "{Raw_Text}")
])

# prompt2 = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant that extracts structured JSON data from unstructured job descriptions."),
#     ("human", """
#                 Extract all relevant information from the following job description into a JSON object. 
#                 Return key-value pairs where keys are the section titles or categories, and values are the content (lists or strings).
#                 Do not invent information; only extract from the text.
#                 Job Description:
#                 \"\"\"{text}\"\"\"
#             """)
# ])

prompt2 = ChatPromptTemplate.from_messages([
    ("system", "You are a strict data extractor that only returns valid, parsable JSON. Do not include explanations, markdown, or additional text."),
    ("human", """
        Extract all relevant structured information from the following unstructured job description.

        ➡️ Return a single valid JSON object.
        ➡️ All field values must be strings, arrays, or nested JSON.
        ➡️ Escape all necessary characters (e.g., quotes inside text).
        ➡️ Do NOT add any extra commentary or markdown.
        ➡️ Only extract what is present in the job description.

        --- EXAMPLE 1 ---

        Job Description:
        \"\"\"
        We are hiring a Backend Engineer at ExampleCorp.

        Location: Remote
        Type: Full-time
        Tech: Python, Django, PostgreSQL, AWS

        Responsibilities:
        - Build scalable backend services
        - Maintain existing APIs
        - Collaborate with frontend and devops teams

        Requirements:
        - 3+ years backend experience
        - Strong Python skills
        - Experience with REST APIs
        \"\"\"

        Expected Output:
        {
        "Job Title": "Backend Engineer",
        "Company": "ExampleCorp",
        "Location": "Remote",
        "Type": "Full-time",
        "Technologies": ["Python", "Django", "PostgreSQL", "AWS"],
        "Responsibilities": [
            "Build scalable backend services",
            "Maintain existing APIs",
            "Collaborate with frontend and devops teams"
        ],
        "Requirements": [
            "3+ years backend experience",
            "Strong Python skills",
            "Experience with REST APIs"
        ]
        }

        --- EXAMPLE 2 ---

        Job Description:
        \"\"\"
        Full Stack Developer (Leadership Role)
        Creative Nuts
        Location: Bengaluru 
        Job Type: Full-Time

        About the Company:
        We are a fast-growing digital agency based in Bengaluru, seeking a skilled and driven Full Stack Developer to join us in a leadership capacity. This is a full-time, on-site role where you'll work closely with cross-functional teams to build and maintain scalable, performance-driven web applications.

        The ideal candidate is not only technically proficient but also strategic, with the ability to lead projects end-to-end, guide junior developers, and contribute to technology choices that align with both client goals and internal strengths.

        Key Responsibilities:
        • Lead the planning, design, and development of complex web applications from the ground up
        • Select and recommend appropriate tech stacks based on client requirements and project goals
        • Mentor and build a high-performing development team by identifying and nurturing key talent
        • Guide and oversee project execution, ensuring delivery timelines, code quality, and performance standards are met
        • Collaborate with UI/UX designers, project managers, and clients to translate business needs into technical solutions
        • Build, integrate, and maintain RESTful APIs and ensure seamless interaction with third-party systems
        • Conduct regular code reviews, maintain documentation, and follow best practices in software development
        • Stay current with emerging technologies and frameworks to continuously improve the tech stack and delivery process

        Job Requirements:
        • Proven ability to manage and execute web development projects independently and in teams
        • Strong leadership skills with a proactive mindset and a collaborative attitude
        • Ability to assess business requirements and translate them into scalable technical architectures
        • Strong decision-making skills for choosing tech stacks and resolving technical bottlenecks

        Qualifications:
        • 2–4 years of hands-on experience as a Full Stack Developer
        • Proficiency in front-end technologies like HTML, CSS, JavaScript, and frameworks such as React.js, Angular, or Vue.js
        • Solid back-end development experience with Node.js, Express, Python, or similar technologies
        • Experience working with relational and NoSQL databases such as MySQL, PostgreSQL, or MongoDB
        • Familiarity with RESTful API architecture, microservices, and system integrations
        • Good understanding of software design patterns, performance optimization, and application security
        • Proficient in Git and version control workflows
        • Excellent problem-solving and debugging skills
        • Strong verbal and written communication skills
        \"\"\"

        Expected Output:
        {
        "Job Title": "Full Stack Developer (Leadership Role)",
        "Company": "Creative Nuts",
        "Location": "Bengaluru",
        "Type": "Full-Time",
        "Work Mode": "On-site",
        "About the Company": "We are a fast-growing digital agency based in Bengaluru, seeking a skilled and driven Full Stack Developer to join us in a leadership capacity. This is a full-time, on-site role where you'll work closely with cross-functional teams to build and maintain scalable, performance-driven web applications.",
        "Responsibilities": [
            "Lead the planning, design, and development of complex web applications from the ground up",
            "Select and recommend appropriate tech stacks based on client requirements and project goals",
            "Mentor and build a high-performing development team by identifying and nurturing key talent",
            "Guide and oversee project execution, ensuring delivery timelines, code quality, and performance standards are met",
            "Collaborate with UI/UX designers, project managers, and clients to translate business needs into technical solutions",
            "Build, integrate, and maintain RESTful APIs and ensure seamless interaction with third-party systems",
            "Conduct regular code reviews, maintain documentation, and follow best practices in software development",
            "Stay current with emerging technologies and frameworks to continuously improve the tech stack and delivery process"
        ],
        "Requirements": [
            "Proven ability to manage and execute web development projects independently and in teams",
            "Strong leadership skills with a proactive mindset and a collaborative attitude",
            "Ability to assess business requirements and translate them into scalable technical architectures",
            "Strong decision-making skills for choosing tech stacks and resolving technical bottlenecks"
        ],
        "Qualifications": [
            "2–4 years of hands-on experience as a Full Stack Developer",
            "Proficiency in front-end technologies like HTML, CSS, JavaScript, and frameworks such as React.js, Angular, or Vue.js",
            "Solid back-end development experience with Node.js, Express, Python, or similar technologies",
            "Experience working with relational and NoSQL databases such as MySQL, PostgreSQL, or MongoDB",
            "Familiarity with RESTful API architecture, microservices, and system integrations",
            "Good understanding of software design patterns, performance optimization, and application security",
            "Proficient in Git and version control workflows",
            "Excellent problem-solving and debugging skills",
            "Strong verbal and written communication skills"
        ]
        }

        --- YOUR TURN ---
        Extract structured JSON from the following job description:

        \"\"\"{text}\"\"\"
    """)
])
