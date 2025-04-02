document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const subject = urlParams.get('subject');
    const difficulty = urlParams.get('difficulty');

    if (subject && difficulty) {
        fetch(`/recommend?subject=${subject}&difficulty=${difficulty}`)
            .then(response => response.json())
            .then(data => {
                let resources = data.resources.map(res => `<li><a href="${res}" target="_blank">${res}</a></li>`).join('');
                document.getElementById('result').innerHTML = `<ul>${resources}</ul>`;
            })
            .catch(error => console.error("Error fetching recommendations:", error));
    }
});
