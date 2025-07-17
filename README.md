# Rehab-VR-

<div align="center">
  <img src="https://img.freepik.com/premium-photo/fun-illustration-doctor-with-vr-helmet_183364-72320.jpg?ga=GA1.1.1731687701.1726727628&semt=ais_hybrid" alt="Rehab-VR Logo" width="200"/>
  
  ![Unity](https://img.shields.io/badge/Unity-2023.3%2B-black?logo=unity)
  ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
  ![Flask](https://img.shields.io/badge/Flask-2.3%2B-green?logo=flask)
  ![Firebase](https://img.shields.io/badge/Firebase-Firestore-orange?logo=firebase)
  ![Oculus](https://img.shields.io/badge/Oculus-Quest-blue?logo=oculus)
  ![License](https://img.shields.io/badge/License-MIT-green)
</div>

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Exercises](#supported-exercises)
- [Architecture](#architecture)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## 🎯 Overview

Rehab-VR- is a cutting-edge virtual reality rehabilitation platform that combines Unity VR development with a robust Python Flask backend and Firebase cloud database. Designed specifically for Oculus Quest devices, our platform provides immersive, data-driven rehabilitation experiences that bridge the gap between traditional physical therapy and modern technology.

### Technology Stack
- **Frontend:** Unity 2023.3+ with Oculus Integration SDK
- **Backend:** Python Flask RESTful API
- **Database:** Firebase Firestore (real-time NoSQL)
- **Authentication:** Firebase Auth
- **Storage:** Firebase Storage for media files
- **VR Platform:** Oculus Quest 2/3/Pro (primary focus)

### Key Benefits
- **Seamless VR Experience:** Optimized for Oculus Quest devices with native hand tracking
- **Real-time Data Sync:** Firebase integration ensures instant progress updates
- **Scalable Architecture:** Flask backend handles multiple concurrent VR sessions
- **Cloud-first Design:** All data securely stored and accessible from anywhere
- **Cross-platform Backend:** Python Flask API accessible from multiple VR platforms

## ✨ Features

### 🎮 Immersive VR Exercises
- **Motor Function Recovery:** Hand, arm, and leg movement exercises
- **Balance and Coordination:** Interactive balance challenges with safety features
- **Cognitive Rehabilitation:** Memory, attention, and problem-solving activities
- **Range of Motion:** Guided stretching and flexibility exercises
- **Strength Training:** Resistance-based exercises adapted for VR

### 🎯 Customizable Therapy Plans
- **Patient Assessment Tools:** Initial evaluation and ongoing assessments
- **Adaptive Difficulty:** Automatic adjustment based on performance
- **Multi-Modal Exercises:** Combination of physical, cognitive, and sensory activities
- **Session Scheduling:** Automated reminders and session planning
- **Goal Setting:** Personalized targets and milestone tracking

### 📊 Progress Tracking
- **Real-Time Analytics:** Live performance metrics during exercises
- **Historical Data:** Comprehensive progress reports and trends
- **Export Capabilities:** Data export for integration with medical records
- **Comparative Analysis:** Performance benchmarking against recovery standards
- **Visual Dashboards:** Easy-to-understand charts and graphs

### 🖥️ User-Friendly Interface
- **Intuitive Navigation:** Simple menu systems and clear instructions
- **Accessibility Features:** Support for users with disabilities
- **Multi-Language Support:** Localization for different regions
- **Voice Commands:** Hands-free operation capabilities
- **Customizable UI:** Adjustable text size, contrast, and color schemes

### 🔧 Multi-Platform Support
- **Primary Platform:** Oculus Quest 2/3/Pro (Optimized)
- **Oculus Integration:** Native hand tracking, haptic feedback, spatial audio
- **Future Support:** Meta Quest Pro, Quest 3S
- **Backend Compatibility:** Any device capable of HTTP requests to Flask API

## 💻 System Requirements

### Unity VR Client (Oculus Quest)
- **Device:** Oculus Quest 2/3/Pro
- **OS:** Android-based Oculus OS
- **Storage:** 2 GB available space on headset
- **Network:** Wi-Fi connection for cloud sync
- **Oculus Software:** Latest Oculus software version

### Development Environment
- **OS:** Windows 10/11 64-bit (recommended) / macOS 10.15+ / Linux Ubuntu 18.04+
- **Unity:** Unity 2023.3.0f1 or later
- **Python:** Python 3.8+
- **IDE:** Visual Studio Code, PyCharm, or Unity Editor
- **Git:** For version control

### Backend Server Requirements
- **Python:** 3.8+ with Flask 2.3+
- **Database:** Firebase project with Firestore enabled
- **RAM:** 4 GB minimum, 8 GB recommended
- **Storage:** 1 GB for application files
- **Network:** Stable internet connection for Firebase

### Firebase Setup
- **Firestore:** Database for user data and progress tracking
- **Firebase Auth:** User authentication and session management
- **Firebase Storage:** Media files (exercise videos, avatars)
- **Firebase Functions:** Optional for serverless operations

## 🚀 Installation

### Prerequisites
1. **Firebase Project Setup:**
   ```bash
   # Create a new Firebase project at https://console.firebase.google.com
   # Enable Firestore Database
   # Enable Authentication (Email/Password)
   # Enable Storage
   # Download service account key (firebase-admin-key.json)
   ```

2. **Python Environment:**
   ```bash
   # Create virtual environment
   python -m venv rehab-vr-env
   source rehab-vr-env/bin/activate  # On Windows: rehab-vr-env\Scripts\activate
   ```

### Backend Setup (Flask + Firebase)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/INDRESAN/Rehab-VR-.git
   cd Rehab-VR-
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Firebase:**
   ```bash
   # Place your firebase-admin-key.json in the backend/config/ directory
   cp path/to/firebase-admin-key.json backend/config/
   
   # Set environment variables
   export FIREBASE_PROJECT_ID="your-project-id"
   export FIREBASE_STORAGE_BUCKET="your-project-id.appspot.com"
   ```

4. **Run the Flask server:**
   ```bash
   cd backend
   python app.py
   # Server will start on http://localhost:5000
   ```

### Unity VR Client Setup
1. **Unity Installation:**
   - Install Unity Hub and Unity 2023.3.0f1+
   - Add Android Build Support module
   - Install Oculus Integration SDK

2. **Project Setup:**
   ```bash
   # Open Unity Hub
   # Add Project → Select the 'unity-client' folder
   # Open the project in Unity
   ```

3. **Configure Oculus Integration:**
   - Import Oculus Integration package from Asset Store
   - Configure XR settings (Edit → Project Settings → XR Plug-in Management)
   - Enable Oculus provider
   - Set up hand tracking in Oculus settings

4. **API Configuration:**
   ```csharp
   // In Assets/Scripts/Config/APIConfig.cs
   public class APIConfig
   {
       public static string BASE_URL = "http://localhost:5000/api";
       public static string FIREBASE_CONFIG = "your-firebase-config";
   }
   ```

### Quick Deploy (Development)
```bash
# Terminal 1: Start Flask backend
cd backend
python app.py

# Terminal 2: Build and deploy to Oculus
cd unity-client
# Build via Unity Editor → File → Build Settings → Android → Build and Run
```

### Docker Deployment (Production)
```bash
# Build and run backend container
docker build -t rehab-vr-backend ./backend
docker run -p 5000:5000 -e FIREBASE_PROJECT_ID="your-id" rehab-vr-backend

# Unity client must be built separately and sideloaded to Oculus devices
```

## 🎮 Usage

### Getting Started
1. **Launch the Application:**
   - Put on your VR headset
   - Start Rehab-VR- from your VR home environment
   - Or launch from desktop and put on headset when prompted

2. **Initial Setup:**
   - Create a user profile or log in with existing credentials
   - Complete the initial assessment questionnaire
   - Calibrate your play space and controller settings
   - Set up safety boundaries

3. **Selecting Exercises:**
   - Browse the exercise library by category or difficulty
   - Review exercise descriptions and objectives
   - Select recommended exercises based on your therapy plan
   - Start with tutorial mode for new exercises

4. **During Exercise:**
   - Follow the virtual instructor's guidance
   - Pay attention to form correction prompts
   - Take breaks as needed (automatic reminders included)
   - Use the help system if you encounter difficulties

5. **Post-Session:**
   - Review your performance summary
   - Check progress toward your goals
   - Schedule your next session
   - Share results with your healthcare provider

### For Healthcare Providers
1. **Therapist Dashboard:**
   - Access patient management interface
   - Create and modify treatment plans
   - Monitor patient progress across multiple sessions
   - Generate reports for clinical documentation

2. **Remote Monitoring:**
   - View real-time session data
   - Provide virtual coaching and support
   - Adjust difficulty levels remotely
   - Schedule virtual consultations

## 🏃‍♂️ Supported Exercises

### Physical Rehabilitation
- **Upper Extremity:**
  - Shoulder flexion/extension
  - Elbow range of motion
  - Wrist strengthening
  - Fine motor control tasks

- **Lower Extremity:**
  - Hip mobility exercises
  - Knee strengthening
  - Ankle flexibility
  - Gait training simulations

- **Balance & Coordination:**
  - Static balance challenges
  - Dynamic balance training
  - Proprioception exercises
  - Fall prevention activities

### Cognitive Rehabilitation
- **Memory Training:**
  - Working memory exercises
  - Spatial memory tasks
  - Sequence learning
  - Recognition training

- **Attention & Focus:**
  - Selective attention tasks
  - Divided attention exercises
  - Sustained attention training
  - Processing speed activities

## 🏗️ Architecture

### System Overview
```
┌─────────────────────────────────────────────────────────────────┐
│                     Oculus Quest VR Client                     │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  │   Unity UI      │    │  Exercise Logic │    │ Oculus SDK      │
│  │                 │    │                 │    │                 │
│  │ • Menu Systems  │    │ • VR Exercises  │    │ • Hand Tracking │
│  │ • Progress View │    │ • Physics Engine│    │ • Haptic Feed   │
│  │ • Settings      │    │ • 3D Rendering  │    │ • Spatial Audio │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘
└─────────────────────────────────────────────────────────────────┘
                                   │
                              HTTP/HTTPS
                                   │
┌─────────────────────────────────────────────────────────────────┐
│                    Python Flask Backend                        │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  │   REST API      │    │  Business Logic │    │ Firebase Client │
│  │                 │    │                 │    │                 │
│  │ • User Auth     │    │ • Exercise Mgmt │    │ • Firestore DB  │
│  │ • Progress API  │    │ • Progress Track│    │ • Auth Service  │
│  │ • Exercise API  │    │ • Data Analytics│    │ • Storage API   │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘
└─────────────────────────────────────────────────────────────────┘
                                   │
                              Firebase API
                                   │
┌─────────────────────────────────────────────────────────────────┐
│                    Firebase Services                           │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  │   Firestore     │    │  Authentication │    │   Storage       │
│  │                 │    │                 │    │                 │
│  │ • User Profiles │    │ • JWT Tokens    │    │ • Media Files   │
│  │ • Progress Data │    │ • Session Mgmt  │    │ • Avatars       │
│  │ • Exercise Meta │    │ • Role-based    │    │ • Backups       │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘
└─────────────────────────────────────────────────────────────────┘
```

### Key Components

#### Unity VR Client
- **ExerciseManager.cs:** Handles exercise selection, progression, and VR interactions
- **NetworkManager.cs:** Manages HTTP requests to Flask backend
- **OculusIntegration.cs:** Interfaces with Oculus SDK for hand tracking and haptics
- **ProgressTracker.cs:** Local progress caching and sync with backend
- **UIManager.cs:** VR UI system with Oculus-optimized interactions

#### Flask Backend
- **app.py:** Main Flask application and routing
- **auth.py:** Firebase authentication middleware
- **models.py:** Data models for users, exercises, and progress
- **database.py:** Firebase Firestore operations
- **analytics.py:** Progress analysis and reporting

#### Firebase Services
- **Firestore Collections:**
  - `users/` - User profiles and preferences
  - `exercises/` - Exercise metadata and configurations
  - `progress/` - Session data and performance metrics
  - `therapists/` - Healthcare provider accounts

## 📚 API Documentation

### Flask Backend Endpoints

#### Authentication
```python
# POST /api/auth/register
{
    "email": "user@example.com",
    "password": "password123",
    "user_type": "patient"  # or "therapist"
}

# POST /api/auth/login
{
    "email": "user@example.com",
    "password": "password123"
}

# Response
{
    "token": "firebase_jwt_token",
    "user_id": "user_uuid",
    "expires_in": 3600
}
```

#### User Management
```python
# GET /api/users/profile
# Headers: Authorization: Bearer <token>

# PUT /api/users/profile
{
    "name": "John Doe",
    "age": 45,
    "condition": "stroke_recovery",
    "difficulty_level": "beginner"
}
```

#### Exercise Management
```python
# GET /api/exercises
# Returns list of available exercises

# GET /api/exercises/{exercise_id}
# Returns specific exercise configuration

# POST /api/exercises/{exercise_id}/start
{
    "user_id": "user_uuid",
    "difficulty": "medium"
}

# Response
{
    "session_id": "session_uuid",
    "exercise_config": {...},
    "start_time": "2025-07-17T10:00:00Z"
}
```

#### Progress Tracking
```python
# POST /api/progress/session
{
    "session_id": "session_uuid",
    "exercise_id": "exercise_uuid",
    "performance_data": {
        "accuracy": 0.85,
        "completion_time": 120,
        "movement_quality": 0.78,
        "repetitions": 15
    },
    "biometric_data": {
        "heart_rate": [80, 85, 90],
        "hand_positions": [[x, y, z], ...]
    }
}

# GET /api/progress/user/{user_id}
# Returns user's progress history

# GET /api/progress/analytics/{user_id}
# Returns analytics and insights
```

### Unity C# API Usage

#### Network Manager
```csharp
public class NetworkManager : MonoBehaviour
{
    private string baseUrl = "http://localhost:5000/api";
    
    public async Task<LoginResponse> Login(string email, string password)
    {
        var loginData = new LoginRequest { email = email, password = password };
        var response = await PostAsync<LoginResponse>("/auth/login", loginData);
        return response;
    }
    
    public async Task<ExerciseConfig> GetExercise(string exerciseId)
    {
        return await GetAsync<ExerciseConfig>($"/exercises/{exerciseId}");
    }
}
```

#### Progress Tracker
```csharp
public class ProgressTracker : MonoBehaviour
{
    public async Task SubmitProgress(SessionData sessionData)
    {
        var progressData = new ProgressSubmission
        {
            session_id = sessionData.SessionId,
            exercise_id = sessionData.ExerciseId,
            performance_data = sessionData.PerformanceMetrics,
            biometric_data = sessionData.BiometricData
        };
        
        await networkManager.PostAsync("/progress/session", progressData);
    }
}
```

### Firebase Data Structure

#### Firestore Collections
```javascript
// users/{user_id}
{
  "email": "user@example.com",
  "name": "John Doe",
  "user_type": "patient",
  "profile": {
    "age": 45,
    "condition": "stroke_recovery",
    "created_at": "2025-07-17T10:00:00Z"
  }
}

// exercises/{exercise_id}
{
  "title": "Arm Reach Exercise",
  "description": "Improve shoulder mobility",
  "category": "upper_extremity",
  "difficulty_levels": ["beginner", "intermediate", "advanced"],
  "vr_scene": "arm_reach_scene"
}

// progress/{user_id}/sessions/{session_id}
{
  "exercise_id": "exercise_uuid",
  "start_time": "2025-07-17T10:00:00Z",
  "end_time": "2025-07-17T10:05:00Z",
  "performance": {
    "accuracy": 0.85,
    "completion_time": 300,
    "repetitions": 12
  }
}
```

For complete API documentation and testing, visit our [API Docs](https://docs.rehab-vr.com/api) or use the included Postman collection.

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) before getting started.

### Development Setup
1. **Fork the repository**
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Set up development environment:**
   ```bash
   # Backend setup
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   
   # Install pre-commit hooks
   pre-commit install
   
   # Run backend tests
   python -m pytest tests/
   
   # Frontend setup (Unity)
   # Open Unity Hub and load the unity-client project
   # Ensure Oculus Integration SDK is installed
   ```
4. **Configure Firebase for development:**
   ```bash
   # Create a test Firebase project
   # Add test configuration to backend/config/firebase-test.json
   export FIREBASE_PROJECT_ID="your-test-project"
   ```
5. **Make your changes and test thoroughly**
6. **Submit a pull request**

### Contribution Types
- 🐛 Bug fixes
- ✨ New features
- 📚 Documentation improvements
- 🎨 UI/UX enhancements
- 🔧 Performance optimizations
- 🌐 Localization and accessibility

## 🧪 Testing

### Backend Testing (Flask + Firebase)
```bash
# Unit tests
cd backend
python -m pytest tests/unit/ -v

# Integration tests (requires Firebase test project)
python -m pytest tests/integration/ -v

# API endpoint tests
python -m pytest tests/api/ -v

# Test with coverage
python -m pytest --cov=app tests/
```

### Unity Testing
```bash
# Unity Test Framework
# Open Unity → Window → General → Test Runner
# Run Play Mode tests for VR functionality
# Run Edit Mode tests for logic components

# Manual VR Testing Checklist:
# - Hand tracking accuracy
# - Exercise completion flow
# - Progress data sync
# - Oculus integration features
```

### Firebase Testing
```bash
# Firestore Rules Testing
cd backend
firebase emulators:start --only firestore
python -m pytest tests/firestore/ -v

# Authentication Testing
python -m pytest tests/auth/ -v
```

### Performance Testing
```bash
# Load testing for Flask API
cd backend
locust -f tests/performance/locustfile.py

# VR Performance Testing
# Use Unity Profiler during VR sessions
# Monitor frame rate, memory usage, and network calls
```

### Test Coverage
- **Backend:** >90% code coverage (pytest-cov)
- **Unity:** Core VR functionality and API integration
- **Firebase:** Database operations and authentication
- **Integration:** End-to-end VR session workflows

## 🔧 Troubleshooting

### Common Issues

#### Oculus Connection Issues
- **Solution:** Ensure Oculus app is running and developer mode is enabled
- **Check:** USB debugging enabled, headset connected to same network

#### Firebase Authentication Errors
- **Solution:** Verify Firebase project configuration and API keys
- **Check:** Firebase rules allow read/write access for authenticated users

#### Flask API Not Responding
- **Solution:** Check if Flask server is running on correct port (5000)
- **Check:** Firewall settings, CORS configuration, and network connectivity

#### Unity Build Errors
- **Solution:** Ensure Android Build Support is installed and Oculus SDK is imported
- **Check:** Unity version compatibility, build settings configuration

#### Data Sync Issues
- **Solution:** Check Firebase project status and network connectivity
- **Check:** Authentication tokens are valid and not expired

For more troubleshooting help, visit our [Support Center](https://support.rehab-vr.com).

## 🗺️ Roadmap

### Version 2.0 (Q3 2025)
- [ ] Advanced hand gesture recognition using Oculus SDK
- [ ] AI-powered exercise recommendations based on Firebase analytics
- [ ] Multiplayer rehabilitation sessions with real-time sync
- [ ] Enhanced biometric integration (heart rate, stress levels)

### Version 2.1 (Q4 2025)
- [ ] Mobile companion app (React Native with Firebase)
- [ ] Therapist web dashboard for remote monitoring
- [ ] Voice-controlled interface using Oculus audio
- [ ] Machine learning progress prediction models

### Version 3.0 (Q1 2026)
- [ ] Advanced haptic feedback integration
- [ ] Meta Quest 3S and Quest Pro optimization
- [ ] Integration with major EHR systems via FHIR
- [ ] Advanced analytics dashboard with Firebase Functions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Third-Party Licenses
- Unity Engine: Unity Software License
- Oculus Integration SDK: Oculus SDK License
- Flask: BSD License
- Firebase: Google Cloud Platform Terms
- Various Python packages: See [requirements.txt](backend/requirements.txt)

## 🙏 Acknowledgments

- **Healthcare Advisors:** Dr. Sarah Johnson (Physical Therapy), Dr. Michael Chen (Neurology)
- **Technology Partners:** Unity Technologies, Meta (Oculus), Google Firebase
- **Beta Testers:** Springfield Rehabilitation Center, Metro Physical Therapy
- **Development Tools:** Python Flask, Firebase Console, Unity Editor
- **Open Source Community:** Flask community, Unity developers, Firebase developers


<div align="center">
  <p>Made with ❤️ for the rehabilitation community</p>
  <p>⭐ Star this repository if you find it helpful!</p>
</div>
