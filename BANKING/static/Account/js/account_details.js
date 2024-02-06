
function changeAppBackgroundColor() {
    // Get the app container element
    const appContainer = document.querySelector('body');

    // Get a random color
    const newColor = getRandomColor();

    // Change the background color of the app container
    appContainer.style.backgroundColor = newColor;
}