# Machine Learning and AI History Timeline

An interactive timeline showcasing the key milestones in the evolution of Machine Learning and Artificial Intelligence, from 1943 to 2023.

## Overview

This timeline project covers major breakthroughs, algorithms, and achievements that shaped the field of AI and ML:

- **1943**: First Neural Network Model (McCulloch-Pitts)
- **1950**: The Turing Test
- **1956**: Birth of Artificial Intelligence (Dartmouth Conference)
- **1957**: The Perceptron Algorithm
- **1986**: Backpropagation Algorithm
- **1997**: Deep Blue vs. Kasparov
- **2006**: Deep Learning Renaissance
- **2012**: AlexNet and ImageNet
- **2016**: AlphaGo vs. Lee Sedol
- **2017**: Transformer Architecture
- **2022**: ChatGPT Launch
- **2023**: Multimodal AI (GPT-4)

## Features

- **Interactive Navigation**: Click on timeline markers to explore different periods
- **Rich Media**: Each event includes relevant images and detailed descriptions
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Keyboard Controls**: Arrow keys for navigation, +/- for zoom
- **Modern Styling**: Beautiful gradient background and smooth animations

## Files Structure

```
timeline-ml-history/
├── index.html          # Main HTML file
├── timeline-data.json  # Timeline data in JSON format
├── styles.css          # Custom CSS styling
├── script.js           # JavaScript for timeline initialization
└── README.md           # This file
```

## How to Run

### Option 1: Local Development Server (Recommended)

1. **Install Node.js** (if not already installed):
   - Download from https://nodejs.org/
   - Install following the instructions for your OS

2. **Navigate to the project directory**:
   ```powershell
   cd "c:\Users\Dell\Desktop\ArewaDS-ML-Assignments\timeline-ml-history"
   ```

3. **Start a local server**:
   ```powershell
   # Using Node.js http-server (install globally first)
   npm install -g http-server
   http-server
   
   # OR using Python (if installed)
   python -m http.server 8000
   
   # OR using PHP (if installed)
   php -S localhost:8000
   ```

4. **Open in browser**:
   - Navigate to `http://localhost:8000` (or the port shown in terminal)

### Option 2: Direct File Access

1. Simply double-click on `index.html` in File Explorer
2. The timeline will open in your default web browser

**Note**: Some browsers may block loading local JSON files for security reasons. If you encounter issues, use Option 1 with a local server.

## Deployment to GitHub Pages

To deploy this timeline as a live website:

1. **Push to GitHub** (if not already done):
   ```powershell
   git add .
   git commit -m "Add ML/AI timeline project"
   git push origin main
   ```

2. **Enable GitHub Pages**:
   - Go to your repository on GitHub
   - Navigate to Settings → Pages
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click Save

3. **Access your timeline**:
   - Your timeline will be available at: `https://auwal007.github.io/ArewaDS-ML-Assignments/timeline-ml-history/`

## Customization

### Adding New Events

To add new events to the timeline:

1. Open `timeline-data.json`
2. Add a new event object to the `events` array:

```json
{
  "start_date": {
    "year": "2024"
  },
  "text": {
    "headline": "Your Event Title",
    "text": "Detailed description of the event..."
  },
  "media": {
    "url": "https://example.com/image.jpg",
    "caption": "Image caption"
  }
}
```

### Modifying Styles

- Edit `styles.css` to change colors, fonts, or layout
- The timeline uses a purple gradient background by default
- Timeline.js provides additional CSS classes for customization

### Timeline Configuration

Modify the `options` object in `script.js` to:
- Change timeline height
- Adjust zoom levels
- Modify navigation behavior
- Set custom fonts

## Technologies Used

- **Timeline.js**: Knight Lab's timeline library
- **HTML5**: Modern semantic markup
- **CSS3**: Custom styling with gradients and animations
- **JavaScript ES6**: Modern JavaScript features
- **JSON**: Structured data format for timeline events

## Browser Compatibility

- Chrome 70+
- Firefox 65+
- Safari 12+
- Edge 79+

## Assignment Requirements Met

✅ **Timeline Focus**: Machine Learning and AI history  
✅ **Multimedia Elements**: Images and detailed descriptions for each event  
✅ **Deployed Timeline**: Ready for GitHub Pages deployment  
✅ **Well-researched Content**: 20 major milestones from 1943-2023  
✅ **Professional Presentation**: Modern design and user-friendly interface

## Data Sources

- Academic papers and historical records
- Technology company announcements
- Research institution publications
- Verified historical timelines from reputable sources

## License

This project is part of the ArewaDS ML Assignments and is intended for educational purposes.

---

**Created by**: [Your Name]  
**Date**: September 12, 2025  
**Course**: ArewaDS Machine Learning Program
