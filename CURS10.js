function responseReceived(response){
    return response.json()
}


function getUsersData (){
    url = ''
    response = fetch()
        .then(responseReceived)
        .then(processResponse)
        .then(errorResponse) 
}