async function searchDestinations() {

    const query = document.getElementById("searchInput").value;

    const resultsDiv = document.getElementById("results");
    const loadingDiv = document.getElementById("loading");

    if (query.trim() === "") {
        resultsDiv.innerHTML = "<p>Please enter a travel requirement.</p>";
        return;
    }

    loadingDiv.innerHTML = "Searching for destinations...";

    resultsDiv.innerHTML = "";

    try {

        const response = await fetch("http://127.0.0.1:8000/search", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                query: query,
                top_n: 5
            })

        });

        const data = await response.json();

        loadingDiv.innerHTML = "";

        if (!data.success) {

            resultsDiv.innerHTML = `
                <p>${data.message}</p>
            `;

            return;
        }

        data.results.forEach((result, index) => {

            const card = document.createElement("div");

            card.className = "result-card";

            card.innerHTML = `
                <h2>${index + 1}. ${result.destination}</h2>

                <p>
                    <strong>State:</strong>
                    ${result.state}
                </p>

                <p>
                    <strong>Category:</strong>
                    ${result.category}
                </p>

                <p class="similarity">
                    Similarity Score:
                    ${result.similarity}
                </p>
            `;

            resultsDiv.appendChild(card);

        });

    } catch (error) {

        loadingDiv.innerHTML = "";

        resultsDiv.innerHTML = `
            <p>
                Unable to connect to the backend.
                Please make sure FastAPI is running.
            </p>
        `;

        console.error(error);
    }
}