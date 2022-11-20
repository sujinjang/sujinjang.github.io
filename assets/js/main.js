async function setNumStars(repo, element) {
    fetch("https://api.github.com/repos/" + repo)
        .then(response => response.json())
        .then(data => {
            element.textContent = data["stargazers_count"];
        })
}

var elements = document.getElementsByClassName("github-star");

for (var i = 0; i < elements.length; i++) {
    setNumStars(elements[i].getAttribute("data-repo"), elements[i]);
}
