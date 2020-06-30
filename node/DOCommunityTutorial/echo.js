const args = process.argv.slice(2);

args.forEach(arg => {
    let v = process.env[arg];

    if (v === undefined){
        console.error("Could not find \'"+arg+"\' in the environment variables");
    } else {
        console.log(arg+": "+v);
    }
});
