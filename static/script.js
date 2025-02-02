function getRecommendations() {
    console.log("Fetching recommendations for genre:", document.getElementById("genre").value);
    
    const genre = document.getElementById("genre").value;

    fetch("/recommend", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ genre: genre })
    })
    .then(response => response.json())
    .then(books => {
        console.log("Books received:", books);

        const bookList = document.getElementById("book-list");
        bookList.innerHTML = ""; // Clear previous results

        if (books.length === 0) {
            bookList.innerHTML = "<li>No books found for this genre.</li>";
            return;
        }

        books.forEach(book => {
            const listItem = document.createElement("li");
            listItem.textContent = `${book[0]} by ${book[1]}`;
            bookList.appendChild(listItem);
        });
    })
    .catch(error => console.error("Error:", error));
}

// Attach event listener after DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("recommend-btn").addEventListener("click", getRecommendations);
});
