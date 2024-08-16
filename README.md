# Goofy Music App

## Overview

Goofy is a feature-rich music streaming platform designed to provide users with a personalized music experience. With a sleek interface, powerful music player, and robust authentication features, Goofy aims to deliver a seamless and enjoyable music listening experience.

## Features

### Pages
- **Home Page**: Overview of new releases and recommended content.
- **Explore Page**: Discover new songs, albums, and artists.
- **My Likes Page**: Displays all the songs liked by the user.
- **Library Page**: Access to playlists, albums, and artists. Option to create personalized playlists.
- **Profile Page**: Update profile picture and manage personal information.
- **Signup/Login Page**: Includes Google authentication and "Forget Password" functionality.

### Music Player
- **Basic Controls**: Play, pause, skip to next/previous song.
- **Advanced Controls**:
  - Shuffle songs
  - Play all or play one option
  - Volume control
  - Seek/skip to different parts in a song
  - Lyrics page
  - Like the current song

### User Experience
- **Personalization**: Custom playlists, personalized profile pictures.
- **Search Functionality**: Users can search for songs, albums, and artists.
- **Google Authentication**: Easy and secure login/signup process.

## Technology Stack
- **Frontend**: HTML, CSS, Tailwind CSS, JavaScript
- **Backend**: Django, PostgreSQL
- **Authentication**: Google Authentication
- **Other Features**: Email integration for password reset

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/warui-slime/Goofy.git
   cd goofy

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Database Configuration:
   The `DATABASES` setting in `settings.py` defines the configuration for the database used by the Goofy Music App. The app uses PostgreSQL as its database management system.   Below is a breakdown of the configuration:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your database name', 
        'USER':'postgres username',
        'PASSWORD': 'yourdatabasepasskey',
        'HOST':'localhost'
    }
}

