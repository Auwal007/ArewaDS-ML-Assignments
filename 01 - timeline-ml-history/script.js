// Initialize the Timeline
document.addEventListener('DOMContentLoaded', function() {
    // Show loading message
    const timelineContainer = document.getElementById('timeline-embed');
    timelineContainer.innerHTML = '<div class="loading"></div>';
    
    // Timeline configuration options
    const options = {
        font: 'Lustria-Lato',
        hash_bookmark: true,
        height: 600,
        scale_factor: 2,
        zoom_sequence: [0.5, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        timenav_height: 200,
        marker_height_min: 30,
        marker_width_min: 100,
        slide_padding_lr: 60,
        slide_default_fade: '0%',
        language: 'en',
        ga_property_id: null,
        track_events: ['back_to_start', 'nav_next', 'nav_previous', 'zoom_in', 'zoom_out']
    };
    
    // Load the timeline data and create the timeline
    fetch('timeline-data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to load timeline data');
            }
            return response.json();
        })
        .then(data => {
            // Create the timeline
            window.timeline = new TL.Timeline('timeline-embed', data, options);
            
            // Add event listeners for analytics/tracking (optional)
            window.timeline.on('change', function(data) {
                console.log('Timeline changed to slide:', data.unique_id);
            });
            
            // Handle timeline ready event
            window.timeline.on('ready', function() {
                console.log('Timeline is ready');
                // You can add additional initialization here
            });
        })
        .catch(error => {
            console.error('Error loading timeline:', error);
            timelineContainer.innerHTML = `
                <div style="text-align: center; padding: 2rem; color: #e74c3c;">
                    <h3>Error Loading Timeline</h3>
                    <p>There was an error loading the timeline data. Please check the console for details.</p>
                    <p>Make sure the timeline-data.json file is in the same directory as this HTML file.</p>
                </div>
            `;
        });
});

// Utility functions for the timeline
const TimelineUtils = {
    // Function to navigate to a specific date
    goToDate: function(year) {
        if (window.timeline) {
            window.timeline.goTo(year);
        }
    },
    
    // Function to go to next slide
    next: function() {
        if (window.timeline) {
            window.timeline.goToNext();
        }
    },
    
    // Function to go to previous slide
    previous: function() {
        if (window.timeline) {
            window.timeline.goToPrev();
        }
    },
    
    // Function to zoom in
    zoomIn: function() {
        if (window.timeline) {
            window.timeline.zoomIn();
        }
    },
    
    // Function to zoom out
    zoomOut: function() {
        if (window.timeline) {
            window.timeline.zoomOut();
        }
    }
};

// Keyboard shortcuts
document.addEventListener('keydown', function(event) {
    switch(event.key) {
        case 'ArrowLeft':
            event.preventDefault();
            TimelineUtils.previous();
            break;
        case 'ArrowRight':
            event.preventDefault();
            TimelineUtils.next();
            break;
        case '+':
        case '=':
            event.preventDefault();
            TimelineUtils.zoomIn();
            break;
        case '-':
            event.preventDefault();
            TimelineUtils.zoomOut();
            break;
    }
});

// Export utilities for global access
window.TimelineUtils = TimelineUtils;
