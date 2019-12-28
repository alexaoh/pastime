// Dependencies
const http = require('http');
const util = require('util');
const debugLog = util.debuglog('server');

//create a server:
const server = http.createServer((req, res) => {
  res.writeHead(200, {'Content-Type': 'text/html'});
  debugLog('Write response');
  res.write('Hello NodeJS! This is a new local server <br/>') //write a response to the client
  res.write('Your url: ' + req.url);
  res.end() //end the response
  debugLog('Response ended.');
});

// start listening to the server
server.listen(8080, () => {
  debugLog('Node server is listening on 8080 port.')
});

/*
CREDIT WHERE CREDIT IS DUE

Written while reading the following article: https://dev.to/elanandkumar/on-demand-colorful-console-log-in-nodejs-1929
(not finished reading)
*/
