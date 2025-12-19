"""Portfolio website configuration"""

SITE_CONFIG = {
    'title': 'Md Aslam Hossin - Android Engineer',
    'description': 'Android Engineer with 9+ years of experience in mobile development',
    'author': 'Md Aslam Hossin',
    'title_short': 'Android Engineer',
    'location': 'Kanagawa, Japan',
    'phone': '070-8586-1148',
    'github_username': 'aslamhossin',
    'github_url': 'https://github.com/aslamhossin',
    'portfolio_url': 'https://aslamhossin.github.io',
    'email': 'aslam.iit.ju41@gmail.com',
    'social_links': {
        'github': 'https://github.com/aslamhossin',
        'linkedin': 'https://linkedin.com/in/aslamhossin',
    },
    'projects': [
        {
            'title': 'Rakuten Ichiba (Current)',
            'description': 'Feature development for Rakuten Ichiba storefront apps serving multiple retail business lines. Integrated Modiface SDK for AR virtual try-on, refactored core features with Clean Architecture.',
            'technologies': ['Kotlin', 'Jetpack Compose', 'MVVM', 'Redux', 'TDD'],
            'role': 'Application Engineer (Android)',
            'company': 'Rakuten',
            'date': 'Oct 2024 - Present',
        },
        {
            'title': 'PayPay Fintech Integration',
            'description': 'Integrated Sendbird SDK for secure chat, implemented network security for data transmission, optimized memory usage for background processing.',
            'technologies': ['Kotlin', 'Sendbird SDK', 'Firebase', 'TDD', 'Network Security'],
            'role': 'Senior Mobile Engineer',
            'company': 'Monstarlab',
            'date': '2018-2024',
        },
        {
            'title': 'TAXA 4x35 - Ride Sharing App',
            'description': 'Led Java-to-Kotlin migration (60% conversion), boosted performance and reduced crashes by 30%. Integrated Google Maps SDK and location services for real-time tracking.',
            'technologies': ['Kotlin', 'Java', 'Google Maps', 'Coroutines', 'Performance Optimization'],
            'role': 'Senior Mobile Engineer',
            'company': 'Monstarlab',
            'date': '2018-2024',
        },
        {
            'title': 'GeneLife 3.0',
            'description': 'Built genome chart visualizations in Compose with complex animations. Good Design Award 2019 winner.',
            'technologies': ['Kotlin', 'Jetpack Compose', 'Animations', 'Data Visualization'],
            'role': 'Senior Mobile Engineer',
            'company': 'Monstarlab',
            'date': '2018-2024',
        },
    ],
    'work_experience': [
        {
            'position': 'Application Engineer (Android)',
            'company': 'Rakuten (via Robert Walters Japan KK)',
            'location': 'Tokyo, Japan',
            'date': 'Oct 2024 - Present',
            'description': 'Feature development for Rakuten Ichiba storefront apps',
            'highlights': [
                'Identified and refactored core feature with technical debt; designed Clean Architecture solution',
                'Integrated Modiface SDK for AR virtual try-on features with optimized performance',
                'Translate Figma designs into production code using Compose and View system',
                'Implement coroutines/Flow pipelines and REST API integrations with Retrofit',
                'Practice TDD with JUnit5 and MockK for robustness',
            ]
        },
        {
            'position': 'Senior Mobile Engineer',
            'company': 'Monstarlab',
            'location': 'Dhaka, Bangladesh',
            'date': 'Nov 2018 - Sep 2024',
            'description': 'Delivered projects for international clients across ride-sharing, fintech, health, and retail',
            'highlights': [
                'PayPay (Japan): Integrated Sendbird SDK, reviewed network security, practiced TDD',
                'TAXA 4x35 (Denmark): Led Java-to-Kotlin migration (60% conversion), reduced crashes by 30%',
                'GeneLife 3.0 (Japan): Built genome visualizations with complex animations - Good Design Award 2019 winner',
                'Mitsukoshi Isetan (Japan): Launched remote video chat for personal shopping - $276M revenue FY2020',
                'Applied Kotlin coroutines and Flow across projects; participated in agile ceremonies',
            ]
        },
        {
            'position': 'Software Developer',
            'company': 'DODOCK LLC',
            'location': 'Dhaka, Bangladesh',
            'date': 'Sep 2016 - Oct 2018',
            'description': 'Developed Android app for media streaming platform',
            'highlights': [
                'Integrated Wowza SDK for live streaming with memory optimization',
                'Profiled with Android Studio Profiler and LeakCanary',
                'Built REST/JSON integrations for authentication and user management',
            ]
        },
    ],
    'education': [
        {
            'degree': 'Master of Science in Information Technology',
            'institution': 'Jahangirnagar University',
            'date': '2016 - 2017',
        },
        {
            'degree': 'Bachelor of Science in Information Technology',
            'institution': 'Jahangirnagar University',
            'date': '2011 - 2016',
        },
        {
            'degree': 'Kotlin Coroutines and Flow for Android Development',
            'institution': 'Udemy',
            'date': '2023',
            'certificate': 'UC-8be9ea26-4fbe-4fc9-90b3-deb65bc0f552',
        },
    ],
    'projects': [
        {
            'title': 'Portfolio Website',
            'description': 'Personal portfolio website built with Python',
            'technologies': ['Python', 'Jinja2', 'GitHub Pages'],
            'github_url': 'https://github.com/aslamhossin/aslamhossin.github.io',
            'demo_url': 'https://aslamhossin.github.io',
        },
    ],
    'skills': {
        'Android': ['Kotlin', 'Java', 'Jetpack Compose', 'View System', 'Coroutines', 'Flow', 'Room', 'WorkManager', 'Navigation', 'Lifecycle'],
        'Architecture': ['MVVM', 'MVI', 'Redux', 'Clean Architecture', 'DI (Hilt/Koin)', 'OOP'],
        'SDK Integration': ['Modiface', 'Sendbird', 'Firebase', 'Wowza', 'Google Maps', 'Location Services'],
        'Testing & CI/CD': ['TDD', 'JUnit5', 'MockK', 'Bitrise', 'GitHub Actions', 'Crashlytics'],
        'Tools': ['Android Studio', 'Gradle', 'Git', 'Profiler', 'LeakCanary', 'Jira', 'Figma'],
        'Languages': ['Kotlin', 'Java', 'Business English'],
    },
}
