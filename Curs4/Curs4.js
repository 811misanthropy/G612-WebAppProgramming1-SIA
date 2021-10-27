function buttonClickedResponse(resp){
    console.log("..IT WORKS!!");
    console.log(resp)

}

function buttonClickedError(err){
    console.log("--There was an error");
    console.log(err)
}


function buttonClicked(e){
    console.log("Someone clicked me");
    console.log(e);
    console.log("I'm going to get data");
    fetch('http://exemple.com/api/v1/movies')
    .then(buttonClickedResponse)
    .catch(buttonClickedError)
    console.log("I'm still waiting.")
}