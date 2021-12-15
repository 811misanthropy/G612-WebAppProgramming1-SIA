function ifSuccess(response) {
    console.log("USER SIGN IN!");
}

function ifError(error){
    console.log(error);
}

function signup (){
    const data = {

        email: document.getElementsByName ("Email")[0].value,
        password: document.getElementsByName ("Password")[0].value
    }

    console.log(data)
    url = "http://localhost:3002/api/v1/signin"
    options = {
        body: JSON.stringify(data),
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-type': 'application/json',
        }
    }

    fetch(url, options)
    .then(ifSuccess)
    .catch(ifError)

}