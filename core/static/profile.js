document.getElementById('profile').innerHTML = "this is a profile";

user = username.innerHTML.substring(1, username.innerHTML.length-1)

baseApiEndpoint = 'http://127.0.0.1:8000/api/core/'
followedUsersEndpoint = baseApiEndpoint + 'users_observed_by_user/' + user + '/';

fetch(followedUsersEndpoint, {
    method: 'GET'
})
.then(function (response) {
    return response.json()
})
.then(function(data){
    followedUsers = document.getElementById('usersFollowing');
    for (i = 0; i < data.length; i++){
        followedUser = document.createElement('a');
        followedUser.setAttribute('href', 'http://127.0.0.1:8000/core/profile/'+ data[i].username);
        followedUser.innerHTML = data[i].username;
        followedUsers.appendChild(followedUser);
    }
})