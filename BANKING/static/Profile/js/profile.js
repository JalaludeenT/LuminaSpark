    document.addEventListener('DOMContentLoaded', function () {
        const mobileNavigation = document.querySelector('.mobile-navigation');
        const iconButton = document.querySelector('.icon-button.large');

        function toggleMobileNavigation() {
            mobileNavigation.classList.toggle('active');
        }

        function closeMobileNavigation(event) {
            if (!mobileNavigation.contains(event.target) && !iconButton.contains(event.target)) {
                mobileNavigation.classList.remove('active');
            }
        }

        iconButton.addEventListener('click', toggleMobileNavigation);
        document.addEventListener('click', closeMobileNavigation);
    });



function getRandomColor() {
    // Generate a random hex color code
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function changeColor() {
    // Get a random color
    const newColor = getRandomColor();

    // Change the background color of the body
    document.body.style.backgroundColor = newColor;
}


function changeTileColor(tile) {
    // Get a random color
    const newColor = getRandomColor();

    // Change the background color of the clicked tile
    tile.style.backgroundColor = newColor;
}



function getRandomColor() {
    // Generate a random hex color code
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function changeAppBackgroundColor() {
    // Get the app container element
    const appContainer = document.querySelector('.app');

    // Get a random color
    const newColor = getRandomColor();

    // Change the background color of the app container
    appContainer.style.backgroundColor = newColor;
}


function toggleMobileNavigation() {
        // Toggle the visibility of the mobile navigation
        const mobileNavigation = document.querySelector('.mobile-navigation');
        mobileNavigation.classList.toggle('active');
    }


