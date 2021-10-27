
function buttonClickedError(err){
    console.log("Succes!");
    console.log(err)
}

function suClicked()
{
    console.log("Someone clicked me");
    console.log("I'm going to get data");
    fetch('https://jsonplaceholder.typicode.com/posts', {
        method: "POST",  body: JSON.stringify({
            title: "titlu", body: "corp", userId: 1
        }),
        headers:{"Content-type": "application/json; charset=UTF-8"} 
    })
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(buttonClickedError)
}