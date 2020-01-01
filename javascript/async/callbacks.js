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

function createPost(post, callback){
    setTimeout(() => {
        posts.push(post);
        callback();
    }, 2000);
}

createPost({ title: "Blogpost three", body: "This is blogpost three" }, getPosts);