const search = document.getElementById("search");
const table = document.getElementById("feedbackTable");

function getDataRows() {
    return [...table.querySelectorAll("tr")].filter(
        row => !row.classList.contains("empty-row")
    );
}

// Search: subject, faculty, course me dhoondhega
search.addEventListener("input", function () {
    const value = search.value.toLowerCase();

    getDataRows().forEach(function (row) {
        const text = (
            row.cells[2].textContent + " " +   // Subject
            row.cells[3].textContent + " " +   // Faculty
            row.cells[4].textContent           // Course
        ).toLowerCase();

        row.style.display = text.includes(value) ? "" : "none";
    });
});

// Dashboard statistics
function updateStatistics() {
    const rows = getDataRows();
    const total = rows.length;

    let sum = 0;
    let rated = 0;

    rows.forEach(function (row) {
        const r = parseFloat(row.cells[6].textContent);   // Rating column
        if (!isNaN(r)) {
            sum += r;
            rated++;
        }
    });

    // Unique students nahi pata, isliye abhi total records dikha rahe hain
    document.getElementById("studentCount").textContent = total;
    document.getElementById("feedbackCount").textContent = total;
    document.getElementById("averageRating").textContent =
        rated ? (sum / rated).toFixed(1) + "/5" : "0/5";
}

updateStatistics();