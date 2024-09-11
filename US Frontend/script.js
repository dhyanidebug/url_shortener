document.getElementById('shorten-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const longUrl = document.getElementById('long-url').value;
    const resultElement = document.getElementById('shorten-result');

    try {
        const response = await fetch('http://localhost:8000/create/?long_url=' + encodeURIComponent(longUrl), {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        const data = await response.json();
        if (response.ok) {

            resultElement.innerHTML = `Short URL: <a href="${data.Short_url}" target="_blank">${data.short_url}</a>`;
        } else {
            resultElement.innerHTML = 'Error: ' + data.message;
        }
    } catch (error) {
        console.error('Error shortening URL:', error);
        resultElement.innerHTML = 'Error: ' + error.message;
    }
});

document.getElementById('list-documents').addEventListener('click', async function() {
    const documentsTable = document.getElementById('documents-table');
    const documentList = document.getElementById('document-list');

    try {
        const response = await fetch('http://localhost:8000/listAllDocument/');
        const data2 = await response.json();

        console.log(data2); // Debugging line

        // Clear existing content
        documentList.innerHTML = '';

        if (!data2.Data || data2.Data.length === 0) {
            documentList.innerHTML = '<tr><td colspan="4">No documents found</td></tr>';
            return;
        }

        // Populate table rows with document data
        data2.Data.forEach(doc => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${doc.key}</td>
                <td><a href="${doc.long_url}" target="_blank">${doc.long_url}</a></td>
                <td><a href="${doc.short_url}" target="_blank">${doc.short_url}</a></td>
                <td>${doc.impression}</td>
            `;
            documentList.appendChild(row);
        });

        // Show the table
        documentsTable.style.display = 'table';
    } catch (error) {
        console.error('Error fetching documents:', error);
    }
});
