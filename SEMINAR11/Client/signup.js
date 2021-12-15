function ifSuccess(response) {
    console.log("USER SIGN UP!");
}

function ifError(error){
    console.log(error);
}

function signup (){
    const data = {
        firstName: document.getElementsByName ("First Name")[0].value,
        lastName: document.getElementsByName ("Last Name")[0].value,
        email: document.getElementsByName ("Email")[0].value,
        password: document.getElementsByName ("Password")[0].value,
        passwordnd: document.getElementsByName ("Second Password")[0].value,
    }
    if (data[3]==data[4]){
    console.log(data)
    url = "http://localhost:3002/api/v1/signup"
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
    .catch(ifError)}
    else {
        console.log("The password retype doesn't match the first password!!!")
    }
}