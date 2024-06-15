const url = ''

fetch(url)
    .then(function(res) {
        // extract the function out of this result
        return res.json()
    })
    .then(function(json) {
        return ({})
    })
    .then(function(data) {

    })
    .catch(function(err){
        // handle error?
    })
