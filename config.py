"""Portfolio website configuration"""

SITE_CONFIG = {
    'title': 'Md Aslam Hossin | Senior Android Engineer',
    'description': 'Senior Android Engineer in Tokyo/Kanagawa with 9+ years of experience in Kotlin, Jetpack Compose, Mobile Architecture, and Applied AI Developer Tooling.',
    'author': 'Md Aslam Hossin',
    'title_short': 'Senior Android Engineer | Mobile Architecture & Applied AI',
    'subtitle': 'Senior Android Engineer · Mobile Architecture, Jetpack Compose & Applied AI Tooling',
    'location': 'Kawasaki, Kanagawa, Japan',
    'github_username': 'aslamhossin',
    'github_url': 'https://github.com/aslamhossin',
    'portfolio_url': 'https://aslamhossin.github.io',
    'email': 'aslam.iit.ju41@gmail.com',
    'social_links': {
        'github': 'https://github.com/aslamhossin',
        'linkedin': 'https://linkedin.com/in/aslamhossin',
        'medium': 'https://medium.com/@aslam.iit.ju41',
    },
    'summary': (
        'Senior Android Engineer based in Japan with 9+ years of experience building and modernizing '
        'consumer Android apps across e-commerce, digital payments, news aggregation, and live sports media '
        '(serving 50M+ users). Focused on Kotlin, incremental XML-to-Compose migrations, multi-module Gradle '
        'and CI/CD release infrastructure, and agentic developer workflows (Claude Code, Codex, MCP, JetBrains Koog, Python FastAPI).'
    ),
    'projects': [
        {
            'title': 'SizzleSense AI',
            'company': 'Open Source',
            'date': '2026',
            'description': 'Full-stack Applied AI system pairing an Android client (Kotlin 2.4, AGP 9.4, Jetpack Compose, Navigation 3, strict MVI, Dagger Hilt, Media3 ExoPlayer RTSP) with a Python FastAPI backend and a 4-stage Google Gemini 3 multimodal pipeline.',
            'technologies': ['Kotlin 2.4', 'Jetpack Compose', 'MVI', 'Dagger Hilt', 'Media3 RTSP', 'Python FastAPI', 'Gemini API', 'EvalBench'],
            'metrics': '10-session EvalBench suite • 22 Pytest tests & GitHub Actions CI',
            'github_url': 'https://github.com/aslamhossin/sizzlesense-ai',
        },
        {
            'title': 'KMP-Template',
            'company': 'Open Source',
            'date': '2024',
            'description': 'Contributed to an open-source Kotlin Multiplatform Mobile project template implementing a shared module architecture across Android and iOS.',
            'technologies': ['Kotlin Multiplatform', 'Coroutines', 'Flow', 'Clean Architecture', 'Android', 'iOS'],
            'metrics': '70% shared business & data logic across Android and iOS',
            'github_url': 'https://github.com/ml-opensource/KMP-Template',
        },
        {
            'title': 'Enterprise Compose Migration & Shared UI Core',
            'company': 'Large-Scale E-Commerce Platform (Tokyo)',
            'date': 'Oct 2024 – Present',
            'description': 'Co-designed incremental XML-to-Compose migration architecture, shared MVI ViewModel contract, Compose-to-RecyclerView bridge, Glide-to-Coil abstraction, and Media3/ExoPlayer shared video player pool.',
            'technologies': ['Kotlin', 'Jetpack Compose', 'MVI', 'Media3/ExoPlayer', 'Benchmark APIs', 'JetBrains Koog', 'MCP'],
            'metrics': '50M+ users • Adopted across multiple Android feature squads',
        },
        {
            'title': 'Fintech P2P Messaging & Multi-Module Android Platform',
            'company': 'Global Digital Consultancy (Tokyo)',
            'date': '2018 – 2024',
            'description': 'Led 5 Android engineers building peer-to-peer chat and payment messaging with Sendbird, Room, and WorkManager, plus shared libraries and Bitrise CI/CD automation inside a large multi-module codebase.',
            'technologies': ['Kotlin', 'Coroutines', 'Sendbird', 'Room', 'WorkManager', 'Multi-Module Gradle', 'Bitrise'],
            'metrics': 'Led 5 Android engineers • Large-scale QR payments & messaging',
        },
        {
            'title': 'Mobility App Java-to-Kotlin Migration & Health Visualizations',
            'company': 'Global Digital Consultancy',
            'date': '2018 – 2024',
            'description': 'Migrated roughly 60% of a legacy Java ride-dispatch codebase to Kotlin while delivering real-time GPS routing, and built interactive MotionLayout health visualizations recognized by the Good Design Award 2019.',
            'technologies': ['Kotlin', 'Google Maps SDK', 'Location Services', 'MotionLayout', 'Android Profiler'],
            'metrics': '60% Java-to-Kotlin migration • 30% reduction in runtime crashes • Good Design Award 2019',
        },
        {
            'title': 'FootyLight & Bangla Papers (Live Sports Media & News Aggregation)',
            'company': 'Media & Sports Startup',
            'date': '2016 – 2018',
            'description': 'Built FootyLight (personalized football news feeds, Wowza live video streaming, match highlights, real-time commentary, head-to-head stats) and Bangla Papers (Android news reader + Java Servlet publisher ingestion APIs).',
            'technologies': ['Android SDK', 'Java', 'Wowza Streaming', 'Java Servlets', 'REST APIs', 'LeakCanary'],
            'metrics': 'Live streaming + licensed publisher news aggregation',
        },
    ],
    'work_experience': [
        {
            'position': 'Senior Android Engineer (Contract)',
            'company': 'Large-Scale E-Commerce & Tech Platform',
            'location': 'Tokyo, Japan',
            'date': 'Oct 2024 – Present',
            'description': 'Android platform modernization, AI developer tooling, and commerce feature delivery at 50M+ user scale.',
            'highlights': [
                'Co-designed the Jetpack Compose migration architecture for a long-lived XML app, building a shared MVI ViewModel contract, Compose-to-RecyclerView bridge, and reusable screen templates adopted across Android teams.',
                'Built a shared internal Compose UI core module (theming, typography, buttons, and a Glide-to-Coil image loader abstraction) and supported migrations through design docs, sample code, and PR reviews.',
                'Built an IntelliJ IDEA bug-fixing plugin using JetBrains Koog and set up Claude Code and Codex MCP workflows to automate spec checks, PR reviews, and QA test planning.',
                'Reduced video feed startup latency with Media3/ExoPlayer preloading and a shared player pool validated via Android Benchmark APIs and Compose stability analysis (@Stable, @Immutable).',
                'Diagnosed and fixed lifecycle memory leaks and main-thread UI freezes with Android Profiler, LeakCanary, and JUnit 5/MockK/Turbine tests; managed two major releases and a production hotfix.',
            ]
        },
        {
            'position': 'Senior Mobile Engineer & Android Team Lead',
            'company': 'Global Digital Consultancy',
            'location': 'Tokyo, Japan / Dhaka, Bangladesh',
            'date': 'Nov 2018 – Sep 2024',
            'description': 'Android engineering leadership across large-scale fintech payments, mobility, and digital health products.',
            'highlights': [
                'Led a team of 5 Android engineers on a major Japanese fintech app during the final two years, owning sprint planning, architecture and code reviews, and 1:1 mentoring.',
                'Built peer-to-peer payment messaging with Sendbird, Room, and WorkManager, covering local persistence, offline sync, and retry recovery.',
                'Maintained shared libraries in a multi-module Android codebase and configured Gradle build logic, Bitrise CI pipelines, and Firebase App Distribution for repeatable QA and Play Store delivery.',
                'Led the Kotlin migration of roughly 60% of legacy Java code on a mobility app, reducing runtime crashes by 30% while delivering real-time GPS routing.',
                'Built custom MotionLayout data visualizations for a consumer genetics app (Good Design Award 2019).',
            ]
        },
        {
            'position': 'Software Developer | Android Engineer',
            'company': 'Media & Sports Startup',
            'location': 'Dhaka, Bangladesh',
            'date': 'Sep 2016 – Oct 2018',
            'description': 'Owned Android engineering and backend news ingestion APIs in a 10-person product team.',
            'highlights': [
                'Built FootyLight, a football media Android app delivering personalized football news feeds, live video streaming, match highlights, real-time commentary, and team head-to-head statistics.',
                'Developed the Android client and Java Servlet backend APIs for Bangla Papers, ingesting and serving articles from licensed Bangladeshi news publishers.',
                'Worked on the Wowza live streaming engine and profiled playback recovery and memory usage with Android Profiler and LeakCanary.',
            ]
        },
    ],
    'education': [
        {
            'degree': 'M.Sc. in Information Technology',
            'institution': 'Jahangirnagar University, Dhaka, Bangladesh',
            'date': '2016 – 2017',
        },
        {
            'degree': 'B.Sc. in Information Technology',
            'institution': 'Jahangirnagar University, Dhaka, Bangladesh',
            'date': '2011 – 2016',
        },
        {
            'degree': 'Kotlin Coroutines and Flow for Android Development',
            'institution': 'Udemy',
            'date': 'Dec 2024',
            'certificate': 'UC-8be9ea26-4fbe-4fc9-90b3-deb65bc0f552',
        },
    ],
    'skills': {
        'Android & Mobile': ['Kotlin', 'Java', 'Android SDK', 'Jetpack Compose', 'Android Views (XML)', 'Coroutines', 'Flow', 'Kotlin Multiplatform (KMP)', 'Media3/ExoPlayer', 'Room', 'WorkManager'],
        'Architecture & Testing': ['MVI', 'MVVM', 'Clean Architecture', 'Multi-Module Gradle', 'Dagger Hilt', 'REST APIs', 'Java Servlets', 'JUnit 5', 'MockK', 'Turbine', 'kotlinx-coroutines-test', 'TDD'],
        'AI Engineering & Developer Tooling': ['Claude Code', 'Codex Workflows', 'Model Context Protocol (MCP)', 'JetBrains Koog', 'IntelliJ IDEA Plugin SDK', 'Python FastAPI', 'Pydantic v2', 'Google Gemini API', 'EvalBench', 'Pytest'],
        'CI/CD, Performance & Release': ['Gradle', 'R8/ProGuard', 'Bitrise', 'GitHub Actions', 'Firebase App Distribution', 'Crashlytics', 'Android Profiler', 'LeakCanary', 'Benchmark APIs', 'Git'],
        'Languages': ['English (Professional Working Proficiency)', 'Japanese (Basic)'],
    },
    'blog': {
        'platform': 'Medium',
        'url': 'https://medium.com/@aslam.iit.ju41',
        'description': 'Technical articles on Kotlin, Jetpack Compose migrations, MVI state management, Android performance profiling, and AI-assisted engineering workflows.',
    },
}
