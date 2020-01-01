const posts = [
    { title: "Blogpost one", body: "This is blogpost one"}, 
    { title: "Blogpost two", body: "This is blogpost two"}
];

function getPosts(){
    setTimeout(() => {
        let output = '';
        posts.forEach((post) => {
            output += '<li>'+post.title+'</li>';
        });
        let unList = document.getElementById('unList');
        unList.innerHTML += output;
    }, 1000);  
}

function createPost(post){
    const promise = new Promise((resolve, reject) => {
        setTimeout(() => {
            posts.push(post);

            const error = false;

            if (!error){
                resolve();
            } else {
                reject("Error: Something went wrong!");
            }
        }, 2000);
    });
    return promise;
     
}

//Same inital code as in promises.js

//Async / await 

async function init(){
    await createPost({ title: "Blogpost three", body: "This is blogpost three" });

    getPosts();
}

//Async / await with fetch
async function fetchUsers(){
    const res = await fetch('https://jsonplaceholder.typicode.com/users');

    const data = await res.json();
    console.log(data);
}

fetchUsers();
