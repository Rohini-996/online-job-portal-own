// Example: Handle form submissions or dynamic content
document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners as needed, e.g., for search
    const searchForm = document.getElementById('search-form');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const query = document.getElementById('search').value;
            window.location.href = `/jobs?q=${query}`;
        });
    }
});