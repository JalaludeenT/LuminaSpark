document.getElementById('searchForm').addEventListener('submit', function(event) {
        event.preventDefault();
        performSearch();
    });

    function performSearch() {
        var searchInput = document.getElementById('searchInput').value.toLowerCase();
        var content = document.body.innerHTML.toLowerCase();

        if (content.includes(searchInput)) {
            alert('That word is in this screen');
        } else {
            alert('Word not found any same word!');
        }
    }