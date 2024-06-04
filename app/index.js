// Function to handle form submission
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        // Your form handling logic goes here
        console.log('Form submitted');
    });
});
