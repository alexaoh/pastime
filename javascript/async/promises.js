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

//createPost({ title: "Blogpost three", body: "This is blogpost three" })
//    .then(getPosts)
//    .catch(err => console.log(err));


//A way to handle multiple promises: 
// Promise.all
const promise1 = Promise.resolve('Hello World!');
const promise2 = 10;
const promise3 = new Promise((resolve, reject) => setTimeout(resolve, 2000, 'Goodbye'));
const promise4 = fetch('https://jsonplaceholder.typicode.com/users').then(res => res.json());

Promise.all([promise1, promise2, promise3, promise4]).then((values) => console.log(values));