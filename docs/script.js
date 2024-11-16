document.addEventListener("DOMContentLoaded", function() {
    fetch('output.json')
        .then(response => response.json())
        .then(data => {
            const outputDiv = document.getElementById('output');
            if (data.out_of_stock_items && data.out_of_stock_items.length > 0) {
                outputDiv.innerHTML = `<h2>Out of Stock Products:</h2>`;
                data.out_of_stock_items.forEach(url => {
                    outputDiv.innerHTML += `<p>${url}</p>`;
                });
            } else {
                outputDiv.innerHTML = `<h2>All products are in stock.</h2>`;
            }
        })
        .catch(error => {
            console.error('Error fetching availability:', error);
            document.getElementById('output').innerHTML = `<p>Error fetching data</p>`;
        });
});
