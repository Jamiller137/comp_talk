// Initialize Reveal.js
Reveal.initialize({
    hash: true,
    controls: true,
    progress: true,
    center: true,
    transition: 'slide',

    // Display slide numbers
    slideNumber: 'c/t',

    // Push each slide change to the browser history
    history: true,

    // Enable keyboard shortcuts for navigation
    keyboard: true,

    // Enable the slide overview mode
    overview: true,

    // Vertical centering of slides
    center: true,

    // Enables touch navigation on devices with touch input
    touch: true,

    // Loop the presentation
    loop: false,

    // Change the presentation direction to be RTL
    rtl: false,

    // Randomizes the order of slides each time the presentation loads
    shuffle: false,

    // Turns fragments on and off globally
    fragments: true,

    // Flags if the presentation is running in an embedded mode
    embedded: false,

    // Flags if we should show a help overlay when the questionmark key is pressed
    help: true,

    // Flags if speaker notes should be visible to all viewers
    showNotes: false,

    // Auto-slide settings
    autoSlide: 0,
    autoSlideStoppable: true,
    autoSlideMethod: Reveal.navigateNext,

    // Enable slide navigation via mouse wheel
    mouseWheel: false,

    // Hides the address bar on mobile devices
    hideAddressBar: true,

    // Opens links in an iframe preview overlay
    previewLinks: false,

    // Transition style for full page slide backgrounds
    backgroundTransition: 'fade',

    // Number of slides away from the current that are visible
    viewDistance: 3,

    // Parallax background image
    parallaxBackgroundImage: '',
    parallaxBackgroundSize: '',
    parallaxBackgroundHorizontal: null,
    parallaxBackgroundVertical: null,

    // The display mode that will be used to show slides
    display: 'block',

    plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
});

// Add custom keyboard shortcuts
Reveal.addKeyBinding({keyCode: 82, key: 'R', description: 'Reset presentation'}, function() {
    Reveal.slide(0);
});

// Custom event listeners
Reveal.addEventListener('ready', function(event) {
    console.log('Presentation is ready');
});

Reveal.addEventListener('slidechanged', function(event) {
    console.log('Slide changed to:', event.indexh);
});

